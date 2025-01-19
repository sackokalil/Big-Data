# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 18:32:41 2024

@author: kalil
"""

import math
import random
import statistics
import os
import glob

print( math.cos(2*math.pi))
print(math.exp(5))


list_1  = [1, 51, 32, 48, 21, 2]
list_2 = ["John", "Pierre", "Kalil","Souleyman"]

print(statistics.mean(list_1))
print(statistics.variance(list_1))
print(statistics.stdev(list_1))

#/random.seed(0)#permet de fixer l'alleatoire à un seul element donné. toute ligne qui vient après cette ligne si c'est du random, le resultat sera fixé au premier element aléatoire pour toutes les autre execution de la partie 
print(random.choice(list_2))
random.shuffle(list_1) # permet de melanger aléatoirement les éléments

print(random.random()) #float
print(random.randint(5, 10))
print(random.randrange(100))

print(random.sample(range(15), 6)) #renvois 6 nombre aléatoires dans la population de 0 à 15
print(random.sample(range(100), random.randrange(40)))# un nombre aléatoire d'elements qui sont  compris entre 0 et 100, sachant que ce nombre aléatoire lui meme est entre 0 et 40



print(os.getcwd()) #renvois le chemin du repertoir de travail courant
#print(glob.glob("*")) # renvois tous les fichier du repertoir courant
print(glob.glob("*.txt")) # renvois tous les fichier d'extension txt du repertoir

filenames = glob.glob("*.txt")
for file in filenames :
    with open(file, 'r') as f:
        print(f.read())
        
        
        

