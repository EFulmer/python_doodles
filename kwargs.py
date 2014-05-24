import math

unit = 1 / math.sqrt(2)
print('unit = 1 / math.sqrt(2)')
print('unit =', unit)
print('')

c1 = complex(unit, unit)
print('c1 = complex(unit, unit)')
print('c1 =', c1)
print('')

c2 = complex(real=unit, imag=unit)
print('c2 = complex(real=unit, imag=unit)')
print('c2 = ', c2)
print('')

d = {'real': unit, 'imag': unit}
c3 = complex(**d)
print("d = {'real': unit, 'imag': unit}")
print('c3 = complex(**d)')
print('c3 = ', c3)
