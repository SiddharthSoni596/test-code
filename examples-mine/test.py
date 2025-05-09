a,b,c = int(input()),int(input()),int(input())
if a == b and b == c:
	print("Equilateral")
elif a != b and b != c:
	print("Scalene")
else:
	# checking something
	print("Iscoseles")