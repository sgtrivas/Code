# this script will take a word and hash it to create a 32char password
import hashlib
import pyinputplus as p

def hashed(word):
    m = hashlib.md5(word.encode())
    return m.hexdigest()

word = p.inputStr("whats the passwoid? ")

print(hashed(word))





