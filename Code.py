import random
from datetime import datetime

subjects = {
    "tech": [
        "Google Cloud India", "TCS Developers", "Infosys AI Lab", "ISRO DevOps Team", "MeitY (Ministry of Electronics)"
    ],
    "office": [
        "HR Manager", "Project Lead", "QA Automation Team", "Finance Department", "Client Account Manager"
    ],
    "politics": [
        "PMO Office", "Election Commission", "Ministry of IT", "Digital India Task Force", "Cybersecurity Council"
    ]
}

actions = {
    "tech": [
        "released an unstable update", "exposed user credentials", "accidentally deleted production database", 
        "triggered service downtime", "rolled back latest patch without changelog"
    ],
    "office": [
        "scheduled a surprise meeting", "shared incorrect report with client", "delayed sprint delivery", 
        "approved budget without review", "forgot to renew software license"
    ],
    "politics": [
        "announced AI guidelines", "proposed new data privacy bill", "launched tech upskilling initiative", 
        "partnered with top IT firms", "allocated funds for digital infra"
    ]
}

suffixes = {
    "tech": [
        "causing major downtime across Asia", "impacting over 10 million users", "raising serious security concerns", 
        "forcing emergency patch deployment", "getting flagged in internal audit"
    ],
    "office": [
        "resulting in escalation from client", "marked critical by senior management", "leading to urgent team sync", 
        "now under internal investigation", "prompting a mail from CTO"
    ],
    "politics": [
        "hailed by tech leaders", "criticized by digital rights groups", "creating buzz among startups", 
        "welcomed by industry bodies", "highlighted in parliament session"
    ]
}

# Headline generator
print("Welcome to Fake News Headline Generator 🎉")
category = input("Choose category (tech / office / politics): ").strip().lower()

if category not in subjects:
    print("Invalid category. Please restart and choose from tech, office, politics.")
else:
    count = int(input("How many headlines do you want? "))

    for _ in range(count):
        subject = random.choice(subjects[category])
        action = random.choice(actions[category])
        suffix = random.choice(suffixes[category])
        timestamp = datetime.now().strftime("[%d-%m-%Y %H:%M:%S]")

        headline = f"{timestamp} 🚨 BREAKING NEWS: {subject} {action}, {suffix}!"
        print("\n" + headline)

    print("\nThanks for using the Fake News Generator. Stay fake, stay fun! 😄")
