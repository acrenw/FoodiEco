#initializing--------------------------------------
from tkinter import *
from math import *
from time import *
from random import *
from PIL import Image, ImageTk

root = Tk()
root.geometry("900x1600")
# make sure app can't be resized
root.resizable(width=False, height=False)
root.title('receipt')

# Define Background Image
bg = ImageTk.PhotoImage(file="receipt.gif")

# Define Canvas
s = Canvas(root, width=900, height=1600, bd=0, highlightthickness=0, background = '#af98d6')
s.pack(fill="both", expand=True)

# Put the image on the canvas
s.create_image(0,0, image=bg, anchor="nw")

#grid-------------------------------------
spacing = 50

for x in range(0, 900, spacing): 
    s.create_line( x, 25, x, 1600, fill="blue")
    s.create_text( x, 5, text=str(x), font="Times 9", anchor = N)

for y in range(0, 1600, spacing):
    s.create_line( 25, y, 1000, y, fill="blue")
    s.create_text( 5, y, text=str(y), font="Times 9", anchor = W)

#functions------------------------------------------

#if press delete, destroy text box and delete button, create "+" again

def deleteBtnClick(event): #doesnt return xy vals bc click register as event, but rather as button click... FIX
	#also it should only owrk when its on top of a button, but this owrks even when not on button
	global counter

	xMouse = event.x
	yMouse = event.y

	for i in range(11):
		iHundred = i*100
		if 650 <= xMouse <= 745 and 277+iHundred <= yMouse <= 351+iHundred: 
			counter = i
			reset()


def reset():
	global plusBtn, indexNum, deleteBtnArray, deleteBtnTextArray, textBoxArray

	#make list go up -- altering pre-exsting buttons and textboxs' y values
	#if delete btn clicked is not last btn, make all post lists go up by one
	if counter != len(deleteBtnArray):
		for i in range(counter+1,len(deleteBtnArray)):
			s.move(deleteBtnArray[i], 0, -100) #parameters: id, right, down

		for i in range(counter+1,len(deleteBtnTextArray)):
			s.move(deleteBtnTextArray[i], 0, -100)
		
		for i in range(counter+1,len(textBoxArray)):
			textBoxArray[i].place(x=200,y=300+(i-1)*100)
	
	#deletes stuff based on which btn it is
	textBoxArray[counter].destroy()
	textBoxArray.pop(counter)
	
	s.delete(deleteBtnArray[counter])
	deleteBtnArray.pop(counter)
	
	s.delete(deleteBtnTextArray[counter])
	deleteBtnTextArray.pop(counter)

	indexNum -= 1
	
	#make "+" button again at bottom
	plusBtn2 = Button(root, text="+", font=("Helvetica Bold", 40), width=2, fg="#000000", background = '#af98d6', command=lambda: createListItems())
	createBtnWindow = s.create_window(150, 277+(indexNum)*100, anchor="nw", window=plusBtn2)

	#destroy delete btn and text box
	plusBtn.destroy()
	#make new btn
	plusBtn = plusBtn2
	s.update()


def createListItems():
	global indexNum, plusBtn, textBox, deleteBtn, plusBtn2, deleteBtnArray, deleteBtnTextArray, textBoxArray

	plusBtn.destroy()
		
	#make text box based on which "+" was clicked
	textBox = Entry(root, font=("Helvetica", 20), width=25, fg="#000000", borderwidth=0)
	textBox.insert(0, "")
	# Add the textBoxArray[i] boxes to the canvas
	textBoxWindow = s.create_window(200, 300+indexNum*100, anchor="nw", window=textBox)
	#store all made text boxes
	textBoxArray.append(textBox)
	
	#make delete button based on which "+" was clicked
	deleteBtn = s.create_rectangle(650, 277+indexNum*100, 745, 351+indexNum*100, fill='#af98d6')
	deleteBtnArray.append(deleteBtn)
	
	deleteBtnText = s.create_text(698, 315+indexNum*100, text="X", fill="black", font=('Helvetica Bold', 40), outline = None)
	deleteBtnTextArray.append(deleteBtnText)

	#update indexnum
	indexNum += 1
	if indexNum < 11: #max num of items
		plusBtn = Button(root, text="+", font=("Helvetica Bold", 40), width=2, fg="#000000", background = '#af98d6', command=lambda: createListItems())
	
		createBtnWindow = s.create_window(150, 277+indexNum*100, anchor="nw", window=plusBtn)
							
#--------------------------------------------------

yVal = 277
indexNum = 0
createBtnArray = []
loopAmount = 10
counter = None
textBoxArray = [] 
deleteBtnArray = []
deleteBtnTextArray = []

#bind the clicks to deleteBtnClick
root.bind("<Button-1>", deleteBtnClick)

# for i in range(loopAmount):
# 	deleteBtnArray.append('')
# 	deleteBtnTextArray.append('')

#page title
s.create_text(450, 215, text="receipt", fill="black", font=('Helvetica Bold', 50))
	
#creating the add item buttons
plusBtn = Button(root, text="+", font=("Helvetica Bold", 40), width=2, fg="#000000", background = '#af98d6', command=lambda: createListItems())

createBtnWindow = s.create_window(150, yVal, anchor="nw", window=plusBtn)

root.mainloop()
