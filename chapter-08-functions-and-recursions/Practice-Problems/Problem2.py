# Q2. Write a program using function to convert Celsius to Fahrenheit.

## Celsius to Fahrenheit
def celcius_to_fahrenheit(c):
    f = 32 + ((9 * c) / 5)

    return f

## Fahrenheit to Celsius
def fahrenheit_to_celcius(f):
    c = 5 * ((f - 32) / 9)

    return c

c = float(input("Enter the Temprature (C*): "))
print(f"The Temprature in Fahrenheit is: {round(celcius_to_fahrenheit(c), 1)}")

f = float(input("Enter the Temprature (F*): "))
print(f"The Temprature in Celcius is: {round(fahrenheit_to_celcius(f), 1)}")