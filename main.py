#PRESIDENT JOHN KENNEDY'S SPEECH#

#open text file#
jfkspeech = open('speech.txt','r')
#save text to the variable - jfkspeech#
jfkspeech = jfkspeech.read()
#set all capital letters to lowercase#
jfkspeech = jfkspeech.lower()
#change all punctuation marks to empty space#
jfkspeech = jfkspeech.replace('.', '')
jfkspeech = jfkspeech.replace(',', '')
jfkspeech = jfkspeech.replace('"','')
jfkspeech = jfkspeech.replace('?','')
jfkspeech = jfkspeech.replace('[','')
jfkspeech = jfkspeech.replace(']','')
jfkspeech = jfkspeech.replace('!','')
jfkspeech = jfkspeech.replace(':','')
#split speech#
word = jfkspeech.split()
#create list to keep track of each word that appeares in the speech#
list_of_words = {}
#for loop to determine the repitition of words#
for item in range(len(word)):
  if word[item] in list_of_words:
    list_of_words[word[item]]+= 1
  else:
    list_of_words[word[item]] = 1
#sorts list by frequency and prints words with their frequency#
print("JFK SPEECH WORD FREQUENCY:")
print(" ")
list_of_words = dict((k, v) for k, v in list_of_words.items() if v >= 2 and len(k) >= 5)
print(list_of_words)
print(' ')

#Same concept for Leonid Brezhnev speech (24 June 1973)#

speech2 = open('lb.txt','r')
speech2 = speech2.read()
speech2 = speech2.lower()
speech2 = speech2.replace('.', '')
speech2 = speech2.replace(',', '')
speech2 = speech2.replace('"','')
speech2 = speech2.replace('?','')
speech2 = speech2.replace('[','')
speech2 = speech2.replace(']','')
speech2 = speech2.replace('!','')
speech2 = speech2.replace(':','')
speech2 = speech2.replace('$','')
word2 = speech2.split()
#create list to keep track of each word that appeared in the speech#
#lb = Leonid Brezhnev#
lb = {}
#for loop to determine the repitition of words#
for item in range(len(word2)):
  if word2[item] in lb:
    lb[word2[item]]+= 1
  else:
    lb[word2[item]] = 1
#identify words that have a frequency greater than 2 and length of words that have more than 5 letters#
lb = dict((k, v) for k, v in lb.items() if v >= 2 and len(k) >= 5)
print("LEONID BREZHNEV WORD FREQUENCY: ")
print(' ')
print(lb)
#To sort dictionary by frequency of keys#

for key, value in sorted(list_of_words.items(), key=lambda item: item[1]):
    print("%s: %s" % (key, value))
