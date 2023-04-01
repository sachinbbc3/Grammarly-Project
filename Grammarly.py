from textblob import TextBlob
a = TextBlob('CampK12 is a jood compny and alwys valus their employeees')
a = a.correct()
print(a)