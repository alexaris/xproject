# -*- coding: utf-8 -*-
import json
import sys
import codecs

def write(filename, configuration):
    with codecs.open(filename, mode='w', encoding='utf8') as f:
        json.dump(configuration, f, indent=2)

def read(filename):
    with codecs.open(filename, mode='r', encoding='utf8') as f:
        return json.load(f)


"""
config = {}
config['left'] =  100
config['top'] = 50
config['width'] = 400
config['height'] = 400
config['servers'] = ('team154.org:21000:home',
                     '212.192.155.118:21000:ViniPuh')

write('.config', config)
"""