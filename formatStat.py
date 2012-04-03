'''
Make formating statistic

'''
def format_stat(d_stat):
    result, buf = '%s%6s%6s%8s%8s\n' % ('Name'+' '*11, 'Score', 'eAir',
                                        'Bullets', '%air'), ''
    for key, value in d_stat.items():
        air_percent = 0
        if value[2] == '0':
            air_percent = 0
        else:
            air_percent = float(value[3])/float(value[2]) * 100 
        if len(key) > 15:
            buf = key[:13] + '..'
        else:
            buf = key + ' '*(15 - len(key))
        
        result += '%s%6s%6s%8s%8.2f\n' % (buf, value[0], value[1],
                                        value[2], air_percent)
    return result