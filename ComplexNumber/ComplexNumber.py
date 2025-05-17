class ComplexNumber:
    def __init__(self,real:float,imag:float):
        self.real = real
        self.imag = imag

    def __add__(self,other):
        return ComplexNumber(self.real+other.real, self.imag+other.imag)
    
    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag

    def __str__(self):
        return (f"{self.real} + {self.imag}i")

a = ComplexNumber(1,2)
b = ComplexNumber(3,4)
print(a)
c= a+b 
print(c)