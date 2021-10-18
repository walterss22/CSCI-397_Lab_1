'''

Author: Scott Walters
File: cracker.py

This file compares the hashes of the words in dictionary.txt to the shadow file using multiple algorithms.

The only hashing algorithms included are those applicable to those in the shadow file

'''

import io
import hashlib

#This function checks keys against hashed, hexdigested passwords
#Args: list of keys, list of hashes, hashing function (must include hashlib.<hashing algorithm>),
#and a boolean to tell to hash with a salt
def check(keys, hashes, func, salted = False):
    if not salted:
        for key in keys:
            coded = key.encode()
            hex = func(coded).hexdigest()
            for ndx in range(len(hashes)):
                if hashes[ndx] == hex:
                    print(str(func) + " match")
                    print(key)
                    print(str(ndx) + "\n")
                    return key
    else:
        for x in range(0,10):
            for y in range(0,10):
                for z in range(0,10):
                    for a in range(0,10):
                        for b in range(0,10):
                            for key in keys:
                                #print(key+ str(x) + str(y) + str(z) + str(a) + str(b))
                                coded = (key+ str(x) + str(y) + str(z) + str(a) + str(b)).encode()
                                hex = func(coded).hexdigest()
                                #print(hex + "\n")
                                for ndx in range(len(hashes)):
                                    if hashes[ndx] == hex:
                                        print(str(func) + " match")
                                        print(key)
                                        print(str(ndx) + "\n")
                                        print(key+ str(x) + str(y) + str(z) + str(a) + str(b))
                                        return key
def main():

    #setup
    shadowFile = open("shadow", 'r')
    shadow = shadowFile.read()
    hashes = shadow.splitlines()
    shadowFile.close()
    for ndx in range(3):
        hashes[ndx] = hashes[ndx][6:]
    keyFile = open("dictionary.txt", 'r').read()
    keys = keyFile.splitlines()

    #for user1
    check(keys, hashes, hashlib.md5)

    #for user2
    check(keys, hashes, hashlib.sha256, True)

    #for user3
    check(keys, hashes, hashlib.sha512)

if __name__ == "__main__":
    main()