import math
a = int(input('nhập a: '))
b = int(input('nhập b: '))
c = int(input('nhập c: '))
if(a+b <= c):
    print('dữ liệu không hợp lệ')
else:
    d = (a + b + c)/2
    s = math.sqrt(d*(d-a)*(d-b)*(d-c))
    print('diện tích của tam giác là: ',f'{s:.1f}')