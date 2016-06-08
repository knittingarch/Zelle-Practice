# Program that prints the lyrics of the song "Old MacDonald" using functions to include 5 different animals.
# by Sarah Dawson


yodel = "Ee-igh, Ee-igh, Oh!"
farm_animals = [["cow", "moo"], ["pig", "oink"], ["duck", "quack"], ["horse", "neigh"], ["lamb", "baa"]]

def HadAFarm():
	setup = "Old MacDonald had a farm, "
	print setup + yodel

def PickAnimal(animal, sound):
	two_sounds = sound + ", " + sound
	print "And on that farm he had a " + animal + ", " + yodel
	print "With a " + two_sounds + " here and a " + two_sounds + " there."
	print "Here a " + sound + ", there a " + sound + ", everywhere a " + two_sounds + "."

def main():
	for i in range(len(farm_animals)):
		HadAFarm()
		PickAnimal(farm_animals[i][0], farm_animals[i][1])
		HadAFarm()
		print

main()