# Start typing your program below this line...
# This program says hello and asks for my name
print('Sanibonani!')
print("Welcome to Saru's Sizzling Safari Guide, where we offer you the best safari deals this side of South Africa.")
print("What's your name?")
myName = input()
print('It is good to meet you, ' + myName)

# This program asks for a booking date and time slot.
print('What day would you like to make your booking?')
myDate = input()
print("Khukhule! That's great!")
print('And which time slot would you like? 6am or 1pm?')
myTime = input()
print('Fantastic! Our African-animal affair is all set for ' + myDate + ' at ' + myTime +'.' )

# This program offers the user T-shirt sizes.
print('We offer a complimentary t-shirt for every online booking. Are you a SMALL, MEDIUM or LARGE?')
mySize = input()
print('Ahhhh, the joys of a perfectly sized, '+ mySize +' T-shirt.')

# This program offers a sunhat purchase with the option to say yes or no.
print('Worried that the heat will be too much? Why not "PAWS" for a minute and buy the Sizzling Safari Sunhat, on sale for only R50! Would you like to make this purchase, Yes or No?')
myHat = input()

Yes = 1
yes = 1
No = 0
no = 0
if Yes == 1:
 print('Noted!')

# This program closes off the conversation.
print('Yebo! Everything is set for our "ROARING" adventure on ' + myDate)
print('Sizobonana! See you there!')