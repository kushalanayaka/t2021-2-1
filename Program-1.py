class Calculator:
    def __init__(self,a,b,operation):
        self.a = a
        self.b = b
        self.operation = operation.lower()
    
    def calculator(self):
        if self.operation == "addition":
            return self.a + self.b
        elif self.operation == "substraction":
            return self.a - self.b
        elif self.operation == "multiplication":
            return self.a * self.b
        elif self.operation == "division":
            if self.b != 0:
                return self.a / self.b
            else:
                return "error: division by zero is not allowed"
        else:
            return "invalid input"
        
a = float(input("Enter a value: "))
b = float(input("Enter b value: "))
operation = input("Enter type of operation: ")

cal = Calculator(a,b, operation)
result = cal.calculator()
print("result : ", result)
