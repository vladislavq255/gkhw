num = int(input("Please enter the number greater than 0: "))
while num < 0:
    print(f'Number is less than 0')
    num = int(input("Please enter the number greater than 0: "))
print(f"{num}{num+num}{num+num+num}")