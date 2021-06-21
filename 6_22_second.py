# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
  n = 3
  m = 4
  array = [[0] * m for _ in range(n)]
  print(array)
  #리스트를 2차원 배열로 초기화하려면 반드시 리스트 컴프리 헨션 사용
  a =  [1,2,3,4,5,5,5]
  remove_set = {3,5}

  #python 에서는 remove_all 함수 같은것이 없으므로 다음과 같이 구현
  result = [i for i in a if i not in remove_set]
  print(result)
  #즉 이렇게 remove set을 만지면 모두 지우거나 내가 원하는 요소만 지울수 가 있다.
  
