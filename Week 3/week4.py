light_color=input("Enter the traffic light color (red, yellow, green): ")

if light_color == "red":
    print("Stop")
elif light_color == "yellow":
    print("Caution")
elif light_color == "green":
    print("Go")
else:
    print("Invalid color")