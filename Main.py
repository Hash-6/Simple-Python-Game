text = input("You find yourself in a dark hallway. Would you like to go left or right? ")
if text.lower() == "right": 
    print("You die.")
elif text.lower() == "left": 
    second_text = input("You fall down a trapdoor into another room. There are 2 doors. Do you go into the front or back door?")
    if second_text.lower() == "back":
        third_text = input("The door leads into a room with 3 potions. There is one in the left corner on the room, the right corner of the room, and the middle. Which one do you drink?")
    elif second_text.lower() == "front":
        print("You die.")
    else:
        print("say front or back as your answer")

if third_text.lower() == "middle":
  third_text = input("You fall asleep and awake in a room with a pig portal. Do you go in?")
elif third_text.lower() == "left":
  text = third_text = input("You fall asleep and awake in a cave underground.")
elif third_text.lower() == "right":
  print("you die")
else:
  print("say middle, left, or right as your answer")

if third_text.lower() == "yes":
  fourth_text = input("You go into the portal and find yourself in some type of colorful jungle. There is a path. Do you go left, right, or forward?")
  if fourth_text.lower() == "left":
    print("you die")
  elif fourth_text.lower() == "right":
    fifth_text = "?"
  elif fourth_text.lower() == "forward":
    print("you die")
  else:
    print("type forward or Forward as your answer.")
