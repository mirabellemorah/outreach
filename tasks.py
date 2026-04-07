"""
3-Week Founder Outreach Action Plan - Task Definitions
Each task: (title, description)
Structure: TASKS[week][weekday][period] where:
  week = 1, 2, 3
  weekday = "monday" ... "friday"
  period = "morning", "midday", "evening"
"""

TASKS = {
    1: {
        "monday": {
            "morning": [
                ("Update LinkedIn bio (15 mins)",
                 "Update to: 'We help B2B startups communicate their product in 30 seconds. Motion explainers, pitch decks, demo reels. 2-week sprint model.'"),
                ("Update Twitter bio",
                 "Update Twitter bio similarly to LinkedIn."),
                ("Update website headline",
                 "Update website headline or pin a post."),
            ],
            "midday": [
                ("Identify 3 past clients for case studies (20 mins)",
                 "Write their names + the problem you solved. Screenshot 1 before/after example from your work."),
            ],
            "evening": [
                ("Product Hunt comments (15 mins)",
                 "Go to producthunt.com/launches. Find 2 B2B launches from last 3 days.\nComment: 'Love [specific thing]. The only gap: investors might not understand [feature] from your current video. I help founders clarify that. Free 30-min audit?'"),
            ],
        },
        "tuesday": {
            "morning": [
                ("Write down your ONE transformation (10 mins)",
                 "What's ONE transformation you've created for a past client? (Before → After)\nExample: 'Confused product demo → 30-sec explainer that helped them close investors'"),
            ],
            "midday": [
                ("LinkedIn founder search + comments (20 mins)",
                 "Search: 'founder + (climate OR fintech OR edtech) + (Glasgow OR Lagos OR London)'\nFind 3 founder posts from last 7 days. Comment genuinely on each. Wait 2 days then DM with offer."),
            ],
            "evening": [
                ("Twitter pitch/explainer search (15 mins)",
                 "Search #startup or #founderlife. Find 1 founder tweeting about 'pitch deck', 'investor meeting', or 'explainer video'.\nReply: 'The gap here is usually motion. Most founders explain features instead of transformation. I've helped startups flip that. DM me if you want a free audit.'"),
            ],
        },
        "wednesday": {
            "morning": [
                ("Create 'hope for founders' post (15 mins)",
                 "Template: 'Helped a [industry] startup go from \"nobody understands our product\" to \"investors got it immediately.\" Here's what changed: [1 thing]. What's your biggest challenge explaining your product?'\nPost on LinkedIn + Twitter."),
            ],
            "midday": [
                ("Indie Hackers outreach (20 mins)",
                 "Go to indiehackers.com. Find 1 discussion about 'pitch deck' or 'how to market my startup'.\nReply: 'I audited 10 founder demos. The gap is usually here: [name 1 mistake]. Here's how we fix it: [1-2 sentences]. Portfolio: [link]. DM me for free audit.'"),
            ],
            "evening": [
                ("Product Hunt again (15 mins)",
                 "Check new/recent launches. Comment on 2 B2B launches with your audit offer."),
            ],
        },
        "thursday": {
            "morning": [
                ("Build accelerator list (20 mins)",
                 "Create list of 10 accelerators/incubators. Search: 'startup accelerator + [your city]'\nWrite names + their partnerships/mentor network email. Google: '[Accelerator name] partnerships email'"),
            ],
            "midday": [
                ("Draft + send accelerator emails (30 mins)",
                 "Subject: 'Motion Design Partner for Your Founders'\nBody: 'Hi [Name], I help your portfolio founders nail investor pitches with motion design. I've worked with [X] startups, they've raised [Y]. Interested in adding this to your curriculum? Let's talk.'\nSend to 3 accelerators (personalize each slightly)."),
            ],
            "evening": [
                ("Twitter reply + LinkedIn DM (15 mins)",
                 "Reply to 1 founder's tweet about communication/pitch/video.\nDM 1 new founder from your LinkedIn search on Tuesday."),
            ],
        },
        "friday": {
            "morning": [
                ("Post: '3 things every founder gets wrong' (15 mins)",
                 "Create post:\n1. Explain features (no one cares)\n2. Don't show transformation (this wins)\n3. Think video is optional (it's the first filter)\nPost on LinkedIn + Twitter."),
            ],
            "midday": [
                ("Crunchbase outreach (20 mins)",
                 "Go to crunchbase.com (free version). Search: 'Funded in last 6 months + [your target industry]'\nFind 5 founders. Draft personalized email: 'Congrats on your seed round. You're now competing for investor attention. Motion design is how founders stand out. I've helped [X] do this. Free 30-min audit?'\nSend 5 emails."),
            ],
            "evening": [
                ("Week 1 check-in (15 mins)",
                 "Count founder DMs received this week. Write down the number.\nReview what worked and what didn't."),
            ],
        },
    },
    2: {
        "monday": {
            "morning": [
                ("Reply to Week 1 DMs (15 mins)",
                 "Check all DMs from Week 1. Reply to each founder: 'Thanks for reaching out. Here's what I typically do: [1-sentence overview]. Can we hop on a 30-min call Tuesday/Wednesday?'\nSchedule 1-2 free audits this week."),
            ],
            "midday": [
                ("Create case study post (20 mins)",
                 "Post format:\n- Startup name: [past client OR anonymized]\n- Problem: Investors didn't understand [their tech/product]\n- Solution: We built a motion-based [explainer/pitch animation]\n- Result: [meetings booked / funding clarity / investor interest]\nPost on LinkedIn + Twitter."),
            ],
            "evening": [
                ("Product Hunt + DMs (15 mins)",
                 "Comment on 2 new Product Hunt launches. DM 1-2 new founders from Product Hunt."),
            ],
        },
        "tuesday": {
            "morning": [
                ("Conduct founder audit (30 mins)",
                 "Conduct 1 free 30-min founder audit (if booked). Take notes on their problem + what they need.\nFollow up with: 'Here's what I'd recommend: [3-5 bullets]. This would cost £[X] and take 2 weeks. Want to move forward?'"),
            ],
            "midday": [
                ("Y Combinator outreach (15 mins)",
                 "Go to ycombinator.com/companies. Search by industry (climate, fintech, edtech).\nFind 3 founders in demo day phase. DM each: 'Saw your YC batch announcement. Helping YC founders nail demo day with motion design. Free 30-min audit to see if it's a fit?'"),
            ],
            "evening": [
                ("Reddit outreach (15 mins)",
                 "Go to r/startups or r/Entrepreneur. Find 1 post about 'pitch deck' or 'demo video'.\nReply: 'Most founder demos lose investors at [specific moment]. Here's why. I help fix this. Portfolio: [link]. DM me for free audit.'"),
            ],
        },
        "wednesday": {
            "morning": [
                ("Post: Behind-the-scenes of a founder audit (15 mins)",
                 "Show your process (what you ask, what you look for).\nExplain: 'Motion design isn't decoration. It's how you compress confusion into clarity.'\nPost on LinkedIn + Twitter."),
            ],
            "midday": [
                ("Follow up + Indie Hackers (20 mins)",
                 "Check responses from YC DMs + Reddit comment. Follow up with anyone who engaged.\nIndie Hackers: Find 1 new discussion about pitching/explaining product. Reply with value + audit offer."),
            ],
            "evening": [
                ("Product Hunt (15 mins)",
                 "Comment on 2 new Product Hunt launches with your audit offer."),
            ],
        },
        "thursday": {
            "morning": [
                ("Find angel investor event (20 mins)",
                 "Search: 'angel investor network + [your city]' or find an online founder community call.\nRSVP or join."),
            ],
            "midday": [
                ("5 more Crunchbase/LinkedIn outreach emails (20 mins)",
                 "Send 5 more Crunchbase emails (new batch of founders), OR find 5 new startups on Google.\nDM each on LinkedIn: 'Just saw you launched [company]. Love [specific thing]. Only missing: motion explainer for investors. Free audit?'"),
            ],
            "evening": [
                ("Attend founder event (30 mins)",
                 "Attend the founder event/call. Talk to 2-3 people.\nShare: 'I help founders communicate their product in 30 seconds. Motion design. Free audit if you want.'"),
            ],
        },
        "friday": {
            "morning": [
                ("Post: What does a founder motion design project look like? (15 mins)",
                 "Walk through: Week 1 (audit + script), Week 2 (design + delivery). Show behind-the-scenes of one project.\nPost on LinkedIn + Twitter."),
            ],
            "midday": [
                ("Week 2 progress check (20 mins)",
                 "Count audits conducted. Any converted to projects?\nIf yes: Start 1 project immediately. Document it for a case study."),
            ],
            "evening": [
                ("Week 2 count (15 mins)",
                 "Count total founder conversations this week (DMs + comments + calls). Write the number down."),
            ],
        },
    },
    3: {
        "monday": {
            "morning": [
                ("Follow up with audit founders (20 mins)",
                 "Follow up with founders from audits who haven't decided.\nMessage: 'How are you thinking about the motion design project? Happy to answer any questions or adjust the scope.'"),
            ],
            "midday": [
                ("Post: What every founder needs before hiring a motion designer (20 mins)",
                 "Post on LinkedIn + Twitter covering:\n- Positioning (what problem do you solve)\n- Script (what story are you telling)\n- Visual language (how does your brand move)\n- Budget (what's realistic)"),
            ],
            "evening": [
                ("Product Hunt + new founder DMs (15 mins)",
                 "Comment on 2 Product Hunt launches. DM 1-2 new founders."),
            ],
        },
        "tuesday": {
            "morning": [
                ("Start project work + document (30 mins)",
                 "If you have 1+ projects, start work. Document the process (photos, videos, screenshots).\nThis becomes your Week 3 post."),
            ],
            "midday": [
                ("5 more outreach emails (20 mins)",
                 "Send 5 more outreach emails (accelerators, Crunchbase, or direct founder emails)."),
            ],
            "evening": [
                ("Check DMs + reply (15 mins)",
                 "Check all DMs. Reply to any new founder inquiries promptly."),
            ],
        },
        "wednesday": {
            "morning": [
                ("Post: How we help founders raise faster (15 mins)",
                 "Share 1 metric/story if you have it.\nExample: 'Founder went from 0 investor meetings to 3 after we clarified their pitch with motion.'\nPost on LinkedIn + Twitter."),
            ],
            "midday": [
                ("Indie Hackers case study reply (20 mins)",
                 "Find 1 new Indie Hackers discussion. Reply with case study or insight."),
            ],
            "evening": [
                ("Continue project work (15 mins)",
                 "Continue work on active projects. Document process for content."),
            ],
        },
        "thursday": {
            "morning": [
                ("Post: What I've learned from 20 founder conversations (20 mins)",
                 "Final post of week:\n- Top 3 things founders struggle with\n- How motion design solves each\nPost on LinkedIn + Twitter."),
            ],
            "midday": [
                ("Check responses + follow up warm leads (20 mins)",
                 "Check responses to all Week 3 posts. Follow up with warm leads.\nDM 3-5 new founders from post comments."),
            ],
            "evening": [
                ("Prepare project delivery (15 mins)",
                 "If project(s) are done or near-done, prepare to deliver.\nPlan how you'll get a testimonial/case study."),
            ],
        },
        "friday": {
            "morning": [
                ("Deliver project + get testimonial (30 mins)",
                 "Deliver 1 completed project (if done). Get feedback + testimonial.\nAsk: 'Can I use this as a case study?'"),
            ],
            "midday": [
                ("3-week totals count (20 mins)",
                 "Count total founders reached this week.\nCount audits conducted this week.\nCount projects booked across all 3 weeks."),
            ],
            "evening": [
                ("Final case study post (20 mins)",
                 "Create 1 final case study post from your completed work.\nPost on LinkedIn + Twitter.\n\nCONGRATS on completing the 3-week plan!"),
            ],
        },
    },
}
