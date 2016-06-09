# A program to print 10 verses of "The Ants Go Marching" using functions
# by Sarah Dawson


number = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]

woot = "hurrah! hurrah!"

action = ["suck his thumb", "tie his shoes", "climb a tree", "shut the door", "take a dive", \
		"pick up sticks", "pray to heaven", "roller-skate", "check the time", "shout THE END"]


def antMarchingWoot(teams):
	print "The ants go marching " + teams + " by " + teams + ", " + woot
	print "The ants go marching " + teams + " by " + teams + ", " + woot


def antMarching(teams):
	print "The ants go marching " + teams + " by " + teams + ", "


def littleAnt(tomfoolery):
	print "The little one stops to " + tomfoolery + ","


def main():
	for i in range(len(number)):
		antMarchingWoot(number[i])
		antMarching(number[i])
		littleAnt(action[i])
		print "And they all go marching down..."
		print "To the ground..."
		print "To get out..."
		print "Of the rain."
		print "Boom! Boom! Boom! Boom! Boom! Boom! Boom! Boom!"
		print


main()	