# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 20:01:05 2016

@author: johnzupan
"""

import extractData as e
reload(e)


def main(startingURL, startingArtist, numOfLoops):
    '''
    
    '''
    
    listOfActs = e.extractData(startingURL)
    startingList = []
    for i in listOfActs:
        startingTuple = (startingArtist, startingArtist, i[0], i[1])
        startingList.append(startingTuple)

    if len(startingList) > numOfLoops:
        userInput = raw_input('''
        The number of loops you entered is less than 
        the first level of associated acts. Select 'Yes' to increase the number of loops,
        select 'No' to keep it the same.\n''')
    
        if userInput == 'Yes':
            numOfLoops = len(startingList)
    
    print 'Here is the starting list:\n', startingList[:numOfLoops], '/n'
    
    finalList = []
    x=0
    
    #TODO: need to fix the OR statement
    while x <= numOfLoops:# or len(startingList) > 0:
        
        baseURL = 'https://en.wikipedia.org'
        artistURL = startingList[0][2]
        fullURL = baseURL + artistURL
            
        try:
            actsToBeAdded = e.extractData(fullURL)
            tempList = []
            for artist in actsToBeAdded:
                newTuple = (artistURL, startingList[0][3], artist[0], artist[1])
                tempList.append(newTuple)
                
            startingList.extend(tempList)

        
        except: pass
            
        finally:
            #once a artist is removed from the working list
            #they are added to the final list
            finalList.append(startingList.pop(0))
            print 'for loop counter: ',x 
            x += 1
    
    #print listOfActs     
    return finalList