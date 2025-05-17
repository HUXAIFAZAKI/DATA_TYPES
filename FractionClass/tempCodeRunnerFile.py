from math import gcd
class Fraction:
    def __init__(self,numerator:int,denominator:int):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        self.numerator = numerator
        self.denominator = denominator
        self.__simplify()

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __simplify(self):
        common = gcd(self.numerator, self.denominator)
        self.numerator //= common
        self.denominator //= common
        if self.denominator < 0:
            self.numerator *= -1
            self.denominator *= -1

    def __add__(self, other:"Fraction")->"Fraction":
        num = self.numerator * other.denominator + other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num, den)
    
    def __sub__(self,other:"Fraction")->"Fraction":
        num = self.numerator*other.denominator - other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num,den)
    
    def __mul__(self,other:"Fraction")->"Fraction":
        return Fraction(self.numerator*other.numerator,self.denominator*other.denominator)
    
    def __truediv__(self,other:"Fraction")->"Fraction":
        if(other.numerator == 0):
            raise ZeroDivisionError("Cannot divide by zero fraction")
        return Fraction(self.numerator*other.denominator, self.denominator*other.numerator)
    
    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __gt__(self, other: "Fraction") -> bool:
        return self.numerator * other.denominator > other.numerator * self.denominator

    def __lt__(self, other: "Fraction") -> bool:
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __ge__(self, other: "Fraction") -> bool:
        return self.numerator * other.denominator >= other.numerator * self.denominator

    def __le__(self, other: "Fraction") -> bool:
        return self.numerator * other.denominator <= other.numerator * self.denominator
    
    def __ne__(self,other:"Fraction")->bool:
        return not self == other

    def to_float(self,decimal_points:int=None)-> float:
        result =  self.numerator/self.denominator
        if decimal_points is not None:
            return round(result, decimal_points)
        return result
    
a = Fraction(4,8)
b = Fraction(8,12)
print(a)