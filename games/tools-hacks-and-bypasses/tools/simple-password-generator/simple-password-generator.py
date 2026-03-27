import random as rand
codelength = int(input("How long is your password? (3-5): "))
if codelength <= 3:
  print("Error: shorter than minimum")
elif codelength == 3:
  num1 = str(rand.randint(0,9))
  num2 = str(rand.randint(0,9))
  num3 = str(rand.randint(0,9))
  print("Your new password is: " + num1 + num2 + num3)
elif codelength == 4:
  num1 = str(rand.randint(0,9))
  num2 = str(rand.randint(0,9))
  num3 = str(rand.randint(0,9))
  num4 = str(rand.randint(0,9))
  print("Your new password is: " + num1 + num2 + num3 + num4)
elif codelength == 5:
  num1 = str(rand.randint(0,9))
  num2 = str(rand.randint(0,9))
  num3 = str(rand.randint(0,9))
  num4 = str(rand.randint(0,9))
  num5 = str(rand.randint(0,9))
  print("Your new password is: " + num1 + num2 + num3 + num4 + num5)
elif codelength >= 5:
  print("Error: longer than maximum")
else:
  print("Error: Unknown value")
print("To use you password, 1) copy the password, 2) paste it anywhere! (probably not a public talk or article editing platform or an unsafe website)")

