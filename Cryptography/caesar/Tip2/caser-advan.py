# Caeser Cipher
 
import sys,os
 
MyCypher = 25
 
MyDict = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz `1234567890-=~!@#$%^&*()_+[]\\;\',./{}|:"<>?'
 
plaintext = 'Hello World!'
cryptmsg = ''
 
def encrypt(text, cypher):
    out_text = ''
    for e in text:
        x = e
        if (e in MyDict):
            idx = MyDict.find(e)
            idx = idx + cypher
            idx = idx % len(MyDict)
            x = MyDict[idx]
        out_text = "%s%c" % (out_text, x)
    return out_text
 
def decrypt(msg, cypher):
    out_text = ''
    for e in msg:
        x = e
        if (e in MyDict):
            idx = MyDict.find(e)
            idx = idx - cypher + len(MyDict)
            idx = idx % len(MyDict)
            x = MyDict[idx]
        out_text = "%s%c" % (out_text, x)
    return out_text
 
def ask_cypher():
    user_input = raw_input('Input Cypher: ')
    return long(user_input)
 
def ask_text():
    user_input = raw_input('Input Text: ')
    return user_input
 
def ask_action():
    print '-----------------------'
    print '0 - Exit'
    print '1 - Encrypt'
    print '2 - Decrypt'
    print '-----------------------'
    user_input = raw_input('Select You Action: ')
    if user_input in ['0', '1', '2']:
        if user_input == '0':
            return 'exit'
        elif user_input == '1':
            return 'enc'
        elif user_input == '2':
            return 'dec'
    else:
        return 'exit'
 
# ---------------------------------------------------------------
# Program Start Here
# ---------------------------------------------------------------
MyCypher = ask_cypher()
print 'Cypher: %d' % MyCypher
 
for i in range(0, 100):
    action = ask_action()
 
    if action == 'dec':
        cryptmsg = ask_text()
        print decrypt(cryptmsg, MyCypher)
    elif action == 'enc':
        plaintext = ask_text()
        print encrypt(plaintext, MyCypher)
    else:
        print 'Exit!'
        break
