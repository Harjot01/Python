import pywhatkit
import random
list = ["Hello", "Hi", "Bie Bie"]
count = 0
for i in range(10):
    msg = random.choice(list)
    pywhatkit.sendwhatmsg("+917888740930", msg, 17, count + 2)
