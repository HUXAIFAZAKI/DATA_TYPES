class SmartCalculator:
    def __init__(self):
        self.__history = []
        self.redo_stack = []

    def add(self, a:float, b:float) -> float:
        result = a + b
        self.__history.append(f"Addition: {a} + {b} = {result}")
        self.redo_stack.clear()
        return result
    
    def subtract(self, a:float, b:float) -> float:
        result = a - b
        self.__history.append(f"Subtraction: {a} - {b} = {result}")
        self.redo_stack.clear()
        return result
    
    def multiply(self, a:float, b:float) -> float:
        result = a * b
        self.__history.append(f"Multiplication: {a} * {b} = {result}")
        self.redo_stack.clear()
        return result
    
    def divide(self, a:float, b:float) -> float:
        if b == 0:
            return "Error: Division by zero"
        result = a / b
        self.__history.append(f"Division: {a} / {b} = {result}")
        self.redo_stack.clear()
        return result
    
    def power(self,a:float,b:float) -> float:
        result = a ** b
        self.__history.append(f"Power: {a} ^ {pow} = {result}")
        self.redo_stack.clear()
        return result
    
    def modulus(self,a:float,b:float) -> float:
        result = a % b
        self.__history.append(f"Modulus: {a} % {b} = {result}")
        self.redo_stack.clear()
        return result
    
    def history(self):
        return self.__history
    
    def clear_history(self):
        self.__history = []
        return "History cleared."
    
    def undo(self):
        if self.__history:
            removed = self.__history.pop()
            self.redo_stack.append(removed)
            print(f"Removed operation \"{removed}\"")
        else:
            print("No operations to undo.")

    def redo(self):
        if(self.redo_stack):
            last = self.redo_stack.pop()
            self.__history.append(last)
            print(f"redid: \"{last}\"")
        else:
            print("Nothing to redo.")


calc = SmartCalculator()
print(calc.add(5, 3))
print(calc.subtract(5, 3))
print(calc.multiply(5, 3))
print(calc.divide(5, 3))
print(calc.history())
calc.undo()
calc.redo()
print(calc.history())