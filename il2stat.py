"""Make statistics from IL2Sturmovik log file.

"""
   
def get_value(text):
    return text.split()[-1]



def get_stat2(filename):
    with open(filename, mode='r') as f:
        lines = f.readlines() 

    NEEDLE = 'Name:'
    sections = ['Score', 
                'Enemy Aircraft Kill', 
                'Fire Bullets', 
                'Hit Bullets']
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
    
    result = ''
    for s in d.iterkeys():
        result += "Name: " + s + '\n'
        for i in d[s]:
            for k in sections:
                if k in i: result += k + ": " + get_value(i) + '\n'
        result += '---' + '\n'

    return result


def get_stat(filename):
    try:
        with open(filename, mode='r') as f:
            print f
            content = f.readlines() 
    except:
        return 'coud not open %s' % filename
            
    SEPARATOR = '-'*55
    NEEDLE = 'Name'
    BEGIN_LOG_SESSION = '------------ BEGIN log session -------------'
    END_LOG_SESSION = '-------------- END log session -------------'
    
    sections = ['Name', 
                'Score', 
                'Hit Air Bullets',
                'Enemy Aircraft Kill', 
                'Fire Bullets', 
                'Hit Bullets']

    data = []
    line_iter = iter(content)
    for line in line_iter:
        if NEEDLE in line:
            alist = []
            while SEPARATOR not in line:
                for section in sections:
                    if section in line: 
                        alist.append(get_value(line))
                line = line_iter.next()
            data.append(alist)
    
    d = dict()
    for item in data:
        d[item[0]] = (item[1:])

    #print d

    result = ''
    for s in d.iterkeys():
        d[s].insert(0, s)
        j = 0
        for i in d[s]:
            result += "%s: %s\n" % (sections[j], i) 
            j += 1
        result += '---' + '\n'

    return result

#print get_stat('log.lst')

#import os
#os.system(r'"d:/games/il-2 sturmovik 1946/il2fb.exe"')