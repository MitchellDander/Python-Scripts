"""this program will be a mad libs story.  it will allow the user to input words and enter them into the story."""
print "Welcome to MadLibs!"
name = raw_input("Enter a character\'s name:")
adjective_A = raw_input("Enter an adjective:")
adjective_B = raw_input("Enter another adjective:")
adjective_C = raw_input("Enter a final adjective:")
verb_A = raw_input("Enter a verb:")
verb_B = raw_input("Enter another verb:")
verb_C = raw_input("Enter a final verb:")
noun_A = raw_input("Enter a noun:")
noun_B = raw_input("Enter another noun:")
noun_C = raw_input("Enter a third noun:")
noun_D = raw_input("Enter a final noun:")
animal = raw_input("Enter an animal:")
food = raw_input("Enter a type of food:")
fruit = raw_input("Enter a typr of fruit:")
number = raw_input("Enter a number:")
superhero_name = raw_input("Enter a superhero\'s name:")
country = raw_input("Enter a Country\'s name:")
dessert = raw_input("Enter a dessert:")
year = raw_input("Enter any year:")
#The template for the story
STORY = "This morning I woke up and felt %s because %s was going to finally %s over the big %s %s. On the other side of the %s were many %ss protesting to keep %ss in stores. The crowd began to %s to the rythym of the %s, which made all of the %ss very %s. %s tried to %s into the sewers and found %s rats. Needing help, %s quickly called %s. %s appeared and saved %s by flying to %s and dropping %s into a puddle of %s. %s then fell asleep and woke up in the year %s, in a world where %ss ruled the world."
print STORY % (adjective_A, name, verb_A, adjective_B, noun_A, noun_B, animal, food, verb_B, noun_C, fruit, adjective_C, name, verb_C, number, name, superhero_name, superhero_name, name, country, name, dessert, name, year, noun_D)