import csv
from datetime import datetime, date

DATE_FORMAT = "%Y-%m-%d"

def parse_date(value: str) -> date:
    return datetime.strptime(value.strip(), DATE_FORMAT).date()

def main():
    filename = "action_items.csv"
    today = date.today()

    try:
        with open(filename, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            items = list(reader)
    except FileNotFoundError:
        print(f"ERROR: Could not find '{filename}'. Make sure it's in the same folder as remind.py")
        return

    if not items:
        print("No action items found.")
        return

    print(f"Action Item Reminders (Today: {today.isoformat()})")
    print("-" * 60)

    for row in items:
        title = (row.get("title") or "").strip()
        owner = (row.get("owner") or "").strip()
        due = (row.get("due_date") or "").strip()
        status = (row.get("status") or "").strip().lower()

        if not title or not owner or not due:
            print("Skipping row with missing required fields (title/owner/due_date).")
            continue

        try:
            due_date = parse_date(due)
        except ValueError:
            print(f"Skipping '{title}' — invalid due_date '{due}'. Use YYYY-MM-DD.")
            continue

        days_left = (due_date - today).days

        # Only remind for open/in-progress items
        if status in ("done", "closed", "complete", "completed"):
            continue

        if days_left < 0:
            print(f"OVERDUE ({abs(days_left)} days): {title} | Owner: {owner} | Due: {due}")
        elif days_left <= 3:
            print(f"DUE SOON ({days_left} days): {title} | Owner: {owner} | Due: {due}")

if __name__ == "__main__":
    main()
