import os

def cleanfile(filename):
    f = open(filename, 'r')
    ss = f.read()
    f.close()
    
    ss = ss.lower()
    ss = ss[ss.find('\n', ss.find('x-filename:')):]
    
    sp = []
    intag = False
    inspc = False
    for i in ss:
        if (i == '<'):
            intag = True
        elif (i == '>'):
            intag = False
        elif (i == '&'):
            inspc = True
        elif (i == ';'):
            inspc = False
        elif (not intag and not inspc):
            sp.append(i)

    s = ''.join(sp)

    s = s.replace('=20', '')
    
    f = open(filename, 'w')
    f.write(s)
    f.close()

hamfiles = []
ee = os.listdir('''kaminski-v.tar/kaminski-v''')
eef = []
for i in ee[0:15]:
    eef.append('''kaminski-v.tar/kaminski-v/''' + i)
for t in (eef):
    jj = os.listdir(t)
    for i in range(len(jj)):
        jj[i] = t + '/' + jj[i]
    hamfiles.extend(jj)

for i in hamfiles:
    cleanfile(i)
