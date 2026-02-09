# Password Generator Test Run I
import random 
letterUp = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
lowers = [lowers.lower() for lowers in letterUp]
numbers = ["1", "2", "3","4","5","6","7","8","9","10"]
symbol = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+"]

randomUp = random.choice(letterUp)
randomLow = random.choice(lowers)
randomNum1 = random.choice(numbers)
randomNum2 = random.choice(numbers)
randomSym = random.choice(symbol)

set = random.random()
if (set < 0.2) :
    password = randomNum2 + randomSym + randomLow + randomNum1 + randomUp
elif (set > 0.4 and set < 0.6) :
    password = randomUp + randomLow + randomSym + randomNum1 + randomNum2
elif (set > 0.6 and set < 0.8) :
    password = randomSym + randomNum1 + randomUp + randomNum2 + randomLow
else :
    password = randomLow + randomUp + randomNum1 + randomNum2 + randomSym

print(password) 
