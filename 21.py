import random


kind_brand=["Diamonds","Hearts","Spades","Clubs"]
all_point_brand={"Ace":11,"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,
                 "Seven":7,"Eight":8,"Nine":9,"Ten":10,"Jack":10,"Queen":10,"King":10}

player_pocess_chips=100


class player(object):
    def __init__(self,name):
        self.pocess_brand = []
        self.name=name
        random_brand(self.pocess_brand)
        random_brand(self.pocess_brand)

def random_brand(pocess_brand):
    while 1:
        a=random.choice(kind_brand)
        b=random.choice(list(all_point_brand.keys()))
        if (a,b) not in selected_brand:
            selected_brand.append((a,b))
            pocess_brand.append((a,b))
            break
        else:
            continue

def game_start(Dealer,Player):
    global selected_brand,Player_point
    selected_brand = []
    show_brand(Dealer)
    show_brand(Player)
    global Dealer_point,Player_pointP
    Dealer_point,Player_point=0,0
    for i in range(len(Player.pocess_brand)):
        Player_point+=all_point_brand[Player.pocess_brand[i][1]]

def show_brand(player,a=0):
    print()
    print(r"{}'s Hand:".format(player.name))
    for i in range(len(player.pocess_brand)):
        if i==0 and "Dealer"==player.name and a==0:
            print("  <card hidden>")
            continue
        print("  {1} of {0}".format(player.pocess_brand[i][0],player.pocess_brand[i][1]))

def check_brand(player):
    global player_pocess_chips
    ace_num=0
    global Player_point
    global ace_use_player
    Player_point += all_point_brand[Player.pocess_brand[len(Player.pocess_brand)-1][1]]
    for i in range(len(Player.pocess_brand)):
        if "Ace" == Player.pocess_brand[i][1]:
            ace_num += 1
    if Player_point>21:
        if ace_use_player < ace_num:
            Player_point -= 10
            ace_use_player += 1
            show_brand(Dealer)
            show_brand(Player)
        else:
            show_brand(Dealer)
            show_brand(Player)
            print("Player busts!")
            player_pocess_chips-=bet
            if bet==0:
                print("Player's winnings stand at 0")
                print("Thanks for playing! You have no chips now!")
                exit(0)
            print("\nPlayer's winnings stand at %d"%player_pocess_chips)
            a=input("Would you like to play another hand? Enter 'y' or 'n'")
            if a=="Y" or a=="y":
                return 1
            else:
                print("Thanks for playing!")
                exit(0)
    else:
        show_brand(Dealer)
        show_brand(Player)



def ask_bet():
    while 1:
        global bet
        bet = input("How many chips would you like to bet?")
        if bet.isdigit():
            bet=int(bet)
            if bet <= player_pocess_chips:
                break
            else:
                print("Sorry, your bet can't exceed ",player_pocess_chips)
        else:
            print("Sorry, a bet must be an integer!")
def player_play():
    while 1:
        a = input("Would you like to Hit or Stand? Enter 'h' or 's'")
        if a == 'h' or a == 'H':
            random_brand(Player.pocess_brand)
            if 1==check_brand(Player):
                return 1
        elif a == 'S' or a == 's':
            print("Player stands. Dealer is playing.")
            break
        else:
            print("Sorry, please try again.")
def dealer_paly():
    global player_pocess_chips
    show_brand(Dealer)
    show_brand(Player)
    a = 0
    ace_num=0
    global ace_use_dealer
    for i in range(len(Dealer.pocess_brand)):
        a += all_point_brand[Dealer.pocess_brand[i][1]]
    while 1:
        if a<17:
            random_brand(Dealer.pocess_brand)
            a+=all_point_brand[Dealer.pocess_brand[i+1][1]]

        elif a > 21:
            for i  in range(len(Dealer.pocess_brand)):
                if "Ace"==Dealer.pocess_brand[i][1]:
                    ace_num+=1
            if ace_use_dealer < ace_num:
                a -= 10
                ace_use_dealer += 1
            else:
                show_brand(Dealer, 1)
                print("Dealer's Hand =", a)
                show_brand(Player)
                print("Player's Hand =", Player_point)
                print("Dealer busts!")
                player_pocess_chips += bet
                print("\nPlayer's winnings stand at %d" % player_pocess_chips)
                a = input("Would you like to play another hand? Enter 'y' or 'n'")
                if a == "Y" or a == "y":
                   return 1
                else:
                    print("Thanks for playing!")
                    exit(0)
        else:
            show_brand(Dealer, 1)
            print("Dealer's Hand =", a)
            show_brand(Player)
            print("Player's Hand =", Player_point)
            compare_point(Player_point, a)
            if player_pocess_chips==0:
                print("Player's winnings stand at 0")
                print("Thanks for playing! You have no chips now!")
                exit(0)
            print("\nPlayer's winnings stand at %d" % player_pocess_chips)
            a = input("Would you like to play another hand? Enter 'y' or 'n'")
            if a == "Y" or a == "y":
                return 1
            else:
                print("Thanks for playing!")
                exit(0)
def compare_point(a,b):
    global player_pocess_chips
    if a>b:
        print("Player wins!")
        player_pocess_chips+=bet
    elif a<b:
        print("Dealer wins!")
        player_pocess_chips -= bet
    else:
        print("Dealer and Player tie! It's a push.")
if __name__=='__main__':
    while 1:
        selected_brand = []
        Dealer_point, Player_point, ace_use_dealer, ace_use_player = 0, 0, 0, 0
        Dealer, Player = player("Dealer"), player("Player")
        print("Welcome to BlackJack! Get as close to 21 as you can without going over!")
        print("       Dealer hits until she reaches 17. Aces count as 1 or 11.")
        ask_bet()
        game_start(Dealer,Player)
        if 1==player_play():
            continue
        if 1==dealer_paly():
            continue









