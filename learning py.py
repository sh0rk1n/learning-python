# """"
# def addition(x,y):
#     return x+y
# def substraction(x,y):
#     return x-y
# def multiplication(x,y):
#     return x*y
# def division(x,y):
#     if y!=0:
#      return x/y
#     else:
#         return "Can't divide by zero!"

# num1 = float(input("Enter first number: "))
# operator =input("Enter operator (+,-,*,/): ")
# num2 = float(input("Enter second number: "))
# if operator == "+":
#   result = addition(num1,num2)
# elif operator == "-":
#     result = substraction(num1,num2)
# elif operator == "*":
#     result = multiplication(num1,num2) # digit1 = digit1 + digit2
# elif operator == "/":
#     result = division(num1,num2)
# else:
#     result = "Invalid operator"
# print(f"Result: {result}")
# """
# """def parity(x):
#     if (x%2==0):
#         print("The number is even")
#     else:
#         print ("The number is not even")
# number = float(input("Enter number: "))
# parity(number)


# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n*factorial(n-1)
# n = int(input("Enter number: "))
# result =factorial(n)
# print(result)
# """
# """"
# #5
# def fibonacci(n):
#     fib_squence=[]
#     a,b=0,1

#     for _ in range(n):
#         fib_squence.append(a)
#         a,b=b,a+b
#     return fib_squence

# num=int(input("Enter the number of fibonacci squence to generate: "))
# fib_result = fibonacci(num)
# print(f"fib result {num}: {fib_result}")

# #6
# numbers = [2,4,6,8,10,55,14]
# sum_result= sum(numbers)
# average_result=sum_result/len(numbers)

# max_result = max(numbers)
# min_result = min(numbers)

# print(f"List of numbers: {numbers}")
# print(f"Sum: {sum_result}")
# print(f"Average: {average_result}")
# print(f"Maximum: {max_result}")
# print(f"Minimum: {min_result}")
# """

# """""
# n = 5

# # Using a loop variable
# for i in range(n):
#     print(f"Iteration {i}")

# # Using a throwaway variable
# for _ in range(n):
#     print(f"Another iteration{_}")

# #GAME OVER 2.0
# print("Game Over")
# print("Toжe",  "самое", "сообщение")
# print ( "Только",
# "чуть-чуть",
# "побольше")
# print("Boт", end=" ") # без перехода на новую строку после выполнения: end=" "
# print ("оно ... ")
# print(
# ╔═══╗╔══╗╔╗──╔╗╔═══╗──╔══╗╔╗╔╗╔═══╗╔═══╗
# ║╔══╝║╔╗║║║──║║║╔══╝──║╔╗║║║║║║╔══╝║╔═╗║
# ║║╔═╗║╚╝║║╚╗╔╝║║╚══╗──║║║║║║║║║╚══╗║╚═╝║
# ║║╚╗║║╔╗║║╔╗╔╗║║╔══╝──║║║║║╚╝║║╔══╝║╔╗╔╝
# ║╚═╝║║║║║║║╚╝║║║╚══╗──║╚╝║╚╗╔╝║╚══╗║║║║
# ╚═══╝╚╝╚╝╚╝──╚╝╚═══╝──╚══╝─╚╝─╚═══╝╚╝╚╝ \n but simply difference)

# print("Программа 'Game Over' 2.0" ) # ALTERNATIVE print('Программа "Game Over" 2.0' )

# print("То", "да")

# print ("Воображаемые благодарности")
# print ("\t Воображаемые благодарности")#escape sequences 
# print ("\t \t Воображаемые благодарности")
# print("\t\t\t \\ \\ \\ \\ \\ \\ \\")
# print ("\t \t\t Шоркин")
# print("\t\t\t \\ \\ \\ \\ \\ \\ \\")
# print("моему парикмахеру Генри по прозвищу \'Великолепный\'. который не знает слова\"невозможно\".")
# print ("\"Apple\"")
# print ("\a")
# print ("Две " + "строки " + "удив" + "ит вас." )#  "конкатенация"

# text = "awesome"
# def func():
#     text = "fantastic"
#     print("Python is " + text, end=", ")
# func()
# print("Python is " +  text)

# print("Ecли беременная самка бегемота массой 800 кг родит детеныша массой 40 кг.")
# print("нo затем съест 20 кг корма. то сколько она будет после всего этого весить?")
# print("800-40+20 = ", 800-40+20)

# print(19/4) # деление с остатком /decimal/
# print(19//4) # целочисленное деление (без остатка)
# print(19%4) # остаток пишется в ответе 

# quote="Думаю СОСиСКА"
# print(quote.upper()) # uppercase 
# print(quote.lower()) # lowercase
# print(quote.title()) # title
# print(quote.replace("Думаю", "Хочу")) # replace
# quote="Думаю СОСиСКА"
# print(quote)
# print(quote.swapcase()) # меняет регистр каждого символа
# print(quote.capitalize()) # новая строка где первый символ - верх регистр а ост нижн регистр
# print(quote.strip()) # в нач и конце убрана табуляция

# car = "1"
# s="2"
# b=car+s
# print(b)

# car=int(car)
# s=int(s)
# b=car+s
# print(b)
# str(b)
# print(b)

# import random # модуль - совокупность ф-ций

# die1 = random.randint(1,6) # точечная нотациЯ  [1;6]
# die2=random.randrange(6)+1 # randrange(6) - от 0 до 5 поэтому +1
# total = die1+die2 # randint(1,6) == randrange(6) + 1
# print("При вашем броске выпало", die1, "и",die2,"очков в сумме",total)

# password=input("Введите пароль: ")
# if password == "secret" :
#     print("Доступ открыт")
#     print(0)
# print(1)

# print("Добро пожаловать!")
# money=int(input("Сколько $ вы готовы дать: "))
# if money: # equivalent if money !=0:
#     print("Проходить")
# else:
#     print("wait")
# count = 0
# while True:
#     count+=1
#     if count >10:
#         break
#     if count == 5:
#         continue
#     print(count)
# import random
# print('\t \t Игра "Отгадай число"')
# print("Добро пожаловать! Правилав игры просты: мы загадываем число от 1 до 100 - ты отгадываешь.\n \t  Удачи! ")

# start = input("Нажми Enter , чтобы начать: ")
# random = random.randint(0,100)
# print(random)

# user_answer=int(input("Я загадал число! Попробуй угадать: "))
# while user_answer!=random:
#     if user_answer > random: 
#         print("Ты близок! Выбери число поменьше.")
#     else :  
#         print("Ну почти! Возьми немного побольше.")
#     user_answer = int(input("Попробуй еще раз: "))
# word = input("Введи слово: ")
# print("Буквы слова по порядку: ")
# for letter in word:
#     print(letter)

# print("Посчитаем")
# for i in range(11): # [0;10]
#     print(i, end=" ")
# print("\nОбратный порядок")
# for i in range(10, -1,-1): # [10;0]
#     print(i,end=" ")
# print( "\n 111")
# for i in range(0,51,5):
#     print(i,end=" ")
# for _ in range(10):
#     print("Привет")

# message = input("Введите текст: ")
# print("Длина текста: ", len(message))
# print("Самая встр буква: 'т',  ")
# if "т" in message:
#     print("встречается в вашем тексте.")
# else:
#     print("не встречается в вашем тексте.")        
# import random
# word = 'индекс'

# print("В переменной word хранится слово: ", word)
# high=len(word)
# low = -len(word)
# for _ in range(10):
#     pos = random.randrange(low,high)
#     print("word[",pos,"]\t", word[pos])
# message=input("Введите текст: ")
# new_message=''
# DIRECT = "ауоиэы"
# print()
# for letter in message:
#     if letter.lower() not in DIRECT:
#         new_message+=letter
#         print(new_message)
# print("Введи индекс: ")
# start = None
# while start != " ":
#     start=input("Введите нач.позицию: ")
#     if start:
#         start=int(start)
#         finish = int(input("Конечная позиция: "))
#         print("Срез word[",start,":",finish,"] выглядит как", end=" ")
#         print(word[start:finish])
# word = "пицца"
# print(word[-5:5])
# print(word[:5]) # [0;5]
# print(word[2:])# [2:5]
# print(word[:] ) # [0:5]
        
# inventory=("меч",
#            "кольчуга",
#            "щит",
#            "целебное снадобье")
# print("\nСодержимое кортежа:\n", inventory)
# print("\nИтак, в вашем арсенале: ")
# for item in inventory:
#     print(item) 
# print("\nСейчас в вашем распоряжении: ", len(inventory), "предмета/-ов.")
# if "целебное снадобье" in inventory:
#     print("\nУ тебя есть хилка! ")
# index=int(input("Введите индекс одного из предметов: ",))
# print("Под индексом",index, "в арсенале лежит: ", inventory[index])
# import random
# WORDS = ("питон", "анаграмма", "простая", "сложная", "ответ", "подстанник")
# word = random.choice(WORDS)
# correct = word

# jumble = ""
# while word:
#     pos = random.randrange(len(word))
 

# inventory = ["меч", "кольчуга", "щит", "целебное снадобье"] # списки -  [] , кортежи - ()
# print("\n Вы имеете: ")
# for item in inventory:
#     print(item)
# print("\n Вы обменяли меч на арбалет!")
# inventory[0] = "арбалет"
# print("\n теперь: ")
# print(inventory)
# #del inventory[2]
# #print(inventory)
# del inventory[:2]
# print(inventory)
   
# scores=[]
# choice=None
# while choice !="0":
#     print(

#     Рекорды
#     0 - Выйти
#     1 - Показать рекорды
#     2 - Добавить рекорд
#     3 - Удалить рекорд
#     4 - Сортировать список
#     )
#     choice = input("Ваш выбор: ")
#     print()
#     if choice =="0":
#         print("До свидания!")
#     elif choice == "1":
#         print("Рекорды")
#         for score in scores:
#             print(score)
#     elif choice == "2":
#         score = int(input( "Впишите свой рекорд: "))
#         scores.append(score) # добавляет значение в списке
#     elif choice == "3":
#         score = int(input("Какой из рядов удалить?"))
#         if score in scores:
#             scores.remove(score) # remove - удаляет элемент заданный не номером позиции а значением, del - номером позиций (del score[2] и тп)
#         else:
#             print("Результат: ", score, "не содержится в списке рекордов.")
#     elif choice == "4":
#         scores.sort(reverse=True) # сортировка от меньших значений - к большим; если передать значение reverse=True , то будет с больших до меньших
#         # reverse - обращает порядок элементов списка
#     else:
#         print("Извините, в меню нет пункта", choice)
#     input("\n\nНажмите Enter, чтобы выйти.")
#     #  count() - сообщает сколько раз данное значение входит в список; index() - возвращает номер первой  из позиций списка, которые заполнены данным значением
#     # insert(i, значение) - вставляет значение в позицию номер i
#     # remove() - удаляет первое вхождение  данного значения в список
#     # pop([i]) - возвращает значение в позиции номер i и удаляет этот элемент из списка (если аргумент не передан то будет возвращаться и удаляться последний элемент)
#     """
    #nested = ["раз", ("два", "три"), ["четыре", "пять"]]
# scores = [("Маша",1500),("Петя",2000),("Вася",3000)]
# print(scores[2][0]) # Вывод: Вася

# scores = []
# choice = None
# while choice != "0":
#     print(
#         """
#         Рекорды 2.0     ё   у ма
#         0 - Выйти
#         1 - Показать рекорды
#         2 - Добавить рекорды
#         """
#     )
#     choice = input( "Ваш выбор: ")
#     print()

#     if choice == "0":
#         print("До свидания!")
#     elif choice == "1":
#         print("Рекорды\n")
#         print("ИМЯ\tРЕЗУЛЬТАТ")
#         for entry in scores:
#             score,name = entry
#             print(name, "\t", score)
#     elif choice == "2":
#         name = input("Введите имя: ")
#         score = int(input("Впишите результат: "))
#         entry = (score,name)
#         scores.append(entry)
#         scores.sort(reverse=True)
#         scores = scores[:5]
#     else:
#         print("Извините, в меню нет пункта", choice)
# input("\n\nНажмите Enter, чтобы выйти.")
# Пример списка dd
n = 6%6
print(n)