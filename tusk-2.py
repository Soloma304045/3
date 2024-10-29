'''
Вводится список целых чисел в одну строку через пробел. 
Необходимо вычислить сумму веденных значений используя рекурсивную функцию. 
Результат вывести на экране.
'''
def listSum(numbers):
    if not numbers:
        return 0
    return numbers[0] + listSum(numbers[1:])

numbers = list(map(int, input("Введите список чисел через пробел: ").split()))
result = listSum(numbers)
print("Сумма чисел списка:", result)
input()