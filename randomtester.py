import random,string
def main1():
    random.seed("random")
    for i in range(0,len("2m8807395d9os2156v70qu84sy1w2i6e")+4):
        print random.randrange(0,26)
def main2():
    flag = "BNZQ:2m8807395d9os2156v70qu84sy1w2i6e"
    encflag = ""
    random.seed("random")
    for c in flag:
      if c.islower():
        #rotate number around alphabet a random amount
        encflag += chr((ord(c)-ord('a')-random.randrange(0,26))%26 + ord('a'))
      elif c.isupper():
        encflag += chr((ord(c)-ord('A')-random.randrange(0,26))%26 + ord('A'))
      elif c.isdigit():
        encflag += chr((ord(c)-ord('0')-random.randrange(0,10))%10 + ord('0'))
      else:
        encflag += c
    print "Unguessably Randomized Flag: "+encflag
main2()
