# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

x1 = int(input('Введите абсцис первой точки '))
y1 = int(input('Введите ординат первой точки '))
x2 = int(input('Введите абсцис второй точки '))
y2 = int(input('Введите ординат второй точки '))
distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print(f'Расстояние между точками = {distance}')