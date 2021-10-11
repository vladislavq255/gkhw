revenue = float(input(f"Please input revenue: -  "))
costs = float(input(f"Please input costs: - "))
result = revenue - costs
if result > 0:
    print(f"Profit- {result}")
    print(f"profitability - {100 * result/revenue:.1f}%")
    employees = int(input("Please enter number of employees: -"))
    print(f"Profit for employees - {result / employees: 1f.}%")
elif result < 0:
    print(f"Damages - {result}")
else: print("break-even")