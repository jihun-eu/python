##내장 함수

#절대값 돌려주는 abs
abs(-3)
3

#반복가능한 자료형 x를 입력인수로 받으며 x가 모두 참이면 True,거짓이 하나라도 있으면 False
all([1,2,3])
True
##반복가능한 자료형: for문으로 그 값을 출력할 수 있는 것.(리스트,튜플,문자열,딕셔너리,집합)

#x중 하나라도 참이 있으면 True,x가 모두 거짓일때만 False를 돌려준다.(all(x)의 반대)
any([1,2,3,0])
True
any([0,""])
False

#아스키 코드 값을 입력받아 코드에 해당하는 문자를 출력하는 함수 chr
chr(97)
'a'
chr(48)
'0'

#객체가 자체적으로 가지고 있는 변수나 함수를 보여줌 dir
dir([1,2,3])
['append','count','extend','index',...])

#a를 b로 나눈 몫과 나머지를 튜플 형태로 돌려주는 함수
divmod(7,3)
(2,1)

#'열거하다'라는 뜻으로 순서가 있는 자료형을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 돌려준다. enumerate
for i, name in enumerate(['body','foo','bar']):
    print(i,name)

    #enumerate를 for문과 함게 사용하면 자료형의 현재 순서와 그 값을 쉽게 알 수 있다.
    #for문처럼 반복되는 구간에서 객체가 현재 어느 위치에 있는지 알려주는 인덱스 값이 필요할 때 유용

#실행 가능한 문자열을 입력받아 문자열을 실행한 결괏값을 돌려주는 함수 eval
eval('1+2')
3
eval("'hi'+'a'")
'hia'
eval('divmod(4,3)')
(1,1)

#무엇인가를 걸러낸다는 뜻, 첫 번째 인수로 함수 이름을, 두번째 인수로 그 함수에 차례로 들어갈 반복 가능한 자료형을 받는다.
#두번째 인수인 반복 가능한 자료형 요소가 첫번째ㅓ 인수인 함수에 입력되었을때 반환값이 참인 것만 묶어서 돌려준다.
def positive(l):
    result=[]
    for i in l:
        if i>0:
            result.append(num)
    return result

print(positive([1,-3,2,0,-5,6]))

#output==[1,2,6]
##위에서 만든 positive함수는 리스트를 입력값으로 받아 각각의 요소를 판별해서 양수 값만 돌려주는 함수이다.

def positive(x):
    return x>0

print(list(filter(positive,[1,-3,2,0,-5,6])))

#output==[1,2,6]

##lambda를 통한 간략화

list(filter(lambda x: x>0,[1,-3,2,0,-5,6]))

#정수를 입력받아 16진수로 변환하는 hex
hex(234)
'0xea'

#객체를 입력받아 객체의 고유 주소 값을 돌려주는 함수 id
a=3
id(3)
id(a)
b=a
id(b)
##id 셋다 동일

#사용자 입력을 받는 함수 input
a=input()
b=input("Enter: ")

#문자열 형태의 숫자나 소수점이 있는 숫자를 정수 형태로 돌려주는 함수, 정수를 입력받으면 그대로 돌려준다. int
int('3')
int (3.4)
##int(x,radix)는 radix 진수로 표현된 문자열 x를 10진수로 변환하여 돌려준다.
int('11',2)
3
int('1A',16)
26

#첫번째 인수로 인스턴스, 두번째 인수로 클래스 이름을 받는다. 입력으로 받은 인스턴스가 그 클래스의 인스턴스인지를 판단하여 참이면 True, 거짓이면 False를 돌려준다.
class Person: pass

a=Person()
isinstance(a,Person)
True
b=3
isinstance(b,Person)
False

#입력값 s의 길이를 돌려주는 함수 len
len("python")
6

#반복 가능한 자료형 s를 입력받아 리스트로 만들어 돌려주는 함수 list
list("python")
['p','y','t','h','o','n']

#반복 가능한 자료형을 입력으로 받는다.
#입력받은 자료형의 각 요소를ㄹ 함수 f가 수행한 결과를 묶어서 돌려주는 함수. map(f,iterable)
def two_times(numberList):
    result=[]
    for number in numberList:
        result.append(number*2)
    return result

result=two_times([1,2,3,4])
print(result)
########==###########
def two_times(x): return x*2
list(map(two_times,[1,2,3,4]))
########간략화#########
list(map(lambda x: x*2,[1,2,3,4]))

#인수로 반복 가능한 자료형을 입력받아 최댓값을 돌려주는 max
max([1,3,4])
4
#min max의 반대

#정수 형태의 숫자를 8진수 문자열로 바꾸어 돌려주는 oct
oct(34)
'0o42'

#파일 이름과 읽기방법을 입력받아 파일 객체를 돌려주는 함수 open(filename,[mode])
##mode생략시 'r'

#문자의 아스키 코드 값을 돌려주는 함수 ord
ord('a')
97

#x의 y제곱한 결과값을 돌려주는 pow
pow(2,4)
16

#for문과 자주 사용하는 함수로 입력받은 숫자에 해당하는 범위값을 반복가능한 객체로 만들어 돌려준다. range
list(range(5))
[0,1,2,3,4]
list(range(5,10))
[5,6,7,8,9]
list(range(1,10,2))
[1,3,5,7,9]

#숫자를 입력받아 반올림해주는 함수 round(number[,ndigits])
round(4.6)
5
round(4.2)
4

#입력값을 정렬한 후 그 결과를 리스트로 돌려주는 함수 sorted
sorted([3,1,2])
[1,2,3]

#문자열 형태로 객체를 변환 str
str(3)
'3'

#입력받은 리스트나 튜플의 모든 요소의 합을 돌려주는 함수
sum([1,2,3])
6

#반복 가능한 자료형을 입력받아 튜플 형태로 바꾸어 돌려주는 함수 tuple
tuple("abc")
('a','b','c')

#입력값의 자료형이 무엇인지 알려주는 type
type("abc")
<class 'str'>

#동일한 개수로 이루어진 자료형을 묶어 주는 역할을 하는 함수 zip

list(zip([1,2,3],[4,5,6]))
[(1,4),(2,5),(3,6)]

