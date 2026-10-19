# EXPENSE-TRACKER# Expense Tracker

A simple command-line Python program that accepts expense amounts from the user, adds them up in real time, and displays the Total Spent.

Built as **Project 2** of the DecodeLabs Industrial Training Kit (Python Programming, Batch 2026).

## Features

- Continuous data entry using a `while True` loop
- Accumulator pattern: `total += expense`
- Type conversion with `float()` so inputs are added as numbers, not joined as text
- Defensive input handling with `try / except ValueError`
- Rejects zero, negative, and non-finite values (`nan`, `inf`)
- Sentinel value `quit` for a graceful shutdown
- Final summary with transaction count, total spent, and average per expense

## Requirements

- Python 3.8 or higher
- No external libraries needed

## How to Run

1. Clone the repository or download `expense_tracker.py`.
2. Open a terminal in the project folder.
3. Run:

```
python expense_tracker.py
```

In VS Code you can also click the Run Python File button at the top right.

## How to Use

1. Type an expense amount and press Enter.
2. Repeat for every expense.
3. Type `quit` and press Enter to see the summary.

## Sample Output

```
=== EXPENSE TRACKER ===
Enter expense amount (or 'quit' to finish): 100
Added $100.00 | Running total: $100.00
Enter expense amount (or 'quit' to finish): 50
Added $50.00 | Running total: $150.00
Enter expense amount (or 'quit' to finish): ten
Invalid data. Please enter a number like 100 or 49.50.
Enter expense amount (or 'quit' to finish): -5
Expense must be a valid number greater than zero.
Enter expense amount (or 'quit' to finish): 20
Added $20.00 | Running total: $170.00
Enter expense amount (or 'quit' to finish): 10.5
Added $10.50 | Running total: $180.50
Enter expense amount (or 'quit' to finish): quit

====================================
        EXPENSE SUMMARY
====================================
Transactions entered : 4
Total Spent          : $180.50
Average per expense  : $45.12
====================================
```

## Project Structure

```
PROJECT 2/
├── expense_tracker.py
└── README.md
```

## Concepts Covered

| Concept | Where it is used |
|---|---|
| Accumulator | `total += expense` inside the loop |
| State initialization | `total = 0` outside the loop |
| Infinite loop with break | `while True` stopped by `quit` |
| Input validation | `try / except ValueError` and range checks |
| Separation of logic and display | `read_expense()` and `show_summary()` functions |

## Author

**Zaid Bin Aamir**
Domain: Python Programming
