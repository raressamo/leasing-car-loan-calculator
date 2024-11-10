def calculate_car_leasing_loan():
    print("Car Leasing Loan Calculator")
    print("----------------------------")
    purchase_price = float(input("Enter the purchase price of the car: $"))
    down_payment = float(input("Enter the down payment: $"))
    interest_rate = float(input("Enter the interest rate (in %): "))
    lease_term = int(input("Enter the lease term (in months): "))
    loan_amount = purchase_price - down_payment
    monthly_interest_rate = (interest_rate / 100) / 12
    monthly_payment = loan_amount * monthly_interest_rate * (
        1 + monthly_interest_rate)**lease_term / (
            (1 + monthly_interest_rate)**lease_term - 1)
    print(f"Monthly payment: ${monthly_payment:.2f}")


calculate_car_leasing_loan()
