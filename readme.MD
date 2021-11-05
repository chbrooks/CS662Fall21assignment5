Uncertainty

Due: Wed 11/25, start of class.

100 points.

Please include the written answers to your questions in a separate file.

In addition to the material in Russell and Norvig, and in the lecture slides, you might find the following 
resources useful:
- Hidden Markov Models: Juravsky & Martin, Ch 8: https://web.stanford.edu/~jurafsky/slp3/8.pdf
- Reinforcement Learning: Sutton, Ch 5: http://incompleteideas.net/book/RLbook2020.pdf


(10 points) Task 1: Modify the Car starting Bayes Net example included here to add the following nodes:
- Key in ignition. This has a prior of P(key) = 0.6.  It should also influence the 'starts' node; modify it to also have 'key' as a parent. You may choose values for 'key's CPT.
- Wheel blocked. This should have a prior of 0.1, and should influence 'moves'. If the wheel is blocked, the car should have a 0.96 probability of not moving.

Suppose that 'wheel blocked' is a node that we can control directly, rather than just observe. We want to make sure that the car has less than a 0.1 probability of moving, but we'd like to not block the wheels unless it is necessary. Use the network to determine values for 'gas' and 'radio' that would lead us to decide to block the wheels.

(40 points) Task 2: Hidden Markov Models.
(Note: this is derived from an assignment in AAAI's Model Assignments workshop)

In this assignment you'll be implementing three algorithms associated with Hidden Markov Models.

You'll be building off of the code presented in HMM.py.
There's also some included data to use. 

The first set models the frequency of different characters in English, along with the transition between "C" (consanant) and "V" (vowel).
- two_english.emit. This contains the probability of a state "emitting" a given output (a letter, in this case). 
- two_english.trans files. These contain the transition probabilities between states.

This is small, but good to use when you're debugging.

The second set contains tagged parts-of-speech from the Brown corpus.
- partsofspeech.BrownTags.emit - the probability of each state (POS tag) emitting a particular word.
- partsofspeech.BrownTags.trans - the transition probability for each hidden state (POS)

1. Use the included code to implement load and dump. Use two_english as a sample file to work with.
You should be able to do:

<pre>
    model = HMM()
    model.load(models/two_english)
    model.dump(two_english_test)
</pre>

2. Implement generate. This should start with the start state of your model and generate a random sequence of state transitions and observations. Try it out with both data sets to generate random words and sentences.


3. Next, implement forward. It should take a sequence of observations and tell us how likely those are for a given model. 


5. Next, implement Viterbi. This tells us, for a sequence of observations, the most likely sequence of states.

Note: since vowels and consonants are almost completely disjoint in English (except for 'y'), these last two
tasks should be very easy with the two_english dataset, but it will help you debug. It's more 
interesting with the Brown set.


(10 points) Task 3: Utility calculations.
1. Suppose that our agent can choose one of four doors to pass through. It knows that:
    1. The reward for door 1 is $5.
    2. The reward for door 2 is either $0 (50%) or $10 (50%)
    3. The reward for door 3 is either $5 (80%) or $20 (20%)
    4. The reward for door 4 is either $0 (10%), $7 (30%), or $12 (60%).

    5. What is the EU for each door?

Which door should we pick? Please show your expected utility calculations.

Suppose we could pay to find out what the reward is for door 3. After we learn this information we can choose a door. How much would we pay for this? Please show your work.


(40 points) Task 4: Monte Carlo simulation.

In this task, we'll use Monte Carlo Simulation to do reinforcement learning in a simple problem.

Consider the dice game "Approach". It works like this: There are two players, and they choose a target number (n).
Player 1 repeatedly rolls a six-sided die and adds up their total. Whenever they want, they can "hold." Then player 2 must roll;' their goal is 
to beat player 1's score without going past n.

The problem we want to solve is this: 

For player 1, for a given n and a particular total so far (called s) should they
'hold' (action 1) or 'roll' (action 2).

(note that player 2's strategy in this game is pretty boring - they just roll until they either beat player 1's score or exceed n.)

To begin, let's use Monte Carlo simulation to better understand player 1's decision.

Write a program that takes as input a limit n. 

It should:
  For all values from 5-n, estimate the probability of winning, given that we 'hold' at that value.
<pre>
For example, if n=10, you might see:
 5: 0.268023
 6: 0.389456
 7: 0.477032
 8: 0.492804
 9: 0.441647
10: 0.288904
</pre>

And so holding when our total is 8 maximizes the chance of winning.
To construct this, use a Monte Carlo simulation with at least 1000000 simulations for each possible value s. Print out the probability 
of winning, given 'hold' for each value from 5 to n.

This gives us a policy for this problem.

2. This is fine when there's a small number of potential policies to consider, but it's not very scalable.
Let's now add in Q-learning. 
Q-learning generates a table that stores Q(s,a). Write a function that takes in a limit n
and computes the Q-table for [0,n] with the actions (hold, roll).

For example, for n=10, you might get:

    sum:   hold     roll   [action]
    0: 0.000000 0.493921 [roll]
    1: 0.000000 0.477271 [roll]
    2: 0.000000 0.479286 [roll]
    3: 0.000000 0.505797 [roll]
    4: 0.000000 0.580803 [roll]
    5: 0.051270 0.498027 [roll]
    6: 0.170403 0.427388 [roll]
    7: 0.297536 0.365115 [roll]
    8: 0.478196 0.285432 [hold]
    9: 0.711051 0.164235 [hold]
    10: 1.000000 0.000000 [hold]

We will do this using *epsilon-soft on-policy control*, a form of reinforcement learning. We will select the optimal action with probability (1-epsilon) and explore with probability epsilon.
(use epsilon=0.1 for this.)

Start  by initializing the Q-table to small random values. Our agent should start with a random s and a and then either take the best action (prob. 1-epsilon), or the other action (prob. epsilon). 
At the end of the game, it receives reward 1 (if it wins) or 0 (if it loses). It then uses this to update the Q value for each state-action pair chosen. 
Run for 1000000 iterations and print out the Q-table, and optimal action for each state. 
