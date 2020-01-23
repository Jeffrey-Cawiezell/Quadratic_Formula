import math
print("Ax^2+bx+c")
a=float(input("Please enter numeric value of A"))
b=float(input("Please enter numeric value of B"))
c=float(input("Please enter numeric value of C"))
squareroot=math.pow(b,2)-4*a*c
squareroot_result=math.sqrt(squareroot)
top1=-b+squareroot_result
top2=-b-squareroot_result
bottom=2*a
plus_result=top1/bottom
minus_result=top2/bottom
print("Solution set is")
print(plus_result)
print(minus_result)