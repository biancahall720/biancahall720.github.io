Done = False
# Update this text to match your story.
start = '''
You wake up one morning and find that you aren't in your bed; you aren't even in your room.
You're in the middle of a giant maze.
A sign is hanging from the ivy: "You have one hour. Don't touch the walls."
There is a hallway to your right and to your left.
'''

print(start)

print("Type 'left' to go left or 'right' to go right.") # Update to match your story.
user_input = input()
while(Done != True):
    print("Try another answer")
    if(Done == True):
        continue
    if user_input == "left":
        print("You find two tunnels. One of them goes under the maze and will free you. The other one leads you to a snake pit and you fall to your sudden death. What you gon' do?") # Update to match your story.
    if user_input == "right":
        print("You find two tunnels. One of them is a mystery tunnel that you do not know nothing about because you've never been in this maze before. And the other one leads you to bigfoot.") # Update to match your story.

    print("Type 'left' to go left or 'right' to go right.")
    user_input = input()
    if user_input == "left":
        print("You decide to go left and you find a tunnel that goes under the maze. When you exit the maze, do you want to go left or right?") # Update to match your story.
    if user_input == "right":
        print("You chose to go right and you are harassed by bigfoot. Do you want to run to the left or the right?") # Update to match your story.

    print("Type 'left' to go left or 'right' to go right.")
    user_input = input()
    if user_input == "left":
        print("You are running to the left and fall into a 10ft hole in the ground filled with spiders. You die from a heart attack. GAME OVER") # Update to match your story.
    if user_input == "right":
        print("You choose to go right and you safely get out the maze.") # Update to match your story.

    # Continue code to finish story.
