import random #import the library called 'random'

def read_file_to_list(filename): #reading the contents of a file into a 2D list
    my_file = open(filename, "r")
    username_password_list = list(my_file)
    for i in range(len(username_password_list)):#iterating through each record and storing each one in the 2D list
        record = username_password_list[i].split(",")
        record[1] = (record[1])[:-1]
        username_password_list[i] = record
    my_file.close()
    return username_password_list

def check_username(done, username_password_list): #checks whether the inputted username is valid
    tries = 3
    user = -1
    check = 0
    while tries > 0:#repeating only when you have used less than 3 tries
        username = input("Please enter your username: ")
        if username in done: #checks if username has been used already
            tries = tries - 1
            print("This username has been used already. You have " + str(tries) + " tries left.")
            continue
        for a in range(len(username_password_list)):#iterating through 2D list to see if inputted username is valid
            if username_password_list[a][0] == username: 
                done = username
                check = 1
                user = a
        if check == 0: #if not found...
            tries = tries - 1
            print("Unknown username, you have " + str(tries) + " tries left.")
        else: #if found...
            print("Correct username!")
            break
    return [check, user, done]

def check_password(user, username_password_list):#checking if the inputted password matches the password registered to the inputted username
    tries = 3
    check = 0
    while tries > 0:#repeating only when you have used less than 3 tries
        password = input("Please enter your password: ")
        if password == username_password_list[user][1]: #if password matches...
            print("Correct password! Welcome " + username_password_list[user][0] + "!")
            print(" ")
            check = 1
            break
        else: #if it doesn't...
            tries = tries - 1
            print("Wrong password, you have " + str(tries) + " tries left.")
    return check

def authentication(): #checking inputted username and password using previous three functions
    username_password_list = read_file_to_list("Authorised_Players.csv")
    done = []
    for i in range(1, 3): #only repeats twice; one for each player
        print("Player " + str(i) + ": ")
        data = check_username(done, username_password_list)
        check = data[0]
        user = data[1]
        done.append(data[2])
        if check == 0: #if you have exceeded your three tries for the username...
            print("You have run out of tries!")
            break
        check = check_password(user, username_password_list)
        if check == 0: #if you have exceeded your three tries for the password...
            print("You have run out of tries!")
            break
    return [check, done]

def tabulate(data): #takes in a list and outputs a formatted row of a table
    string = "|"
    for rec in data: #iterates through inputted list
        string = string + '{:^10}'.format(rec) + "|"
    print(string)

def print_cards(card1, card2): #outputs the details of the drawn card and shows who drew it
    print("-" * 34)
    tabulate(["Player", "Colour", "Number"])
    tabulate(["1"] + card1)
    tabulate(["2"] + card2)
    print("-" * 34)

def store_cards(player, card1, card2): #stores the card details in the correct player's list
    if player == 1: # if player 1...
        player1.append(card1)
        player1.append(card2)
    else: # if player 2...
        player2.append(card1)
        player2.append(card2)
    
def game(): #here is the code where the cards are drawn, the winner of each round is found, and the overall winner is returned
    deck = [["yellow", 1], #the card deck
            ["yellow", 2],
            ["yellow", 3],
            ["yellow", 4],
            ["yellow", 5],
            ["yellow", 6],
            ["yellow", 7],
            ["yellow", 8],
            ["yellow", 9],
            ["yellow", 10],
            ["black", 1],
            ["black", 2],
            ["black", 3],
            ["black", 4],
            ["black", 5],
            ["black", 6],
            ["black", 7],
            ["black", 8],
            ["black", 9],
            ["black", 10],
            ["red", 1],
            ["red", 2],
            ["red", 3],
            ["red", 4],
            ["red", 5],
            ["red", 6],
            ["red", 7],
            ["red", 8],
            ["red", 9],
            ["red", 10]]

    random.shuffle(deck) #the deck is shuffled
    print("--------------------------------------------------------------------------------")
    for i in range(15): #there are 15 rounds...
        input("Press enter to continue...") #to force the program to stop until an input is given
        card1 = deck[0]# draw top two cards
        card2 = deck[1]
        deck.pop(0) #take top two cards out of deck
        deck.pop(0)
        print("New cards have been drawn...")
        print_cards(card1, card2)
        print("  ")
        print("Checking colours...")
        #decides who won this round...
        if card1[0] == card2[0]: #if same colour...
            print("Your colours are the same, checking numbers...")
            if card1[1] > card2[1]: #if player 1 has the higher number...
                print("Player 1 has the higher number.")
                print("Player 1 wins this round!")
                store_cards(1, card1, card2)
            else: #if player 2 has the higher number...
                print("Player 2 has the higher number.")
                print("Player 2 wins this round!")
                store_cards(2, card1, card2)
        else: #if different colours...
            #look through every possible combination of colours...
            if card1[0] == "red" and card2[0] == "black":
                print("Player 1 has the winning colour.")
                print("Player 1 wins this round!")
                store_cards(1, card1, card2)
            elif card1[0] == "black" and card2[0] == "red":
                print("Player 2 has the winning colour.")
                print("Player 2 wins this round!")
                store_cards(2, card1, card2)
            elif card1[0] == "yellow" and card2[0] == "red":
                print("Player 1 has the winning colour.")
                print("Player 1 wins this round!")
                store_cards(1, card1, card2)
            elif card1[0] == "red" and card2[0] == "yellow":
                print("Player 2 has the winning colour.")
                print("Player 2 wins this round!")
                store_cards(2, card1, card2)
            elif card1[0] == "black" and card2[0] == "yellow":
                print("Player 1 has the winning colour.")
                print("Player 1 wins this round!")
                store_cards(1, card1, card2)
            else:
                print("Player 2 has the winning colour.")
                print("Player 2 wins this round!")
                store_cards(2, card1, card2)
        print("  ")
        print("Player 1 has " + str(len(player1)) + " cards.")
        print("Player 2 has " + str(len(player2)) + " cards.")
        print("--------------------------------------------------------------------------------") #effectively break up rounds
    if len(player1) > len(player2): #if player 1 won more rounds...
        return 1
    else: #if player 2 won more rounds...
        return 2

def list_cards(cards): #lists the cards of the winning player in a formatted table
    print("  ")
    print("-" * 34)
    tabulate(["Cards", "Colour", "Number"])
    for i in range(len(cards)): #iterates through the cards, one at a time
        data = ["Card " + str(i + 1), (cards[i][0]).capitalize(), str(cards[i][1])]
        #prints card data as a formatted row in a table
        tabulate(data)
    print("-" * 34)
    print("  ")

def store_details(player, cards): #stores the details of the winning player in an external csv file
    my_file = open("Winning_Players.csv", "a")
    my_file.write(player + "," + str(cards) + "\n")
    my_file.close()

def display_top_5(): #output the details of the top five players
    winning_players = read_file_to_list("Winning_Players.csv")
    winning_players = sorted(winning_players, key = lambda x:int(x[1]), reverse = True) #sorts winning players data by number of cards
    # outputs top 5 in a formatted table
    print("-" * 34)
    tabulate(["Rank", "Username", "Score"])
    for i in range(1, 6): #iterates through the top five players, from fifth to first
        data = [str(i), winning_players[i - 1][0], str(winning_players[i-1][1])]
        tabulate(data)
    print("-" * 34)
    print("Goodbye, thanks for playing!")
    return winning_players

def write_to_winning(winning_players): #save the number of cards and username of the winning players in order
    my_file = open("Winning_Players.csv", "w")
    for i in winning_players: #iterates through the sorted list of past winning players and saves them in the file
        data = i[0] + "," + i[1] + "\n"
        my_file.write(data)
    my_file.close()


check, players = authentication() #calling the function authentication() and storing the result and the players' names
if check == 1: #if username and password data valid...
    #the lists where each players' cards will be stored
    global player1, player2 #so that the variables can be accessed from the functions above
    player1 = []
    player2 = []
    number = game() #calling the function game() and storing the winning player's number
    if number == 1: #if player 1 is the winner...
        print("  ")
        print("Player 1 wins!")
        list_cards(player1)
        print("Storing data on winning player in file...")
        store_details(players[0], len(player1))
    else: #if player 2 is the winner...
        print("  ")
        print("Player 2 wins!")
        list_cards(player2)
        print("Storing data on winning player in file...")
        store_details(players[1], len(player2))
    print("  ")
    print("Finding top 5...")
    winning_players = display_top_5()
    write_to_winning(winning_players)
else: #if invalid...
    print("Bye!")


