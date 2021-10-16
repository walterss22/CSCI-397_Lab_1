'''

Author: Scott Walters
File: cracker.py

This file compares the hashes of the words in dictionary.txt to the shadow file using multiple algorithms 

'''

import io
import hashlib

def check(keys, hashes, func):
    curr = func
    for ndx in range(len(keys)):
        for hash in range(len(hashes)):
            curr.update(keys[ndx])
            curr.digest()
            if str(curr) == hashes[hash]:
                return ndx

def main():

    #setup
    shadowFile = open("shadow", 'r')
    shadow = shadowFile.read()
    hashes = shadow.splitlines()
    shadowFile.close()
    for ndx in range(3):
        hashes[ndx] = hashes[ndx][6:]
        print(ndx)
    print(hashes)
    keyFile = open("dictionary.txt", 'r').read()
    keys = keyFile.splitlines()
    done = False

    for key in keys:
        coded = key.encode()
        md = hashlib.md5(coded).hexdigest()
        #sha = hashlib.sha1(coded).hexdigest()
        for ndx in range(len(hashes)):
            print(key)
            if hashes[ndx] == md:
                print("md match")
                print(key)
                print(str(ndx) + "\n")
                done = True
                break
            '''    
            elif hash == sha:
                print("sha match")
                print(key)
                print(ndx+"\n")
            '''
        if done:
            break
    print("done")


if __name__ == "__main__":
    main()