
import time
from splinter import Browser
import numpy as np
from Trie import Trie

def wordStatus(word):
        return words.wordStatus(word)


def enterWords():
        for word in foundWords:
                textBox.fill(word)
                enterBox.click()


def inBounds(x,y):
        if(x>3 or x<0):
                return False
        if(y>3 or y<0):
                return False
        return True

def solve(array,visited,word,x,y):
        moves = [[0,1],[1,0],[1,1],[0,-1],[-1,0],[-1,-1],[-1,1],[1,-1]]
        isAWord = wordStatus(word)
        if(isAWord == 0):
                return
        if(isAWord == 3):
                if word not in foundWords:
                    foundWords.append(word)
                return
        if(isAWord==2):
                if word not in foundWords:
                    foundWords.append(word)
        if(isAWord==1 or isAWord==2):
                for i in moves:
                        newX = x+i[0]
                        newY = y+i[1]
                        if(inBounds(newX,newY) and not visited[newX][newY]):
                                visited[newX][newY] = True
                                newWord = word + array[newX][newY]
                                solve(array,visited,newWord,newX,newY)
                                visited[newX][newY] = False

def analyzeMatrix(letterArray):
        visited = [[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False]]
        global textBox
        global foundWords
        foundWords = []
        textBox = browser.find_by_name("word")
        global enterBox
        enterBox = browser.find_by_xpath('//*[@id="submitit"]')
        for x in range(0,4):
                for y in range(0,4):
                        word = letterArray[x][y]
                        visited[x][y] = True
                        solve(letterArray,visited,word,x,y)
			visited[x][y] = False



def addToTrie(wordslin):
    result = Trie()
    for word in wordslin:
        result.add(word)
    return result


with Browser() as browser:
    #Visit URL
    #url = 'http://www.wordtwist.org/'
    #browser.visit(url+'init.php')
    #username = ''
    #password = ''
    #Find and click the 'search' button
    #browser.find_by_name('vb_login_username').fill(username)
    #browser.find_by_name('vb_login_password').fill(password)
    #browser.find_by_value('Log In').click()
    #time.sleep(3)
    browser.visit('http://www.wordtwist.org/init4.php')
    browser.find_by_xpath('/html/body/div[2]/div[4]/div[1]/div/p[4]/a').click()
    letterArray = [['A' for row in range(0,4)] for col in range(0,4)]
    boxNum=17
    for x in range(0, 4):
            for y in range(0, 4):
                    letterArray[x][y] = browser.find_by_id('box'+str(boxNum)).text
                    boxNum+=1
    with open('dictionary.txt', 'r') as f:
             wordslin = [line.strip() for line in f]

    global words
    words = addToTrie(wordslin)
    start = time.time()
    analyzeMatrix(letterArray)
    end = time.time()
    change = end-start
    enterWords()
	








        
