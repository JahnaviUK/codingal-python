def calculate_due_amount(total_bill, amount_paid):
    """This function calculates the due amount after payment."""
    due = total_bill - amount_paid
    return due
total = float(input("Enter total bill amount: ₹"))
paid = float(input("Enter amount paid by customer: ₹"))

due_amount = calculate_due_amount(total, paid)

if due_amount > 0:
    print("The customer still owes ₹{due_amount:}.")
elif due_amount < 0:
    print("Extra payment of ₹{-due_amount:3} received. Please return the change.")
else:
    print("The bill is fully paid. No due amount.")