fahrenheit_str = input("Enter a temperature in Fahrenheit: ")
fahrenheit = float(fahrenheit_str)
celsius = (fahrenheit-32)*5/9
print("The temperature in Celsius: " + str(celsius))
print(f"The temperature in Celsius: {celsius:.2f}")
