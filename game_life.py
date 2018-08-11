# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 13:11:44 2018

@author: Achraf Baiz
"""


import numpy as np
import random
from collections import Counter
from scipy.misc import imsave

class life(object):
    
    def __init__(self,size,generation,setmotif=0):

        self.preuniver  = np.zeros(size,dtype='int64')
        self.postuniver = np.zeros(size,dtype='int64')
        self.generation = generation
        self.setmotif   = setmotif
        # Set up a random initial configuration for the grid.
        # 0   dead
        # 255 alive
        if setmotif == 0 :
            for i in range(0,self.preuniver.shape[0]):
               for j in range(0,self.preuniver.shape[1]):
                   if(random.randint(0, 100) < 15):
                      self.preuniver.itemset((i,j), 255)
                   else:
                      self.preuniver.itemset((i,j), 0)
        
    
    def set_motif(self,*args,i,j):
        if self.setmotif == 1 and len(args)==9:
            # by default the origin of the motif is the cell 5 since the motif is 9 cases
            self.preuniver.itemset((i,j-1)  ,args[3])
            self.preuniver.itemset((i,j)    ,args[4]) # center of motif
            self.preuniver.itemset((i,j+1)  ,args[5])
            self.preuniver.itemset((i-1,j-1),args[0])
            self.preuniver.itemset((i-1,j)  ,args[1])
            self.preuniver.itemset((i-1,j+1),args[2])
            self.preuniver.itemset((i+1,j-1),args[6])
            self.preuniver.itemset((i+1,j)  ,args[7])
            self.preuniver.itemset((i+1,j+1),args[8])
        else:
            print("univer is already populated randomly")
            return
        
    def check_cell(self,i,j):
        l = list()
        # by default the origin of the motif is the cell 5 since the motif is 9 cells
        try :
               # append all neighbours but the cell i j itself
               # l.append(self.preuniver.item(i,j))
               l.append(self.preuniver.item(i,j-1))
               l.append(self.preuniver.item(i,j+1))
               l.append(self.preuniver.item(i-1,j-1))
               l.append(self.preuniver.item(i-1,j))
               l.append(self.preuniver.item(i-1,j+1))
               l.append(self.preuniver.item(i+1,j-1))
               l.append(self.preuniver.item(i+1,j))
               l.append(self.preuniver.item(i+1,j+1))
               s = Counter(l)[255]
               return s
        except:
          pass
    
    def play(self):
       snapshot_frequency = 5
       imsave('outfile_.png',self.preuniver)
       for g in range(self.generation):
          for x in range(self.preuniver.shape[0]):
             for y in range(self.preuniver.shape[1]):
                  s = self.check_cell(i=x,j=y)
                  if(s != None):
                      if(self.preuniver.item(x,y) == 255 and s < 2):
                          self.postuniver.itemset((x,y),0) # Dead from starvation.
                      elif(self.preuniver.item(x,y) == 255 and (s == 2 or s == 3)):
                          self.postuniver.itemset((x,y),255) # Continue living.
                      elif(self.preuniver.item(x,y) == 255 and s > 3):
                          self.postuniver.itemset((x,y),0) # Dead from overcrowding.
                      elif(self.preuniver.item(x,y) == 0 and s == 3):
                          self.postuniver.itemset((x,y),255) # Alive from reproduction.
          if g % snapshot_frequency == 0:  imsave('outfile_{}.png'.format(g), self.postuniver)
          self.preuniver = self.postuniver.copy()
       
          
       
       
                
      
if __name__ == '__main__':
    dim   = 128 
    #midim =int((dim/2)-1)
    #l     = [0,0, 0, 255, 255, 255, 0, 0, 0] # Oscillators pattern motif    
    life_game    = life(size=(dim,dim),generation=200,setmotif=0)
    ##game.set_motif(*l,i=midim,j=midim)  # since index start from 0 to (64/2) - 1
    life_game.play()



       
