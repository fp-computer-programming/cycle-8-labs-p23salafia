def count_a(word):                                      #Define the input string
    count = 0
    for letter_a in word:
        if letter_a == 'a' or letter_a == 'A':          #Define what should tick up the count by 1
            count += 1                                  #Add 1 to the count for every A
    return count
print(count_a("AaAaa"))                                 #Call the function and print the result