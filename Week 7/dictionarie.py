# Written by Ousman

# 1. Isogram check
def is_isogram(word):
    word = word.lower()
    return len(set(word)) == len(word)

# 2. Find unique number
def find_unique(numbers):
    for n in numbers:
        if numbers.count(n) == 1:
            return n

# 3. Return two unique numbers
def return_unique(numbers):
    result = []
    for n in numbers:
        if numbers.count(n) == 1:
            result.append(n)
    return result

# 4. Get names from dictionary
def get_names(names):
    return list(names.values())

# 5. Find oldest person
def find_oldest(people):
    return max(people, key=people.get)

# 6. Letter count
def letter_count(word):
    counts = {}
    for letter in word:
        counts[letter] = counts.get(letter, 0) + 1
    return counts

# 7. Course with minimal grade
def min_grade(exams):
    return min(exams, key=exams.get)

# 8. Find youngest person
def find_youngest(people):
    return min(people, key=people.get)

# 9. Receipt total
receipt = {}
receipt["Side Salad"] = 6
receipt["Chicken Parm"] = 12
receipt["Cookie"] = 3
total_cost = sum(receipt.values())
print("Receipt total:", total_cost)

# 10. Menu printing
menu = {}
menu["burger"] = 10
menu["fries"] = 4
menu["soda"] = 3
print("Menu items:")
for item, price in menu.items():
    print(item, ":", price)

# 11. Count repetitions
def count_repetitions(elements):
    counts = {}
    for item in elements:
        counts[item] = counts.get(item, 0) + 1
    return counts

# 12. Items you can purchase
def items_purchase(store, wallet):
    result = []
    for item, price in store.items():
        if price <= wallet:
            result.append(item)
    return result

# 13. Total sales
def total_sales(sales):
    return sum(sales.values())

# 14. High earners
def high_earners(employee_salaries, salary):
    return [name for name, pay in employee_salaries.items() if pay > salary]

# 15. Total donations
def total_donations(donations):
    return sum(donations.values())

# 16. Total calories
calories = { "apple": 95, "banana": 105, "orange": 62, "grape": 3, "pear": 102 }
def total_calories(fruits):
    total = 0
    for fruit in fruits:
        if fruit in calories:
            total += calories[fruit]
    return total

# 17. Total cost
prices = { "flour": 2.50, "sugar": 1.80, "eggs": 3.00, "milk": 2.00, "butter": 2.75, "vanilla": 4.50, "chocolate": 5.00 }
def total_cost(ingredients):
    total = 0
    for item in ingredients:
        if item in prices:
            total += prices[item]
    return total

# 18. Majority element
def majority_element(nums):
    for n in nums:
        if nums.count(n) >= len(nums) / 2:
            return n
