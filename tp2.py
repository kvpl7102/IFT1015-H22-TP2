# Date : April 23rd 2022
# Author : Vi Phung  - Matricule: 20178538
# Author 2 : Cong Long Ren - Matricule: 20220497

# This code launches an web application to play poker shuffle. It is played  
# with the standard deck of 52 playing cards. Player needs to draw 25 cards
# in the deck and place them one at a time in a grid board 5x5 one at a time
# to form the poker hands on 5 rows and 5 columns.

# Each poker hand will be rewarded with different points. The final point 
# is the sum of all the points in all rows and columns.

import math
import functools

poker = """
<!DOCTYPE html>

<html>
    <head>
        <meta charset="UTF-8"> 
        <title>Poker Shuffle</title>
        <link rel="stylesheet" href="codeboot.bundle.css">
        <script src="codeboot.bundle.js"></script>
        <script type="text/python" src="TP2.py"></script>
 </head>

<body onload = "init()">
    <style>      
        #main table { margin-top: 15px; margin-left: 10px }
        
        #main table td {border: 0; padding: 1px 2px; font-size: 30px }
                        
        #main table td img { height: auto}
                             
        #main table button {
                             width: 90px;
                             height: 45px;                         
                             font-size: 18px;                   
                             letter-spacing: normal;
                             word-spacing: normal;
                             line-height: normal;                            
                             display: inline-block;
                             text-align: center;                          
                             box-sizing: border-box;                                               
                             padding: 1px 6px;
                             border-width: 2px;
                             border-radius: 4px;
                           }
        
        #main table button:hover{ background-color: #D3D3D3 }        
       
    </style>

    <div id="main">
        <table>
            <tbody>
                <tr>
                    <td>
                        <button onclick="init()" style="float: left">
                            Nouvelle Partie
                        </button>
                    </td>                        
                    <td></td>                        
                    <td id="card25" onclick="clic(25)">
                        <img src="http://codeboot.org/cards/back.svg">
                    </td>                         
                    <td></td>
                </tr>
            </tbody>
        </table>
              
        <table>
            <tbody>
                <tr>
                    <td id="card0" onclick="clic(0)">
                        <img src="http://codeboot.org/cards/empty.svg">
                    </td>
                    <td id="card1" onclick="clic(1)">
                        <img src="http://codeboot.org/cards/empty.svg">
                    </td>
                    <td id="card2" onclick="clic(2)">
                        <img src="http://codeboot.org/cards/empty.svg">
                    </td>
                    <td id="card3" onclick="clic(3)">
                        <img src="http://codeboot.org/cards/empty.svg">
                    </td>
                    <td id="card4" onclick="clic(4)">
                        <img src="http://codeboot.org/cards/empty.svg">
                    </td>
                    <td id="R0"></td>
                </tr>
                
                <tr>
                    <td id="card5" onclick="clic(5)">
                        <img src="http://codeboot.org/cards/empty.svg">
                    </td>
                    <td id="card6" onclick="clic(6)">
                        <img src="http://codeboot.org/cards/empty.svg">
                    </td>
                    <td id="card7" onclick="clic(7)">
                        <img src="http://codeboot.org/cards/empty.svg">
                    </td>
                    <td id="card8" onclick="clic(8)">
                        <img src="http://codeboot.org/cards/empty.svg">
                    </td>
                    <td id="card9" onclick="clic(9)">
                        <img src="http://codeboot.org/cards/empty.svg">
                    </td>
                    <td id="R1"></td>
                </tr>
                
                <tr>
                    <td id="card10" onclick="clic(10)">
                        <img src="http://codeboot.org/cards/empty.svg">
                    </td>
                    <td id="card11" onclick="clic(11)">
                        <img src="http://codeboot.org/cards/empty.svg">
                    </td>
                    <td id="card12" onclick="clic(12)">
                        <img src="http://codeboot.org/cards/empty.svg">
                    </td>
                    <td id="card13" onclick="clic(13)">
                        <img src="http://codeboot.org/cards/empty.svg">
                    </td>
                    <td id="card14" onclick="clic(14)">
                        <img src="http://codeboot.org/cards/empty.svg">
                    </td>
                    <td id="R2"></td>
                </tr>
                
                <tr>
                    <td id="card15" onclick="clic(15)">
                        <img src="http://codeboot.org/cards/empty.svg">
                    </td>
                    <td id="card16" onclick="clic(16)">
                        <img src="http://codeboot.org/cards/empty.svg">
                    </td>
                    <td id="card17" onclick="clic(17)">
                        <img src="http://codeboot.org/cards/empty.svg">
                    </td>
                    <td id="card18" onclick="clic(18)">
                        <img src="http://codeboot.org/cards/empty.svg">
                    </td>
                    <td id="card19" onclick="clic(19)">
                        <img src="http://codeboot.org/cards/empty.svg">
                    </td>
                    <td id="R3"></td>
                </tr>
                
                <tr>
                    <td id="card20" onclick="clic(20)">
                        <img src="http://codeboot.org/cards/empty.svg">
                    </td>
                    <td id="card21" onclick="clic(21)">
                        <img src="http://codeboot.org/cards/empty.svg">
                    </td>
                    <td id="card22" onclick="clic(22)">
                        <img src="http://codeboot.org/cards/empty.svg">
                    </td>
                    <td id="card23" onclick="clic(23)">
                        <img src="http://codeboot.org/cards/empty.svg">
                    </td>
                    <td id="card24" onclick="clic(24)">
                        <img src="http://codeboot.org/cards/empty.svg">
                    </td>
                    <td id="R4"></td>
                </tr>
                
                <tr>
                    <td id="C0"></td>
                    <td id="C1"></td>
                    <td id="C2"></td>
                    <td id="C3"></td>
                    <td id="C4"></td>
                    <td id="total">0</td>
                </tr>
                
            </tbody>                  
        </table>
        
    </div>
</body>

</html>
"""

# -------------------------------------------------------------------------- #   
# The function cardValue takes a list of card image source 
# and returns the extracted card value (rank + suit) in it
def cardValue(lst):
    hand = []
    for img in lst:
        start = img.find('s/') + len('s/')
        end = img.rfind('.')
        card = img[start:end]
        hand.append(card)
    
    return hand


# Checking the number of pair of cards of current combination of cards  
# Returning the value of 1 or 2 
def numPair(lst):
    pairs = []
    numPair = 0
    for i in range(len(lst)):        
        for j in range(i+1, len(lst)):
            if lst[i] == lst[j] and lst[i] not in pairs:
                pairs.append(lst[i])
                
    if len(pairs) == 1:
        numPair = 1
    if len(pairs) == 2:
        numPair = 2
    
    return numPair


# Checking if current combination of cards have three-of-a-kind
# Returning a boolean value
def isTrips(lst):
    for i in range(len(lst)):
        if lst.count(lst[i]) == 3:
            return True
            break
          
    return False


# Checking if current combination of cards have four-of-a-kind
# Returning a boolean value
def isQuads(lst):
    for i in range(len(lst)):
        if lst.count(lst[i]) == 4:
            return True
            break
          
    return False


# Checking if current combination of cards is a full house
# Returning a boolean value    
def isFullHouse(lst):
    if len(lst) == 5 and isTrips(lst) and numPair(lst) == 2:
        return True
    else:
        return False

    
# Checking if current combination of cards is a straight
# Returning a boolean value   
def isStraight(lst):
    if len(lst) != 5:
        return False
    
    else:
        minVal = min(lst)
        maxVal = max(lst)
        
        if maxVal - minVal == 12 and numPair(lst) == 0:
            
            newLst = lst.copy()
            newLst.remove(maxVal)
            secondMax = max(newLst)
            
            if secondMax - minVal == 3:
                return True
            else:
                return False
                
        elif maxVal - minVal + 1 == len(lst) and numPair(lst) == 0:
            
            for i in range(len(lst)):              
                if lst[i] - minVal < 0:
                    return False
                
            return True
        
        return False   

    
# Checking if current combination of cards is a flush
# Returning a boolean value   
def isFlush(lst):
    if len(lst) != 5:
        return False
    
    else:
        ele = lst[0]
        for suit in lst:
            if ele != suit:
                return False
                break
        
        return True

# The function checkPoker takes 2 parameters: a list of cards and its ID
# of the corresponding row / column. It determines whether the current 
# list of cards is a poker hand or not, and gives corresponding points if so
def checkPoker(lst, id):
    point = document.querySelector("#"+id)
    ranks = []
    suits = []
    for rank in lst:                 
        if rank != 'empty':
            if rank[:-1] == 'J':
                ranks.append(11)
            elif rank[:-1] == 'Q':
                ranks.append(12)
            elif rank[:-1] == 'K':
                ranks.append(13)
            elif rank[:-1] == 'A':
                ranks.append(14)
            
            else:
                ranks.append(int(rank[:-1]))
           
    for suit in lst:
        if suit != 'empty': 
            suits.append(suit[-1])
    
    if isStraight(ranks) and isFlush(suits) \
    and max(ranks) == 14 and min(ranks) == 10:
        point.innerHTML = '100'  # Royal flush!!
    
    elif isStraight(ranks) and isFlush(suits):
        point.innerHTML = '75' # Straight flush
        
    elif isQuads(ranks):
        point.innerHTML = '50' # Four of a kind
        
    elif isFullHouse(ranks):
        point.innerHTML ='25' # Full house
        
    elif isFlush(suits):
        point.innerHTML = '20' # Flush
        
    elif isStraight(ranks):
        point.innerHTML = '15' # Straight
        
    elif isTrips(ranks):
        point.innerHTML = '10' # Three of a kind
        
    elif numPair(ranks) != 0:
        if numPair(ranks) == 2:
            point.innerHTML = '5' # Two pairs
        else:
            point.innerHTML = '2' # One pair
    else:
        point.innerHTML = ''  # Nothing / High card

# -------------------------------------------------------------------------- #   

# Checking if there is a selected card in the grid
# Returning a boolean value
def isSelected():
    for i in range(26):
        card = document.querySelector('#card'+str(i))
        if card.hasAttribute('style'):
            return True                
    return False


# Returning the position of the previous selected card
def prev():
    for i in range(26):
        prevCard = document.querySelector('#card'+str(i))
        if prevCard.hasAttribute('style'):
            return prevCard


# Returning True if all positions of the grid is filled by cards
# Returning False otherwise
def isFinished():
    for card in grid[:-1]:
        if card == empty:
            return False
    return True


# This function takes a list as a parameter 
# and returns a random element in the list
def randomEle(lst):
    randIndex = math.floor(random()*len(lst))
    return lst[randIndex]


# This functions returns the sum of all the elements  
# in a list of numbers
def sumList(lst):
    return functools.reduce(lambda x,y: x+y, lst, 0)


# Update the representation of HTML of the game 
def updateHTML():             
    for i in range(26):
        content = grid[i]
        card = document.querySelector('#card'+str(i))       
        card.innerHTML = content

        
# Executing a click in a card case 
def clic(index):
    global currentImg, prevCard, prevIndex
    
    currentCard = document.querySelector('#card'+str(index))
    prevCard = prev()   
    
    if index == 25: # if clicking the deck card case
        
        if not isSelected():
            currentCard.setAttribute('style', 'background-color: lime')                     
            
            if grid[25] == back:  
                currentImg = randomEle(cards)
                grid[25] = currentImg
                cards.remove(currentImg)
                prevIndex = 25
                            
            else: #if grid[25] != back
                if prevIndex != 25:
                    currentCard.setAttribute('style',
                                             'background-color: lime')
                    currentImg = grid[25]
                    prevIndex = 25
                            
        else: #if isSelected() 
            
            if prevIndex == 25:
                currentCard.removeAttribute('style')
            
            else: #if prevIndex != 25
                
                if grid[25] == back:
                    prevCard.removeAttribute('style')
                    currentCard.setAttribute('style',
                                             'background-color: lime')
                    currentImg = randomEle(cards)
                    grid[25] = currentImg
                    cards.remove(currentImg)
                    prevIndex = 25
                                 
                else: #if grid[25] != back
                    prevCard.removeAttribute('style')
                    currentCard.setAttribute('style',
                                             'background-color: lime')
                    currentImg = grid[25]
                    prevIndex = 25
                           
                        
    if index != 25: # if clicking 1 of the card case on grid table

        if not isSelected():          
            
            if grid[index] != empty:             
                currentCard.setAttribute('style',
                                         'background-color: lime')                                              
                currentImg = grid[index]
                prevIndex = index
        
        else: #if isSelected()
            
            if grid[index] == empty:               
                grid[index] = currentImg             
                grid[prevIndex] = back if prevIndex == 25 else empty                                               
                prevCard.removeAttribute('style')
 
            else: #if grid[index] != empty
                
                if grid[index] == currentImg:
                    currentCard.removeAttribute('style')
                                 
                else: #if grid[index] != currentImg                
                    
                    if prevIndex != 25:
                        prevCard.removeAttribute('style')
                        temp = grid[index]             
                        grid[index] = currentImg
                        grid[prevIndex] = temp                                          
                                                
                    else: #if prevIndex == 25                                             
                        prevCard.removeAttribute('style')
                        currentCard.setAttribute('style',
                                                 'background-color: lime')
                        prevIndex = index
                        currentImg = grid[index]

    # --------------------------------------------------------------------- # 
    # Extracting the cards values from the card image sources in each row 
    # or column and check poker hand in these combinations of cards                 
    rows = [ grid[0:5],
             grid[5:10],
             grid[10:15],
             grid[15:20],
             grid[20:25] ]
    
    cols = [ grid[0:21:5],
             grid[1:22:5],
             grid[2:23:5],
             grid[3:24:5],
             grid[4:25:5] ]
       
    handRow = list(map(cardValue, rows))    
    handCol = list(map(cardValue, cols))
    
    checkPoker(handRow[0], 'R0')
    checkPoker(handRow[1], 'R1')
    checkPoker(handRow[2], 'R2')
    checkPoker(handRow[3], 'R3')
    checkPoker(handRow[4], 'R4')
    
    checkPoker(handCol[0], 'C0')
    checkPoker(handCol[1], 'C1')
    checkPoker(handCol[2], 'C2')
    checkPoker(handCol[3], 'C3')
    checkPoker(handCol[4], 'C4')
    
    # --------------------------------------------------------------------- #
    # Calculate total point
    rowsPoint = []
    colsPoint = []
    for i in range(5):
        rowId = document.querySelector("#R" + str(i))
        colId = document.querySelector("#C" + str(i))
        
        if rowId.innerHTML == "":
            rowsPoint.append(0)       
        else:
            rowsPoint.append(int(rowId.innerHTML))
            
        if colId.innerHTML == "":
            colsPoint.append(0)
        else:    
            colsPoint.append(int(colId.innerHTML))           
    
    total.innerHTML = str(sumList(rowsPoint) + sumList(colsPoint))   
   # --------------------------------------------------------------------- #        
    updateHTML()

    # If the game is finished, alert the total point and start a new game
    if isFinished():
        sleep(0.1)
        alert('Your total point is ' + total.innerHTML)
        init()

        
# Initialising a new game of poker shuffle    
def init():
    global grid, total, cards, back, empty
    
    back = '<img src="http://codeboot.org/cards/back.svg">'
    empty = '<img src="http://codeboot.org/cards/empty.svg">'
    
    grid = [empty]*25 + [back] # create a new empty grid board

    # Reset the points 
    total = document.querySelector('#total')           
    for i in range(5):
        rowId = document.querySelector("#R" + str(i))
        colId = document.querySelector("#C" + str(i))       
        rowId.innerHTML = ''       
        colId.innerHTML = ''      
    total.innerHTML = '0'

    # Reset the deck
    src = '<img src="http://codeboot.org/cards/[valeur][couleur].svg">'
    start = src.find('[')
    end = src.rfind(']') + 1

    ranks = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    suits = ['S','C','D','H']

    cards = []    
    for rank in ranks:
        for suit in suits:
            value = rank + suit
            card = src.replace(src[start:end], value)
            cards.append(card)
    
    updateHTML()
       
page = document.querySelector('#main')
page.innerHTML = poker


def unitTest():
    assert sumList([6,4,4])  == 14
    assert randomEle(['AH','AD','AC']) == 'AH' or 'AD' or 'AC'

    assert numPair([5,2,3,4,6]) == 0   # 0 pair
    assert numPair([2,2,3,4,6]) == 1   # 1 pair
    assert numPair([2,2,4,4,6]) == 2   # 2 pairs
    
    assert isQuads([9,9,9,9,5]) == True    # four of a kind
    assert isTrips([8,8,8,2,3])  == True  # three of a kind
    assert isFullHouse([10,10,10,6,6]) == True # full house
    
    assert isStraight([6,2,3,4,5])  == True  # a straight
    assert isStraight([14,2,3,4,5]) == True  # a straight of with Ace as the 
                                             # smallest card
   
    assert isFlush(['H','H','H','H','H']) == True  # a flush of Hearts
    assert isFlush(['S','H','H','H','H']) == False # not a flush

unitTest()
    

init()
