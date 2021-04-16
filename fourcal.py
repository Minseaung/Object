# class FourCal:
#    def __init__(self, first, second):
#        self.first = first
#        self.second = second
#    def add(self):
#        return self.first + self.second
#a = FourCal(4,2)
#b = a.add()
#print(b)

class FourCal:
     def __init__(self, first, second):
         self.first = first
         self.second = second
     def setdata(self, first, second):
         self.first = first
         self.second = second
     def add(self):
         result = self.first + self.second
         return result
     def mul(self):
         result = self.first * self.second
         return result
     def sub(self):
         result = self.first - self.second
         return result
#     def div(self):
#         result = self.first / self.second
#         return result
#x = int(input("첫번째 숫자: "))
#y = int(input("두번째 숫자: "))
#a = FourCal(x,y)

#print('두 수의 합은 {}'.format(a.add()))
#print('두 수의 곱은 {}'.format(a.mul()))
#print('두 수의 차는 {}'.format(a.sub()))
#print('두 수의 나누기는 {}'.format(a.div()))

class FourCal_div(FourCal):
     def div(self):
         result = self.first / self.second
         return result

div_data = FourCal_div(4,2)
a = div_data.add()
print(a)