alfabet = list("abcdefghijklmnopqrstuvwxyz")
circleCount = 0
lineCount = 0

while True:
  letter = input("Letter: ")
  letterIndex = alfabet.index(letter) + 1
  
  if letterIndex >= 21:
      circleCount = 5
      lineCount = letterIndex - 21
  elif letterIndex >= 15:
    circleCount = 4
    lineCount = letterIndex - 15
  elif letterIndex >= 9:
    circleCount = 3
    lineCount = letterIndex - 9
  elif letterIndex >= 5:
    circleCount = 2
    lineCount = letterIndex - 5
  elif letterIndex >= 1:
    circleCount = 1
    lineCount = letterIndex - 1
  else:
      print("Invalid letter")
      continue

  print(f"Circles: {circleCount}")
  print(f"Lines: {lineCount}")
