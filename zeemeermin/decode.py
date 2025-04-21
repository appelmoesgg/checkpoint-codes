'''
Decode.py - appelmoesGG
'''

alfabet = "abcdefghijklmnopqrstuvwxyz"
circleCount = 0
lineCount = 0

while True:
  circleCount = int(input("Amount of circles: "))
  lineCount = int(input("Amount of lines: "))
  
  match circleCount:
    case 1:
      alfabetIndex = 1
    case 2:
      alfabetIndex = 5
    case 3:
      alfabetIndex = 9
    case 4:
      alfabetIndex = 15
    case 5:
      alfabetIndex = 21
      
  if lineCount == 0:
    pass
  else:
    alfabetIndex += lineCount
  
  print(alfabet[alfabetIndex - 1])
