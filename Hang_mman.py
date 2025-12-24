import random
word_list=["hello","python","ducks","techscap"]
secret_word=random.choice(word_list)

def start():
    tries=5
    print("word list (hello   python   ducks  techscap)")
    print("guess the word from above list! ")
    while tries>0:
         try:
             A=str(input("guess the word ").lower()) # I think usage of try except is useless here! but it also not effects our code

             if A==secret_word:
                print("Congrats you guessed the word!")
                break
             if A!=secret_word:
                print("try again")
                tries-=1
                print("you have",tries,"tries remaining ")
                if tries==0:
                    print("opps! game over: ")
                    print("The secret word was",secret_word)
         except ValueError:
             print("please enter appropriate values")

print("Welcome to word guess game! ")
while True:
    a=int(input("To continue enter '1' to exit enter '2' "))
    print(a)
    if a==1:
        start()
    else:
        if a==2:
            break



          
      
