a = int(input("Entre a number between 1 and 10: "))

match a:
  case 1:
    print("You won a charger")
  case 3:
    print("You won 3 dollar")
  case 7:
    print("You won a phone")
  case _:
    print("Better luck next time")