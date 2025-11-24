"""
Simple AD Disabled Login Alert (Beginner-Friendly)
This script simulates monitoring login attempts from disabled AD accounts.
For demo purposes, it uses a sample list of login attempts.
"""

# Sample list of login attempts (in real life, read from logs)
login_attempts = [
    {"username": "john", "status": "success"},
    {"username": "mary", "status": "failed", "disabled": True},
    {"username": "alex", "status": "success"},
    {"username": "disabled_user1", "status": "failed", "disabled": True}
]

# Check for logins from disabled users
print("=== Checking for disabled account logins ===")
alert_count = 0
for attempt in login_attempts:
    if attempt.get("disabled") and attempt["status"] == "failed":
        print(f"⚠️ ALERT: Disabled account '{attempt['username']}' attempted to log in!")
        alert_count += 1

if alert_count == 0:
    print("No disabled accounts attempted login.")
