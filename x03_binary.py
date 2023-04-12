#!python3

"""
Create a function that takes an integer value from 0-255 and
converts it into a list.  Each element is equal to the power
of 2 that corresponds to that place value
"""
import itertools
def toBinary(value):
  '''
  input: value (int)
  return : list of values
  '''
  numbers = [0,1,2,4,8,16,32,64,128]
  target = value

  result = [combo for i in range(len(numbers), 0, -1)
    for combo in itertools.combinations(numbers, i)
    if sum(combo) == target]

  result = result[0]
  length = len(result) - 1
  num1 = result[length]

  if num1 == 0:
    return [0,0,0,0,0,0,0,0]


  eight = numbers.index(num1)
  newList = [0,0,0,0,0,0,0,0]
  newList.insert(eight,1)
  print(newList)
  print(eight)
  return newList

def toDecimal(myList):
  '''
  input: list of values
  return int
  convert binary to decimal
  '''
  return None

def problem1():
  assert toBinary(0) == [0,0,0,0,0,0,0,0]
  assert toBinary(1) == [1,0,0,0,0,0,0,0]
  assert toBinary(2) == [0,1,0,0,0,0,0,0]
  assert toBinary(5) == [1,0,1,0,0,0,0,0]
  assert toBinary(10) == [0,1,0,1,0,0,0,0]
  assert toBinary(30) == [0,1,1,1,1,0,0,0]
  assert toBinary(45) == [1,0,1,1,0,1,0,0]

def problem2():
  assert toDecimal([0,0,0,0,0,0,0,0]) == 0
  assert toDecimal([1,0,0,0,0,0,0,0]) == 1
  assert toDecimal([0,1,0,0,0,0,0,0]) == 2
  assert toDecimal([1,0,1,0,0,0,0,0]) == 5
  assert toDecimal([0,1,0,1,0,0,0,0]) == 10
  assert toDecimal([0,1,1,1,1,0,0,0]) == 30
  assert toDecimal([1,0,1,1,0,1,0,0]) == 45
  
if __name__ == "__main__":
  problem1()
  problem2()
