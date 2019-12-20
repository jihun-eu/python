##def
def 함수명(매개변수):

##매개변수의 개수가 몇개가 될지 모를때
def 함수명(*매개변수):

##키워드 파라미터
def print_kwargs(**kwargs):
    print(kwargs)
#키워드 파라미터를 쓸때 별이 두개

##매개변수에 초깃값 미ㅊ리 설정하기
def say_myself(name,old,man=True):
    print("My name is %s"%name)
    print("%d years old"%old)
    if man:
        print("Man")
    else:
        print("Woman")

#define SWAP(x,y,t)=(t=x,x=y,y=t) ==lambda
add=lambda a,b:a+b
result=add(93,4)
print(result)