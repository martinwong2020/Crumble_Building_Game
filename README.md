# Crumble_Building_Game


### Description 
This is a python game created using the pygames library. The objective of this game is to get the highest score while doding falling buildings(blocks).
Every block dodge rewards you with a point but the higher your score the more blocks there will be. The controls are arrow keys or WASD. While playing the game, a melody will play in the background
### How the Code Looks:

There are two classes
1. Player class used to keep track of positioning and displaye player
2.  Block class used to keep track of block positioning

There are two move functions
 1. There is a player move function that tracks the key clicked to move the player horizontally.
 2. There is a block move function that tracks if the block has hit the ground and resets at a random value along the x-axis

There are other values such as score, level, and game_over
1. Score: Keeps track of the score based on how many blocks hit the ground
2. Level: Keeps track of the board level and it implements a new block per level
3. Game_over: Keeps track if the game is still running or if the player has lost
   
### Game Images
