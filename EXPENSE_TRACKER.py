import math


def read_expense():
    raw = input("Enter expense amount (or 'quit' to finish): ").strip()
    if raw.lower() == "quit":
        return None
    try:
        amount = float(raw)
    except ValueError:
        print("Invalid data. Please enter a number like 100 or 49.50.")
        return -1
    if not math.isfinite(amount) or amount <= 0:
        print("Expense must be a valid number greater than zero.")
        return -1
    return amount


def show_summary(total, count):
    print("\n" + "=" * 36)
    print("        EXPENSE SUMMARY")
    print("=" * 36)
    print(f"Transactions entered : {count}")
    print(f"Total Spent          : ${total:,.2f}")
    if count:
        print(f"Average per expense  : ${total / count:,.2f}")
    print("=" * 36)


def main():
    total = 0
    count = 0
    print("=== EXPENSE TRACKER ===")
    while True:
        expense = read_expense()
        if expense is None:
            break
        if expense == -1:
            continue
        total += expense
        count += 1
        print(f"Added ${expense:,.2f} | Running total: ${total:,.2f}")
    show_summary(total, count)


if __name__ == "__main__":
    main()