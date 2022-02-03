import random

#global variables
rank = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
suit = ('Spades','Clubs','Diamonds','Hearts')
value = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':1}

class Card:
    
    #initialization of class attributes
    def __init__(self,rank,suit):
        self.rank=rank
        self.suit=suit
        self.value=value[rank]
        
    def __str__(self):
        return (f'{self.rank} of {self.suit}')
                
class Deck:
                
    def __init__(self):
        self.deck=[]
        for ranks in rank:
            for suits in suit:
                card=Card(ranks,suits)
                self.deck.append(card)
        random.shuffle(self.deck)
    
    def __len__(self):
        return (len(self.deck))
    
    def remove_one_card(self):
        return self.deck.pop()
    
class Player:
    
    def __init__(self,deck):
        self.cardset=[]
        self.value=0
        self.cardset.append(deck.remove_one_card())
        self.value+=self.cardset[0].value
        self.cardset.append(deck.remove_one_card())
        self.value+=self.cardset[1].value
    
    def __str__(self):
        for i in range(0,len(self.cardset)):
            print(self.cardset[i])
        return''
    
    def card_value(self):
        print(f"Your total card value is {self.value}.")
        
    def hit(self,deck):
        self.cardset.append(deck.remove_one_card())
        self.value+=self.cardset[-1].value
        
    def check(self):
        if self.value>21:
            print("Busted off")
            return True
        return False

chips =100
exit_option='y'
while exit_option=='y':
    if chips==0:
        print("Sorry You don't have enough chips to play.")
        input("Please press ENTER key to exit")
        break
    exit_option =''
    Winner=''
    newdeck = Deck()
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!')
    print('Dealer hits until she reaches 17. Aces count as 1.')
    print(f'You have {chips} chips.\n')
    
    while True:
        try:
            bet=int(input('How many chips would you like to bet?: '))
        except:
            print('Please enter an number')
        else:
            if bet>chips:
                print(f'You have only {chips} chips.')
            elif bet<1:
                print('Bet atleast 1 chip to play.')
            else:
                break
    Dealer = Player(newdeck)
    Player1 = Player(newdeck)
    choice='h'
    hiddencard=Dealer.cardset[0]
    Dealer.cardset[0]="<hidden card>"
    while choice=='h':
        choice=''
        while choice not in ['h','s']:
            print("\n Dealer's card:")
            print(Dealer)
            print("\n Player's card:")
            print(Player1)
            Player1.card_value()

            choice=input("\nWould you like to hit or stand (h/s)?: ").lower()

            if choice == 'h':
                Player1.hit(newdeck)
                choice=''
                if Player1.check():
                    Winner='Dealer'
                    break
            else:
                print("You chose to stand. Dealer is playing.")
                break
        while Dealer.value<17 and Winner!='Dealer':
            Dealer.hit(newdeck)
            if Dealer.check():
                Winner='You'
            print("\nDealer's card:")
            print(Dealer)
            print("\nPlayer's card:")
            print(Player1)
            Player1.card_value()
        
        if Winner not in ['Dealer','You']:
            if Dealer.value > Player1.value:
                Winner='Dealer'
            elif Dealer.value < Player1.value:
                Winner='You'
        
        Dealer.cardset[0]=hiddencard
        print("\nDealer's card:")
        print(Dealer)
        Dealer.card_value()
        print("\nPlayer's card:")
        print(Player1)
        Player1.card_value()
        
        if Winner=='Dealer':
            print('\nYou Lost the Game!!! Dealer won')
            chips-=bet
        elif Winner=='You':
            print('\nYou Won the Game!!! Dealer lost')
            chips+=bet
        else:
            print("\nThe  Game is a draw")
    while exit_option not in ['y','n']:
        exit_option=input('Do you want to continue playing (Y/N): ').lower()