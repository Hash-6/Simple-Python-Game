# MADE BY HASH6 (DO NOT REMOVE)

# Get input from user
text = input("You find yourself in a dark hallway. Would you like to go left or right?").lower()

# Handle left choice
if text == "left":
    # Get input from user
    second_text = input("You see a trapdoor and under it is a ladder that you climb down into a room with 2 doors. Would you like to go into the back or front door?").lower()
    
    # Handle back door choice
    if second_text == "back":
        # Get input from user
        third_text = input("You climb down a ladder into a room with three potions. There is one in the right and left corner, and one in the middle. Which one do you drink?").lower()
        
        # Handle middle potion choice
        if third_text == "middle":
            # Get input from user
            fourth_text = input("You fall asleep and awake in a room with a pig portal. Do you go in?").lower()
            
            # Handle yes/no choice
            if fourth_text == "yes":
                # Get input from user
                sixth_text = input("You go into the portal and find yourself in some type of colorful jungle. There is a path. Do you go left, right, or forward?").lower()
                
                # Handle path after portal
                if sixth_text == "forward":
                    print("You die")
                elif sixth_text == "right":
                    # Get input from user
                    eighth_text = input("The ground opens up from under you and you fall into a cave. Do you go to the left or to the right?").lower()
                elif sixth_text == "left":
                    # Get input from user
                    ninth_text = input("The path splits again. Do you go forward, left, or right?").lower()
                else:
                    print("Say left or right")

            elif fourth_text == "no":
                # Print statement
                print("Say yes")
        
        # Handle left potion choice
        elif third_text == "left":
            # Get input from user
            fifth_text = input("You fall asleep and awake in a cave underground. There are 2 levers on each side of you. Which one do you pull?").lower()
            
            # Handle lever choice
            if fifth_text == "right" or fith_text == "left"
                print("You get blown up")
            else:
                # Print statement
                print("say left or right")
        
        # Handle right potion choice
        else:
            # Print statement
            print("You die")
    
    # Handle front door choice
    elif second_text == "front":
        # Print statement
        print("You die")

# Handle right choice
elif text == "right":
    # Print statement
    print("You die")    
