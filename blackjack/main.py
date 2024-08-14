from tkinter import *
import random
from PIL import Image, ImageTk

# Code for displaying cards from 
# https://github.com/flatplanet/Intro-To-TKinter-Youtube-Course


root = Tk()
root.title('Card Deck')
root.iconbitmap('assets/cards.ico')
root.geometry("900x500")
root.configure(background="green")

# Resize Cards
def resize_cards(card):
	# Open the image
	our_card_img = Image.open(card)

	# Resize The Image
	our_card_resize_image = our_card_img.resize((150, 218))
	
	# output the card
	global our_card_image
	our_card_image = ImageTk.PhotoImage(our_card_resize_image)

	# Return that card
	return our_card_image

# Shuffle The Cards
def shuffle():
	# Define Our Deck
	suits = ["diamonds", "clubs", "hearts", "spades"]
	values = range(2, 15)
	# 11 = Jack, 12=Queen, 13=King, 14 = Ace

	global deck
	deck =[]

	for suit in suits:
		for value in values:
			deck.append(f'{value}_of_{suit}')

	# Create our players
	global dealer, player
	dealer = []
	player = []

	# Grab a random Card For Dealer
	card = random.choice(deck)
	# Remove Card From Deck
	deck.remove(card)
	# Append Card To Dealer List
	dealer.append(card)
	# Output Card To Screen
	global dealer_image
	dealer_image = resize_cards(f'assets/cards/{card}.png')
	dealer_label.config(image=dealer_image)

	# Grab a random Card For Player
	card = random.choice(deck)
	# Remove Card From Deck
	deck.remove(card)
	# Append Card To Dealer List
	player.append(card)
	# Output Card To Screen
	global player_image
	player_image = resize_cards(f'assets/cards/{card}.png')
	player_label.config(image=player_image)

	#player_label.config(text=card)

	# Put number of remaining cards in title bar
	root.title(f'{len(deck)} Cards Left')


# Deal Out Cards
def deal_cards():
	try:
		# Get the dealer Card
		card = random.choice(deck)
		# Remove Card From Deck
		deck.remove(card)
		# Append Card To Dealer List
		dealer.append(card)
		# Output Card To Screen
		global dealer_image
		dealer_image = resize_cards(f'assets/cards/{card}.png')
		dealer_label.config(image=dealer_image)
		#dealer_label.config(text=card)

		# Get the player Card
		card = random.choice(deck)
		# Remove Card From Deck
		deck.remove(card)
		# Append Card To Dealer List
		player.append(card)
		# Output Card To Screen
		global player_image
		player_image = resize_cards(f'assets/cards/{card}.png')
		player_label.config(image=player_image)
		#player_label.config(text=card)


		# Put number of remaining cards in title bar
		root.title(f'{len(deck)} Cards Left')

	except:
		root.title(f'No Cards In Deck')

def setup():
	# Set up ad display the GUI
	my_frame = Frame(root, bg="green")
	my_frame.pack(pady=20)

	# Create Frames For Cards
	dealer_frame = LabelFrame(my_frame, text="Dealer", bd=0)
	dealer_frame.grid(row=0, column=0, padx=20, ipadx=20)

	player_frame = LabelFrame(my_frame, text="Player", bd=0)
	player_frame.grid(row=0, column=1, ipadx=20)

	# Put cards in frames
	global dealer_label 
	dealer_label = Label(dealer_frame, text='')
	dealer_label.pack(pady=20)

	global player_label
	player_label = Label(player_frame, text='')
	player_label.pack(pady=20)


	# Create a couple of buttons
	shuffle_button = Button(root, text="Shuffle Deck", font=("Helvetica", 14), command=shuffle)
	shuffle_button.pack(pady=20)

	card_button = Button(root, text="Get Cards", font=("Helvetica", 14), command=deal_cards)
	card_button.pack(pady=20)

	# Shuffle Deck On Start
	shuffle()

	root.mainloop()

if __name__ == "__main__":
    setup()