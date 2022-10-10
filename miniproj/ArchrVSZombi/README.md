# ArchrVSZombi
This was my final assignment for my programming module in Semester 1. Just uploading the code for fun. To summarise, a Plant VS Zombie rendition in Python text only mode.
# To get it to work
1. Just run the py file. Should work on most systems.
# Overview of the game
Here's an excerpt from the document file.
"Undead creatures are attacking the city! Position your units to protect the city until you have killed enough of the creatures to drive them off.
In this “tower defence” strategy game, monsters are advancing on the city from right to left across 5 lanes. To kill the monsters, you have to purchase units and place them on the field of battle so that they can shoot or block the monsters. However, you start with 10 gold and only get 1 gold per turn, so spend your precious resources wisely!

There are two types of monsters:
-   Zombies (ZOMBI) start with 15 hit points, deal 3-6 damage and move 1 square each turn. They initially give 2 gold as a reward when killed.
-   Werewolves (WWOLF) start with 10 hit points, deal 1-4 damage and move 2 squares each turn. They initially give 3 gold as a reward when killed. **Note: Implementing Werewolves is an Advanced Requirement.**
Players can purchase two types of “defender” units:

-   (Pea Shooter) Archers (ARCHR) start with 5 hit points. Each turn, they will shoot an arrow down their lane from left to right, dealing 1-4 damage to the first monster it hits. They cost 5 gold to purchase.
    
-   (Nut) Walls (WALL) start with 20 hit points. They do not deal any damage and serve to block and slow down the monsters. They cost 3 gold to purchase.

Units purchased by the players can only be placed in the first 3 columns of the field.

The assignment consists of “**Basic Requirements**” and “**Advanced Requirements**” as described in sections 4 and 5 respectively. You are advised to complete the basic requirements BEFORE proceeding with the advanced requirements.

For this assignment, you are expected to:

-   Understand the problem completely and plan your program layout before you start coding
    
-   Develop the solution for each task by using functions
    
-   Functions developed should be as generic as possible - values used in functions should be passed in as the function parameters
    
-   You may use global variables **sparingly**
    
-   Implement and test each feature as it is developed
    
-   Do all the relevant data validations

# Advanced objectives from my teachers
Excerpt again.
1.  **Display main menu**
When the program is first run, it should display the main menu. When a user enters an option 1, 2 or 3, the program will process the option accordingly.

2.   **Start New Game**
This option starts a new game. The field of battle consists of 5 lanes (labelled A to E), each 7 squares long. When the game starts, a monster is spawned (i.e., created) on the rightmost square in a random lane. **For your Basic Requirements, implement only the Zombie.** The numbers below a monster are its current and maximum hit points. Players begin Turn 1 with 10 gold. **Advanced feature**: the “Threat Metre” is empty, and the Danger Level starts at 1.

3. **Load Saved Game**
This option reads the saved file and restores the game state. You can only have one saved game.
4. **Exit Game**
This option exits the program.
5.  **Playing the Game**
When you are playing the game, it should display the game menu as shown in Figure 1.1. When a user enters an option from 1 to 4, the program will process the option accordingly.
6.  **Buy Unit**
Option 1 allows the player to purchase and place a unit. The player first selects whether to purchase an Archer (for 5 gold) or a Wall (for 3 gold). The player must then specify which square to place the unit. Note that purchased units can only be placed on an empty square in one of the first 3 columns. An appropriate error message should be shown if the input is invalid.
If the purchase is successful, time advances and several things happen (see Section 2.2 below). Note that if the purchase is not successful, time does not advance.
7.  **End Turn**
When the player chooses option 2, time advances in the game, and several things happen. Each lane is checked starting from lane A and ending in lane E. For each lane, consider each unit from left to right:
8.  Archers shoot an arrow from left to right, hitting the first monster on its lane that it encounters and dealing 1-4 damage (i.e., deduct that amount of damage from the monster’s hit points). If this reduces the monster’s hit points to zero:
    
    -   The monster is removed from the field
        
    -   The player is given some gold as a reward according to which monster was killed
        
    -   **Advanced feature:** The Threat Metre increases by the same amount as the reward
9.  Monsters move a number of spaces equal to their movement speed towards the left.
    
    -   If it would land on a defender unit, it instead deals its damage to the defender. If this kills the defender, it is removed from the field.
        
    -   If it would land on another monster, it is blocked and does nothing.
        
    -   If it would go off the field on the left side, the player has lost the game.
After all the lanes have been checked, the following happens at the end of the turn:
- If there are no monsters left on the field, a new monster is immediately spawned
    
- The player is given 1 gold.
3.  **Advanced feature:** The Threat Metre is increased by a random number between 1 and the Danger Level.
    
4.  **Advanced feature:** The Threat Metre has 10 spaces. If the Threat Metre is full, a new monster is spawned, and the Threat Metre is reduced by 10. Note that theoretically, if the Threat Metre is over 20, then multiple monsters will be spawned, reducing the Threat Metre by 10 each time until it is below 10.
    
5.  **Advanced feature:** Every 12 turns, the monsters get stronger. All monsters will add 1 to their minimum and maximum damage (e.g., 3-6 becomes 4-7), their maximum hit points and the amount of reward they give. The increase in hit points do not affect the current hit points of the monsters already on the field. Furthermore, the Danger Level increases by 1, which could make the Threat Metre rise faster.
6.  **Save Game**
This saves the current state of the game, so that after the player quits the game, they can return to the current state by selecting “Load Saved Game” in the main menu (see 3).
7.  **End of Game**
The player loses if any monster exits the left side of the field.

The player wins once 20 monsters have been killed.

# Advanced features

1.  **Program validation -- 10 marks**
Add appropriate validation for the basic requirements of the program.
2. **Werewolves -- 5 marks**
Implement the Werewolf monster
3. **Threat -- 10 marks**
Implement the **threat metre** and **danger level**. This includes:
-   The threat metre that contains 10 spaces and shows the current threat amount. When it fills up, a new monster is spawned and the threat amount is reduced by 10.
    
-   When a monster is killed, the threat amount is increased by the monster’s reward.
    
-   At the end of each turn, the threat amount is increased by a random number between 1 and the danger level, inclusive.
    
-   Every 12 turns, the danger level is increased by 1. This causes the minimum damage, maximum damage, maximum hit points and reward for all monsters to increase by 1.
4. **Additional features – up to 10 BONUS marks**
You may gain up to 10 bonus marks if you implement additional features to improve the game. The following are some suggestions. Feel free to devise your own additional features.
-   **Upgrade Unit –** Allow players to upgrade their Archer units, which increases their minimum damage, maximum damage and hit points by 1. This costs 8 gold the first time, and an extra 2 gold each time after that (8, 10, 12 …)
Similarly, players can upgrade their Walls with an extra 5 hit points by spending gold equal to 6, 8, 10 …
-   **Mine –** New defender unit Mine (MINE) that costs 8 gold. When a monster walks onto a mine, it explodes to deal 10 damage to all monsters in the 9 squares surrounding it (including its own position). It does not damage defenders.
-   **Heal/Repair** – Allow players to spend 5 gold to allow all defender units in a 3x3 square to recover 5 hit points.
-   **Cannon**  – New defender unit Cannon (CANON) that costs 7 gold. It has 8 hit points, deals 3-5 damage, but can only fire every other turn. It also has a 50% chance to push a monster backwards by one square.
-   **Skeleton** – New monster unit Skeleton (SKELE). It has 10 hit points and deals 1-3 damage, but it only takes half damage from Archers. This monster should only be included if you have already implemented some other defender unit that can deal damage (like the Mine or Cannon).
-   **Game Options** **–** Allow players to specify various game options, such as the board dimensions (number of lanes and length of each lane), number of kills needed to win, Threat Metre length, etc.
-   **Challenge Scenarios** – Allow players to play games that have a specific set of monster spawns in a fixed sequence every time. The game records when the player has successfully beaten a scenario.
# So yes, this is my implementation of it.
If you guys somehow wanna help me improve it feel free, or even improve it? I don't mind.
# Any questions
Feel free to make a github issue or email me if you don't understand the code. I will find a free time to explain. :) Always here to help.
