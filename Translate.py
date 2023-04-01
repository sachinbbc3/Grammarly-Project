from textblob import TextBlob
blob = TextBlob("Comment vas-tu? ") #French

print(blob.detect_language())
print(blob.translate(to= 'es')) #Spanish
print(blob.translate(to= 'en')) #English
print(blob.translate(to= 'zh')) #Chinese