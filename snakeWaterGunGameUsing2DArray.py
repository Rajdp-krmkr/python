# D for Draw, W for Win, L for Lose
# Snake = 0 or S, Water = 1 or W, Gun = 2 or G
import random
import math

arr = [["Draw","Win","Lose"],["Lose","Draw","Win"],["Win","Lose","Draw"]];
num = math.floor(random.random()*100);

computer = None;
computerTook = None;

if(num < 33):
    computer = 0; # Snake or S
    computerTook = "Snake";
elif(num < 66):
    computer = 1; # Snake or W
    computerTook = "Water";
else:
    computer = 2; # Snake or L
    computerTook = "Gun";
    
player = int(input("Enter 0 for Snake, 1 for Water, 2 for Gun: "));
PlayerTook = None;

if(player < 0 or player > 2):
    print("Invalid Input");
else :
    if(player == 0):
        PlayerTook = "Snake";
    elif(player == 1):
        PlayerTook = "Water";
    else:
        PlayerTook = "Gun";
    print("You: ", PlayerTook);
    print("Computer: ", computerTook);
    print("Result: ", arr[computer][player]); 
exit(0);   
