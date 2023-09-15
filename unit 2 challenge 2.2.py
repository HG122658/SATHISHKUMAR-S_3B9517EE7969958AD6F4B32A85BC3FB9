'''Implement a class called Player that represents a cricket player. The Player class should have a 
method called play() which prints "The player is playing cricket. Derive two classes, Batsman and 
Bowler, from the Player class. Override the play() method in each derived class to print "The batsman
is batting" and "The bowler is bowling", respectively. Write a program to create objects of both the
Batsman and Bowler classes and call the play() method for each object.'''


#define the base class player
class player:
  def play(self):
    print("The batsman is batting.")

# Define the derived class batsman
class Batsman(player):
  def play (self):
    print("The batsman is batting.")

# Define tha derived class bowler
class Bowler:
  def play(self):
    print("The bowler is bowling.")

#Create objects of batsman and bowler classes
batsman = Batsman()
bowler = Bowler()

#call the play() method for each subject
batsman.play()
bowler.play()