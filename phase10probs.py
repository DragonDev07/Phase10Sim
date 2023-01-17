# Libraries
from art import *
from progress.bar import Barsu
# Other files
from functions import *

# Control Vars
iterations = 10000000

# Vars
probs = { "twoSetsOfThree": 0, "oneSetOfThreeOneRunOfFour": 0, "oneSetOfFourOneRunOfFour": 0, "oneRunOfSeven": 0, "oneRunOfEight": 0, "oneRunOfNine": 0, "twoSetsOfFour": 0, "sevenCardsOfOneColor": 0, "oneSetOfFiveOneSetOfTwo": 0, "oneSetOfFiveOneSetOfThree": 0}
phaseFinishes = { "twoSetsOfThree": 0, "oneSetOfThreeOneRunOfFour": 0, "oneSetOfFourOneRunOfFour": 0, "oneRunOfSeven": 0, "oneRunOfEight": 0, "oneRunOfNine": 0, "twoSetsOfFour": 0, "sevenCardsOfOneColor": 0, "oneSetOfFiveOneSetOfTwo": 0, "oneSetOfFiveOneSetOfThree": 0}
finishPhase = 0

# Startup.
tprint("Phase10 SIM", font="poison")
print("---------------------------------------------------------------------------------------------------------")

hands = generateHands(iterations)

bar = Bar('Calculating Probabilities', max=len(hands))
# Calculate phase probabilities
for i in range(len(hands)):
    if twoSetsOfThree(hands[i]): # two sets of three probability
        phaseFinishes["twoSetsOfThree"] += 1
    if oneSetOfThreeOneRunOfFour(hands[i]): # one set of three one run of four probability
        phaseFinishes["oneSetOfThreeOneRunOfFour"] += 1
    if oneSetOfFourOneRunOfFour(hands[i]): # one set of four one run of four probability
        phaseFinishes["oneSetOfFourOneRunOfFour"] += 1
    if oneRunOfSeven(hands[i]): # one run of seven probability
        phaseFinishes["oneRunOfSeven"] += 1
    if oneRunOfEight(hands[i]): # one run of eight probability
        phaseFinishes["oneRunOfEight"] += 1
    if oneRunOfNine(hands[i]): # one run of nine probability
        phaseFinishes["oneRunOfNine"] += 1
    if twoSetsOfFour(hands[i]): # two sets of four probability
        phaseFinishes["twoSetsOfFour"] += 1
    if sevenCardsOfOneColor(hands[i]): # seven cards of one color
        phaseFinishes["sevenCardsOfOneColor"] += 1
    if oneSetOfFiveOneSetOfTwo(hands[i]): # one set of five one set of two
        phaseFinishes["oneSetOfFiveOneSetOfTwo"] += 1
    if oneSetOfFiveOneSetOfThree(hands[i]): # one set of five one set of three
        phaseFinishes["oneSetOfFiveOneSetOfThree"] += 1
    bar.next()
bar.finish()

# Save Probabilites to Dict
probs["twoSetsOfThree"] = phaseFinishes["twoSetsOfThree"] / iterations
probs["oneSetOfThreeOneRunOfFour"] = phaseFinishes["oneSetOfThreeOneRunOfFour"] / iterations
probs["oneSetOfFourOneRunOfFour"] = phaseFinishes["oneSetOfFourOneRunOfFour"] / iterations
probs["oneRunOfSeven"] = phaseFinishes["oneRunOfSeven"] / iterations
probs["oneRunOfEight"] = phaseFinishes["oneRunOfEight"] / iterations
probs["oneRunOfNine"] = phaseFinishes["oneRunOfNine"] / iterations
probs["twoSetsOfFour"] = phaseFinishes["twoSetsOfFour"] / iterations
probs["sevenCardsOfOneColor"] = phaseFinishes["sevenCardsOfOneColor"] / iterations
probs["oneSetOfFiveOneSetOfTwo"] = phaseFinishes["oneSetOfFiveOneSetOfTwo"] / iterations
probs["oneSetOfFiveOneSetOfThree"] = phaseFinishes["oneSetOfFiveOneSetOfThree"] / iterations

# Print Probabilities
# print("Probability of finishing two sets of three: " + str(probs["twoSetsOfThree"]))
# print("Probability of finishing one set of three one run of four: " + str(probs["oneSetOfThreeOneRunOfFour"]))
# print("Probability of finishing one set of four one run of four: " + str(probs["oneSetOfFourOneRunOfFour"]))
# print("Probability of finishing one run of seven: " + str(probs["oneRunOfSeven"]))
# print("Probability of finishing one run of eight: " + str(probs["oneRunOfEight"]))
# print("Probability of finishing one run of nine: " + str(probs["oneRunOfNine"]))
# print("Probability of finishing two sets of four " + str(probs["twoSetsOfFour"]))
# print("Probability of finishing seven cards of one colour " + str(probs["sevenCardsOfOneColor"]))
# print("Probability of finishing one set of five one set of two " + str(probs["oneSetOfFiveOneSetOfTwo"]))
# print("Probability of finishing one set of five one set of three " + str(probs["oneSetOfFiveOneSetOfThree"]))

sorted_d = dict(sorted(probs.items(), key=lambda item: item[1], reverse=True))
tuple_list = [tuple(item) for item in sorted_d.items()]

print(str(sorted_d))
print(str(tuple_list))

for i in range(len(tuple_list)):
    print("Phase " + str(i + 1) + ": " + str(tuple_list[i][0]))