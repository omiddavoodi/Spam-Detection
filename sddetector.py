import sdvectorizer
import sdvectormul
#import sdvectorfind
import os

allw = {}
w = []

def init():
    global allw
    global w
    
    numwords = 0
    
    f = open('w.txt', 'r')
    s = f.read()
    f.close()

    wstr = s.split('\n')
    wstr.pop()

    for i in wstr:
        w.append((numwords,float(i[i.find(':')+1:])))
        allw[i[:i.find(':')]] = numwords
        numwords += 1

        
def check(fn):
    global allw
    global w
    qq = sdvectorizer.vectorize(fn)
    newqq = []
    for i in qq:
        ttt = allw.get(i)
        if (ttt):
            newqq.append((ttt, qq[i]))
    newqq = sorted(newqq)
    
    return sdvectormul.multiply(w, newqq)


init()

spamfiles = []
ee = os.listdir('''GP.tar/GP''')
#ee = os.listdir('''farmer-d.tar/farmer-d''')
eef = []
for i in ee[5:7]:
    eef.append('''GP.tar/GP/''' + i)
#    eef.append('''farmer-d.tar/farmer-d/''' + i)
    
for t in (eef):
    jj = os.listdir(t)
    for i in range(len(jj)):
        jj[i] = t + '/' + jj[i]
    spamfiles.extend(jj)

nall = 0
nspam = 0
nham = 0

for i in spamfiles:
    t = check(i)
    if (t):
        nall += 1
        if (t >= 0):
            nspam += 1
        else:
            nham += 1

print ("From " + str(nall) + " spam emails, the program detected " + str(nspam) + " spam mails, and " + str(nham) + " normal mails which is a success ratio of " + str(nspam / nall))

hamfiles = []
#ee = os.listdir('''GP.tar/GP''')
ee = os.listdir('''kaminski-v.tar/kaminski-v''')
eef = []
for i in ee[0:15]:
    eef.append('''kaminski-v.tar/kaminski-v/''' + i)
#    eef.append('''GP.tar/GP/''' + i)
    
    
for t in (eef):
    jj = os.listdir(t)
    for i in range(len(jj)):
        jj[i] = t + '/' + jj[i]
    hamfiles.extend(jj)

nall = 0
nspam = 0
nham = 0

for i in hamfiles:
    t = check(i)
    if (t):
        nall += 1
        if (t >= 0):
            nspam += 1
        else:
            nham += 1

print ("From " + str(nall) + " normal emails, the program detected " + str(nspam) + " spam mails, and " + str(nham) + " normal mails which is a success ratio of " + str(nham / nall))

