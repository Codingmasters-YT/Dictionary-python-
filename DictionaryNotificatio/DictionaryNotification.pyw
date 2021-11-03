from plyer import notification
import time
import random
from PyDictionary import PyDictionary
import winsound

dictionary = PyDictionary()

file = open("words.txt")
words = file.read().split("\n")


def get_word():
    valid_word = False
    while(not valid_word):
        index = random.randint(0,466551)
        word = words[index]

        if(word[0].islower() and len(word)>2):
            valid_word = True
            return word

def define_word():
    valid_word = False
    while(not valid_word):
        word = get_word()
        if(dictionary.meaning(word, disable_errors=True)):
            wordname = word.upper()+ "\n"
            defs = dictionary.meaning(word)
            for key,value in defs.items():
                finalword = wordname + str(key)+": "+str(value).strip("[]\'\"").replace("\'","")
                valid_word = True

    return finalword
#         # syns = dictionary.synonym(word)
#         # if syns:
#         #     s = ""
#         #     for syn in syns:
#         #         s+=syn+", "
#         #         print("Synonyms: "+s[:-2]+"\n")
#         # ants = dictionary.antonym(word)
#         # if ants:
#         #     a = ""
#         #     for ant in ants:
#         #         a+=ant+", "
#         #         print("Antonyms: "+a[:-2])



def notifyMe(title, message):
    notification.notify(
    title = title,
    message = message,
    app_icon = "image.ico",
    timeout = 20
    )


if __name__ == '__main__':
    while True:
        notifyMe("Here is a word for you!!", define_word())
        time.sleep(3600)
