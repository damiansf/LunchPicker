import json
import random

fileName = "options.json"

print("Welcome to the lunch picker!\n\nDeterming where you will eat today...\n")

with open(fileName, 'r') as myfile:

	options = json.load(myfile)
	choice = random.randint(1,9)

	print("Today you will eat at: " + options[str(choice)] + ", Enjoy Your Lunch!")