#!/usr/bin/env python3
"""
Founder Outreach Notifier
Sends desktop/terminal notifications for your 3-week outreach plan.
"""

import json
import os
import subprocess
import sys
import time
import threading
from datetime import date, datetime, timedelta
from pathlib import Path

import schedule

from tasks import TASKS

CONFIG_FILE = Path(__file__).parent / "config.json"

WEEKDAY_NAMES = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
PERIOD_LABELS = {"morning": "Morning", "midday": "Midday", "evening": "Evening"}
PERIOD_EMOJI = {"morning": "🌅", "midday": "☀️", "evening": "🌙"}


# ── Config ────────────────────────────────────────────────────────────────────

def load_config():
    with open(CONFIG_FILE) as f:
        return json.load(f)

def save_config(cfg):
    with open(CONFIG_FILE, "w") as f:
        json.dump(cfg, f, indent=2)


# ── Notification backends ─────────────────────────────────────────────────────

def _notify_libnotify(title, body):
    subprocess.Popen(["notify-send", "-t", "15000", title, body],
                     stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def _notify_plyer(title, body):
    from plyer import notification
    notification.notify(title=title, message=body[:255], timeout=15)

def _notify_terminal(title, body):
    sep = "─" * 60
    print(f"\n{sep}")
    print(f"  {title}")
    print(sep)
    for line in body.split("\n"):
        print(f"  {line}")
    print(f"{sep}\n")
    sys.stdout.flush()

def _notify_terminal_bell(title, body):
    print("\a", end="", flush=True)
    _notify_terminal(title, body)

def detect_notify_method():
    if subprocess.run(["which", "notify-send"], capture_output=True).returncode == 0:
        return "libnotify"
    try:
        from plyer import notification
        return "plyer"
    except ImportError:
        pass
    return "terminal"

def send_notification(title, body, method="auto"):
    if method == "auto":
        method = detect_notify_method()
    try:
        if method == "libnotify":
            _notify_libnotify(title, body)
        elif method == "plyer":
            _notify_plyer(title, body)
        else:
            _notify_terminal_bell(title, body)
    except Exception:
        _notify_terminal(title, body)


# ── Plan logic ────────────────────────────────────────────────────────────────

def get_plan_day(start_date: date, today: date):
    """
    Returns (week, weekday_name) for today relative to the plan start date,
    or None if today is outside the 3-week plan or is a weekend.
    start_date is treated as Week 1 Monday regardless of actual weekday.
    """
    delta = (today - start_date).days
    if delta < 0 or delta >= 21:
        return None
    week = (delta // 7) + 1
    day_index = delta % 7
    if day_index >= 5:          # Saturday / Sunday
        return None
    return week, WEEKDAY_NAMES[day_index]


def build_notification(week, weekday, period):
    task_list = TASKS.get(week, {}).get(weekday, {}).get(period, [])
    if not task_list:
        return None, None

    label = PERIOD_LABELS[period]
    title = f"Outreach Plan | Week {week} {weekday.capitalize()} {label}"

    lines = []
    for i, (task_title, desc) in enumerate(task_list, 1):
        lines.append(f"{i}. {task_title}")
        for dl in desc.split("\n"):
            lines.append(f"   {dl}")
        if i < len(task_list):
            lines.append("")

    body = "\n".join(lines)
    return title, body


def fire_notification(period, cfg):
    today = date.today()
    start = date.fromisoformat(cfg["start_date"])
    result = get_plan_day(start, today)

    if result is None:
        return  # weekend or outside plan

    week, weekday = result
    title, body = build_notification(week, weekday, period)

    if title is None:
        return  # no tasks for this slot

    method = cfg.get("notification_method", "auto")
    send_notification(title, body, method)

    # Also print to terminal for visibility
    if method not in ("terminal",):
        print(f"[{datetime.now().strftime('%H:%M')}] Notification sent: {title}")


# ── Setup & scheduler ─────────────────────────────────────────────────────────

def setup_start_date():
    cfg = load_config()
    if cfg.get("start_date"):
        print(f"Plan start date is already set to: {cfg['start_date']}")
        change = input("Change it? (y/N): ").strip().lower()
        if change != "y":
            return cfg

    print("\nFounder Outreach Plan - Setup")
    print("─" * 40)
    print("Enter the date you want Week 1 Monday to begin.")
    print("(This doesn't have to be an actual Monday — the plan")
    print(" will map Week 1 Mon = Day 1, Tue = Day 2, etc.)")
    print()

    while True:
        raw = input("Start date (YYYY-MM-DD) [today]: ").strip()
        if not raw:
            chosen = date.today()
        else:
            try:
                chosen = date.fromisoformat(raw)
            except ValueError:
                print("Invalid date format. Use YYYY-MM-DD.")
                continue
        break

    print(f"\nNotification times (press Enter to keep defaults):")
    times = cfg["notification_times"]
    for period in ("morning", "midday", "evening"):
        raw = input(f"  {period.capitalize()} [{times[period]}]: ").strip()
        if raw:
            times[period] = raw

    cfg["start_date"] = chosen.isoformat()
    cfg["notification_times"] = times
    save_config(cfg)
    print(f"\nSaved. Plan starts: {chosen.isoformat()}")
    return cfg


def run_scheduler(cfg):
    times = cfg["notification_times"]

    for period, t in times.items():
        schedule.every().day.at(t).do(fire_notification, period=period, cfg=cfg)

    print(f"\nOutreach notifier running.")
    print(f"  Plan start : {cfg['start_date']}")
    print(f"  Morning    : {times['morning']}")
    print(f"  Midday     : {times['midday']}")
    print(f"  Evening    : {times['evening']}")
    print(f"\nPress Ctrl+C to stop.\n")

    while True:
        schedule.run_pending()
        time.sleep(30)


def preview_today(cfg):
    """Print today's tasks to terminal without waiting for scheduled time."""
    if not cfg.get("start_date"):
        print("No start date set. Run with --setup first.")
        return

    today = date.today()
    start = date.fromisoformat(cfg["start_date"])
    result = get_plan_day(start, today)

    if result is None:
        delta = (today - start).days
        if delta < 0:
            print(f"Plan hasn't started yet. Starts {cfg['start_date']}.")
        elif delta >= 21:
            print("You've completed the 3-week plan!")
        else:
            print("Today is a rest day (weekend in your plan). Enjoy the break!")
        return

    week, weekday = result
    print(f"\nToday's plan: Week {week}, {weekday.capitalize()}")
    print("=" * 60)
    for period in ("morning", "midday", "evening"):
        title, body = build_notification(week, weekday, period)
        if title:
            t = cfg["notification_times"][period]
            print(f"\n[{t}] {PERIOD_LABELS[period]}")
            print("-" * 40)
            print(body)
    print()


def fire_now(cfg, period=None):
    """Immediately fire notifications (for testing or manual trigger)."""
    if not cfg.get("start_date"):
        print("No start date set. Run with --setup first.")
        return
    periods = [period] if period else ["morning", "midday", "evening"]
    for p in periods:
        fire_notification(p, cfg)


# ── Entry point ───────────────────────────────────────────────────────────────

def print_help():
    print("""
Founder Outreach Notifier
Usage: python3 notifier.py [command]

Commands:
  (none)        Run scheduler (sends notifications at configured times)
  --setup       Configure start date and notification times
  --preview     Print today's tasks to terminal right now
  --fire        Send all of today's notifications immediately (good for testing)
  --fire=morning|midday|evening  Send a specific period's notification now
  --help        Show this message
""")


if __name__ == "__main__":
    args = sys.argv[1:]

    if "--help" in args or "-h" in args:
        print_help()
        sys.exit(0)

    if "--setup" in args:
        cfg = setup_start_date()
        print("\nRun `python3 notifier.py` to start the scheduler.")
        sys.exit(0)

    cfg = load_config()

    if not cfg.get("start_date"):
        print("First run! Let's set up your plan.")
        cfg = setup_start_date()
        print()

    if "--preview" in args:
        preview_today(cfg)
        sys.exit(0)

    fire_args = [a for a in args if a.startswith("--fire")]
    if fire_args:
        arg = fire_args[0]
        period = arg.split("=")[1] if "=" in arg else None
        fire_now(cfg, period)
        sys.exit(0)

    run_scheduler(cfg)
