from tkinter import *
import os
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import shelve
# -*- coding: iso-8859-15 -*- 
from random import choices

bla =""	
root = Tk()
rlist = []
iteml = []
inventories=[[],[],[],[]]
zwischenspeicher = shelve.open('penpaps')
if 'chars' in zwischenspeicher:
	Charaktere = zwischenspeicher['chars']
else:
	Charaktere = []

	
for i in range(0,4):
	if 'inv' + str(i) in zwischenspeicher:
		inventories[i] = zwischenspeicher['inv' + str(i)]
	else:
		inventories[i] = []

	
root.title("Pen & Paper")
Label(root, 
		 text="Willkommen!",
		 fg = "light blue",
		 bg = "dark blue",
		 font = "Verdana 12 italic").grid(row=0,column=2)
Label(root, text="Füge Charaktere hinzu: ").grid(row=1)

e1 = Entry(root)
e1.grid(row=1, column=1)		 
def addchar():
	Charaktere.append(e1.get())
	zwischenspeicher['chars'] = Charaktere
	e1.delete(0, 'end')
	
def ran_item():
	global iteml
	global rlist
	tier1= open("t1it.txt","r")
	for e in tier1:
		iteml.append(e.rstrip())
	for ix in range(1,int(e1.get())+1):
		rlist.append(choices(iteml))
	messagebox.showinfo("Du hast Item(s) erhalten",rlist)
	iteml= []
	e1.delete(0,'end')
	rlist = []	
	tier1.close()

def ran_item2():
	global iteml
	global rlist
	tier2= open("t2it.txt","r")
	for e in tier2:
		iteml.append(e.rstrip())
	for ix in range(1,int(e1.get())+1):
		rlist.append(choices(iteml))
	messagebox.showinfo("Du hast Item(s) erhalten",rlist)	
	iteml= []
	e1.delete(0,'end')
	rlist = []	
	tier2.close()

def ran_item3():
	global iteml
	global rlist
	tier3= open("t3it.txt","r")
	for e in tier3:
		iteml.append(e.rstrip())
	for ix in range(1,int(e1.get())+1):
		rlist.append(choices(iteml))
	messagebox.showinfo("Du hast Item(s) erhalten",rlist)
	iteml= []
	e1.delete(0,'end')
	rlist = []
	tier3.close()	
	
button = Button(root, text='Erstellen!', width=12, command = addchar).grid(row=2,column=1)
button = Button(root, text="T1-Zufallsitem", width=12, command = ran_item).grid(row=1,column=2)
button = Button(root, text="T2-Zufallsitem", width=12, command = ran_item2).grid(row=1,column=3)
button = Button(root, text="T3-Zufallsitem", width=12, command = ran_item3).grid(row=1,column=4)
def counter_label(label,charnr):
	def count():
		try:
			label.config(text="Charakter " + str(charnr+1) + ":   " + Charaktere[charnr])
		except IndexError:
			label.config(text="Charakter " + str(charnr+1) + ":   " + "")
		label.after(200, count)
	count()

def counter_label3(label,charnr):
	def count():
		try:
			label.config(text="Charakter " + str(charnr+1) + ":   " + Charaktere[charnr])
		except IndexError:
			label.config(text="Charakter " + str(charnr+1) + ":   " )
		label.after(200, count)
	count()

def counter_labell(label,charnr):
	def count():
		label.config(text="Das Inventar beinhaltet: " + str(inventories[charnr]))
		label.after(200, count)
	count()
	
def add_inv(troll):
	if troll ==0:
		inventories[troll].append(e2.get())
		zwischenspeicher['inv' + str(troll)] = inventories[troll]
		e2.delete(0, 'end')
	elif troll ==1:
		inventories[troll].append(e3.get())
		zwischenspeicher['inv' + str(troll)] = inventories[troll]
		e3.delete(0, 'end')
	elif troll ==2:
		inventories[troll].append(e4.get())
		zwischenspeicher['inv' + str(troll)] = inventories[troll]
		e4.delete(0, 'end')
	elif troll ==3:
		inventories[troll].append(e5.get())
		zwischenspeicher['inv' + str(troll)] = inventories[troll]
		e5.delete(0, 'end')
		
def del_inv(troll):
	if troll ==0:
		lösch = e2.get()
		inventories[troll].remove(lösch)
		zwischenspeicher['inv' + str(troll)] = inventories[troll]
		e2.delete(0, 'end')	
	if troll ==1:
		lösch = e3.get()
		inventories[troll].remove(lösch)
		zwischenspeicher['inv' + str(troll)] = inventories[troll]
		e3.delete(0, 'end')	
	if troll ==2:
		lösch = e4.get()
		inventories[troll].remove(lösch)
		zwischenspeicher['inv' + str(troll)] = inventories[troll]
		e4.delete(0, 'end')	
	if troll ==3:
		lösch = e5.get()
		inventories[troll].remove(lösch)
		zwischenspeicher['inv' + str(troll)] = inventories[troll]
		e5.delete(0, 'end')	
e2 = Entry(root)
e2.grid(row=3,column=2)
e3 = Entry(root)
e3.grid(row=4,column=2)
e4 = Entry(root)
e4.grid(row=5,column=2)
e5 = Entry(root)
e5.grid(row=6,column=2)
for i in range (0,4):
	label = Label(root, fg="blue")
	label.grid(row=i+3)
	counter_label(label,i)
	label2 = Label(root,fg="red")
	label2.grid(row=i+3,column=1)
	counter_labell(label2,i)
	button2 = Button(root, text='Hinzufügen!', width=12, command = lambda i=i: add_inv(i)).grid(row=i+3,column=3)	
	button3 = Button(root, text='Entferne!', width=12, command = lambda i=i: del_inv(i)).grid(row=i+3,column=4)	


def del_all():
	global Charaktere
	if messagebox.askyesno('Bestätige', 'Möchtest du wirklich ALLES löschen?'):
		try:
			del zwischenspeicher["chars"]
		except KeyError:
			pass
		try:
			del zwischenspeicher["inv0"]
		except KeyError:
			pass
		try:
			del zwischenspeicher["inv1"]
		except KeyError:
			pass
		try:
			del zwischenspeicher["inv2"]
		except KeyError:
			pass
		try:
			del zwischenspeicher["inv3"]
		except KeyError:
			pass
		for i in range(0,4):
			inventories[i] = []
		Charaktere = []
		for i in range (0,4):
			label5 = Label(root, fg="blue")
			label5.grid(row=i+3)
			counter_label3(label5,i)
			label2 = Label(root,fg="red")
			label2.grid(row=i+3,column=1)
			counter_labell(label2,i)
			button2 = Button(root, text='Hinzufügen!', width=12, command = lambda i=i: add_inv(i)).grid(row=i+3,column=3)	
			button3 = Button(root, text='Entferne!', width=12, command = lambda i=i: del_inv(i)).grid(row=i+3,column=4)	
		messagebox.showinfo('Yes','Die Nutzerdaten wurden gelöscht!')
	else:
		messagebox.showinfo("No","Die Nutzerdaten wurden NICHT gelöscht!")
def quitt():
	zwischenspeicher.close()
	root.destroy()
button = Button(root, text='LÖSCHE ALLES!', width=15, command=del_all).grid(row=12,column=2)
button = Button(root, text='Stop', width=15, command=quitt).grid(row=12,column=1)



root.mainloop() 