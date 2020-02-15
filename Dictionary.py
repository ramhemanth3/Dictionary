from tkinter import *
from PyDictionary import PyDictionary

ab = Tk()
ab.geometry('400x300')
meaning=""
def find_Meaning():
    word=ent.get()
    dictionary= PyDictionary(word)
    meaning = str( dictionary.printMeanings())
    print(meaning)    

def find_Synonym():
    word=ent.get()
    print("Synonym is ")
    dictionary= PyDictionary(word)
    print(dictionary.synonym(word))

def find_Antonym():
    word=ent.get()
    print("Antonym is ")
    dictionary= PyDictionary(word)
    print(dictionary.antonym(word))    
        
    
ent = Entry(ab, font=("times", 17))
ent.grid(row=2,column=2)
btn = Button(ab, text = "Meaning",command=find_Meaning)
btn.grid(row=4,column=1)
btn2 = Button(ab, text = "Synonym",command=find_Synonym)
btn2.grid(row=4,column=2)
btn3 = Button(ab, text = "Antonym",command=find_Antonym)
btn3.grid(row=4,column=3)
labelMeaning = Label(ab,text=meaning).grid(row=5, column=0)

ab.mainloop()
