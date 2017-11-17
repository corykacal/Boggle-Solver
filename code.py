
import time
from splinter import Browser
import numpy as np

def wordStatus(word):
        if(word not in foundWords):
                word = word.upper()
                letter = ord(word[:1])-65

                searchLength = int(letpos[letter+1]) - int(letpos[letter])

                for x in range(int(letpos[letter]), int(letpos[letter+1])) :
                        currentWord = words[x]
                        if(currentWord.startswith(word)):
                                if(currentWord==word):
                                        #is a word
                                        if(len(word)<3):
                                                return 1
                                        return 0
                                else:
                                        #almost a word
                                        return 1

                #not a word
                return 2


def enterWord(word):
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
        #print("solving " + str(word))
        isAWord = wordStatus(word)
        if(isAWord == 2):
                return
        if(isAWord == 0):
                foundWords.append(word)
                enterWord(word)
        if(isAWord==1 or isAWord==0):
                for i in moves:
                        newX = x+i[0]
                        newY = y+i[1]
                        if(inBounds(newX,newY) and not visited[newX][newY]):
                                visited[newX][newY] = True
                                newWord = word + array[newX][newY]
                                solve(array,visited,newWord,newX,newY)
                                visited[newX][newY] = False

def analyzeMatrix(letterArray):
        global textBox
        textBox = browser.find_by_name("word")
        global enterBox
        enterBox = browser.find_by_xpath('//*[@id="submitit"]')
        global foundWords
        foundWords = []
        for x in range(0,4):
                for y in range(0,4):
                        #print(letterArray[x,y])
                        word = letterArray[x][y]
                        visited = [[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False]]
                        visited[x][y] = True
                        solve(letterArray,visited,word,x,y)
                #print("\n")

with Browser() as browser:
        #Visit URL
        url = 'http://www.wordtwist.org/'
        browser.visit(url+'init.php')
        username = 'haxorman'
        password = 'lotus911'
        #Find and click the 'search' button
        browser.find_by_name('vb_login_username').fill(username)
        browser.find_by_name('vb_login_password').fill(password)
        browser.find_by_value('Log In').click()
        time.sleep(3)
        browser.visit('http://www.wordtwist.org/init4.php')
        browser.find_by_xpath('/html/body/div[2]/div[4]/div[1]/div/p[4]/a').click()
        letterArray = [['A' for row in range(0,4)] for col in range(0,4)]
        boxNum=17
        for x in range(0, 4):
                for y in range(0, 4):
                        letterArray[x][y] = browser.find_by_id('box'+str(boxNum)).text
                        boxNum+=1
        global words 
        global letpos
        with open('dictionary.txt', 'r') as f:
                 words = [line.strip() for line in f]

        with open('letterposition.txt', 'r') as f:
                 letpos = [line.strip() for line in f]

        analyzeMatrix(letterArray)
        time.sleep(120)









        