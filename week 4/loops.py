#Ousman Kandeh
'''
larger_num = int(input("Enter a larger number: "))
smaller_num = int(input("Enter a smaller number: "))


num = 0
while larger_num>smaller_num:
    larger_num / 2
    num += 1
    print(f"number of times if halfed: {num}")

'''

#Question 2
'''
word = input("Enter a word: ")
result = ""

for i in range(1, len(word) - 1, 2):
    result += word[i]
print(f"Output = {result}")
'''
#Question 3
'''
for num in range(37, 1051):  
    if num % 2 == 0:          
        print(num)
'''

  #Question 
'''
while True:
    user_input = input('Enter a letter: ')
    if user_input == "done":
        break
    else:
        word += user_input
        print(f"The final word is {word}")
'''
#Question 5
'''
for num in range(50, 518):  
    if num % 2 == 1:          
        print(num)

    Or
for number in range(51, 518, 2):
        print(number)
'''
#Question 6
total = 0
while True:
    num = int(input("Enter an integer (negative number to stop): "))
    if num < 0:
        break   # stop the loop if number is negative
    total += num  # add the number to the total if it's not negative

print("The sum of the numbers is:", total)