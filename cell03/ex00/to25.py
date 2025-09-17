#cell 3.0
num1 = int(input("Enter a number less than 25:"))
if num1 > 25 :
    print("Error")
else :
    while num1 < 26 :
         print(f'Inside the loop, my variable is {num1}')
         num1 = num1 + 1