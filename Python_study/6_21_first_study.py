# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
  a = [1,2,3,4,5,6,7,8,9]
  print(a)
  a = list()
  print(a)
  a= []
  print(a)
  n = 10
  a = [0] * n
  print(a)
  array = [i for i in range(20) if i % 2 == 0]
  result = [ i if i % 2 == 0 else 10 for i in range(10)]
  print(result)
  print(array)
  #리스트 컴프리 헨션 기초
  word_1 = "Hello"
  word_2 = "World"
  result = [i + j for i in word_1 for j in word_2]
  print(result)
  case_1 = ["A","B","C"]
  case_2 = ["D","E","A"]
  result = [i+j for i in case_1 for j in case_2 if not(i==j)]
  print(result)
  #컴프리헨션 중첩 반복문
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
