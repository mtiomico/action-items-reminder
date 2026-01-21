# Action Items Reminder Tool

A lightweight Python script that reads action items from a CSV file and prints reminders for items that are due soon (within 3 days) or overdue.

## Why I built this
I wanted a simple tool that mirrors real operational work: tracking action items, due dates, and improving follow-through with clear reminders.

## How it works
- Reads `action_items.csv`
- Skips completed items
- Prints reminders for items due within 3 days or overdue

## Run locally
1. Make sure you have Python 3 installed
2. In Terminal, go to the folder:
   ```bash
   cd path/to/action-items-reminder

## Email reminders (optional)
This tool can send reminder emails via SMTP.

1) Create a `.env` file (do NOT commit it) based on `.env.example`
2) Recommended: Gmail App Passwords (requires 2-step verification)
3) Run:
```bash
python3 remind.py
