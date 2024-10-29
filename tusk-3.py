'''
Используя замыкания функций, объявите внутреннюю функцию которая 
заключает строку в произвольный тег, 
содержащийся в параметре внешней функции tag.
'''
def tagSave(tag):
    def textTag(s):
        return f"<{tag}>{s}</{tag}>"
    return textTag

tag = input("Введите тег: ")
text = input("Введите содержимое: ")
textTag = tagSave(tag)
print(textTag(text))
input()