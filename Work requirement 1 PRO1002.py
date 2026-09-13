#Oppgave 1. Greeting and age check

name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age >= 18:
 print(f"Hello {name}! You are old enough to enter.")
else:
 print(f"Sorry {name}, you are too young to enter.")



#Oppgave 2. Number list processor

n = int(input("Enter a number: "))

numbers = []

i = 1

while i <= n:
  numbers.append(i)
  i+= 1

print(numbers)

if n > 5:
 print("The list is long.")
else:
 print("The list is short.")


 #Oppgave 3. Sum of user inputs


number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

numbers = [number1, number2, number3]
total = number1 + number2 + number3

print("Total:", total)
print("Numbers:", numbers)

if total % 2 == 0:
 print("Your sum is even!")
else:
 print("Your sum is odd!")

 #Oppgave 4. Fruit basket

fruits = {
    "apple": 20,
    "banana": 100,
    "lemon": 50,
    "pineapple": 44
}

fruit_name = input("Enter a fruit name: ").lower()

if fruit_name in fruits:
    print(f"We have {fruits[fruit_name]} {fruit_name}(s) available.")

    print("Letters in the fruit name:")
    for letter in fruit_name:
        print(letter)
else:
    print("We don't have that fruit.")

#Oppgave 5. Temprature converter

celsius = float(input("Enter a temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print(f"{celsius}°C is equal to {fahrenheit}°F")

if fahrenheit > 80:
  print("It's hot!")
else:
  print("It's not too hot")

temperatures = [celsius, fahrenheit]
print("Temperature in celcius and Fahrenheit:", temperatures)