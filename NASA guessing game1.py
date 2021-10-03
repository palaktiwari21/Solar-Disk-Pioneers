def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print('''                                                                ******************Correct Answer****************''')
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input('''                                                               Sorry Wrong Answer, bonus chance''')
            attempt = attempt + 1
    if attempt == 3:
        print('''                                                               Again Wrong, The Correct answer is ''',answer )
    
score = 0
print("----------------------------------------------------------------WELCOME----------------------------------------------------------------------")
print("-------------------------------------------------------------GUESS THE ANSWER-------------------------------------------------------------")

print('''
                                                                            1- EASY PEASY
                                                                            2. MODERATE
                                                                            3. ICE CHILLING''')
x=int(input('''                                                               Enter the choice :'''))
#easy
if (x==1):
    guess1 = input('''                                                                How many planets revolve around the sun                                                               ''')
    check_guess(guess1, '''8''')
    guess2 = input('''                                                               Sun is a part of how many constellations ''')
    check_guess(guess2, '''0''')
    guess3 = input('''                                                               Which gas does the sun consist of mostly   ''')
    check_guess(guess3, '''Hydrogen''')
    guess4 = input('''                                                               What is the name of 1st ever series of spacecrafts made by nasa specifically to orbit the sun''')
    check_guess(guess4, '''Pioneer''')
    guess5 = input('''                                                               The black spots on suns surface are called  ''')
    check_guess(guess5, '''Sunspots''')
    print('''                                                                                 Your Score is '''+ str(score))
    
    
    
#mod    
elif (x==2):
    guess1 = input('''                                                               Whats the surface of sun called ''')
    check_guess(guess1, '''Photosphere''')
    guess2 = input('''                                                               Whats the name of the spacecraft planned by isro to launch in 2022 to orbit the sun ''')
    check_guess(guess2, '''Adityal1''')
    guess3 = input('''                                                                In which year was the nasa's solar parker probe launched ''')
    check_guess(guess3, '''2018''')
    guess4 = input('''                                                                What is the name of the planet named after greek goddess of love''')
    check_guess(guess4, '''Venus ''')
    guess5 = input('''                                                                Which is the brightest star in the nightsky ''')
    check_guess(guess5, '''Sirius''')
    print('''                                                                                 Your Score is '''+ str(score))
    
    
    
    
    
    
    
 #tough   
elif (x==3):
    guess1 = input('''                                                               Where is the headquarter of nasa ''')
    check_guess(guess1, '''Washington''')
    guess2 = input('''                                                               When did first Indian went to space''')
    check_guess(guess2, '''1984''')
    guess3 = input('''                                                               When did Neil Armstrong landed on moon? ''')
    check_guess(guess3, '''1969''')
    guess4 = input('''                                                               In 2017, ISRO launched how many satellites in one go?(WORLD RECORD)''')
    check_guess(guess4, '''104''')
    guess5 = input('''                                                               Halley's comet appears after every''')
    check_guess(guess5, '''75''')
    print('''                                                                                 Your Score is '''+ str(score))

    
    
# guess1 = input("Which bear lives at the North Pole? ")
# check_guess(guess1, "polar bear")
# guess2 = input("Which is the fastest land animal? ")
# check_guess(guess2, "Cheetah")
# guess3 = input("Which is the larget animal? ")
# check_guess(guess3, "Blue Whale")
# print("Your Score is "+ str(score))