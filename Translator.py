from googletrans import Translator
from tkinter import *

r=Tk()
r.title("Language convert")



def he():
	
	t=Translator()
	lan={'af': 'afrikaans', 'sq': 'albanian', 'am': 'amharic', 'ar': 'arabic', 'hy': 'armenian', 'az': 'azerbaijani', 'eu': 'basque', 'be': 'belarusian', 'bn': 'bengali', 'bs': 'bosnian', 'bg': 'bulgarian', 'ca': 'catalan', 'ceb': 'cebuano', 'ny': 'chichewa', 'zh-cn': 'chinese (simplified)', 'zh-tw': 'chinese (traditional)', 'co': 'corsican', 'hr': 'croatian', 'cs': 'czech', 'da': 'danish', 'nl': 'dutch', 'en': 'english', 'eo': 'esperanto', 'et': 'estonian', 'tl': 'filipino', 'fi': 'finnish', 'fr': 'french', 'fy': 'frisian', 'gl': 'galician', 'ka': 'georgian', 'de': 'german', 'el': 'greek', 'gu': 'gujarati', 'ht': 'haitian creole', 'ha': 'hausa', 'haw': 'hawaiian', 'iw': 'hebrew', 'hi': 'hindi', 'hmn': 'hmong', 'hu': 'hungarian', 'is': 'icelandic', 'ig': 'igbo', 'id': 'indonesian', 'ga': 'irish', 'it': 'italian', 'ja': 'japanese', 'jw': 'javanese', 'kn': 'kannada', 'kk': 'kazakh', 'km': 'khmer', 'ko': 'korean', 'ku': 'kurdish (kurmanji)', 'ky': 'kyrgyz', 'lo': 'lao', 'la': 'latin', 'lv': 'latvian', 'lt': 'lithuanian', 'lb': 'luxembourgish', 'mk': 'macedonian', 'mg': 'malagasy', 'ms': 'malay', 'ml': 'malayalam', 'mt': 'maltese', 'mi': 'maori', 'mr': 'marathi', 'mn': 'mongolian', 'my': 'myanmar (burmese)', 'ne': 'nepali', 'no': 'norwegian', 'ps': 'pashto', 'fa': 'persian', 'pl': 'polish', 'pt': 'portuguese', 'pa': 'punjabi', 'ro': 'romanian', 'ru': 'russian', 'sm': 'samoan', 'gd': 'scots gaelic', 'sr': 'serbian', 'st': 'sesotho', 'sn': 'shona', 'sd': 'sindhi', 'si': 'sinhala', 'sk': 'slovak', 'sl': 'slovenian', 'so': 'somali', 'es': 'spanish', 'su': 'sundanese', 'sw': 'swahili', 'sv': 'swedish', 'tg': 'tajik', 'ta': 'tamil', 'te': 'telugu', 'th': 'thai', 'tr': 'turkish', 'uk': 'ukrainian', 'ur': 'urdu', 'uz': 'uzbek', 'vi': 'vietnamese', 'cy': 'welsh', 'xh': 'xhosa', 'yi': 'yiddish', 'yo': 'yoruba', 'zu': 'zulu', 'fil': 'Filipino', 'he': 'Hebrew'}
	lav=dict(map(reversed,lan.items()))
	

	w=str(e.get())
	s1=str(e1.get())
	s2=str(e2.get())

	o=t.translate(w,scr=lav[s1],dest=lav[s2])


	e3.insert(0,o.text)









lab=Label(r,text="Enter the sentence")
lab.grid(row=0,column=0,pady=10)

e=Entry(r,width=70,bd=5)
e.grid(row=0,column=1,pady=10)

lab1=Label(r,text="Enter the source language")
lab1.grid(row=1,column=0,pady=10)

e1=Entry(r,width=70,bd=5)
e1.grid(row=1,column=1,pady=10)

lab2=Label(r,text="Enter the destination language")
lab2.grid(row=2,column=0,pady=10)


e2=Entry(r,width=70,bd=5)
e2.grid(row=2,column=1,pady=10)

b1=Button(r,text="Click",command=he,padx=10)
b1.grid(row=3,column=1,pady=10)

lab3=Label(r,text="The required solution")
lab3.grid(row=4,column=0,pady=10)


e3=Entry(r,width=70,bd=5)
e3.grid(row=4,column=1,pady=10)



r.grid_columnconfigure(0,weight=1)
r.grid_columnconfigure(1,weight=1)
r.grid_rowconfigure(0,weight=1)
r.grid_rowconfigure(1,weight=1)
r.grid_rowconfigure(2,weight=1)
r.grid_rowconfigure(3,weight=1)
r.grid_rowconfigure(4,weight=1)



r.mainloop()