text = input("You find yourself in a dark hallway. Would you like to go left or right?").lower()
match text:
  case "left":
    second_text = input("You see a trapdoor and under it is a ladder that you climb down into a room with 2 doors. Would you like to go into the back or front door?").lower()
    match second_text:
      case "back":
        third_text = input("You climb down a ladder into a room with three potions. There is one in the right and left corner, and one in the middle. Which one do you drink?").lower()
#2
        match third_text:
          case "middle":
            fourth_text = input("You fall asleep and awake in a room with a pig portal. Do you go in?").lower()
            match fourth_text:
              case "yes":
                sixth_text = input("You go into the portal and find yourself in some type of colorful jungle. There is a path. Do you go left, right, or forward?").lower()
              case "no":
                print("Say yes")
          case "left":
            fith_text = input("You fall asleep and awake in a cave underground. There are 2 levers on each side of you. Which one do you pull?").lower()
#3
            match fith_text:
              case "right":
                seventh_text = input("You go into the portal and find yourself in some type of colorful jungle. There is a path. Do you go left, right, or forward?").lower()
              case "left", "right":
                print("You die")
          case "right":
            print("You die")
      case "front":
        print("You die")
  case "right":
    print("You die")
