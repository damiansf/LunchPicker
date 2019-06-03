import json
import random

def addOption(options, numOptions, fileName):
	newOption = str(input("Enter name of new Lunch option:\n"))
	options.append(newOption)
	save(options, fileName)
	numOptions += 1
	print("\nNew Option Added\n")
	listOptions(options)
def removeOption(options, numOptions, fileName):
	if numOptions == 0:
		print("No options provided, please add some lunch options")
	else:
		listOptions(options)
		indexRM = int(input("\nEnter a number that coresponds to a option you want removed:\n"))
		if indexRM >= 1 and indexRM <= numOptions:
			options.remove(options[indexRM-1])
			numOptions -= 1
			save(options, fileName)
			print("\nOption removed\n")
		else:
			print("INVALID INPUT, NUMBER DOES NOT CORRESPOND TO OPTION")

def save(options, fileName):
	data = {}
	data["Options"] = options
	with open(fileName, 'w') as saveFile:
		json.dump(data, saveFile)

def pickOption(options, numOptions):
	if numOptions == 0:
		print("No options provided, please add some lunch options")
	else:
		print("\nGenerating your lunch destination...\n")
		choice = (random.randint(1,numOptions)) - 1
		print("Today you will eat at: " + options[choice] + ", Enjoy Your Lunch!")
		quit()

def listOptions(options):
	print("\nCurrent Options:\n")
	for count, option in enumerate(options, start=1):
		print(str(count) + ":" + option)
def quit():
	exit()

fileName = "options.json"

print("Welcome to the lunch picker!\n\n")

with open(fileName, 'r') as myFile:

	options = (json.load(myFile))["Options"]
	numOptions = len(options)

	userInput = ""

	while userInput != 'q':
		userInput = str(input(("\nEnter A to add a new lunch option, R to remove a lunch option, L to list all lunch options, P to pick your lunch spot and Q if you would like to quit:\n\n"))).lower()

		if userInput == 'q':
			quit()

		elif userInput == 'a':
			addOption(options, numOptions, fileName)

		elif userInput == 'r':
			removeOption(options, numOptions, fileName)

		elif userInput == 'l':
			listOptions(options)

		elif userInput == 'p':
			pickOption(options, numOptions)

		else:
			print("INVALID INPUT, TRY AGAIN\n")