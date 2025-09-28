# Written by Ousman 
# Question 1
def pyramid_volume(baae, height):
    volume = (base**2 * height) / 3
    return volume
print(f"Volume of the pyramid is: {pyramid_volume(3, 4)}")

# Question 2
def pool_time(grade, time):
    # Kindergarten case
    if grade == 'k':
        if time.lower() == "morning":
            return "9 AM"
        elif time.lower() == "afternoon":
            return "1 PM"
    
    # Grades 1–3
    elif isinstance(grade, int) and 1 <= grade <= 3:
        if time.lower() == "morning":
            return "9 AM"
        elif time.lower() == "afternoon":
            return "1 PM"
    
    # Grades 4–8
    elif isinstance(grade, int) and 4 <= grade <= 8:
        if time.lower() == "morning":
            return "10 AM"
        elif time.lower() == "afternoon":
            return "2 PM"
    
    # Grades 9–12
    elif isinstance(grade, int) and 9 <= grade <= 12:
        if time.lower() == "morning":
            return "11 AM"
        elif time.lower() == "afternoon":
            return "3 PM"
    
    # If nothing matches
    return "Invalid grade or time"
