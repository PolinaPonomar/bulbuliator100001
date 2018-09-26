import math
buf = input()
a, c, b = ('\040' + buf).split('\040') if (buf.split('\040').__len__() == 2)else buf.split('\040')
print(a, c, b)
#a = int(a)
b = int(b)
if c == '-':
    print(a, c, b, '=', a - b, sep='\40', end='')
elif c == '+':
    print(a, c, b, '=', a + b)
elif c == '*':
    print(a, c, b, '=', a * b)
elif c == '/':
    print(a, c, b, '=', a / b)
elif c == '^':
    print(a, c, b, '=', a ** b)
elif c == 'sqrt':
    print(c, '(', b, ')', '=', math.sqrt(b))
elif c == 'exp':
    print(c, '(', b, ')', '=', math.exp(b))
