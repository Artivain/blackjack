import random, time
print("Bienvenue dans Blackjack!")
time.sleep(1)

cartes = [1,2,3,4,5,6,7,8,9,10,10,10]
def piger():
	return random.choice(cartes)

def quit():
	print("Au revoir!")
	time.sleep(1)
	raise SystemExit

def menu():
	print("=== Menu ===\n1 - Jouer\n2 - Quitter")
	i = input("Option: ")
	if i == "1":
		jouer()
	elif i == "2":
		quit()
	else:
		print("Option non-valide.")
		time.sleep(1)
		return menu()

def jouer():
	print("=== Début de la partie ===")
	a = piger()
	b = piger()
	player = a + b
	print("Vos cartes sont", a, "et", b, "pour un total de", player)
	time.sleep(0.5)
	bank = piger()
	print("La banque a", bank)
	time.sleep(0.5)

	def intent():
		print("1 - Piger\n2 - Passer")
		i = input("Option: ")
		if i != "1" and i != "2":
			print("Option invalide.")
			time.sleep(1)
			return intent()
		return i

	while intent() == "1":
		a = piger()
		player += a
		print("Vous avez pigé", a, "et votre total est de", player)
		if player > 21:
			print("Vous avez dépassé 21, vous avez perdu. #rekt")
			time.sleep(1)
			return menu()
	
	print("Au tour de la banque")
	time.sleep(1)

	while bank < 16:
		a = piger()
		bank += a
		print("La banque vient de piger", a, "pour un total de", bank)
		time.sleep(0.5)
		if bank > 21:
			print("La banque a dépassée 21, vous avez donc gagné! GG!")
			time.sleep(1)
			return menu()
	
	print("=== Fin de la partie ===\nBanque:", bank, "\nVous:", player)
	if bank > player:
		print("Vous avez perdu.")
	elif bank < player:
		print("Vous avez gagné!")
	else:
		print("Wow, égalité!")
	time.sleep(1)
	return menu()
		
menu()