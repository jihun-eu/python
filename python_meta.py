##정규 표현식

#메타 문자
#.^$+?{}[]\|()

[]:문자 클래스'[]사이의 문자들과 매치'
ex) [abc]=='a,b,c 중 한개의 문자와 매치'
[]안의 두 문자 사이에 하이픈(-_)을 사용하면 두 문자 사이의 범위

^==not

\d:숫자와 매치 [0-9]와 동일
\D:숫자가 아닌 것과ㅏ 매치[^0-9]와 동일
\s:whitespace 문자(space or tab 처럼 공백을 표현하는 문자)와 매치,[ \t\n\r\f\v]와 동일
\S:whitespace 문자가 아닌 문자와 매치
\w:문자+숫자와 매치
\W:문자+숫자가 아닌 문자와 매치

Dot(.)
#정규 표현식의 Dot 메타문자는 줄바꿈 문자인 \n을 제외한 모든 문자와 매치됨을 의미한다.
a.b=="a+모든 문자+b"
a[.]b=="a+Dot문자.+b"

*(반복)
ca*t
#*앞에 있는 문자 a가 0부터 무한대로 반복될 수 있다는 의미

+(반복)
#최소 1회 이상 반복할 때 사용
ca+t

{m,n},?(반복)

1. {m}
ca{2}t=="c+a(반드시 2번 반복)+t"
2. {m,n}
ca{2,5}t=="c+a(2~5번 반복)+t"
3.?
반복은 아니지만 이와 비슷한 개념으로 ?
?=={0,1}

파이썬에서 정규 표현식을 지원하는 re 모듈
import re
p=re.compile('ab*')
#.정규 표현식을 컴파일
#re.compile의 결과로 돌려주는 객체 p를 사용하여 그 이후의 작업을 수행

정규식을 사용한 문자열 검색
match():문자열의 처음부터 정규식과 매치되는지 조사한다.
search():문자열 전체를 검색하여 정규식과 매치되는지 조사한다.
findall():정규식과 매치되는 모든 문자열을 리스트로 돌려준다.
finditer(): 정규식과 매치되는 모든 문자열을 반복 가능한 객체로 돌려준다.

match 객체의 메서드
group():매치된 문자열을 돌려준다.
start():매치된 문자열의 시작위치를 돌려준다.
end():매치된 문자열의 끝 위치를 돌려준다.
span():매치된 문자열의 (시작,끝)에 해당하는 튜플을 돌려준다.

p=re.compile('[a-z]')
m=p.match("python")
m=re.match('[a-z]+',"python")#축약형

컴파일 옵션
#DOTALL:S:DOT문자가 줄바꿈 문자(\n)를 포함하여 모든 문자와 매치한다.
import re
p=re.compile('a.b',re.DOTALL)
m=p.match('a\nb')
print(m)

#IGNORECASE:I:대,소문자에 관계없이 매치한다.
import re
p=re.compile('[a-z]',re.I)
p.match('python')
p.match('Python')

#MULTILINE:M:여러줄과 매치한다.
import re
p=re.compile("^python\s\w+",re.MULTILINE)

data="""python one
life is too short
python two
you need python
python three"""

print(p.findall(data))

#VERBOSE:X:verbose 모드를 사용한다.
#정규식을 주석 또는 줄 단위로 구분한다.
charref=re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')
charref=re.compile(r"""&[#]
(
    0[0-7]+
    | [0-9]+
    | x[0-9a-fA-F]+
    )
    ;
    """.re.VERBOSE)

백슬래시 문제
p=re.compile('\\\\section')
\\section
p=re.compile(r'\\section')

메타문자
|: or과 동일한 의미로 사용된다.
^: 문자열의 맨 처음과 일치함을 의미한다.
$: 문자열의 끝과 매치함을 의미로
\A: 문자열의 처음과 매치됨을 의미한다.re.MULTILINE옵션 사용시 전체 문자열의 처음하고만 매치
\Z: 문자열의 끝과 매치됨.re.MULTILINE옵션 사용시 전체 문자열의 끝과 매치
\b: 단어 구분자.whitespace에 의해 구분된다.백스페이스가 아닌 raw string임을 알려주기 위해 r을 붙인다.
\B: \b와 반대경우

그루핑
(): 그룹을 만들어주는 메타문자
p=re.compile(r"\w+\s+\d+[-]\d+[-]\d+")
m=p.search("park 010-1234-1234")

##이름만 뽑아내려한다면

p=re.compile(r"(\w+)\s+\d+[-]\d+[-]\d+")
m=p.seach("park 010-1234-1234")
print(m.group(1))

이름에 해당하는 '\w+'부분을 그룹으로 만들면 match객체의 group메서드를 사용하여 그루핑된 부분의 문자열만 뽑아낼 수 있다.
group(0)=매치된 전체 문자열
group(n)=n번째 그룹에 해당하는 문자열

그루핑된 문자열 재참조하기
p=re.compile(r'(\b\w+)\s+\1')#(그룹)+""+그룹과 동일한 단어와 매치됨
p.search('Paris in the the spring').group()
##'the the'

#두개의 동일한 단어를 연속적으로 사용해야만 매치된다. \1: 정규식의 그룹중 첫번째 그룹을 가리킨다.

그루핑된 문자열에 이름 붙이기
(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)

재참조시에는 (?P=그룹이름)이라는 확장구문을 사용

전방탐색
긍정형 전방탐색:...에 해당하는 정규식과 매치되어야 하며 조건이 통과되어도 문자열이 소비되지 않는다.(?=...)

부정형 전방탐색:...에 해당하는 정규식과 매치되지 않아야 하며 조건이 통과되어도 문자열이 소비되지 않는다.(?!...)

문자열 바꾸기
sub메서드를 사용하면 정규식과 매치되는 부분을 다른문자로 쉽게 바꿀 수 있다.
p=re.compile('(blue|white|red)')
p.sub('colour','blue socks and red shoes')
'colour socks and colour shoes'
p.sub('colour','blue scoks and red shoes',count=1)
'colour socks and red shoes'

p.subn('colour','blue socks and red shoes')
('colour socks and colour shoes',2)##subn은 바꾼 횟수가 같이 나옴

sub메서드를 사용할 때 참조구문 사용하기
p=re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)")
print(p.sub("\g<phone> \g<name>","park 010-1234-1234"))
#\g<그룹 이름>을 사용하면 정규식의 그룹이름을 참조할 수 있게된다.
#그룹이름이 아닌 참조번호를 사용해도 마찬가지결과를 가져올 수 있다.

sub메서드의 매개변수로 함수 넣기
p=re.compile(r'\d+')
p.sub(hexrepl,'Call 65490 for printing, 49152 for user code.')

Greedy vs Non-Greedy
Greedy:<.*>
Non-Greedy:<.*?>