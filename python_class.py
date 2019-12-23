#클래스와 객체
#클래스: 객체를 만드는 것
#객체: 클래스로 만들어진 것
#인스턴스: 객체중 해당 클래스로 만들어진 객체를 해당 클래스의 인스턴스라고 한다.

class FourCalf:
    pass

a=FourCalf()
type(a)
#<calss'__main__.Fourcal'>

class FourCals:
    def setdata(self,first,second):
        self.first=first
        self.second=second
    #class 안의 def : 매서드

a=FourCals()
a.setdata(4,2)
#매개변수가 두개인 이유
#self는 관례적으로 객체를 호출시 호출한 객체 자신이 전달되기 때문(self이외 다른 이름도 상관없음)
#객체변수는 다른 객체들 영향받지 않고 독립적으로 그 값을 유지한다.

class FourCalt:
    def setdata(self,first,second):
        self.first=first
        self.second=second
    def add(self):
        result=self.first+self.second
        #result=a.first+a.second
        return result
a=FourCalt()
a.setdata(4,2)

print(a.add())
#6


##생성자
#Fourcalf,s,t는 setdata메서드를 수행하지 않으면 오류가 발생
#초기값 설정이 필요시 메서드 호출보다 생성자 구현이 안전
#생성자: 객체가 생성될 때 자동으로 호출되는 메서드
#파이썬 메서드 이름으로 __init__ 를 사용하면 이 메서드는 생성자가 된다.

class FourCalinit:
    def __init__(self,first,second):
        self.first=first
        self.second=second
    def setdata(self,first,second):
        self.first=first
        self.second=second
    def add(self):
        result=self.first+self.second
        return result
    def mul(self):
        result=self.first*self.second
        return result
    def div(self):
        result=self.first/self.second
        return result
    def sub(self):
        result=self.first-self.second
        return result

def __init__(self,first,second):
    self.first=first
    self.second=second
#__init__메서드는 setdata메서드와 이름만 다르고 모두 동일
#단 이름을 __init__으로 해서 생성자로 인식되어 객체가 생성되는 시점에 자동으로 호출되는 차이

a=FourCalinit()
#초기값을 제공해주지 않았기에 오류
#객체생성시 값을 같이 전달해야 한다.

a=FourCalinit(4,2)


##상속
#상속이란 어떤 클래스를 만들때 다른 클래스의 기능을 물려받을 수 있게 만드는 것

class MoreFourCal(FourCalinit):
#상속하는 방법
    pass

a=MoreFourCal(4,2)
a.add()
#6

#매서드 오버라이딩
a=MoreFourCal(4,0)
a.div()
#나누기에서 4를 0으로 나누면 ZeroDivisionError가 발생
#0으로 나눌 때 오류가 아닌 0을 돌려주도록 만들고 싶다면
#메서드를 동일한 이름으로 다시 만들어준다.
class SafeFourCal(FourCalinit):
    def div(self):
        if self.second==0:
            return 0
            #0으로 나누게 되었을때 오류대신 0을 반환
        else:
            return self.first/self.second

##클래스 변수
class Family:
    lastname="김"

print(Family.lastname)

a=Family()
b=Family()
print(a.lastname)
print(b.lastname)
#김 김
Family.lastname="박"
print(a.lastname)
print(b.lastname)
#박 박
#클래스 변수 값을 변경하면 객체의 값도 모두 변경
#클래스로 만든 모든 객체에 공유된다.
id(Family.lastname)
id(a.lastname)
id(b.lastname)
#id값이 모두 동일함