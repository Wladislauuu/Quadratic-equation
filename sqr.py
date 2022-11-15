a = float(input("Введите число: "))
b = float(input("Введите число: "))
c = float(input("Введите число: "))
D = b * b - 4*a*c
if D>0:
	print('Есть 2 решения')
	print("x1=" , (-b+((D)**0.5)) / (2*a) , "x2=" , (-b-((D)**0.5))/(2*a) )
elif D == 0:
	print("Есть 1 решение")
	print("x1=" , (-b+((D)**0.5)) / (2*a))
elif D < 0:
	print("Нет решений")