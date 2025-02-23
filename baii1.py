import math
a = int(input('nhập a: '))
b = int(input('nhập b: '))
c = int(input('nhập c: '))

S1 = a**2 - 2*b + ((a*b)/(c**2 +3))
S2 = (b**2 - 4*a*c) / (2*a)
S3 = 3*a - b**3 + 2* math.sqrt(c**2 + 1)
S4 = math.sqrt(((a**2)/4) + ((4*a) /(b*c))+ 1)

print(f'{S1:.1f}')
print(f'{S2:.1f}')
print(f'{S3:.1f}')
print(f'{S4:.1f}')