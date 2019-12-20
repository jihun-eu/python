##while
형식:
while 조건:
    실행문...

#강제로 빠져나가는 break
while 조건:
    실행문...
    break

#반복문 계속 실행 continue
while 조건:
    실행문...
    continue

#무한루프 while True:
while True:
    실행문...


##for
형식:
for 변수 in '리스트, 튜플,문자열'
    실행문...

#코드 계속 실행 continue
marks=[90,25,67,45,80]
number=0
for mark in marks:
    number = number+1
    if mark<60: continue
    print("%d번 학생 축하합니다. 합격입니다."%number)

#n개의 객체를 생성해주는 함수 range
a=range(10)

##응용
add =0
for i in range(0,10):
    add=add+i

print(add)

#리스트 내포 사용
a=[1,2,3,4]
result=[]
for num in a:
    result.append(num*3)

print(result)


