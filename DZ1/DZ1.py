# *******************
width = int(input("введите ширину: "))
height = int(input("введите высоту: "))

for h in range(height):
    for w in range(width):
        if w == 0 or w == width - 1:
            print("|", end="")
        elif h == 0 or h == height - 1:
            print("-", end="")
        else:
            print("*", end="")
    print(end="\n")
# *****************

# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

a = int(input("a: "))
b = int(input("b: "))
c = int(input("с: "))

if (a + b) > c and (b + c) > a and (c + a) > b:
    print("Это треугольник")
    if a == b == c:
        print("и этот треугольник равносторонний")
    elif a == b or b == c or c == a:
        print("и этот треугольник равнобедеренный")
    else:
        print("и он разносторонний")
else:
    print("это не треугольник!")

# *****************
# Напишите программу, которая считает количество простых чисел в заданной
# последовательности и выводит ответ на экран.

n = int(input("введите количество: "))
count = 0
for i in range(n):
    num = int(input("введите число: "))
    if num > 1:
        for j in range(2, num):
            if num % j == 0:
                break
        else:
            count += 1
            print(count)

print("итого ", count)

# яма
num = int(input("введите число: "))

rows = num  # ряд
cols = num * 2  # столбец

for row in range(1, rows + 1):
    for col in range(cols):
        if col < row:
            print(num, end=" ")
            num -= 1
        elif col > cols - 1 - row:
            num += 1
            print(num, end=" ")
        else:
            print("*", end=" ")
    print(end="\n")

""" Мальчик загадывает число между 1 и 100 (включительно). Компьютер может # type: ignore
спросить у мальчика: «Твоё число равно, меньше или больше, чем число N?»,
где N — число, которое хочет проверить компьютер. Мальчик отвечает одним из
трёх чисел: 1 — равно, 2 — больше, 3 — меньше.
Напишите программу, которая с помощью цепочки таких вопросов и ответов
мальчика угадывает число. """

print("загадайте число от 1 до 100")
print("***************************")
i = 1
n = 100
mid = (i + n) // 2
while i < n:
    print(
        "введите '1' если число равно ",
        mid,
        ", '2' если число больше ",
        mid,
        ", '3' если число меньше ",
        mid,
        end="\n",
    )
    value = int(input())
    # print(value)
    if value == 1:
        print("вы загадали число ", mid)
        break
    elif value == 2:
        i = mid
        # print("i ", i)
        mid = (i + n) // 2
        # print("mid ", mid)
    elif value == 3:
        n = mid
        # print("n ", n)
        mid = (i + n) // 2
        # print("mid ", mid)
