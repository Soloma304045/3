'''
�������� �������, ������� ��������� �������� ���������� �����, 
����� ���������� ������� � ����� ���������� ��������� ����� �������� �������� 
���� �� �������� ����� 1. ������ ����� ������� �� �����.
'''
def numberEven(number):
    return number % 2 == 0

number = 0
while (number != 1):
    number = int(input())
    if numberEven(number):
        print(number)