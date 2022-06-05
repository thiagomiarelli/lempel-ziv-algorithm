import random
text = ""

for i in range(int(10e4)):
    text += chr(random.randint(0, 255))

open("a.txt", "w").write(text)