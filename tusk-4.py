'''
На вход программы поступает строка из целых чисел, записанных через пробел. 
Описать функцию get_list, которая преобразует строку в список из целых чисел 
и вернет его. Определить декоратор который 
дополнительно отсортирует значения возвращаемого списка.
'''
def sort(func):
    def newList(numbers_str):        
        numbersList = func(numberString)
        return sorted(numbersList)
    return newList

@sort
def get_list(numberString):
    # Преобразуем строку в список целых чисел
    return list(map(int, numberString.split()))

numberString = input("Введите числа через пробел: ")
list = get_list(numberString)
print("Отсортированный список:", list)
input()