'''make statistics from IL2Sturmovik log file'''
   
def get_value(text):
    return text.split()[-1]


with open('log.lst', mode='r') as f:
    lines = f.readlines() 

NEEDLE = 'Name:'
sections = ['Score', 'Enemy Aircraft Kill', 'Fire Bullets', 'Hit Bullets']
d = dict()
data = []
key = ''

for i in range(len(lines)):
    if NEEDLE in lines[i]:
        key = get_value(lines[i])
        data = []
    for k in sections:
        if k in lines[i]:
            data.append(k + '\t' + get_value(lines[i]))
    if key != '': d[key] = data
    
for s in d.iterkeys():
    print "Name: " + s
    for i in d[s]:
        for k in sections:
            if k in i: print k + ": " + get_value(i)
    print '---'
