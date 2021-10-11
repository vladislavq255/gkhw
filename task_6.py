while True:
    days = 1
    start = float(input("Please, enter initial result: "))
    final = float(input("Please, enter final result: "))
    if start <= 0 or final < 0:
        print("Enter positive values")
    else:
        while start < final:
            start = start + start * 0.1
            days = days + 1
        print(f"The goal will be achieved in {days} days")
        break