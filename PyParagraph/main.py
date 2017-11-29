import re

average = []
count = 0 
Average_sentence = 0 
Average_sentence2 = 0 


f = open('LanguageHM.txt', 'r', encoding = 'latin1')
message = f.read()

#print("The document contains this text: ")
#print(message)

# Split the text just by space delimiter 
#words = message.split(" ")
# Split the text by space, commas, full stop.
words = re.split("\W+", message) 
#print(words)
#print(len(words))

#loop to go throgh each word in the text 
for i in words:
    letter_count = len(i) 
    #print(letter_count)
    average.append(letter_count)
    #print(letter_count)


#print(words)
#print("The number of words is: ")
#print(len(words))

# Split the paragraph by "." to get the number of sentences
sentences = message.split(".")
# Excluding "/n/n"
sentences =  sentences[:-1]
#print(sentences)
for sentence in sentences:
    
    words2 = sentence.split(" ")
    #print(words)
    Average_sentence = len(words2)
    #print(Average_sentence)
    Average_sentence2 += len(words2)

#print(Average_sentence2)
Average_sentenceCount = Average_sentence2 / (len(sentences))

#print (Average_sentenceCount)


Averageletter = sum(average)/len(words)
print("Paragraph Analysis")
print("-------------------")
print("Approximate Word Count: ", (len(words)))
print("Approximte Sencences Count: ", (len(sentences)))
print("Average Letter Count: ", Averageletter)
print("Average Sentence Lenght: ", Average_sentenceCount)
