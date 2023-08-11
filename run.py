# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

def main():
  print("Would you like to add or subtract?")
  answer = input("if you want to subtract type S if you want add type A: S/A? : ")
  num1 =  int(input("Number 1: "))
  num2 = int(input("Number 2: "))

  result =  num1 + num2  if answer == "A" else num1 - num2
  print(f"Your answer is: {result}")


main()
