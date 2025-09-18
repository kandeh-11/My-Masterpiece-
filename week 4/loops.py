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

  #Question 4
while True:
    user_input = input('Enter a letter: ')
    if user_input == "done":
        break
    else:
        word += user_input
        print(f"The final word is {word}")
