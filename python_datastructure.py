##리스트
a=[1,2,5,7,9]
b=[]

#리스트 인덱싱
a[0]
a[0]+a[2]
a[-1]
a=[1,2,3,['a','b','c']]
a[0]
a[-1]
a[3]
a[-1][0]

#리스트 슬라이싱
a = "python is the best choice"
a[0:2]
a[:2]
a[4:]

#리스트 연산
a=[1,2,3]
b=[4,5,6]
a+b#리스트 덧셈
a*3#리스트 반복
len(a)#리스트 길이

#문자열 형 변환
str(a[2])+"hi"

#리스트 요소 삭제
del a[1]
del b[0:]

#리스트에 요소 추가 append
a=[1,2,3]
a.append(4)
a.append([5,6])

#리스트 정렬 sort
a=[1,4,3,2]
a.sort()

#리스트 뒤집기 reverse
a=['a','c','b']
a.reverse()

#위치 반환 index
a.index(3)

#리스트에 요소 삽입 insert
a.insert(0,'F')

#리스트 요소 제거 remove
a.remove('b')

#리스트 요소 끄집어내기 pop
a.pop()#마지막 요소 반환후 삭제
a.pop(x)#x요소 반환 후 삭제

#리스트에 포함된 요소 개수 새기 count
a.count('c')

#리스트 확장 extend
a.extend([4,5])

##튜플
t1=(1,2,3)
t2=()
#요솟값의 삭제나 변경이 불가능
#값을 변경하지 못하는것 제외 리스트와 동일

##딕셔너리
dic={'name':'pey','phone':'01199933322','birth':'1118'}
dic_form={'key:value','...'}

#딕셔너리 쌍 추가
a={1:'a'}
a[2]='b'

#딕셔너리 요소 삭제 del
del a[1]

###딕셔너리 사용법
#key를 통해 value를 얻는다
#key값은 인덱스의 개념
#중복key값의 경우 첫번째 key가 무시됨
#key는 튜플로도 사용 가능

##딕셔너리 관련 함수

#key 리스트 만들기
a={'name':'pey','phone':'01199933322','birth':'1118'}
a.keys()
#key값만 모아서 dict_keys객체를 돌려준다.

#dict_keys->리스트 list
list(a.keys())

#value리스트 만들기 values
a.values()
#values값만 모아서 dict_values객체를 돌려준다.

#key,value쌍 얻기 items
a.items()

#key:value쌍 모두 지우기 clear
a.clear()

#key로 value얻기 get
a.get('name')
##찾으려는 key가 없을 경우
a.get(x,'default')

#해당 key가 딕셔너리 안에 있는지 조사하기 in
'name' in a

#집합 set
s2 = set("Hello")

##특징
###중복을 허용하지 않는다.
###순서가 없다.
###인덱싱으로 접근하려면 리스트나 튜플로 변환해야한다.

#교집합 &
s1&s2

#합집합 |
s1|s2

#차집합 -
s1-s2


#집합 자료형 관련 함수

#값 1개 추가 add
s1=set([1,2,3])
s1.add(4)

#값 여러개 추가 update
s1=set([1,2,3])
s1.update([4,5,6])

#특정값 제거 remove
s1.rmove(2)

##불 자료형
##참과 거짓을 나타내는 자료형
a=True
b=False

#자료형이 비어있는지 아닌지를 확인해주는 bool
bool('python')
##'python'은 내부가 비어있지 않기때문에 True
bool('')
##''내부는 비어있기 때문에 False

##변수 주소값 id
id(a)

##리스트 복사
b=a
###b의 주소값은 a의 주소값과 동일하게 된다.

#동일한 객체를 가리키고 있는지에 대해서 판단하는 is
a is b
##동일하기 때문에 True(출력타입: bool)

##리스트 복사 [:]
b=a[:]
##리스트 복사  copy
from copy import copy
a=[1,2,3]
b=copy(a)
##b의 주소값과 a의 주소값이 다르게 나온다.

#변수만들기
a,b=('python','life')#튜플 대입
(a,b)='python','life'#튜플 대입 2
[a,b]=['python','life']#리스트로 변수생성
a=b='python'#여러개의 변수에 같은값 대입
a,b=b,a#a와 b의 값을 바꿈


