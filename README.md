# codingtest_verdi
this is coding test from verdi

Code Question:

===============================================================================================

After the nuclear war, a strange and deadly virus has infected the planet. Living creatures are becoming zombies that spread their zombiness by an unfriendly bite. 



So, in an area of NxN (top left assumed to be (0,0) ), zombie awakes. Zombie can move within the area and can move up, down, left and right (U,D,L,R). There are also poor creatures within the area that can become zombie's victims. Their position is defined with a pair of coordinates (x,y). The creatures are aware of zombie presence, but so frightened - that never move. If zombie moves so that it ends up on the same location as a poor creature - the creature disappears and zombie scores 1 point. 



Given the file that contains:

dimensions of the area (N)
initial position of the zombie
a list of positions of poor creatures 
and a list of moves zombie will make
the program should output:

the final position of the zombie and the amount of points scored.



This exercise does not have "right" or "wrong" and is pretty open-ended. You can pick any programming language of your choice and can make it as simple or as complex as you would like (or time allows). There is no requirement in visualising this in any way (as in - no UI needed), however you are welcome to create one if you wish.



Example:

4

1 1

0 0,2 2,0 2

LURRDD



Output:

score: 2

location: 2 2

===============================================================================================

In this package, we have four python files(modules)

creature.py and zombie.py are used to create two main elements in the project, poor creatures and zombie

main.py is used to control the system and test.py is test module

To run the project, you can import it into eclipse with plugin named Pydev(http://pydev.org/) and run the main.py

and this project is on github now:https://github.com/flydsc/codingtest_verdi
