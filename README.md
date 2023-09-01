# Dice Roll Statistics Model

When rolling two six-sided dice, the probability of rolling a sum of 7 is about 17%, which is much higher than the probability of rolling a sum of 2, which is only 3%. This is because there is only one combination that gives a sum of 2 (when both dice roll 1), while there are many combinations that give a sum of 7, such as 1 and 6, 2 and 5, 3 and 4, and so on.

What happens when three dice are rolled? Or four? Or a thousand? We can calculate theoretical probability values mathematically, or we can ask the computer to "roll the dice" a million times and get empirical values. It is this second approach that our program implements. We ask the computer to "roll" N dice a million times, memorize the results, and then display the probabilities of rolling each sum of points as a percentage.

## How to Use

1. Run the program in a compatible environment.
2. Specify the number of dice to roll (e.g., 2, 3, 4, or any desired number).
3. The program will simulate a million dice rolls for the specified number of dice.
4. Explore the displayed probabilities of rolling each sum of points as a percentage.

## Features

- Gain empirical insights into the probabilities of rolling specific sums with multiple dice.
- Simulate a million dice rolls to obtain empirical probability values.
- Visualize the probabilities of rolling each sum of points based on the simulation results.

## Instructions

1. Open a terminal or command prompt.
2. Navigate to the program's directory.
3. Run the program using `python dice_roll_statistics.py`.
4. Follow the on-screen prompts to specify the number of dice and observe the simulated probabilities.

## Note

The Dice Roll Statistics Model provides an empirical approach to understanding the probabilities of rolling specific sums with multiple dice. Whether you're exploring probabilities for two dice or a thousand, this program offers valuable insights based on a million simulated rolls.
