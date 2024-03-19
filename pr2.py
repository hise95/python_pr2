#1
a = 3
b = 8

#2
#Істинна
(5 > 3) and (10 <= 10) and ("a" < "b")
(not (2 == 2)) and (4 != 4) or ("hello" == "hello")
#Хибність
(5 > 10) and (10 > 5) and ("a" > "b")
(not (2 != 2)) and (4 == 4) and ("world" != "world")

#3
#Істинна
(5 < 3) or (10 >= 10) or ("a" > "b")
(not (2 == 2)) or (4 != 4) and ("hello" == "world")
#Хибність
(5 > 10) or (10 < 5) or ("a" < "b")
(not (2 != 2)) or (4 == 4) or ("world" != "world")

#4
name = "Ivan"

is_long_name = len(name) >= 5

print(f"Чи довше ім'я за 5 символів? {is_long_name}")

#5-6
x = 5

if x > 0:
  print("Значення змінної x більше 0")
else:
  print("Значення змінної x не більше 0")
#Від'ємне значення змінної
x = -2

if x > 0:
  print("Значення змінної x більше 0")
else:
  print("Значення змінної x не більше 0")

#7
a = 10
b = 5

if a > b:
  c = a - b
else:
  if a < b:
    c = a + b
  else:
    c = a

print(f"Значення c: {c}")

#8
number = float(input("Введіть дійсне число: "))

if number > 0:
  print("Число є додатним")
elif number < 0:
  print("Число є від'ємним")
else:
  print("Число є нулем")

#9.1
a, b = 0, 1

n = 20

i = 0
while i < n:
  print(a)

  temp = a
  a = b
  b = temp + b

  i += 1


start = 5
end = 20

i = start
while i <= end:
  print(a)

  temp = a
  a = b
  b = temp + b

  i += 1

#9.2
i = 0
while i <= 20:
  if i % 2 == 0:
    print(i)
  i += 1

i = -1
while i >= -21:
  if i % 3 == 0:
    print(i)
  i -= 1

#10
sum = 0
count = 0

numbers = []
for i in range(int(input("Введіть кількість чисел: "))):
  number = float(input("Введіть число: "))
  if number > 0:
    numbers.append(number)
    sum += number
    count += 1

if count > 0:
  average = sum / count
else:
  average = 0

print(f"Сума: {sum}")
print(f"Середнє арифметичне: {average}")
