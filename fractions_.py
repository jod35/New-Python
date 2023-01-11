from fractions import Fraction

f = 1/4

print(f) #0.25

f =Fraction(1,4)

print(f.numerator)
print(f.denominator)

print(f.as_integer_ratio())
