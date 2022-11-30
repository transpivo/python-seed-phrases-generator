from random import randrange


phrase = []
c = input('How many lines you need: ')
count_words = input('how many words are in a phrase?(12,24 ...): ')
count_words = int(count_words)
c = int(c)
file = open('words.txt','w')
def generation():
    f = open('en_words.txt')
    words = f.read().split()

    count = count_words
    

    phrase = []
    seed = 0
    while seed !=count:
        seed +=1
        phrase.append(words[randrange(len(words))])
    phrase = ' '.join(phrase)
    file.write(phrase + '\n')
def count():
    a = 0
    while a != c:
        generation()
        a+=1
        print('generation...')
    if a==c:
        print('Finished generation')
count()
print('Check words.txt =)')
print('You can check these phrases on iancoleman and find out the address and through a script that finds out the balance of the BTC address')

