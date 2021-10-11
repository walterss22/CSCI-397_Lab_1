'''
Analysis.py
Author: Scott Walters

This file is meant to crack the subsitution cipher used in encrypted.py
'''

import io

#count total number of characters and number of instances for each character
def countChars(txt):
    count = {}
    tot = 0
    for ndx in txt:
        if ndx != " ":
            if ndx not in count.keys():
                count[ndx] = 1
            else:
                count[ndx] += 1
            tot += 1
    return count, tot


def main():
    enc = open("encrypted.txt", "r").readline()

    count, tot = countChars(enc)

    #print ("Raw count" + str(count))
    print ("Total " + str(tot))

    perc = {}

    for key in count.keys():
        perc[key] = round((count.get(key) / tot) * 100, 2)

    print(perc, "\n")

    #frequency table of English language
    #sourced from Cornell University
    #http://pi.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html
    
    freq = {"e" : 12.02, "t": 9.10, "a" : 8.12, "o" : 7.68, "i" : 7.31, "n" : 6.95, "s" : 6.28, "r" : 6.02, "h" : 5.92, "d" : 4.32, "l" : 3.98, "u" : 2.88, "c" : 2.71, "m" : 2.61, "f" : 2.30, "y" : 2.11, "w" : 2.09, "g" : 2.03, "p" : 1.82, "b" : 1.49, "v" : 1.11, "k" : 0.69, "x" : 0.17, "q" : 0.11, "j" : .10, "z" : 0.07}
    
    #KEY IS ENCRYPTED, VALUE IS DECRYPTED
    table = {}

    #match calculated keys to frequency table
    """ for key in perc.keys():
        for ndx in freq.keys():
            if perc.get(key) == freq.get(ndx):
                table[key] = ndx """

    for ndx in (0, len(perc.keys())):
        table[perc.keys()[ndx]] = freq.keys()[ndx]

    print(table, "\n")

    #decrypt
    plain = ""
    for ndx in enc:
        if ndx in table.keys():
            plain += table.get(ndx)
        else:
            plain += ndx

    print(len(enc))
    print(perc.keys(), "\n")

    print(plain,"\n")

if __name__ == "__main__":
    main()