#Factorial but adding

def sum_to(n):              #Define  function
    total = 0
    i = 0                   #Set value for i                         <------)
    while (i < int(n)):     #Conditional for: when i is less than n         )   Loop the funtion until it meets the input number
        i += 1              #add 1 to i                                     (
        total += i          #sum of total + i + 1                      -----)

    return total

#Define N
n=4
#Call function
print(sum_to(n))