def factorial(num):
    result = 1                                          #Set the result variable to 1
    for n in range(1, num + 1):                         #Iterate over the numbers from 1 to num
        result *= n                                     #Multiply the result by the current number
    return result                                       #Return the result

print(factorial(4))