# Written by Ousman 
import math
import random

# 1. Volume of a right square pyramid
def pyramid_volume(b, h):
    return round((b**2 * h) / 3, 2)

# 2. Volume of a cone
def cone_volume(r, h):
    return round((math.pi * r**2 * h) / 3, 2)

# 3. Basketball score
def basketball_score(two_pointers, three_pointers):
    return two_pointers * 2 + three_pointers * 3

# 4. Tennis score
def tennis_score(aces, winning_shots):
    return aces * 2 + winning_shots

# 5. Animal legs counter
def leg_counter(chickens, cows, pigs):
    return chickens * 2 + cows * 4 + pigs * 4

# 6. Battery counter
def battery_counter(e_dolls, rc_cars, robo_dogs):
    return e_dolls * 2 + rc_cars * 4 + robo_dogs * 6

# 7. Resting heart rate
def resting_rate(age, athl_goal):
    if 20 <= age <= 39:
        return "47-72" if athl_goal == "Above Average" else "73-93"
    elif 40 <= age <= 59:
        return "46-71" if athl_goal == "Above Average" else "72-94"
    elif 60 <= age <= 79:
        return "45-70" if athl_goal == "Above Average" else "71-97"
    else:
        return "Unknown"

# 8. Pool times
def pool_time(grade, time):
    if grade in ['k', 1, 2, 3]:
        return "9 AM" if time == "Morning" else "1 PM"
    elif 4 <= grade <= 8:
        return "10 AM" if time == "Morning" else "2 PM"
    elif 9 <= grade <= 12:
        return "11 AM" if time == "Morning" else "3 PM"
    else:
        return "Unknown"

# 9. Traffic light
def traffic_light(color):
    c = color.lower()
    if c == "green":
        return "Go"
    elif c == "yellow":
        return "Yield"
    elif c == "red":
        return "Stop"
    return "Invalid color"

# 10. Access rights
def access_rights(role):
    role = role.lower()
    if role == "admin":
        return "full"
    elif role == "user":
        return "limited"
    elif role == "guest":
        return "view"
    return "unknown"

# 11. Convert knuts
def convert_knuts(knuts):
    galleons = knuts // (29 * 17)
    knuts %= (29 * 17)
    sickles = knuts // 29
    knuts %= 29
    result = []
    if galleons: result.append(f"{galleons} galleon{'s' if galleons > 1 else ''}")
    if sickles: result.append(f"{sickles} sickle{'s' if sickles > 1 else ''}")
    if knuts: result.append(f"{knuts} knuts")
    return " ".join(result)

# 12. Convert bronze
def convert_bronze(bronze):
    gold = bronze // (20 * 15)
    bronze %= (20 * 15)
    silver = bronze // 20
    bronze %= 20
    result = []
    if gold: result.append(f"{gold} gold")
    if silver: result.append(f"{silver} silver")
    if bronze: result.append(f"{bronze} bronze")
    return " ".join(result)

# 13. Toss coin
def toss_coin(guess):
    value = random.randint(0, 1)
    return "Correct!" if guess == value else "Incorrect!"

# 14. Odd or even
def guess_num(guess):
    value = random.randint(0, 9)
    if (value % 2 == 0 and guess == "even") or (value % 2 == 1 and guess == "odd"):
        return "Correct!"
    return "Incorrect!"

# 15. Count duplicates
def count_duplicates(num1, num2, num3):
    nums = [num1, num2, num3]
    max_count = max(nums.count(x) for x in nums)
    if max_count == 3:
        return "You entered the same number 3 times"
    elif max_count == 2:
        return "You entered the same number 2 times"
    else:
        return "Each number is unique"

# 16. Highway directions
def highway_directions(num):
    if 1 <= num <= 99:
        return f"I-{num} runs north/south" if num % 2 else f"I-{num} runs east/west"
    elif 100 <= num <= 999:
        primary = num % 100
        if primary == 0:
            return f"I-{num} is an invalid highway number"
        return f"I-{num} services I-{primary}"
    return f"I-{num} is an invalid highway number"

# 17. Check letter
def check_letter(letter):
    return "Vowel" if letter in "aeiou" else "Consonant"

# 18. Serve ice cream
def serve_icecream(flavor):
    flavor = flavor.lower()
    if flavor in ["vanilla", "chocolate", "strawberry"]:
        return f"Here is your {flavor} ice cream!"
    return f"Sorry, we don’t have {flavor} ice cream."

# 19. Serve coffee
def serve_coffee(coffee):
    coffee = coffee.lower()
    if coffee in ["espresso", "latte", "cappuccino"]:
        return f"Here is your {coffee}!"
    return f"Sorry, we don’t have {coffee}."

# 20. Rock Paper Scissors
def find_winner(player1, player2):
    if player1 == player2:
        return "It’s a tie!"
    elif (player1 == "Rock" and player2 == "Scissors") or \
         (player1 == "Scissors" and player2 == "Paper") or \
         (player1 == "Paper" and player2 == "Rock"):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"

# 21. Triangle type
def triangle_type(a, b, c):
    if a == b == c:
        return "equilateral"
    elif a == b or b == c or a == c:
        return "isosceles"
    return "scalene"

# 22. Luke’s relations
def find_relation(name):
    relations = {
        "Darth Vader": "Father",
        "Leia": "Sister",
        "Han": "Brother in law",
        "R2D2": "Droid"
    }
    return relations.get(name, "Unknown")

# 23. Sherlock relations
def find_suspect(name):
    suspects = {
        "Moriarty": "Archenemy",
        "Watson": "Best Friend",
        "Mrs. Hudson": "Landlady",
        "Inspector Lestrade": "Detective"
    }
    return suspects.get(name, "Unknown")

# 24. Skip every other letter (start 2nd)
def skip_letter_second(word):
    return word[1::2]

# 25. Skip every other letter (start 1st)
def skip_letter_first(word):
    return word[::2]

# 26. Output evens
def output_even(small, large):
    return list(range(small + (small % 2), large + 1, 2))

# 27. Odd sum
def odd_sum(small, large):
    return sum(x for x in range(small, large + 1) if x % 2 == 1)

# 28. Create word interactively
def create_word():
    word = ""
    while True:
        letter = input("Enter a letter (or 'done' to stop): ")
        if letter == "done":
            break
        word += letter
    return word

# 29. Sum loop
def sum_loop():
    total = 0
    while True:
        num = int(input("Enter a number (negative to stop): "))
        if num < 0:
            break
        total += num
    return total

# 30. Hailstone sequence
def hailstone_seq(n):
    seq = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        seq.append(n)
    return seq

# 31. Find factors
def find_factors(num):
    return [i for i in range(1, num + 1) if num % i == 0]

# 32. Rug design
def design_rug(width, length, pattern):
    return "\n".join([pattern * width for _ in range(length)])

# 33. Square sum
def square_sum(num):
    if num < 0:
        return "unknown"
    return sum(i**2 for i in range(1, num + 1))

# 34. Cube sum
def cube_sum(num):
    if num < 0:
        return "unknown"
    return sum(i**3 for i in range(1, num + 1))
