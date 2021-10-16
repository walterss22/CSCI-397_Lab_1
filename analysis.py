'''
Analysis.py
Author: Scott Walters

This file is meant to crack the subsitution cipher used in encrypted.txt and write the plaintext and key to a file
titled plain.txt
'''

import io

#count total number of characters and number of instances for each character
def countChars(txt):
    count = {}
    tot = 0
    for ndx in txt:
        if ndx != " " and ndx != "," and ndx != ".":
            if ndx not in count.keys():
                count[ndx] = 1
            else:
                count[ndx] += 1
            tot += 1
    return count, tot


def main():
    enc = open("encrypted.txt", "r").readline()

    count, tot = countChars(enc)
    perc = {}
    for key in count.keys():
        perc[key] = (count.get(key) / tot) * 100

    #print(perc, "\n")

    #Letter frequency (for texts) table of English language
    #sourced from Wikipedia
    # https://en.wikipedia.org/wiki/Letter_frequency
    
    freq = {"e" : 13, "t": 9.10, "a" : 8.2, "o" : 7.5, "i" : 7, "n" : 6.7, "s" : 6.3, "h" : 6.1, "r" : 6, "d" : 4.3, "l" : 4, "c" : 2.8, "u" : 2.8, "m" : 2.4, "w" : 2.4, "f" : 2.2, "g" : 2, "y" : 2, "p" : 1.9, "b" : 1.5, "v" : 0.98, "k" : 0.77, "j" : 0.15, "x" : 0.15, "q" : .095, "z" : 0.074}
    
    #KEY IS ENCRYPTED, VALUE IS DECRYPTED
    table = {}

    #match calculated keys to frequency table
    curr = list(perc.keys())[0]
    last = ""
    buff = 0
    
    while len(table.keys()) < 25:
        for key in perc.keys():
            if key in table:
                continue
            elif perc.get(key) > perc.get(curr):
                if last == "" or perc.get(key) < perc.get(last) or curr == last:
                    curr = key
            #print("key: " + key)
            #print("curr: " + curr)
            #print("last: " + last)
        
        #print("End inner loop, " + str(x))
        #print("add to table", "\n")
        

        #this buffer keeps the current letter from being too high frequency
        if not curr in table.keys():
            table[curr] = list(freq.keys())[len(table)]
        else:
            buff +=1
        last = curr
        curr = list(perc.keys())[0 + buff]

    #print("len table: " + str(len(table)), "\n")
    #print("Table: " + str(table))
    #print("Percs: " + str(perc))

    #print(table, "\n")
    #print(len(table))
    
    #manual replacements
    table['d'] = 'i'
    table['z'] = 'o'
    table['u'] = 'd'
    #table['f'] = 'r'
    table['k'] = 'y'
    #table['t'] = 'w'
    #table['y'] = 'p'
    table['i'] = 'g'
    table['c'] = 't'
    table['n'] = 'e'
    table['f'] = 's'
    #table['v'] = 'r'
    table['t'] = 'f'
    table['x'] = 'w'
    table['r'] = 'm'
    #table['g'] = 'u'
    table['w'] = 'v'
    table['e'] = 'k'
    table['j'] = 'l'
    #table['l'] = 'h'
    table['v'] = 'h'
    #table['l'] = 'r'
    table['g'] = 'b'
    #table['h'] = 'u'
    #table['l'] = 'p'
    table['y'] = 'r'
    table['h'] = 'p'
    table['l'] = 'u'
    table['p'] = 'q'
    table['m'] = 'x'
    table['b'] = 'z'

    #decrypt
    plain = ""
    for ndx in enc:
        if ndx in table.keys():
            plain += table.get(ndx)
        else:
            plain += ndx

    #print(len(enc))
    #print(perc.keys(), "\n")

    #print(plain,"\n")
    plaintxt = open("plain.txt", 'x')
    plaintxt.write(plain)

if __name__ == "__main__":
    main()