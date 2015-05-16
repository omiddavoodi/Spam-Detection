
def cleanfile(filename):
    f = open(filename, 'r')
    ss = f.read()
    f.close()
    
    ss = ss.lower()
    ss = ss[ss.find('<html>'):]
    
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
