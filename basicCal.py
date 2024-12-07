global x, y

def add(x, y):
  sum = x + y
  print(f"\nThe sum of {x} and {y} is {sum}")

def subtract(x, y):
  diff = x - y
  print(f"\nThe difference of {x} and {y} is {diff}")

def multiply(x, y):
  prod = x * y
  print(f"\nThe product of {x} and {y} is {prod}")

def divide(x, y):
  quo = x / y
  print(f"\nThe quotient of {x} and {y} is {quo}")

def square(x):
  area = x**2
  print(f"The area of {x} is  {area}")

def main():
  print("Welcome to the calculator!")
  choice = input("\n[A] Add \n[B] Subtract \n[C] Multiply \n[D] Divide \n[E] Square\n\nWhat would you like to do? ")
  if choice == "A" or choice =="a":
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    add(x, y)
  elif choice == "B" or choice == "b":
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    subtract(x, y)
  elif choice == "C" or choice == "c":
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    multiply(x, y)
  elif choice == "D" or choice == "d":
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    divide(x, y)
  elif choice == "E" or choice== "e":
    x = int(input("Side of Square: "))
    square(x)
  else:
    print("Invalid choice")


if __name__ == "__main__":
  main()