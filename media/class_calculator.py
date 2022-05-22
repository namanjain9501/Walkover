class Calculator:
    def __init__(self,num):
        self.num=num
    def square(self):
        print(f"square of {self.num}= {self.num*self.num}")
a=Calculator(4)
a.square()