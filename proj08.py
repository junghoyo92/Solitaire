###############################
# CSE231- Section 2             #
# Project 8                     #
#################################

import cards

def setup():
    '''
    paramaters: None
    returns a tuple of:    
    - a foundation (a single list to hold completed runs)
    - a tableau (a list of 10 lists, containing 54 cards (all are hidden except
        top cards)
    - a stock contains the remaining 50 cards. Cards from four total decks are used.
    '''
    foundation = []
    game_deck = cards.Deck()
    for i in range(52):
        game_deck.deal()
    for i in range(4):
        new_deck = cards.Deck()
        for i in range(52):
            c = new_deck.deal()
            if c.get_suit() == 'S':
                game_deck.add_card_top(c)
            elif c.get_suit() == 'H':
                game_deck.add_card_top(c)
            else:
                game_deck.shuffle()
    tableau = []
    for i in range(10):
        new_list = []
        if i<4:
            for i in range(6):
                if i<5:
                    c = game_deck.deal()
                    c.set_hidden()
                    new_list.append(c)
                else:
                    c = game_deck.deal()
                    new_list.append(c)
            tableau.append(new_list)
        elif i>=4:
            for i in range(5):
                if i<4:
                    c = game_deck.deal()
                    c.set_hidden()
                    new_list.append(c)
                else:
                    c = game_deck.deal()
                    new_list.append(c)
            tableau.append(new_list)
    stock = game_deck
    return foundation,tableau,stock
    pass
  
def print_game(foundation,tableau,stock):
    '''
    parameters: a foundation, a tableau and a stock
    returns: Nothing
    prints the game, i.e, print all the info user can see.
    Includes:
        a) print tableau  (Make sure only show those cards which are revealed. For hidden cards, just print "XX".
        b) print foundation (report how many runs have been completed)
        c) print stock  (only need to show how many cards left in stock)
    '''
    row = 0
    for lists in tableau:
        row += 1
        print('\nRow {}:'.format(row), end = ' ')
        for card in lists:
            if card == 'XX':
                print(card)
            else:
                print(card, end = ' ')
        
    print('\n\nRuns completed: {}/8 runs completed'.format(len(foundation)))
    if stock != None:
        print('Cards left in stock: {} cards remaining'.format(stock.cards_left()))
    else:
        print('No More cards left in stock.')
    pass
    
def reveal_card(tableau, tRow):
    '''
    parameters: a tableau row and a tableau
    returns: Nothing
    reveal the top card of the indicated row
    '''
    reveal_list = tableau[tRow]
    card = reveal_list[-1]
    card.show_card()
    pass
    
def check_completion(tableau, foundation, tRow):
    '''
    parameters: a tableau, a foundation
    on, and a tableau row
    returns: Nothing
    checks for a completed run in the given row, adds that completed run to the
    foundation, and prints a message
    '''
    check_list = tableau[tRow]
    run = []
    length = len(check_list)
    while length >= 13:
        length -= 1
        for i in range(13):
            i += 1
            if check_list[-i].get_suit() == check_list[-(i+1)].get_suit()-1:
                if check_list[-i].get_rank() == check_list[-(i+1)].get_rank()-1:
                    run.append(check_list[-i])
            else:
                break
            
    if len(run) == 13:
        foundation.append(run)
        for i in range(13):
            i += 1
            check_list.pop(-i)
          
    pass

def move_in_tableau(tableau,num_of_cards,t_row_source_index,t_row_dest_index):
    '''
    parameters: a tableau, number of cards, the source tableau row and the destination tableau row
    returns: nothing
    moves a certain number of cards from one row to another
    hint: 1. first make sure the cards you are moving are built down by rank and are the same suit
          2. if the dest row is empty, move those cards
             else, make sure the card of tableau[t_row_source_index][-num_of_cards] is one rank lower than the top card of destination row (tableau[t_row_dest_index][-1]),
                     and the suit doesn't matter
             If a single card is moved, if it's rank is one less than the destination card, allow opposing colors
    '''
    tRow = t_row_source_index
    source = tableau[t_row_source_index]
    dest = tableau[t_row_dest_index]
    check_num = num_of_cards
    while check_num > 0:
        if check_num > 1:
            source[-num_of_cards].has_same_color(source[-(num_of_cards-1)])
            check_num -= 1
        elif check_num == 1:
            break

    for i in range(num_of_cards):
        if dest == []:
            if source[-num_of_cards] == 'XX':
                break
            else:
                dest.append(source[-num_of_cards])
                source.pop(-num_of_cards)
        elif dest != [] and source[-num_of_cards].get_rank() == dest[-1].get_rank()-1:
            if source[-num_of_cards] == 'XX':
                break
            else:
                dest.append(source[-num_of_cards])
                source.pop(-num_of_cards)
        else:
            print('Invalid Move')
            break
        num_of_cards-=1
    reveal_card(tableau, tRow)

    pass
        
def deal_more_cards(stock,tableau):
    '''
    parameters: a stock and a tableau
    returns: Boolean
    Deal one card to each tableau row if there are no empty rows in the tableau. Otherwise, print an error message.
    For the last deal operation, deal the remaining cards to the first couple rows of tableau.
    returns False if the stock is empty or if there was an empty row. Otherwise, deal cards, and return True
    '''

    while stock.cards_left() > 0:
        for lists in tableau:
            if lists == []:
                print('Empty Row Error')
                return False
        for i in range(10):
            c = stock.deal()
            tableau[i].append(c)
        return True
        break
    pass

def is_winner(foundation):
    '''
    parameters: a fdation
    return: Boolean
    If all of the cards have been successfully ordered and put in the foundation,
    return True
    '''
    while True:
        if len(foundation) == 8:
            print('Winner! Winner!')
            return True
        else:
            return False
    pass

def print_rules():
    '''
    parameters: none
    returns: nothing
    prints the rules
    '''
    print('''
Rules of Spider Solitaire:
The goal is to move all cards to the foundation. Cards can only be moved
to the foundation if in a completed run of cards (King, Queen, ..., Ace).
A single card in the tableau can be moved to another row if the destination
card is one rank higher than the moving card. Multiple cards can be moved at
once, but all cards within the stack being moved must be in descending order,
and they must all be the same suit. The destination card must also be one
rank higher than the top card of the stack being moved.
        ''')
    pass

def show_help():
    '''
    parameters: none
    returns: nothing
    prints the supported commands
    '''
    print('''Acceptable commands:
            d - Deals more cards until there are no more cards to deal
            q - Quits the game
            h - Prints help information
            m (# of cards) (source row #) (dest row #) - moves
                the number of cards from the source row to the
                destination row, if the move is allowed
            ''')
    pass

def play():
    ''' 
    main program. Does error checking on the user input. 
    '''
    print_rules()
    show_help()
    foundation, tableau, stock = setup()
    print_game(foundation, tableau, stock)
    while True:
        command = input('What is your move? ')
        command = command.split()
        if command[0] == 'd':
            deal_more_cards(stock,tableau)
            print_game(foundation, tableau, stock)
            continue
        elif command[0] == 'q':
            break
        elif command[0] == 'h':
            show_help()
            print_game(foundation, tableau, stock)
            continue
        elif command[0] == 'm':
            num_of_cards = int(command[1])
            t_row_source_index = int(command[2])-1
            t_row_dest_index = int(command[3])-1           
            move_in_tableau(tableau,num_of_cards,t_row_source_index,t_row_dest_index)
            tRow = t_row_source_index
            check_completion(tableau, foundation, tRow)
            is_winner(foundation)
            print_game(foundation, tableau, stock)
    pass

play()
