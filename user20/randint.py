import random
import time
a = 0
b = 300
r1 = 0
zeit = 0.0
while (r1 != 13):
    time.sleep(0.01)
    zeit = 0.01 + zeit
    r1 = random.randint(a, b)
    print(r1)
    zeitende = "{:0.2f}".format(zeit)
    ##zeitende = round(zeit * 10)/10
print("Treffer nach: " + str(zeitende) + " Sekunden.")