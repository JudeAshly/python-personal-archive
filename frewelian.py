#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on 

Course work: 

@author: Jude

Source:
    
'''

# Import necessary modules
 


# Import necessary modules
import requests
import json
import sys

KEY = 'trnsl.1.1.20190319T222338Z.d93706c419b2d04f.80bc5f0f6f99967ee34e80c3612898353f492d06'
API_BASE = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


def startpy():

    word = 'World'

    #rint('len of argv : ', len(sys.argv))

    if(len(sys.argv) > 1):
        word = sys.argv[1]

    fr_content = translate_en_to_fr(word)
    it_content = translate_en_to_it(word)
    cy_content = translate_en_to_cy(word)

    print(word)
    print(fr_content)
    print(it_content)
    print(cy_content)


def translate_en_to_it(content):
    response = requests.get(API_BASE+'?key='+KEY+'&text='+content+'&lang=en-it')
    #print(response.text)

    r_content = response.text

    content_json = json.loads(r_content)

    tr_content = content_json['text'][0]

    #print(tr_content)

    return tr_content

def translate_en_to_cy(content):
    response = requests.get(API_BASE+'?key='+KEY+'&text='+content+'&lang=en-cy')
    #print(response.text)

    r_content = response.text

    content_json = json.loads(r_content)

    tr_content = content_json['text'][0]

    #print(tr_content)

    return tr_content

def translate_en_to_fr(content):
    response = requests.get(API_BASE+'?key='+KEY+'&text='+content+'&lang=en-fr')
    #print(response.text)

    r_content = response.text

    content_json = json.loads(r_content)

    tr_content = content_json['text'][0]

    #print(tr_content)

    return tr_content



if __name__ == '__main__':
    startpy()