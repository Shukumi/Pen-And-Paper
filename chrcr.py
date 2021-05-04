from tkinter import *
import os
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import shelve
# -*- coding: iso-8859-15 -*- 
from random import choices

a= { 1 : 1, 2:1, 3:1, 4:1, 5:1,6:1,7:1,8:1,9:1,10:1,11:1,12:1,13:2,14:3,15:4,16:5,17:6,18:7,19:8,20:9,21:10,22:11,23:12,24:13,25:14}
b = { 1 :2, 2:2, 3:2, 4:2, 5:2, 6:2, 7:2, 8:2, 9:2, 10:2, 11:2, 12:2, 13:4, 14:6, 15:8, 16:10, 17:12, 18:14, 19:16, 20:18, 21:20, 22:22, 23:24, 24:26, 25:28}
c = { 1 :3, 2:3, 3:3, 4:3, 5:3, 6:3, 7:3, 8:3, 9:3, 10:3, 11:3, 12:3, 13:6, 14:9, 15:12, 16:15, 17:18, 18:21, 19:24, 20:27, 21:30, 22:33, 23:36, 24:39, 25:42}
d = { 1:4, 2:4, 3:4, 4:4, 5:4, 6:4, 7:4, 8:4, 9:4, 10:4, 11:4, 12:4, 13:8, 14:12, 15:16, 16:20, 17:24, 18:28, 19:32, 20:36, 21:40, 22:44, 23:48, 24:52, 25:56}

bla = 0
root = Tk()
root.title("Charaktererstellung")
Label(root, text ="Attribute", font = "Verdana 12 italic bold").grid(row=0,column=0)
Label(root, text ="Kampfkünste", font = "Verdana 12 italic bold").grid(row=0,column=2)

	
Label(root, text="Körperkraft").grid(row=1)
Label(root, text="Konstitution").grid(row=2)
Label(root, text="Klugheit").grid(row=3)
Label(root, text="Intuition").grid(row=4)
Label(root, text="Geschicklichkeit").grid(row=5)
Label(root, text="Charisma").grid(row=6)
Label(root, text ="Körperliche Talente", font = "Verdana 12 italic bold").grid(row=0,column=4)
# KörperlicheTalente
Label(root, text="Klettern").grid(row=1,column=4)
Label(root, text="Werfen").grid(row=2,column=4)
Label(root, text="Verbergen").grid(row=3,column=4)
Label(root, text="Schwimmen").grid(row=4,column=4)
Label(root, text="Sinnesschärfe").grid(row=5,column=4)
Label(root, text="Zechen").grid(row=6,column=4)

e15 = Entry(root)
e15.grid(row=1, column=5)
e15.insert(END, '0')
e16 = Entry(root)
e16.grid(row=2, column=5)
e16.insert(END, '0')
e17 = Entry(root)
e17.grid(row=3, column=5)
e17.insert(END, '0')
e18 = Entry(root)
e18.grid(row=4, column=5)
e18.insert(END, '0')
e19 = Entry(root)
e19.grid(row=5, column=5)
e19.insert(END, '0')
e20 = Entry(root)
e20.grid(row=6, column=5) 
e20.insert(END, '0')
# Wissenstalente @@@@@@@@@@@@@@@@@@@@@

Label(root, text ="Wissenstalente", font = "Verdana 12 italic bold").grid(row=9,column=0)

Label(root, text="Medizin").grid(row=10,column=0)
Label(root, text="Magiekunde").grid(row=11,column=0)
Label(root, text="Urbanes Wissen").grid(row=12,column=0)
Label(root, text="Rechtskunde").grid(row=13,column=0)
Label(root, text="Glücksspiel").grid(row=14,column=0)
Label(root, text="Willenskraft").grid(row=15,column=0)

e21 = Entry(root)
e21.grid(row=10, column=1)
e21.insert(END, '0')
e22 = Entry(root)
e22.grid(row=11, column=1)
e22.insert(END, '0')
e23 = Entry(root)
e23.grid(row=12, column=1)
e23.insert(END, '0')
e24 = Entry(root)
e24.grid(row=13, column=1)
e24.insert(END, '0')
e25 = Entry(root)
e25.grid(row=14, column=1)
e25.insert(END, '0')
e26 = Entry(root)
e26.grid(row=15, column=1) 
e26.insert(END, '0')

# Soziale Talente @@@@@@@@@@@@@@@@@@@@@

Label(root, text ="Soziale Talente", font = "Verdana 12 italic bold").grid(row=9,column=2)

Label(root, text="Menschenkenntnis").grid(row=10,column=2)
Label(root, text="Überzeugen").grid(row=11,column=2)
Label(root, text="Gassenwissen").grid(row=12,column=2)
Label(root, text="Beruhigen").grid(row=13,column=2)
Label(root, text="Feilschen").grid(row=14,column=2)
Label(root, text="Etikette").grid(row=15,column=2)

e27 = Entry(root)
e27.grid(row=10, column=3)
e27.insert(END, '0')
e28 = Entry(root)
e28.grid(row=11, column=3)
e28.insert(END, '0')
e29 = Entry(root)
e29.grid(row=12, column=3)
e29.insert(END, '0')
e30 = Entry(root)
e30.grid(row=13, column=3)
e30.insert(END, '0')
e31 = Entry(root)
e31.grid(row=14, column=3)
e31.insert(END, '0')
e32 = Entry(root)
e32.grid(row=15, column=3) 
e32.insert(END, '0')


# Handwerkliche Talente @@@@@@@@@@@@@@@@@@@@@

Label(root, text ="Handwerkliche Talente", font = "Verdana 12 italic bold").grid(row=9,column=4)

Label(root, text="Alchemie").grid(row=10,column=4)
Label(root, text="Spuren lesen").grid(row=11,column=4)
Label(root, text="Schlösser knacken").grid(row=12,column=4)
Label(root, text="Kochen").grid(row=13,column=4)
Label(root, text="Wildnis Leben").grid(row=14,column=4)
Label(root, text="Angeln").grid(row=15,column=4)

e33 = Entry(root)
e33.grid(row=10, column=5)
e33.insert(END, '0')
e34 = Entry(root)
e34.grid(row=11, column=5)
e34.insert(END, '0')
e35 = Entry(root)
e35.grid(row=12, column=5)
e35.insert(END, '0')
e36 = Entry(root)
e36.grid(row=13, column=5)
e36.insert(END, '0')
e37 = Entry(root)
e37.grid(row=14, column=5)
e37.insert(END, '0')
e38 = Entry(root)
e38.grid(row=15, column=5) 
e38.insert(END, '0')


#Attribute
e1 = Entry(root)
e1.grid(row=1, column=1)
e1.insert(END, '8')
e2 = Entry(root)
e2.grid(row=2, column=1)
e2.insert(END, '8')
e3 = Entry(root)
e3.grid(row=3, column=1)
e3.insert(END, '8')
e4 = Entry(root)
e4.grid(row=4, column=1)
e4.insert(END, '8')
e5 = Entry(root)
e5.grid(row=5, column=1)
e5.insert(END, '8')
e6 = Entry(root)
e6.grid(row=6, column=1) 
e6.insert(END, '8')


#Kampfkünste
Label(root, text="Armbrüste").grid(row=1,column=2)
Label(root, text="Bögen").grid(row=2,column=2)
Label(root, text="Dolche").grid(row=3,column=2)
Label(root, text="Schwerter").grid(row=4,column=2)
Label(root, text="Hiebwaffen(Axt/Hammer)").grid(row=5,column=2)
Label(root, text="Schilde").grid(row=6,column=2)
Label(root, text="Wurfwaffen").grid(row=7,column=2)
Label(root, text="Martial Arts").grid(row=8,column=2)
e7 = Entry(root)
e7.grid(row=1, column=3)
e7.insert(END, '6')
e8 = Entry(root)
e8.grid(row=2, column=3)
e8.insert(END, '6')
e9 = Entry(root)
e9.grid(row=3, column=3)
e9.insert(END, '6')
e10 = Entry(root)
e10.grid(row=4, column=3)
e10.insert(END, '6')
e11 = Entry(root)
e11.grid(row=5, column=3)
e11.insert(END, '6')
e12 = Entry(root)
e12.grid(row=6, column=3) 
e12.insert(END, '6')
e13 = Entry(root)
e13.grid(row=7, column=3)
e13.insert(END, '6')
e14 = Entry(root)
e14.grid(row=8, column=3) 
e14.insert(END, '6')


def Punkte ():
	global bla
	bla = 0
	bla += int(e1.get()) -8
	bla += int(e2.get()) -8
	bla += int(e3.get()) -8
	bla += int(e4.get()) -8
	bla += int(e5.get()) -8
	bla += int(e6.get()) -8
	return bla*20
	
def Punkte2 ():
	global bla
	bla = 0
	for i in range (6,int(e7.get())):
		try:
			bla += b[i+1]
		except KeyError:
			bla +=0
	for i in range (6,int(e8.get())):
		try:
			bla += c[i+1]
		except KeyError:
			bla +=0
	for i in range (6,int(e9.get())):
		try:
			bla += b[i+1]
		except KeyError:
			bla +=0
	for i in range (6,int(e10.get())):
		try:
			bla += c[i+1]
		except KeyError:
			bla +=0	
	for i in range (6,int(e11.get())):
		try:
			bla += c[i+1]
		except KeyError:
			bla +=0	
	for i in range (6,int(e12.get())):
		try:
			bla += c[i+1]
		except KeyError:
			bla +=0	
	for i in range (6,int(e13.get())):
		try:
			bla += b[i+1]
		except KeyError:
			bla +=0
	for i in range (6,int(e14.get())):
		try:
			bla += b[i+1]
		except KeyError:
			bla +=0
	return bla
	
def Punkte3 ():
#Körperliche Talente
	global bla
	bla = 0
	for i in range (0,int(e15.get())):
		try:
			bla += b[i+1]
		except KeyError:
			bla +=0
	for i in range (0,int(e16.get())):
		try:
			bla += b[i+1]
		except KeyError:
			bla +=0
	for i in range (0,int(e17.get())):
		try:
			bla += c[i+1]
		except KeyError:
			bla +=0
	for i in range (0,int(e18.get())):
		try:
			bla += b[i+1]
		except KeyError:
			bla +=0	
	for i in range (0,int(e19.get())):
		try:
			bla += d[i+1]
		except KeyError:
			bla +=0	
	for i in range (0,int(e20.get())):
		try:
			bla += a[i+1]
		except KeyError:
			bla +=0	
	return bla
	
def Punkte4 ():
#Wissenstalente
	global bla
	bla = 0
	for i in range (0,int(e21.get())):
		try:
			bla += c[i+1]
		except KeyError:
			bla +=0
	for i in range (0,int(e22.get())):
		try:
			bla += c[i+1]
		except KeyError:
			bla +=0
	for i in range (0,int(e23.get())):
		try:
			bla += b[i+1]
		except KeyError:
			bla +=0
	for i in range (0,int(e24.get())):
		try:
			bla += a[i+1]
		except KeyError:
			bla +=0	
	for i in range (0,int(e25.get())):
		try:
			bla += a[i+1]
		except KeyError:
			bla +=0	
	for i in range (0,int(e26.get())):
		try:
			bla += d[i+1]
		except KeyError:
			bla +=0	
	return bla

def Punkte5 ():


#Soziale Talente
	global bla
	bla = 0
	for i in range (0,int(e27.get())):
		try:
			bla += c[i+1]
		except KeyError:
			bla +=0
	for i in range (0,int(e28.get())):
		try:
			bla += b[i+1]
		except KeyError:
			bla +=0
	for i in range (0,int(e29.get())):
		try:
			bla += c[i+1]
		except KeyError:
			bla +=0
	for i in range (0,int(e30.get())):
		try:
			bla += c[i+1]
		except KeyError:
			bla +=0	
	for i in range (0,int(e31.get())):
		try:
			bla += b[i+1]
		except KeyError:
			bla +=0	
	for i in range (0,int(e32.get())):
		try:
			bla += b[i+1]
		except KeyError:
			bla +=0	
	return bla	

def Punkte6 ():
#Handwerkliche Talente
	global bla
	bla = 0
	for i in range (0,int(e33.get())):
		try:
			bla += c[i+1]
		except KeyError:
			bla +=0
	for i in range (0,int(e34.get())):
		try:
			bla += c[i+1]
		except KeyError:
			bla +=0
	for i in range (0,int(e35.get())):
		try:
			bla += c[i+1]
		except KeyError:
			bla +=0
	for i in range (0,int(e36.get())):
		try:
			bla += a[i+1]
		except KeyError:
			bla +=0	
	for i in range (0,int(e37.get())):
		try:
			bla += c[i+1]
		except KeyError:
			bla +=0	
	for i in range (0,int(e38.get())):
		try:
			bla += a[i+1]
		except KeyError:
			bla +=0	
	return bla		
	
	
def counter_label(label):
	def count():
		try:
			label.config(text="Punkte, die durch Attributsverbesserungen verbraucht wurden :" + str(Punkte()))
			label.after(200, count)
		except ValueError:
			#label.config(text='ZahlenPLS')
			label.after(200,count)
	count()
def counter_label2(label):
	def count():
		try:
			label.config(text="Punkte, die durch Kampfkünste verbraucht wurden :" + str(Punkte2()))
			label.after(200, count)
		except ValueError:
			#label.config(text='ZahlenPLS')
			label.after(200,count)
	count()	
def counter_label3(label):
	def count():
		try:
			label.config(text="Punkte, die durch Körperliche Talente verbraucht wurden :" + str(Punkte3()))
			label.after(200, count)
		except ValueError:
			#label.config(text='ZahlenPLS')
			label.after(200,count)
	count()	
	
def counter_label4(label):
	def count():
		try:
			label.config(text="Punkte, die durch Wissenstalente verbraucht wurden :" + str(Punkte4()))
			label.after(200, count)
		except ValueError:
			#label.config(text='ZahlenPLS')
			label.after(200,count)
	count()	
	
def counter_label5(label):
	def count():
		try:
			label.config(text="Punkte, die durch Soziale Talente verbraucht wurden :" + str(Punkte5()))
			label.after(200, count)
		except ValueError:
			#label.config(text='ZahlenPLS')
			label.after(200,count)
	count()	 
	
def counter_label6(label):
	def count():
		try:
			label.config(text="Punkte, die durch Handwerkliche Talente verbraucht wurden :" + str(Punkte6()))
			label.after(200, count)
		except ValueError:
			#label.config(text='ZahlenPLS')
			label.after(200,count)
	count()	

def counter_label7(label):
	def count():
		try:
			test= 400 - int(e49.get()) + int(e50.get())
			if (Punkte() + Punkte2() + Punkte3() + Punkte4() + Punkte5() + Punkte6() <= test):
				label.config(text="Ingesamt verbrauchte Punkte :" + str(Punkte() + Punkte2() + Punkte3() + Punkte4() + Punkte5() + Punkte6()), fg="green")
				label.after(200, count)
			else:
				label.config(text="Ingesamt verbrauchte Punkte :" + str(Punkte() + Punkte2() + Punkte3() + Punkte4() + Punkte5() + Punkte6()), fg="red")
				label.after(200, count)			
		except ValueError:
			#label.config(text='ZahlenPLS')
			label.after(200,count)
	count()	
	
LabelEnde = Label(root)
LabelEnde.grid(row=7)
counter_label(LabelEnde)
LabelEndeKK = Label(root)
LabelEndeKK.grid(row=8)
counter_label2(LabelEndeKK)
LabelEndeKöTa = Label(root)
LabelEndeKöTa.grid(row=7,column=4)
counter_label3(LabelEndeKöTa)
LabelEndeWiTa = Label(root)
LabelEndeWiTa.grid(row=16,column=0)
counter_label4(LabelEndeWiTa)
LabelEndeSoTa = Label(root)
LabelEndeSoTa.grid(row=16,column=2)
counter_label5(LabelEndeSoTa)
LabelEndeHaTa = Label(root)
LabelEndeHaTa.grid(row=16,column=4)
counter_label6(LabelEndeHaTa)
LabelVor = Label(root, text="Punkteverlust Vorteile").grid(row=17,column=1)
LabelVor = Label(root, text="Punktegewinn Nachteile").grid(row=18,column=1)
e49 = Entry(root)
e49.grid(row=17,column=2)
e49.insert(END, '0')
e50 = Entry(root)
e50.grid(row=18,column=2)
e50.insert(END, '0')
LabelEndeZus = Label(root,text="Lul")
LabelEndeZus.grid(row=19,column=2)
counter_label7(LabelEndeZus)
root.mainloop()