# 📰 Fake News Headline Generator

Welcome to the **Fake News Headline Generator** — a fun and interactive Python project that produces fake, yet oddly believable news headlines. Choose from categories like **Tech**, **Office**, or **Politics**, and get instant headlines with realistic phrasing and timestamped drama!

---

## 📌 Features

✅ Category-based headlines (Tech, Office, Politics)  
✅ Randomized subject, action, and suffix for uniqueness  
✅ Timestamped news-style formatting  
✅ Simple and user-friendly CLI (Command Line Interface)  
✅ Pure Python — no external libraries needed  

---

## 🧠 Project Overview

This script mimics the structure of a real-world news flash by randomly assembling three core components:

| Component | Description |
|----------|-------------|
| **Subject** | The entity (e.g., "TCS Developers", "PMO Office") |
| **Action**  | What the subject did (e.g., "released unstable update") |
| **Suffix**  | Result or outcome (e.g., "causing downtime in Asia") |

Each generated headline includes a **timestamp** to make it feel like a real breaking update.

🧭 User Interaction Flow 
The interaction with the script is fully terminal-based and user-friendly:

🟢 Step 1: Choose a Category
After starting the script, the user is prompted to select one of the following categories:


Welcome to Fake News Headline Generator 🎉
Choose category (tech / office / politics): tech
Accepted options:

tech

office

politics

If an invalid option is entered:
Invalid category. Please restart and choose from tech, office, politics.

🟢 Step 2: Enter the Number of Headlines
Next, the script asks how many headlines should be generated:


How many headlines do you want? 3
🟢 Step 3: Headline Generation Output
The script then prints the specified number of headlines like this:


[18-07-2025 00:23:12] 🚨 BREAKING NEWS: Infosys AI Lab triggered service downtime, getting flagged in internal audit!

[18-07-2025 00:23:13] 🚨 BREAKING NEWS: Google Cloud India released an unstable update, causing major downtime across Asia!

[18-07-2025 00:23:14] 🚨 BREAKING NEWS: ISRO DevOps Team rolled back latest patch without changelog, raising serious security concerns!

🟢 Step 4: Closing Message
At the end, a fun closing line is displayed:

Thanks for using the Fake News Generator. Stay fake, stay fun! 😄


