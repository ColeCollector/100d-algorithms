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
  numbers = [128,64,32,16,8,4,2,1]
  binary = []
  
  for i in range (0,8):
    if value >= numbers[i]:
      binary.append(1)
      value = value - numbers[i]

    else:
      binary.append(0)

    if len(binary) > 8:
      break
  
  binary.reverse()
  return binary
  
def toDecimal(myList):
  '''
  input: list of values
  return int
  convert binary to decimal
  '''

  myList.reverse()
  numbers = [128,64,32,16,8,4,2,1]
  total = 0

  for i in range(0,8):
    if myList[i] == 1:
      total = total + numbers[i]
    
  return total

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
