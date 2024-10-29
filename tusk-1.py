'''
ќбъ€вить функцию, котора€ провер€ет четность введенного числа, 
после объ€влени€ функции в цикле необходимо считывать целое числовое значение 
пока не поступит число 1. „етные числа вывести на экран.
'''
def numberEven(number):
    return number % 2 == 0

number = 0
while (number != 1):
    number = int(input())
    if numberEven(number):
        print(number)