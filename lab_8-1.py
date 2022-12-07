#JS 12/2/2022 Lab 8-1
#Define the number that is being worked with
num = input("Input a number: ")
#Define function
def num_sum(number):
    sum=0                               #Starting Number in the range
    for x in range(number+1):           #Range up to the input number
        sum += int(num)                 #Find the sum
    return sum

print(num_sum(int(num)))                #Call the function