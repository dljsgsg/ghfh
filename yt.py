#1
a = int(input("tell first number"))
b = int(input("tell second number"))
cot = 0
ctep = 0


for i in range(a, b + 1):
    cot += i
    ctep += 1



print(f"results: {cot}")
print(f"среднее арифметическое: { cot / ctep }")
#3
i = int(input("tell your number"))
print('*' * i)
#4
i = int(input("tell your number"))
print('&' * i)