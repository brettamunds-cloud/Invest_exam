# Version 1 : Basic Investment Calculator
initial_investment = 10000
final_value = 1200
profit = final_value - initial_investment
return_pct = (profit/initial_investment) *100

print("INVESTMENT CALCULATOR")
print (f"Initial Investment: ${initial_investment}")
print (f"Final Value: ${final_value}")
print (f"Profit : ${profit}")
print (f"Investment Return: ${return_pct:.2F}%")