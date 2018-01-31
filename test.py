from trie import Trie

meme = Trie()

meme.add("WEW")
meme.add("AMA")
meme.add("AMAS")
meme.add("ANIMAL")

print(meme.wordStatus("AMAS")) #3 end and word
print(meme.wordStatus("AMA")) #2 word but not end
print(meme.wordStatus("AM")) #1 almost word
print(meme.wordStatus("AMZ")) #0 dead end
print(meme.wordStatus("Z")) #0
print(meme.wordStatus("WEW")) #3
print(meme.wordStatus("ANIMA"))

