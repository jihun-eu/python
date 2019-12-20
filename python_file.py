#파일 생성
f=open"new.txt",'w')
f.close()
#파일 객체 = open(파일 이름, 파일 열기 모드)
#r=읽기모드/w=쓰기모드/a=추가모드

#파일을 쓰기모드로 열어 출력값 적기
f=open("C:/python_study/new.txt",'w')
for i in range(1,11):
    data="%d번째 줄입니다.\n"%i
    f.write(data)
f.close()

#프로그램의 외부에 저장디ㅗㄴ 파일을 읽는 여러가지 방법

##readline
f= open("C:/python_study/new.txt",'r')
while True:
    line = f.readline()
    if not line:break
    print(line)
f.close()
#readline: 파일의 한줄을 읽어오는 것

#readlines: 모든 줄을 읽어서 각 줄을 요소로 갖는 리스트를 생성
f=open("C:/python_study/new.txt",'r')
lines=f.readlines()
for line in lines:
    print(line)
f.close()

#read:파일의 내용 전체를 문자열로 돌려준다.
f=open("C:/python_study/new.txt",'r')
data=f.read()
print(data)
f.close()

#파일에 새로운 내용 추가하기.
f=open("C:/python_study/new.txt",'a')
for i in range(11,20):
    data="%d 번째 줄입니다.\n"%i
    f.write(data)
f.close()

#with문과 함께 사용하기
with opne("new.txt","w")as f:
    f.write("Life is too short, you need python")
#with 문을 사용하면 with 블록을 벗어나는 순간 파일객체 f가 자동으로 close되어 편리하다.

##sys모듈로 매개변수 주기
import sys

args=sys.argv[1:]
for i in args:
    print(i)
    print(i.upper(),end=' ')