import sdvectorizer
import sdvectormul
#import sdvectorfind
import os

def learn():
    spamfiles = []
    ee = os.listdir('''GP.tar/GP''')
    eef = []
    for i in ee[:3]:
        eef.append('''GP.tar/GP/''' + i)
    for t in (eef):
        jj = os.listdir(t)
        for i in range(len(jj)):
            jj[i] = t + '/' + jj[i]
        spamfiles.extend(jj)
        
    hamfiles = []
    ee = os.listdir('''beck-s.tar/beck-s''')
    eef = []
    for i in ee:
        eef.append('''beck-s.tar/beck-s/''' + i)
        
    for t in (eef):
        jj = os.listdir(t)
        for i in range(len(jj)):
            jj[i] = t + '/' + jj[i]
        hamfiles.extend(jj)
    allv = []
    allw = {}
    numwords = 0

    w = []

    for i in spamfiles:
        qq = (sdvectorizer.vectorize(i))
        
        if (len(qq) > 20):
            newqq = []
            for i in qq:
                if allw.get(i) is None:
                    allw[i] = numwords
                    numwords += 1
                newqq.append((allw[i], qq[i]))
            allv.append(['s']+sorted(newqq))

    for i in hamfiles:
        qq = (sdvectorizer.vectorize(i))
        
        if (len(qq) > 20):
            newqq = []
            for i in qq:
                if allw.get(i) is None:
                    allw[i] = numwords
                    numwords += 1
                newqq.append((allw[i], qq[i]))
            allv.append(['h']+sorted(newqq))

    for i in allw:
        w.append([allw[i], 0])

    w = sorted(w)

    n = 0
    maxn = 8
    learningrate = 0.3
    wlen = len(w)
    print (len (allv))
    while (n < maxn):
        print (n)
        #v = 0
        for i in allv:
            #v += 1
            #print (v)
            ilen = len(i)
            y = sdvectormul.multiply(w, i[1:])
            #print (y)
            d = 1
            if (i[0] == 'h'):
                d = -1
    ##        for j in range(len(w)):
    ##            tu = sdvectorfind(i, w[j][0])
    ##            if (tu != -1):
    ##                w[j][1] = w[j][1] + learningrate*(d - y)*i[tu]
            j = 0
            k = 1
            while (j < wlen and k < ilen):
                wj0 = w[j][0]
                ik0 = i[k][0]
                if (wj0 == ik0):
                    #print(w[j][1])
                    w[j][1] = w[j][1] + learningrate*(d - y)*i[k][1]
                    #print(w[j][1])
                    k += 1
                    j += 1
                elif (wj0 > ik0):
                    k += 1
                elif (wj0 < ik0):
                    j += 1
        n += 1
                    
    hh = ""
    for i in allw:
        hh += i + ':' + str(w[allw[i]][1]) +'\n'

    f = open('w.txt', 'w')
    f.write(hh)
    f.close()








learn()
