#implicit conversion
firstNumber = 10
secondNumber = 10.1
number = firstNumber+secondNumber
print("Value: ",number)
print(type(number))

#Explicit Conversion
num_string = '12'
num_int = 22
print(type(num_string))
num_string = int(num_string)
print(type(num_string))
number = num_string+num_int
print(number)