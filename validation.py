def get_amount():
    try:
        return float(input("Enter amount: ₹"))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return None