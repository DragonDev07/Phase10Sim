import random
from progress.bar import Bar

def generateHands(iterations):
    # Create a list of the cards in a Phase 10 deck
    deck = [(1, 'Y'), (1, 'Y'), (1, 'B'), (1, 'B'), (1, 'R'), (1, 'R'), (1, 'G'), (1, 'G'),
            (2, 'Y'), (2, 'Y'), (2, 'B'), (2, 'B'), (2, 'R'), (2, 'R'), (2, 'G'), (2, 'G'), 
            (3, 'Y'), (3, 'Y'), (3, 'B'), (3, 'B'), (3, 'R'), (3, 'R'), (3, 'G'), (3, 'G'),
            (4, 'Y'), (4, 'Y'), (4, 'B'), (4, 'B'), (4, 'R'), (4, 'R'), (4, 'G'), (4, 'G'),
            (5, 'Y'), (5, 'Y'), (5, 'B'), (5, 'B'), (5, 'R'), (5, 'R'), (5, 'G'), (5, 'G'),
            (6, 'Y'), (6, 'Y'), (6, 'B'), (5, 'B'), (6, 'R'), (6, 'R'), (6, 'G'), (6, 'G'),
            (7, 'Y'), (7, 'Y'), (7, 'B'), (7, 'B'), (7, 'R'), (7, 'R'), (7, 'G'), (7, 'G'),
            (8, 'Y'), (8, 'Y'), (8, 'B'), (8, 'B'), (8, 'R'), (8, 'R'), (8, 'G'), (8, 'G'), 
            (9, 'Y'), (9, 'Y'), (9, 'B'), (9, 'B'), (9, 'R'), (9, 'R'), (9, 'G'), (9, 'G'), 
            (10, 'Y'), (10, 'Y'), (10, 'B'), (10, 'B'), (10, 'R'), (10, 'R'), (10, 'G'), (10, 'G'),
            (11, 'Y'), (11, 'Y'), (11, 'B'), (11, 'B'),  (11, 'R'), (11, 'R'), (11, 'G'), (11, 'G'),
            (12, 'Y'), (12, 'Y'), (12, 'B'), (12, 'B'), (12, 'R'), (12, 'R'), (12, 'G'), (12, 'G'),
            ('Wild', 'BlackW'), ('Wild', 'BlackW'), ('Wild', 'BlackW'), ('Wild', 'BlackW'), ('Wild', 'BlackW'), ('Wild', 'BlackW'), ('Wild', 'BlackW'),
            ('Skip', 'BlackS'), ('Skip', 'BlackS'), ('Skip', 'BlackS'), ('Skip', 'BlackS')
        ]
    
    # Create empty list to store hands
    hands = []

    # Choose 10 cards at random from the deck
    bar = Bar('Generating Hands', max=iterations)
    for i in range(0, iterations):
        hands.append(random.sample(deck, 10))
        bar.next()
    bar.finish()
    
    return hands

# Two sets of 3
def twoSetsOfThree(hand):
    numbers = [card[0] for card in hand]
    counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
    finishedAmount = 0
    finished = False

    for i in range(len(numbers)):
        if numbers[i] != "Wild" and numbers[i] != "Skip":
            counts[numbers[i]] += 1
        elif numbers[i] == "Wild":
            for i in range(1, 11):
                counts[i] += 1

    for i in range(1, 11):
        if counts[i] >= 3:
            finishedAmount += 1

    if finishedAmount >= 2:
        finished = True

    return finished

# One set of 3 + One run of 4
def oneSetOfThreeOneRunOfFour(hand):
    numbers = [card[0] for card in hand]
    counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
    runLength = 4
    finishedRun = False
    finishedSet = False
    finished = False

    # Count Numbers and add one to all if Wild
    for i in range(len(numbers)):
        if numbers[i] != "Wild" and numbers[i] != "Skip":
            counts[numbers[i]] += 1
        elif numbers[i] == "Wild":
            for i in range(1, 11):
                counts[i] += 1

    # Check for set of three
    for i in range(1, 11):
        if counts[i] >= 3:
            finishedSet = True

    # Check for run of four
    for i in range(1, 11 - runLength + 1):
        run_found = True
        for j in range(i, i + runLength):
            if counts[j] == 0:
                run_found = False
                break
        if run_found:
            finishedRun = True
    
    if finishedSet and finishedRun:
        finished = True

    return finished

# One set of 4 + One run of 4
def oneSetOfFourOneRunOfFour(hand):
    numbers = [card[0] for card in hand]
    counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
    runLength = 4
    finishedRun = False
    finishedSet = False
    finished = False

    # Count Numbers and add one to all if Wild
    for i in range(len(numbers)):
        if numbers[i] != "Wild" and numbers[i] != "Skip":
            counts[numbers[i]] += 1
        elif numbers[i] == "Wild":
            for i in range(1, 11):
                counts[i] += 1

    # Check for set of three
    for i in range(1, 11):
        if counts[i] >= 4:
            finishedSet = True

    # Check for run of four
    for i in range(1, 11 - runLength + 1):
        run_found = True
        for j in range(i, i + runLength):
            if counts[j] == 0:
                run_found = False
                break
        if run_found:
            finishedRun = True
    
    if finishedSet and finishedRun:
        finished = True

    return finished

# One run of Seven
def oneRunOfSeven(hand):
    numbers = [card[0] for card in hand]
    counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
    length = 7
    finished = False

    # Count Numbers and add one to all if Wild
    for i in range(len(numbers)):
        if numbers[i] != "Wild" and numbers[i] != "Skip":
            counts[numbers[i]] += 1
        elif numbers[i] == "Wild":
            for i in range(1, 11):
                counts[i] += 1

    # Check for run of four
    for i in range(1, 11 - length + 1):
        run_found = True
        for j in range(i, i + length):
            if counts[j] == 0:
                run_found = False
                break
        if run_found:
            finished = True
    
    return finished

# One run of Eight
def oneRunOfEight(hand):
    numbers = [card[0] for card in hand]
    counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
    length = 8
    finished = False

    # Count Numbers and add one to all if Wild
    for i in range(len(numbers)):
        if numbers[i] != "Wild" and numbers[i] != "Skip":
            counts[numbers[i]] += 1
        elif numbers[i] == "Wild":
            for i in range(1, 11):
                counts[i] += 1

    # Check for run of four
    for i in range(1, 11 - length + 1):
        run_found = True
        for j in range(i, i + length):
            if counts[j] == 0:
                run_found = False
                break
        if run_found:
            finished = True
    
    return finished

# One run of Nine
def oneRunOfNine(hand):
    numbers = [card[0] for card in hand]
    counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
    length = 9
    finished = False

    # Count Numbers and add one to all if Wild
    for i in range(len(numbers)):
        if numbers[i] != "Wild" and numbers[i] != "Skip":
            counts[numbers[i]] += 1
        elif numbers[i] == "Wild":
            for i in range(1, 11):
                counts[i] += 1

    # Check for run of four
    for i in range(1, 11 - length + 1):
        run_found = True
        for j in range(i, i + length):
            if counts[j] == 0:
                run_found = False
                break
        if run_found:
            finished = True
    
    return finished

# Two sets of four
def twoSetsOfFour(hand):
    numbers = [card[0] for card in hand]
    counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
    finishedAmount = 0
    finished = False

    for i in range(len(numbers)):
        if numbers[i] != "Wild" and numbers[i] != "Skip":
            counts[numbers[i]] += 1
        elif numbers[i] == "Wild":
            for i in range(1, 11):
                counts[i] += 1

    for i in range(1, 11):
        if counts[i] >= 4:
            finishedAmount += 1

    if finishedAmount >= 2:
        finished = True

    return finished

def sevenCardsOfOneColor(hand):
    colours = [card[1] for card in hand]
    counts = {"Y": 0, "B": 0, "R": 0, "G": 0}
    finished = False

    for i in range(len(colours)):
        if colours[i] != "BlackW" and colours[i] != "BlackS":
            counts[colours[i]] += 1
        elif colours[i] == "BlackW":
            for j in range(1, 3):
                match j:
                    case 1:
                        counts["Y"] += 1
                    case 2:
                        counts["B"] += 1
                    case 3:
                        counts["R"] += 1
                    case 4:
                        counts["G"] += 1
    
    for i in range(1, 3):
        match i:
            case 1:
                if counts["Y"] >= 7:
                    finished = True
            case 2:
                if counts["B"] >= 7:
                    finished = True
            case 3:
                if counts["R"] >= 7:
                    finished = True
            case 4:
                if counts["G"] >= 7:
                    finished = True

    return finished

def oneSetOfFiveOneSetOfTwo(hand):
    numbers = [card[0] for card in hand]
    counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
    finishedTwo = False
    finishedFive = False
    finished = False

    for i in range(len(numbers)):
        if numbers[i] != "Wild" and numbers[i] != "Skip":
            counts[numbers[i]] += 1
        elif numbers[i] == "Wild":
            for i in range(1, 11):
                counts[i] += 1
    
    for i in range(1, 11):
        if counts[i] >= 5:
            finishedFive = True
        elif counts[i] >= 2:
            finishedTwo = True

    if finishedFive and finishedTwo:
        finished = True

    return finished

def oneSetOfFiveOneSetOfThree(hand):
    numbers = [card[0] for card in hand]
    counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
    finishedTwo = False
    finishedFive = False
    finished = False

    for i in range(len(numbers)):
        if numbers[i] != "Wild" and numbers[i] != "Skip":
            counts[numbers[i]] += 1
        elif numbers[i] == "Wild":
            for i in range(1, 11):
                counts[i] += 1
    
    for i in range(1, 11):
        if counts[i] >= 5:
            finishedFive = True
        elif counts[i] >= 3:
            finishedTwo = True

    if finishedFive and finishedTwo:
        finished = True

    return finished