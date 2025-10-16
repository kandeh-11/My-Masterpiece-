#written by Ousman
#question 5

def is_acronym(s, words):
    # If any word is empty, it's not possible
    if any(word == "" for word in words):
        return False
    
    # Build the acronym from the first letters
    acronym = "".join(word[0] for word in words)
    
    # Compare with s
    return acronym == s


# Test cases
print(is_acronym("abc", ["alice", "bob", "charlie"]))  # True
print(is_acronym("a", ["an", "apple"]))                # False
print(is_acronym("ngguoy", ["never", "gonna", "give", "up", "on", "you"]))  # True
print(is_acronym("ab", ["apple", "banana", "cat"]))    # False (length mismatch)
print(is_acronym("ab", ["apple", "", "cat"]))          # False (empty string in words)
