#String & Numeric values can operate together with *
a,b = 2,3
txt = "@"
print(a*txt*b)

""" a,b = 2,3
txt = "@"
print(2*txt*3) """

#String & string can operate with + 
c,d = "2",3
Txt = "@"
print((c+Txt)*d)

#Numeric values can operate with all arithmetic operators
e,f = 4,5
g = 6
print(e+f*g)

#Arithmetic expression with integer anf float will result in float
h,i = 10,5.0
j = h*i
print(j)

#Result of division operator with two integers will be float
A,B = 1,2
C = A/B
print(C)

#Integer division with float & integer(int) will give int displayed as float
D,E = 1.5,3
F = D//E
print(F,D/E)

#Floor gives closest integer, which is lesser than or equal to the float value
G,H = 12,5
I = G//H
print(I)

#Remainder is negative when denominator is negative
x,y = 5,-2
z = x%y
print(z)

