import hashlib

def findHash (goal):
    i = 0
    while True:
        m = hashlib.md5()
        m.update("bgvyzdsv" + str(i))
        out = m.hexdigest()
        if out[0:len(goal)] == goal:
            print out
            break
        if i == 1000000000:
            print "fail"
            return
        i += 1
    print i
    
findHash("00000")
findHash("000000")