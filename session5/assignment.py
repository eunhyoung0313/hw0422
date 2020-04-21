def gugudan_odd():
        for i in range (2,10,2):
            for j in range(1,10):
                print("%d x %d = %d" %(i,j,i*j))
def gugudan_even():
        for i in range (1,10,2):
            for j in range(1,10):
                print("%d x %d = %d" %(i,j,i*j))
def gugudan_odd_or_even(number):
    if number%2==0:
        print(gugudan_odd())
    else:
        print(gugudan_even())
gugudan_odd_or_even(4)


def limited_gugudan(number):
    for i in range(1, number+1):
        for j in range(1, 10):
           print("%d x %d= %d" %(i, j, i*j))
limited_gugudan(3)

class FourCal:
    def __init__(self,name,age,university):
        self.name = name
        self.age = age
        self.university = university 
        self.sub_num=0
        self.add_num=0
        self.mul_num=0
        self.div_num=0
    def add(self, num1, num2):
      self.add_num+=1
      return num1+num2
    def sub(self, num1, num2):
      self.sub_num+=1
      return num1-num2
    def mul(self, num1, num2):
      self.mul_num+=1
      return num1*num2
    def div(self, num1, num2):
      self.div_num+=1
      return num1/num2
    def show_count(self):
      print("덧셈 수 =%d"%self.add_num)
      print("뺄셈 수 =%d"%self.sub_num)
      print("곱하기 수 =%d"%self.mul_num)
      print("나눗셈 수 =%d"%self.div_num)

calculator1 = FourCal("은형",20,"Korea")
print(calculator1.add(3,4))
print(calculator1.sub(3,4))
print(calculator1.show_count())