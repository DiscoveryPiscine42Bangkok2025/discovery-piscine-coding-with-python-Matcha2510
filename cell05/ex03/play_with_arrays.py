#cell 5-3
num1 = [2,8,9,48,8,22,-12,2]
num2 = []
for i in num1 :
       if i >= 5 :
            num2.append(i)

num3 = set([j+2 for j in num2])

print(num3)


