# class Complex:
#         def __init__(self, real=0.0,imaginary=0.0):
#             self.real = real
#             self.imaginary = imaginary
#
#         def __repr__(self):
#             return 'Complex({!r},{!r})'.format(self.real,self.imaginary)
#
#         def __str__(self):
#             return '{}{:+d}i'.format(self.real, self.imaginary)
#
#         def __add__(self, other):
#             return Complex(self.real +other.real, self.imaginary + other.imaginary)
#
#         def __neg__(self):
#             return Complex(-self.real, -self.imaginary)
#
#         def __sub__(self, other):
#             return self+(-other)
#
#         def __abs__(self):
#             return (self.real **2 + self.imaginary**2)**0.5
#
# hasattr()
class Singletone:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)

        return cls._instance

    def __init__(self):
        self.value='some value'
    def __get
