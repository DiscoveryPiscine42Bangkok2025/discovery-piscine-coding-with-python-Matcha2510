#cell 4-1
num1 = int(input("please tell me your age: "))
year = 10
print(f'You are currently {num1} years old.')
for i in range(3):
    print(f'In {year}, you will be {num1 + year} years old.')
    year += 10
