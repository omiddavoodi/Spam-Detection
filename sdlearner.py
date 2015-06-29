import sdvectorizer
import sdvectormul
#import sdvectorfind
import os, datetime

def learn():
    spamfiles = []
    ee = os.listdir('''GP.tar/GP''')
    eef = []
    for i in ee[:4]:
        eef.append('''GP.tar/GP/''' + i)
    for t in (eef):
        jj = os.listdir(t)
        for i in range(len(jj)):
            jj[i] = t + '/' + jj[i]
        spamfiles.extend(jj)
    print (len(spamfiles))
    hamfiles = []
    ee = os.listdir('''beck-s.tar/beck-s''')
    eef = []
    for i in ee:
        eef.append('''beck-s.tar/beck-s/''' + i)

    ee = os.listdir('''kaminski-v.tar/kaminski-v''')
    for i in ee[:len(ee)//3]:
        eef.append('''kaminski-v.tar/kaminski-v/''' + i)

    ee = os.listdir('''farmer-d.tar/farmer-d''')
    for i in ee[:len(ee)//2]:
        eef.append('''farmer-d.tar/farmer-d/''' + i)
    
    for t in (eef):
        jj = os.listdir(t)
        for i in range(len(jj)):
            jj[i] = t + '/' + jj[i]
        hamfiles.extend(jj)
    print (len(hamfiles))
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
    maxn = 12
    learningrate = 0.3
    wlen = len(w)
    print (len (allv))
    while (n < maxn):
        before = datetime.datetime.now()
        print (n)
        v = 0
        vv = 0
        for i in allv:
            v += 1
            vv += 1
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
            if v == 500:
                print (vv)
                v = 0
        n += 1
        print (datetime.datetime.now() - before)
                    
    hh = ""
    for i in allw:
        hh += i + ':' + str(w[allw[i]][1]) +'\n'

    f = open('w.txt', 'w')
    f.write(hh)
    f.close()








learn()
