##외장함수

#sys모듈은 파이썬 인터프리터가 제공하는 변수와 함수를  제어할 수 있게 해주는 모듈

import sys
print(sys.argv)

#cmd창에서 파일명 뒤에 다른 값을 넣어주면 sys.argv 리스트에 값이 추가됨

#sys.exit()
#프로그램 파일 안엣거 사용하면 프로그램을 중단시킨다.

#sys.path()
#파이썬 모듈들이 저장되어있는 위치를 나타낸다.
sys.path.append("mydir")
#mydir의 경로가 추가됨

#pickle
#객체의 형태를 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈

import pickle
f=opne("test.txt",'wb')
data={1:'python',2:'you need'}
pickle.dump(data,f)
f.close

import pickle
f=opne("test.txt",'rb')
data=pickle.load(f)
print(data)
{1:'python',2:'you need'}

##os모듈은 환경 변수나 디렉터리, 파일 등의 OS자원을 제어할 수 있게 해주는 모듈이다.

#내 시스템의 환경 변수 값을 알고 싶을 때 os.environ
import os
os.environ

environ({'PROGRAMFILES':'C://Program Files','APPDATA':...})
#환경변수에 대한 정보를 딕셔너리 객체로 돌려준다.

os.environ['PARH']


#디렉터리 위치 변경하기 os.chdir
os.chdir("C:/WINDOWS")

#디렉토리 위치 돌려받기 os.getcwd
os.getcwd()

#시스템 명령어 호출하기 os.system
os.system("dir")

#실행한 시스템 명령어의 결과값 돌려받기 os.popen
f=os.popen("dir")
##시스템 명령어를 실행한 결과값을 읽기 모드 형태의 파일 객체로 돌려준다.
print(f.read())
#읽어 들인 파일 객체내용 보기

#디렉토리 생성 os.mkdir("dir")
#디렉토리 삭제 os.rmdir("dir")
#파일 삭제 os.unlink("filename")
#src라는 이름의 파일을 dst라는 이름으로 변경 os.rename(src,dst)

#파일을 복사해주는 파이썬 모듈 shutil
import shutil
shutil.copy("src.txt","dst.txt")
##dst가 디렉토리 이름이라면 src라는 파일 이름으로 dst디렉토리에 복사하고 동일한 파일 이름이 있을경우 덮어쓴다.

#특정 디렉토리에 있는 파일 이름을 모두 알아야 할 때 glob
#디렉토리에 있는 파일들을 리스트로 만들기 glob(pathname)
import glob
glob.glob("c:/user/mark*")

#파일을 임시로 만들어서 사용할때 tempfile.
##tempfile.mktemp()
#중복되지 않는 임시 파일의 이름을 무작위로 만들어서 돌려준다.
import tempfile
filename=tempfile.mktemp()
filename

###tempfile.TemporaryFile()은 임시 저장 공간으로 사용할 파일 객체를 돌려준다.
#wb(바이너리 쓰기 모드)를 기본적으로 갖는다.
#f.close()가 호출되면 이 파일 객체는 자동으로 사라진다.
import tempfile
f= tempfile.TemporaryFile()
f.close()

#시간과 관련된 time 모듈
##time.time()
##UTC를 사용하여 현재시간을 실수 형태로 돌려주는 함수.(초단위)
import time
time.time()

##time.localtime
#실수 값을 사용해 월,일,시,분,초,...형태로 돌려주는 함수

##time.asctime
#time.localtime에 의해서 반환된 튜플 형태의 값을 인수로 받아서 날짜와 시간을 알아보기 쉬운 형태로 돌려주는 함수

##time.ctime
#현재시간 표시

#time.strftime('출력할 형식 포맷 코드',time.localtime(time.time()))

#time.sleep
##주로 루프안에서 많이 사용. 일정 시간 간격을 두고 루플 실행 가능

###calendar
##파이썬에서 달력을 볼 수 있게 해주는 모듈
import calendar
print(calendar.calendar(2015))
#2015년 달력
calendar.prcal(2015)
#2015년 달력
calendar.prmonth(2015,12)
#2015년 12월 달력
calender.weekday(2015,12,31)
#2015년 12월 31일 요일
calendar.monthrange(2015,12)
#입력받은 달의 1일이 무슨 요일인지와 그 달이 며칠까지 있는지를 튜플로 돌려준다.

##random
#난수를 발생

import random
random.random()

random.randint(1,10)
#1,10사이의 정수 중 난수 값을 돌려준다.

random.choice(data)
#입력으로 받은 리스트에서 무작위로 하나를 선택해 돌려준다.

random.shuffle(data)
#리스트의 항목을 무작위로 섞고 싶을때 사용

###webbrowser
#자신의 시스템에서 사용하는 기본 웹 브라우저를 자동으로 실행하는 모듈

import webbrowser
webbrowser.open("http://google.com")
#구글 열기
webbrowser.open_new("http://google.com")
#새창에서 열기

##threading모듈
#스레드 프로그램시 필요

t=threading.Thread(target=def)
#스레드 생성
t.join()
#스레드가 종료될때까지 기다린다.
