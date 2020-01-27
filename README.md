# carnival-game

# Exercise
There is a game at a carnival which involves players randomly selecting balls from inside a chest. 
There are 15 balls in the chest, six are yellow, three are red, three are green, two are orange, one is purple.
Yellow balls are worth 1 point, red balls 2, green balls 4, orange balls 5 and the purple ball is worth 10.
You pick 5 balls out of the bag, if you score is more than 22 you win a big prize, if your score is between 15 and 22 you win a small prize, if your score is less than 15 you go home empty handed.
The problem is, the worker manning the game isn’t that great at maths, so we are going to write a programme to help them calculate the score and check what prize they deserve!

1.	We need to simulate someone randomly picking 5 balls out of the chest. We can do this by creating a list that contains 5 random numbers and creating a while loop that will only stop once we have a list of the right length.
2.	We need to map each of those randomly selected balls to a colour so that we can select its score. Create a collection that states which randomly selected number corresponds to each ball. Then use a for loop to turn each randomly selected number into its colour

1.	Create a while loop that iterates through each balls selected colour, and calculates the total score.

1.	Using if/elif/else statements to print out if the person has won a prize and what size it is.
  Additional points to consider
•	We can’t pick the same ball out of the chest twice
•	How are you storing the points system? What is the best collection type to use
Can you reduce the number of lines of code you are using (our best is 30) this might mean you stray away from the steps we’ve given you above
