# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 11:29:18 2016

@author: johnzupan
"""


class rapper(object):
    '''
    '''
    def __init__(self, name):
        self.name = name
        self.associatedActs = []
    
    def __str__(self):
        return self.name
    
    def addAssociatedAct(self, associatedAct):
        self.associatedActs.append(associatedAct)
        return 'associated {} and {}'.format(self.name, associatedAct)
        
    def getAssociatons(self):
        return self.associatedActs