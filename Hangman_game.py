import random
from replit import clear
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
word_list = ["aravind","harikrishna","vashist","shashi","vikram","niharika","vipul","kartikeya","kranthi","nikhil","sowmya","srikar","vinay","nikhila","koushik","anjali","preetham","poojitha","hethal","deepika","priyanka","akanksha","navya","vivek","praveen","chandu","saiteja","sourabh","vineeth","shiva","navneeth","shivani","renuka","sripriya","prashanth","srikanth","srinath","meghana","manideep","manisha","ganesh"]
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
print(logo)
print("Guess your friend's name letter by letter")
choosen_word = random.choice(word_list)
length = len(choosen_word)
guess_word = ['_']*length
wrong = 6
exclude_letters = []
temp_word = list(choosen_word)
while(wrong > 0):
  letter=input("Guess a Letter: ").lower()
  clear()
  if letter not in exclude_letters:
    exclude_letters.append(letter)
  else:
    print(f"You have already chosen this letter: {letter}\n----------life's left {wrong}----------")
    print(stages[wrong])    
    solution = ' '.join([str(elem) for elem in guess_word])    
    print(solution+"\n")
    continue  
  lst = []
  if letter in choosen_word:
    for i in range(0,len(choosen_word)):
      if choosen_word[i] == letter:
        lst.append(int(i))
    for i in range(0,len(temp_word)):
      if temp_word[i] == letter:
        guess_word[i]=letter
    solution = ' '.join([str(elem) for elem in guess_word])
    print(f"----------life's left {wrong}----------")
    print(stages[wrong])    
    print(solution+"\n")    
    choosen_word=choosen_word.replace(choosen_word[lst[0]],'')  
  else:
    wrong-=1
    print(f"You chose a letter that is not in the Name\n----------life's left {wrong}----------")
    solution = ' '.join([str(elem) for elem in guess_word])
    print(stages[wrong])    
    print(solution+"\n")         

  if len(choosen_word) == 0:
    print("---YOU GUESSED IT RIGHT! YOU WON!!---")  
    break    
  else:    
    if wrong == 0:      
      answer = ''.join([str(elem) for elem in temp_word])
      print(f"---YOU FAILED TO GUESS '{answer.upper()}'---")
      print("----------Game Over---------")
        
  