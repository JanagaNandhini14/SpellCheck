from textblob import TextBlob


word = input("Enter a word: ")
blob = TextBlob(word)
print("Corrected word:", blob.correct())
