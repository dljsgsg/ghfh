from random import randint

n = randint(1,500)

while 1:
  k = input("Угадайте целое число от 1 до 500: ")

  if k == "Выход":
    print("В следующий раз повезёт!")
    break

  k = int(k)

  if k == n:
    print("Вы угадали")
    break

  print("Ваше число " + ("больше" if k > n else "меньше") + ", чем задумал компьютер")

print("Загаданным числом было: " + str(n))


#2

coast = float(1)
rub = 0,89

while int(coast) != 0:
  coast = float(input('Введите стоимость товара  доллорах: '))
  rub = round((coast * 1.25) * 100, 2)
  if coast > 0:
    print('Стоимость товара в рублях составила:', rub)
    break
    #3
  # 3
  a = int(input("tell first number"))
  b = int(input("tell second number"))
  c = int(input("tell your third number"))
  for i in range(a, b + 1):

    if c not in range(a, b + 1):
      print("print your number again")
    if i == c:
      print(f"!{i}!", end=" ")
      continue
    print(i, end=" ")