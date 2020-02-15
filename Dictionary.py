from tkinter import *
from PyDictionary import PyDictionary

ab = Tk()
ab.geometry('400x300')
meaning=[""]
def find_Meaning():
    word=ent.get()
    dictionary= PyDictionary(word)
    meaning[] = dictionary.printMeanings()
    print(meaning[])    
        
    
ent = Entry(ab, font=("times", 17))
ent.grid(row=2,column=2)
btn = Button(ab, text = "Meaning",command=find_Meaning)
btn.grid(row=4,column=2)
labelMeaning = Label(ab,text=meaning[]).grid(row=5, column=0)

ab.mainloop()
