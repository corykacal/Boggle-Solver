
import time
from splinter import Browser
import numpy as np

def wordStatus(word):
                word = word.upper()
                letter = ord(word[:1])-65

                searchLength = int(letpos[letter+1]) - int(letpos[letter])

                for x in range(int(letpos[letter]), int(letpos[letter+1])):
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



def inBounds(x,y):
        if(x>3 or x<0):
                return False
        if(y>3 or y<0):
                return False
        return True

def solve(array,visited,word,x,y):
        moves = [[0,1],[1,0],[1,1],[0,-1],[-1,0],[-1,-1],[-1,1],[1,-1]]
        isAWord = wordStatus(word)
        if(isAWord == 2):
        		return
        if(isAWord == 0):
                foundWords.append(word)
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
	visited = [[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False]]
        global foundWords
        foundWords = []
        for x in range(0,4):
                for y in range(0,4):
                        word = letterArray[x][y]
                        visited[x][y] = True
                        solve(letterArray,visited,word,x,y)
			visited[x][y] = False

def main():
        letterArray = [['E','I','J','L'],['P','R','S','V'],['X','Y','O','T'],['E','O','S','S']]
        global words 
        global letpos
        with open('dictionary.txt', 'r') as f:
                 words = [line.strip() for line in f]
	print("added dictionary to list")
        with open('letterposition.txt', 'r') as f:
                 letpos = [line.strip() for line in f]
        start = time.time()
        analyzeMatrix(letterArray)
        end = time.time()
        print("solved in: " + str(end-start))

if __name__=='__main__':
	main()
	
