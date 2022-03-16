# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   data = dict()
   data['사과'] = 'Apple'
   data['바나나'] = 'Banana'
   data['코코넛'] = 'Coconut'

   print(data)
   #딕셔너리는 다음과 같은 방법으로 메모리를 절약 할 수 있다.
   if '사과' in data:
       print("'사과'를 키로 가지는 데이터가 존재합니다.")
   #사전 자료형 관련 함수
   key_list = data.keys()
   value_list = data.values()
   print(key_list)
   print(value_list)

   for key in key_list:
       print(key)
  #집합 자료형
   data = set([1,1,2,3,4,4,5])
   print(data)
   #초기화 방법 1
   data = {1,1,2,3,4,4,5}
   print(data)
   #집합 자료형 연산
   a = set([1,2,3,4,5])
   b = set([3,4,5,6,7])

   print(a | b)
   print(a & b)
   print(a - b)
   #집합 자료형 관련 함수
   data = set([1,2,3])
   print(data)

   #새로운 원소 추가
   data.add(4)
   print(data)
   data.update([5,6])
   print(data)
   data.remove(3)
   print(data)
   #전반적인 자료형 마무리 
