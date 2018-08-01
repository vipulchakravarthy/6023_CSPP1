A = input("enter the first number")
B = input("enter the second number")
x = type(A)
y = type(B)
if (x == "str" or y == "str") :
	print("strings are involved")
elif A==B :
	print("equal")
elif A<B :
	print("smaller")
elif  A>B :
	print("larger")