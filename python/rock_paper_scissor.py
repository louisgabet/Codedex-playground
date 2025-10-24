# Write code below 💖
import random 
while(1):
  print("===================")
  print("Rock Paper Scissors")
  print("===================")

  print("\n\n1) ✊")
  print("2) ✋")
  print("3) ✌️")
  choice = int(input("Pick a number : "))
  CpuChoice = random.randint(1, 3)

  if choice == 1:
    if CpuChoice == 1:
      print("\nYou chose : ✊")
      print("CPU chose : ✊")
      print("It's a tie!")
    elif CpuChoice == 2:
      print("\nYou chose : ✊")
      print("CPU chose : ✋")
      print("CPU Won!")
    elif CpuChoice == 3:
      print("\nYou chose : ✊")
      print("CPU chose : ✌️")
      print("The player won!")

  elif choice == 2:
    if CpuChoice == 1:
      print("\nYou chose : ✋")
      print("CPU chose : ✊")
      print("The player won!")
    elif CpuChoice == 2:
      print("\nYou chose : ✋")
      print("CPU chose : ✋")
      print("It's a tie!")
    elif CpuChoice == 3:
      print("\nYou chose : ✋")
      print("CPU chose : ✌️")
      print("CPU Won!")

  elif choice == 3:
    if CpuChoice == 1:
      print("\nYou chose : ✌️")
      print("CPU chose : ✊")
      print("CPU Won!")
    elif CpuChoice == 2:
      print("\nYou chose : ✌️")
      print("CPU chose : ✋")
      print("The player won!")
    elif CpuChoice == 3:
      print("\nYou chose : ✌️")
      print("CPU chose : ✌️")
      print("It's a tie!")
  print("\n")
