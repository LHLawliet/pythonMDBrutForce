import hashlib

from itertools import chain, product
from multiprocessing import Process


def bruteforce(charset, maxlength):
    return (''.join(candidate)
        for candidate in chain.from_iterable(product(charset, repeat=i)
        for i in range(1, maxlength + 1)))

def run(lettre, all_char, objectiv):
    complete_list = bruteforce(all_char,15)
    oldlen = 0
    for test in complete_list:
            test = lettre+test
            if oldlen != len(test):
                oldlen=len(test)
                
            hash_object = hashlib.sha1(test.encode('utf-8'))
            pbHash = hash_object.hexdigest()
            if pbHash == objectiv:
                print("Le mdp est : ",test)
                return


# Création des threads
if __name__ == '__main__':
    all_char = '!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'

    processList = []

    objectiv = input("hash : ")

    for lettre in all_char:
        
        processList.append(Process(target=run, args=(lettre, all_char, objectiv,)))
        
    for process in processList:
        process.start()
        
    for process in processList:
        process.join()
