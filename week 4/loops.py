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
'''
while True:
    num = int(input("Enter an integer (negative number to stop): "))
    if num < 0:
        break   # stop the loop if number is negative
    total += num  # add the number to the total if it's not negative

print("The sum of the numbers is:", total)
'''
#Question 7
'''
n = int(input("Enter a positive integer: "))

print("Hailstone sequence:")

while n != 1:
    print(n, end=" ")  # print current number
    
    if n % 2 == 0:  # even
        n = n // 2
    else:  # odd
        n = 3 * n + 1

print(1)
'''

#Question 8
'''
num = int(input("Enter an integer: "))

print(f"Factors of {num} are:")

# Loop through numbers from 1 to num
for i in range(1, num + 1):
    if num % i == 0:  # Check if i is a factor
        print(i)
'''
#Question 9
'''
width = int(input("Enter rug width: "))
length = int(input("Enter rug length: "))
pattern = input("Enter a pattern character (e.g., *, #, @): ")

print("\nHere is your rug:\n")

# Print the rug
for _ in range(length):
    print(pattern * width)
'''
#Question 10
'''
argest_even = -1  # Default if no even numbers are entered

while True:
    num = int(input("Enter an integer (negative to stop): "))
    
    if num < 0:  # Stop if negative number entered
        break
    
    if num % 2 == 0:  # Check if even
        if num > largest_even:
            largest_even = num

print("Largest even number entered:", largest_even)
'''
# Question 11
'''
n = int(input("Enter an integer: "))

total = 0
for i in range(1, n + 1):
    total += i ** 2

print("Sum of squares up to", n, "is:", total)
'''