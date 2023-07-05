# # # import os
# # #
# # # root = os.getcwd()
# # # fname = 'info.txt'
# # # list_1 = [1, 3, 5, 8, 12, 24, 37, 55, 89]
# # # list_2 = [2, 4, 5, 8, 14, 24, 39, 58, 89]
# # # q=0
# # # if os.path.isfile(fname):
# # #     with open(fname,'wt', encoding='utf-8') as file:
# # #         for i in list_1:
# # #             if int(i) == list_2[q]:
# # #                 file.write +=i
# # #                 q+=1
# # #     file.close()
# # # if os.path.isfile(fname):
# # #     file = open('info.txt', wt, encoding='utf-8')
# # #     print('Имя файла:')
# # # print(file)
# # import pickle
# # with open('dictinary.bin', 'rb') as f:
# #     d = pickle.load(f)
# #     # 'стол' : 'table',
# #     # 'стул' : 'chair'
# #
# # while True:
# #     word = input('Введите слова для перевода (или QQ - для входа): ')
# #     if word == 'QQ':
# #         break
# #     if word in d:
# #         print(f'Слово {word} переводится как {d[word]}.')
# #     else:
# #         print(' не знаю этого слова, но можете мнен подсказать')
# #         new_word = input(f'Как переводится {word}: ')
# #         d[word] = new_word
# # with open('dictionary.bin', 'wb') as f:
# #     pickle.dump(d, f)
# # # with open(fname,'rb') as file:
# # #     d = pickle.load(file)
# # #
# # # print(d)
# #
# # пишу слово стул.стол - переводит.
# # ввожу слово яблоко - пишет "такого слова нет, хотите добавить?" добавляем перевод.
# # всё это записывается в файл.
# #
# # d = dict()
# # with open ('dictinary.txt', 'rt', encoding='utf-8') as f:
# #   keys = f.readline().rstrip('\n')
# #   values = f.readline().rstrip('\n')
# #
# # print(keys)
# # print(values)
# # print(
# # print('Делим 10 на любое целое число!')
# # try:
# #     value = int(input('На что делим 10 (введите целое число): '))
# #     res = 10 / value
# #     print(f'Остаток от деления {value} на 10 будет {res}.')
# #
# # except ValueError:
# #     print('Вас просили ввести целое число. А вы!!!')
# # except ZeroDivisionError:
# #     print('а ноль делить нельзя')
# # except Exception as exp:
# #     print( 'Вот что произошло', exp, exp.__class__.__name__)
# # finally:
# #     print('Всё относительно!')
# # is_opened = False
# # try:
# #     f = open('informer.txt')
# #     print(f.read())
# #     is_opened = Truy
# # except FileNotFoundError:
# #     print('Файл не существует')
# #     is_opened = False
# # finally:
# #     if is_opened:
# #         print('Файл прочитан и закрыт.')
# #         f.close()
# #     else:
# #         print('Файл и не открывался, закрывать нечего!')
# #
# #
# # x = input('Введите число.')
# # while True:
# #     try:
# #         int(x)
# #         print('Спасибо. Досвидание!')
# #         break
# #     except ValueError:
# #         x = input('Введите число.')
# # except:
# #     if x == complex:
# #         x = input('Введите число.')
# # except Exception as exp:
# #      print( 'Вот что произошло', exp)
# # finally:
# #     print('Спасибо!')
# #
# # s_num = input(f'Прошу ввести число в диапазоне от {min_val} до {max_val}: ')
# #
# #
# #     if not min_val<= num <=max_val:
# #         x = True
# #         raise ValueError('Введённое число вне заданного диапазона')
# # except ValueError as exp:
# #     if x == False:
# #         print(f'Вас просили ввести целое число, а Вы ввели "{s_num}"')
# #     print('Будьте внимательней', exp)
# #
# # while True:
# #     a = input('Введите первое число: ')
# #     b = input('Введите второе число: ')
# #     if a.isdigit() and b.isdigit():
# #         if int(b) == 0:
# #             print('На ноль делить нельзя')
# #         else:
# #             print(int(a)/int(b))
# # #             break
# # #     else:
# # #         print('Необходимо вводить только числа')
# # # def multy(*args):
# # #     print(f'Мне передали {len(args)} аргументов.')
# # #     sum=0
# # #     for i in args:
# # #        sum +=i
# # #     print(f'Среднее значение: {sum/len(args)}')
# # # multy(1,2,3,4,5)
# # # double = lambda  x: x*2
# # strings = ['Банан', 'Виноград','Арбуз']
# # s_list = sorted(strings, reverse=True)
# # print(s_list)
# # import re
# #
# # pattern = '20'
# # test_string = '10 плюс 20 будет 30'
# # result = re.search((pattern, test_string)
# #
# # print(result[0])
# # rus = ['стул','стол','яблоко']
# # eng = ['chair','table','apple']
# #
# # d = dict(zip(rus,eng))
# # print(d)
# # import re
# #
# # pattern = '<img.*>'
# # test_string = 'Картинка ,img src="bg.jpg"> тексте </p>'
# #
# # result = re.findall(pattern,test_string, re.I)
# # print(result)
#
# # def decorator_function(func):
# #     def wrapper()
# #         print(f'оборачиваемая функция: {func}')
# #         print('Выполняем обёрнутуб функцию')
# #         func()
# #         print('Выходим из обёртки')
# #     return wrapper
# #
# # @decorator_function
# # def say_hello():
# #     print('Hello')
#
#
# # def benchmark(func):
# #     import time
# #     def wrapper():
# #         start = time.time()
# #         func()
# #         end = time.time()
# #         print(f'Затраченное время:{end - start} сек.')
# #     return wrapper
# #
# # @benchmark
# # def long_list_creator():
# #     a = [i for i in range(1000000)]
# #
# # long_list_creator()
# from lib import get_size, Fruit, Greeter, Car
# #
# # class Fruit:
# #     pass
# #
# #
# #
# # a= Fruit()
# # b= Fruit()
# # c = Fruit()
# #
# # a.name = 'Apple'
# # a.weight = 120
# # c.name = 'Lemon'
# # c.weight = 180
# # c.color = 'yellow'
# # b.name = 'Orange'
# # b.weight = 220
# #
# # g = Greeter()
# # g.say_hello()
# # g.hello_and_talk('Bob', 'Good weather')
# #
# # print(a.name, a.weight)
# # print(b.name, b.weight)
# # print(c.name, c.weight, c.color)
# # b.weight -= 10
# # get_size(a)
# # get_size(b)
# car = Car()
# c?
from lib import Special
s =  Special()
print(s + 1)
print(1 + s)
s +=1
print(s)
#
lib import Time

= Time(10,20)
t2 = Time(10, 40)
t3 = [t1, t2]
#t3 = t1 + t2
print(t3)











from lib import Okno

if __name__ == '__main':
    app = Okno()