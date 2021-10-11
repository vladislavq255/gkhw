num = int(input("Please enter integer: "))
max = 0
num_rem = num
while num_rem > 0:
    last = num_rem % 10
    if last > max:
        max = last
        if last == 9:
            break
    num_rem = num_rem // 10
print (f"The higher number in {num} is {max}")