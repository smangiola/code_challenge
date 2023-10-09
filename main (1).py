rent_expense = int(input("How much is your rent?"))
electric_expense = int(input("How much is your electric bill for this month?"))
water_expense = int(input("How much is your water bill for this month?"))
internet_expense = int(input("How much is your internet bill for this month?"))
personal_expense = int(input("How much have your personal expenses cost this month?"))
grocery_expense = int(input("How much have your groceries cost this month?"))
monthly_expense = rent_expense + electric_expense + water_expense + internet_expense + personal_expense + grocery_expense
print("Your monthly expense is", monthly_expense, "dollars.")