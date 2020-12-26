
# Legend of Miri decision making game
from random import randint


def game():
	print(
		"++++++++++++++++++++++++\n"
		"+| The Legend of Miri |+")
	print("++++++++++++++++++++++++")
	name()
	scene_1()
	print("++++++++++++++++++++++++\n"
		  "Thank you for playing 'The Legend of Miri'\n"
		  "++++++++++++++++++++++++")


def name():
	name = input('What is your name? \n'
	'>>> ')
	print('Welcome ' + name + ', have fun!')
	if name == 'xime':
		admin()
	elif name in friends:
		print('Oh! I know you!')
		if name == 'dom':
			print('You better not be greedy again Dom')
		elif name == 'mirenda':
			print('I love you! Hope you enjoy the game I made for you!')
		elif name == 'luiz':
			print('A warrior of light! Have fun!')
		elif name == 'theo':
			print('Thank you for play testing as one if the first!')
		elif name == 'sameer':
			print('Please excuse the linguistic booboos...')
		elif name == 'monkey2':
			print('Und der Affe ist auch da...')


def scene_1():
	print("++++++++++++++++++++++++")
	print('Once upon a time, there was a dark, cloudy night. \n' 
		  'Flashes of lightning brighten the scene, as a large ship \n' 
		  'fights it way through waves as tall as trees.')
	print('Suddenly there is a loud sound that cuts through the crashing \n'
		  'waves as the ships mast gets struck by lightning. \n'
		  'Instantly ablaze, it plummets towards the deck. ')
	choice = input('You only have a split second to react. \n'
				   'In which direction do you want to dodge? (left/right) \n'
				   '>>> ')
	choices.append(choice)
	if choice == 'left':
		choice_left()
	elif choice == 'right':
		choice_right()
	else:
		choice_death()
	scene_2()


def choice_left():
	print('Taking a small but precise step to the left, you manage to \n'
		'position yourself in a way that none of the falling pieces of wood hit you. ')


def choice_right():
	print('Leaping towards the right, you get out of the area below the mast.')


def choice_death():
		print('Trying to outsmart god, you make an unexpected move. \n'
		'Sadly it does not work out well and you end up slipping  \n'
		'and falling over board. Noone will ever find your body.')
		death()


def death():
	inventory.clear()
	choices.clear()
	correct_window = randint(1, 23)
	# name.clear()
	print("\n\n"
		  "     X   X\n"
		  "      --- \n"
		  "    You died.\n\n\n")
	scene_1()


def win():
	inventory.clear()
	choices.clear()
	correct_window = randint(1, 23)
	# name.clear()
	print('++++++++++++++++++++++\n\n'
	'You actually did it!!!!\n\n'
	'       YOU WIN!\n'
	'++++++++++++++++++++++')
	print("Thank you for playing the early version of 'The Legend of Miri'. \n"
	"I hope you had a good time time\n"
	"++++++++++++++++++++++\n\n\n")
	scene_1()


def scene_2():
	print('After barely avoiding death, you look around \n'
		  'to see if anyone else got less lucky. On the other side of the ship \n'
		  'you see one of your best friends laying under a piece of wood. \n'
		  'Looking some more you also see the captains dog, surrounded by flames in a corner.')
	choice = input('Who will you try to save? (friend/dog) \n'
	'>>> ')
	choices.append(choice)
	if choice == 'friend':
		choice_friend()
	elif choice == 'dog':
		choice_dog()
	else:
		choice_death()


def choice_friend():
	print('You help your friend. dragging them out from under the logs. \n'
		  'Once they are free, you look around again, but the dog is nowhere to be seen.\n'
		  'A person you do see is the captain, looking at you angrily.\n'
		  'It looks like you would need to give him something valuable to calm him down.')
	scene_3()


def choice_dog():
	print('You run over to the dog and leap over the burning pieces of the mast.\n'
		  ' He looks at you with fear in his eyes and jumps into your arms. \n'
		  'As you carry him to safety, you see your friend get buried by more falling parts. \n'
		  'The dog is injured and you need to find something to tend to his wounds. Maybe bandages?')
	scene_3()


def scene_3():
	print('Heading below deck, you find yourself in a dark and damp place.\n'
	'The ship is shaking and you have trouble making out where to go.\n')
	choice = input('Where do you want to go? (combuse/storage/sleeping area/above deck/magazine)\n'
	'>>> ')
	if choice == 'combuse':
		print('You follow your nose towards the kitchen.')
		combuse()
	elif choice == 'storage':
		print('What you are looking for must be where pretty much everything is, right? To the storage it is.')
		storage()
	elif choice == 'sleeping area':
		print('For some reason you get the feeling that it should be where everyone sleeps.')
		sleeping_area()
	elif choice == 'above deck' or choice == 'up':
		above_deck()
	elif choice == 'hidden door':
		print('While standing in the hallway you hear a faint noise below you. \n'
			  'Upon further inspection you find a trapdoor leading to a hidden compartment.')
		hidden_door()
	elif choice == "magazine" or choice == "powder":
		magazine()
	else:
		choice_death()


def combuse():
	print('This is a kitchen with a little window. It smells of different kinds of meats and herbs in here.\n '
		  'The chef seems to not be around.')
	choice = input('What are you looking for? \n'
	'>>> ')
	if choice == 'meat':
		print('You find some pieces of cooked meat. Smells delicious!')
		store('meat')
	elif choice == 'herb' or choice == 'herbs':
		print('There are many herbs here for the taking.')
		store('herbs')
	elif choice == 'water':
		print('There is a large barrel of water. You also find a bucket to fill.')
		store('water')
	elif choice == "window":
		print("You look out of the window. It is still storming outside...")
		window = input("Do you want to lean outside? \n>>> ")
		if window == "yes":
			print("For whatever reason you lean out. You fall out obviously. \n"
				  "Today seems your lucky day though, since you manage to hold onto something.")
			ship_outside()
		else:
			print("Yeah, that would have been dumb.")
	else:
		not_here()
	back = input("Do you want to head back? (yes/no)\n"
	'>>> ')
	if back == 'yes':
		scene_3()
	elif back == 'no':
		combuse()
	else:
		choice_death()


def storage():
	print('This is the storage. There are many crates and barrels here, full of loot and supplies.')
	choice = input('What are you looking for? \n'
	'>>> ')
	if choice == 'money' or choice =='gold':
		print('You find a large crate filled with gold from your last mission.')
		if inventory.count('money') > 3:
			print('While trying to grab another bag of gold, you suddenly hear someone loudly clearing their throat behind you.\n'
			'As you turn around, the captains cutlass is faster than you expect.')
			death()
		elif 'money' in inventory:
			print("Looks like we're feeling greedy today... hope that goes well.")
		store("money")
		print(inventory)
	elif choice == 'bandages' or choice == 'bandage':
		print('Looks like there used to be bandages here, but they are all gone.')
	else:
		not_here()
	back = input("Do you want to head back? (yes/no)\n"
	'>>> ')
	if back == 'yes':
		scene_3()
	elif back == 'no':
		storage()
	else:
		choice_death()
	
	
def sleeping_area():
	print('this is the sleeping area. There are hammocks.')
	choice = input('What are you looking for? \n'
	'>>> ')
	if choice == 'money' or choice == 'gold':
		print('Someone had to have money here right? You start searching through the things that belong to the crew.\n'
		'After a minute of searching you hear a voice behind you. "Whats all this then?"\n'
		'You got caught and will be sent to walk the plank.')
		death()
	elif choice == 'hammock' or choice == 'bedroll' or choice == 'bedding':
		print('You quickly find bedding.')
		store("bedding")
	elif choice == 'teddy bear' or choice == 'bear' or choice == 'teddy':
		print('You find someones teddy bear in a corner, he looks at you with his one/n remaining eye and you know he wants to be returned to his owner.')
		store('teddy bear')
	elif choice == 'bandage' or choice == 'bandages':
		print('You rip up some bedding and create some makeshift bandages')
		store('bandages')
	else: 
		not_here()
	back = input("Do you want to head back? (yes/no)\n"
	'>>> ')
	if back == 'yes':
		scene_3()
	elif back == 'no':
		sleeping_area()
	else:
		choice_death()


def hidden_door():
	print('Inside the small space is a little girl, now looking at you with large, fearful eyes.')
	if 'teddy bear' in inventory:
		print('Her eyes widen and she smiles wide.')
		win()
	choice = input('Do you want to try and get closer? '
	'>>> ')
	if choice == 'yes':
		print('As you make a move to get closer, she suddenly jumps at you. You only see the blade that ends your life after it already did so.')
		death()
	elif choice == 'no':
		print('Staying at a distance, you get a closer look. She seems very young and surely doesnt belong here.'
		'You notice that she is holding a button that you think could have once been the eye of a teddy bear.')
		leave = input("Do you want to leave again? (yes/no)\n>>> ")
		if leave == "yes":#
			print("You turn around, knowing what to do.")
			scene_3()
		else:
			print("After a moment of awkward silence, she tells you that her name is Miriam and\n"
				  "that she will one day be the greatest pirate of all. After that she asks you to find her \n"
				  "teddy bear. She thinks she lost it somewhere in the area with all the hammocks.")
			scene_3()
	else:
		choice_death()


def magazine():
	print("This is the magazine, where the weapons and the gunpowder are stored.\n"
		  "As you walk in, a shape moves quickly away from you. After your eyes get used to the dark, \n"
		  "you see a little monkey running around, carrying many different, probably highly explosive items.")
	choice = input("Do you want to approach the monkey? (yes/no) \n>>> ")
	if choice == "yes":
		print("You walk closer. As you approach, you notice that he seems to \n"
			  "constantly be saying numbers and speaking in the third person. Weird.")
		monkey = input("Say something to the monkey? \n>>> ")
		if monkey == "calculate" or monkey == "compute":
			math_monkey()
		elif monkey == "stowaway":
			print("He mumbles something about a hidden door to himself.")
		else:
			print("He doesnt seems to understand.")
			magazine()
	elif choice == "no":
		print("You keep your distance and walk away again.")
		scene_3()
	else:
		print("Messing around with something you just picked up, you manage to light the powder")
		death()


def math_monkey():
	print("His eyes instantly fixate on you.")
	num1 = float(input("He seems to be waiting for a number... \n>>> "))
	op = input("Now he seems to require a method of operation... \n>>> ")
	num2 = float(input("Looks like he understood... now he needs another number...\n>>> "))
	if op == "+" or op == "plus":
		ans = (num1+num2)
	elif op == "-" or op == "minus":
		ans = (num1-num2)
	elif op == "*" or op == "times" or op == "multiply":
		ans = (num1*num2)
	elif op == "/" or op == "divide":
		ans = (num1/num2)
	else:
		print("He looks at you very confused.")
		x = input("Do you want to try again? (yes/no) \n>>> ")
		if x == "yes":
			math_monkey()
	print("He yells '" + str(ans) + "! Thats what monkey calculated!'")
	more = input("Do you want to ask him something else? (yes/no) \n>>> ")
	if more == "yes":
		math_monkey()
	else:
		magazine()


def above_deck():
	print('You go back up above deck. The wind and the smell of salty water are more intense here.')
	if 'dog' in choices:
		print('You saved the dog from the flames but he is still injured.')
		if 'bandages' in inventory:
			print('You use the bandages to tend to his wounds.')
			print("After feeling better, the dog leads you below deck again and sniffs on the floor.\n"
				  "Could there be a hidden door?")
		else:
			print('You watch this poor dog find a slow and sad death.')
			print('Like a normal person, this gives you a heart attack.')
			death()
	elif 'friend' in choices:
		print('You saved your friend but the captains dog is no more... he ANGERY and storms at you.')
		if 'money' in inventory:
			print("You show him the bag of gold and he instantly seems to calm down.\n"
			"He says: 'Thanks for the gold! I never liked that dog anyway...\n"
			"Oh also, could you do me a favor matey? I think there is a stowaway on this ship. Find her!'")
			scene_3()
		else:
			print('Before you can react, he draws his pistol and shoots you in the chest.')
			death()


def ship_outside():
	hint = correct_window*23+2
	print("You are on the outside of the ship.\n"
		"There are 23 windows on the side of the ship.\n"
		"You feel like you could only try to get into three windows before falling.")
	print("There must be a way to calculate this number... since there are " + str(hint) + " passengers on the ship, \n"
		"two of those being a monkey and a dog, you would need to divide the number of people by 23 to find a open\n"
		"window. If only there was someone who could help. (subject to change)")
	attempts = 0
	while attempts <= 3:
		in_window = input("What window do you want to climb into? (enter a number/back)\n>>> ")
		# print(correct)
		attempts += 1
		if in_window == str(correct_window):
			print("You try window number " + str(correct_window) + " and it opens!")
			hidden_door()
		elif in_window == "back":
			print("You climb back in.")
			combuse()
		else:
			print("You try window number " + str(in_window) + ".\n"
				"It doesnt seems to open.")
		if attempts == 3:
			print("You slip and fall.")
			death()


def not_here():
	print("You don't find that here.")


def store(item):
	inventory.append(item)
	print('You now have: ' + str(inventory))


def admin():
	print('Welcome to adminland! (Nothing really happens)')
	add = input("Do you want to add something to the inventory? ")
	if add != "no":
		store(add)
	skip = input("Do you want to skip to a part? ")
	if skip == "storage":
		storage()
	elif skip == "up":
		above_deck()
	elif skip == "hidden":
		hidden_door()
	elif skip == "kitchen":
		combuse()
	elif skip == "sleep":
		sleeping_area()
	elif skip == "magazine":
		magazine()

	
while True:
	playing = input("Do you want to play the game? (yes/no)\n"
	'>>> ')
	while playing == "yes":
		inventory = []
		choices = []
		friends = ['mirenda', 'dom', 'theo', 'jarvin', 'luiz', 'john', 'paddy', 'jonas', 'sameer', 'monkey2']
		correct_window = randint(1, 23)
		game()

	print("Goodbye!")
