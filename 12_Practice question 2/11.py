password = "D141008S"
entered_password = input("Enter your password: ")

while (entered_password != password):
  entered_password = input("Incorrect password. Please try again: ")

print("Success! You are logged in.")