# Задача 4. Вариант 28.
# Напишите программу, которая выводит имя,
# под которым скрывается Эмиль Эрзог.
# Дополнительно необходимо вывести область интересов указанной личности,
# место рождения, годы рождения и смерти (если человек умер),
# вычислить возраст на данный момент (или момент смерти).
# Для хранения всех необходимых данных требуется использовать переменные.
# После вывода информации программа должна дожидаться пока пользователь
# нажмет Enter для выхода.
#Чинкиров.В.В.
# 28.03.2016
name = "Эмиль Эрзог"
city = "Эльбёф,Франция"
rod = int (1895)
dead = int (1934)
age = int (dead - rod)
interest = "Писатель"

print(name+" наиболее известен как Андреа Моруа - Французский писатель и член Французской академии. ")
print("Место рождения: "+city)
print("Год рождения: "+str(rod))
print("Год смерти: "+str(dead))
print("Возраст смерти: "+str(age))
print("Область интересов: "+interest)
input("Нажмите Enter для закрытия")
