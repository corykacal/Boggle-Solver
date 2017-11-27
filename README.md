# Solving Boggle

While the code is original and all my own, the idea is not. I saw a video onces of code solving the online boggle game, word twist, but I could not find the source code. So I deicded to recreate it myself.

I first used a linear system to search through the dictionary and decide if it was a word but then I made my own Trie data structure.

The Trie data structure speeds up the code from 6-11 seconds to thousandths of a second. It is very fast becuase it is O(M) where M is the length of the longest word.

Below is an example of my code in action. It first adds all words to a list and then turns the words into a big Trie. After this is done the board is solved in a fraction of a second and then the words are entered into the game.

![Alt Text](https://github.com/corykacal/Boggle-Solver/blob/master/solving.gif?raw=true)

These are the results. You can see that 74 out of 74 possible words were found and entered.

![Alt Text](https://github.com/corykacal/Boggle-Solver/blob/master/results.png?raw=true)
