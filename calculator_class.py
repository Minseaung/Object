class Calculator:
    def __init__(self, num = 0):
        self.result = num

    def add(self, num):
        self.result += num
        return self.result

cal = Calculator(3)
data = cal.add(5)
print(data)