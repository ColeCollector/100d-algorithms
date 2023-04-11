#!python3

""" 
Necklace numbers are a number sequence.  You start with 2 digits. The 3rd digit is created by adding the previous 2 digits, but if it's greater than 10, you add the sum of those 2 digits again.  You keep repeating this process until you get back to the 2 digits you started with

extra: What is the shortest necklace number sequence that can be made?
"""

def necklace(a,b):
  """
  inputs: 
  a : int value [0..9]
  b : int value [0..9]
  
  return
  str necklace number
  """
  z = a+b
  x = str(a)
  y = str(b)
  necknum = x+y

  while len(necknum) < 50:
    digi = [int(i) for i in str(necknum)]
    length = len(necknum)
    lastdig = int(necknum[length-1])
    seclastdig = int(necknum[length-2])

    if lastdig == b and seclastdig == a and len(necknum) != 2:
      break
    
    z = lastdig + seclastdig
    if z >= 10:
      digi = [int(i) for i in str(z)]
      zdigit1 = digi[0]
      zdigit2 = digi[1]
      zdigits = str(zdigit1 + zdigit2)
      necknum = necknum+zdigits
    else:
      necknum = necknum+(str(z))
    
  return necknum

def main():
  assert necklace(9,4) == "94483257314595516742685494"
  assert necklace(1,3) == "13472922461786527977538213"
  assert necklace(5,1) == "51674268549448325731459551"
  assert necklace(3,4) == "34729224617865279775382134"

if __name__ == "__main__":
  main()
  
  
