**Local Connect**
Local Connect is a simple digital tool designed to help people easily find local businesses around them — especially those that often go unnoticed. From small shops and salons to local restaurants and service providers, this platform brings them all into one place, making discovery easier and more inclusive for everyone.

**Why We Built This**
In many communities, local businesses struggle to be found. Their information isn’t available online, and word of mouth can only go so far. People often don't know where to get affordable services close to home unless they physically go out searching.

Local Connect was built to solve this challenge — to help connect people to local businesses through a centralized, accessible, and easy-to-use platform.

**What You Can Do With Local Connect**
🏪 Add new businesses to the system

🔎 Search businesses by location and category (e.g., “salon in Kimironko”)

📋 View all registered businesses in one place

🌟 Leave reviews and rate businesses

📞 Get contact details and website links directly

**Who Is This For?**
- Business owners who want more visibility

- People looking for reliable local services

 -Developers and community organizers helping small businesses go digital

- Students or anyone wanting to learn how databases and reviews systems work

**How It Works (Quick Guide)**
This system is written in Python and uses a local SQLite database to store data. Everything runs in your terminal/command line interface.

**Requirements**
Python 3.x
No external libraries needed — just Python’s built-in sqlite3

**How to Use It**

**1. Start the Program**
From your terminal, write:
python local_connect.py

You’ll see a menu like:

…………… Welcome to Local Connect ……………
1. Add Business
2. View All Businesses
3. Search Businesses
4. Leave Review
5. Exit

**2. Add a Business**
Follow the prompts to input:

Name

Category (e.g., Restaurant, Salon)

Location (e.g., Kimironko)

Contact info (phone/email)

Website

The system prevents duplicates by checking if a similar business already exists.

**3. Search for Businesses**
You can look for businesses by:

Location (e.g., Kicukiro)

Optionally filter by category (e.g., Grocery, Mechanic)

Results will show name, contact info, and average rating.

**4. Leave a Review**
Help others by giving your feedback:

Enter the business name and location

Give a rating (1–5 stars)

Leave a comment

The system updates the business’s average rating.

**Files in This Project**
local_connect.py	Main program with all features (add/search/review/view)
local_connect.db	SQLite database (auto-created when you run the app)

**Note for First-Time Users**
The database is automatically created when you run the program — no setup required.

If you make a typo or enter invalid info, the system will help you correct it.

You don’t need internet access for it to work — it’s a local solution for local problems.

**Closing Thoughts**
Local Connect is a student-built system with a real-world mission:
**To empower small businesses and make life easier for people in their communities. It’s a reminder that sometimes, digital solutions don’t have to be complex to make a difference.**

Together, let’s make sure no local business is left behind. 🫱🏽‍🫲🏾
