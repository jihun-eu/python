#패키지
##__init.py__용도
#해당 디렉터리가 패키지의 일부임을 알려주는 역할

#from game.soud.echo import echo_test
#from ..sound.echo import echo_test

#예외 처리
##오류동작 이유는 프로그램이 잘못 동작하는 것을 막기 위한 파이썬의 배려.
#이러한 오류를 무시하고 싶을때
#try,except사용

###try,except
try 블록 수행중 오류가 발생하면 except 블록이 수행된다.

except[발생오류[as오류메시지 변수]]:
#[]는 생략 가능

finally:
    #try문 수행 후 예외발생 여부와 상관없이 수행
    
##여러개 오류 처리

try:
    ...
except error 1:
    ...
except error 2:
    ...

##2개 이상의 오류를 동시에 처리하기
try:
    ...
except (error1,error2) as e:
    print(e)

#오류 회피하기
try:
    f=open("없는 파일",'r')
except FileNotFoundError:
    pass

#오류 일부러 발생시키기 raise

class Bird:
    def fly(self):
        raise NotImplementedError
    #fly를 구현하도록 만들고 싶은 경우

#예외 만들기
#특수한 경우에만 예외 처리를 하기 위해서 사용
class MyError(Exception):
    pass

def say_nick(nick):
    if nick == 'fool':
        raise MyError
    print(nick)
say_nick("angel")
say_nick("fool")

try:
    say_nick("angel")
    say_nick("fool")
except MyError:
    print("허용되지 않는 별명입니다.")
    #예외처리 기법을 사용하여 MyError발생 예외처리

try:
    say_nick("angel")
    say_nick("fool")
except MyError as e:
    print(e)
    #하지만 이때 print(e)로 오류메시지 출력이 되지 않음
    #오류메시지가 보이게 하려면 __str__메서드 구현
##__str__: print(e)처럼 오류 메시지를 print문으로 출력할 경우 호출

class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다."
    #오류메시지 출력됨