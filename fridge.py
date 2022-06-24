from tkinter import *
from tkinter import ttk
from time import *
import math
'''the recipe = https://replit.com/@acrenw/test-1#main.py'''

root = Tk()
root.geometry("450x800")
root.title('fridge')
s = Canvas(root, width= 450, height=800, bg='#f1d9fa')
s.pack(fill = BOTH, expand=True)

foodEntry = Entry(s)
foodEntry.insert(0, "Insert food name")
foodEntry.delete(0, END)
foodEntry.pack()
foodEntry.place(x=225,y=20,anchor=CENTER)

options = ["drink", "fruit", "legume", "meat", "veggie"]
value_inside = StringVar()
value_inside.set("Select an Option")
categoryBar = OptionMenu(s, value_inside, *options)
categoryBar.pack()
categoryBar.place(x=225, y=50,height=25,anchor=CENTER)

#import image
fridge = PhotoImage(file="images/fridgeOpen.gif")
drinksCategory = PhotoImage(file="images/drinksCategory.gif")
veggiesCategory = PhotoImage(file="images/veggiesCategory.gif")
legumesCategory = PhotoImage(file="images/legumesCategory.gif")
fruitsCategory = PhotoImage(file="images/fruitsCategory.gif")
meatsCategory = PhotoImage(file="images/meatsCategory.gif")

labels = []
icons = []
for i in range(35):
	labels.append('')
	icons.append('')

coordinates = []
y = 25
for nFood in range(35):
	if (nFood/5) == int(nFood/5):
		x = 120
		y += 95
	else:
		x += 50
	coordinates.append([x,y])

def getEntry():
	global foodInput, categoryInput
	foodInput = foodEntry.get()
	categoryInput = value_inside.get()

	if categoryInput == "drink":
		labelDrinks()
	elif categoryInput == "veggie":
		labelVeggies()  
	elif categoryInput == "legume":
		labelLegumes()
	elif categoryInput == "fruit":
		labelFruits()
	elif categoryInput == "meat":
		labelMeats()
	elif categoryInput == "other":
		labelOthers()

enterButton = Button(root, text = "Enter", command = getEntry, anchor = CENTER)
enterButton.pack()
enterButton.place(x=225, y=80,height=20,anchor=CENTER)

def labelDrinks():
	global foodInput, drinks, nFood, drinksCategory, label, coordinates
	index = labels.index('')
	coordinate = coordinates[index]
	x = coordinate[0]
	y = coordinate[1]
	foodIcon = s.create_image(x,y,image=drinksCategory,anchor=CENTER)
	foodLabel = s.create_text(x,y,text=foodInput,font="Arial 6")
	icons[index] = foodIcon
	labels[index] = foodLabel
	nFood += 1

def labelVeggies():
	global foodInput, veggies, nFood, veggiesCategory
	index = labels.index('')
	coordinate = coordinates[index]
	x = coordinate[0]
	y = coordinate[1]
	foodIcon = s.create_image(x,y,image=veggiesCategory,anchor=CENTER)
	foodLabel = s.create_text(x,y,text=foodInput,font="Arial 6")
	icons[index] = foodIcon
	labels[index] = foodLabel
	nFood += 1
	
def labelLegumes():
	global foodInput, legumes, nFood, xCoordinate, yCoordinate
	index = labels.index('')
	coordinate = coordinates[index]
	x = coordinate[0]
	y = coordinate[1]
	foodIcon = s.create_image(x,y,image=legumesCategory,anchor=CENTER)
	foodLabel = s.create_text(x,y+20,text=foodInput,font="Arial 6")
	icons[index] = foodIcon
	labels[index] = foodLabel
	nFood += 1

def labelFruits():
	global foodInput, fruits, nFood, xCoordinate, yCoordinate
	index = labels.index('')
	coordinate = coordinates[index]
	x = coordinate[0]
	y = coordinate[1]
	foodIcon = s.create_image(x,y,image=fruitsCategory,anchor=CENTER)
	foodLabel = s.create_text(x,y+20,text=foodInput,font="Arial 6")
	icons[index] = foodIcon
	labels[index] = foodLabel
	nFood += 1

def labelMeats():
	global foodInput, meats, nFood, xCoordinate, yCoordinate
	index = labels.index('')
	coordinate = coordinates[index]
	x = coordinate[0]
	y = coordinate[1]
	foodIcon = s.create_image(x,y,image=meatsCategory, anchor=CENTER)
	foodLabel = s.create_text(x,y,text=foodInput,font="Arial 6")
	icons[index] = foodIcon
	labels[index] = foodLabel
	nFood += 1

def labelOthers():
	global foodInput, others, nFood, xCoordinate, yCoordinate
	index = labels.index('')
	coordinate = coordinates[index]
	x = coordinate[0]
	y = coordinate[1]
	foodIcon = s.create_text(x,y,text=' ')
	foodLabel = s.create_text(x,y,text=foodInput,font="Arial 6")
	icons[index] = foodIcon
	labels[index] = foodLabel
	nFood += 1

s.create_image(225,400,image=fridge)

#PLEASE DO NOT TOUCH#
def removeFood(event):
	x = event.x
	y = event.x
  
	if 100 <= y <= 150:
		if 100 <= x <= 150:
			s.delete(labels[0])
			labels[0] = ''
			s.delete(icons[0])
		elif 150 <= x <= 200:
			s.delete(labels[1])
			labels[1] = ''  
			s.delete(icons[1])
		elif 200 <= x <= 250:
			s.delete(labels[2])
			labels[2] = ''
			s.delete(icons[2])
		elif 250 <= x <= 300:
			s.delete(labels[3])
			labels[3] = ''
			s.delete(icons[3])
		elif 300 <= x <= 350:
			s.delete(labels[4])
			labels[4] = ''
			s.delete(icons[4])
		
	elif 200 <= y <= 250:
		if 100 <= x <= 150:
			s.delete(labels[5])
			labels[5] = ''
			s.delete(icons[5])
		elif 150 <= x <= 200:
			s.delete(labels[6])
			labels[6] = ''
			s.delete(icons[6])
		elif 200 <= x <= 250:
			s.delete(labels[7])
			labels[7] = ''
			s.delete(icons[7])
		elif 250 <= x <= 300:
			s.delete(labels[8])
			labels[8] = ''
			s.delete(icons[8])
		elif 300 <= x <= 350:
			s.delete(labels[9])
			labels[9] = ''
			s.delete(icons[9])
		
	elif 275 <= y <= 350:
		if 100 <= x <= 150:
			s.delete(labels[10])
			labels[10] = ''
			s.delete(icons[10])
		elif 150 <= x <= 200:
			s.delete(labels[11])
			labels[11] = ''
			s.delete(icons[11])
		elif 200 <= x <= 250:
			s.delete(labels[12])
			labels[12] = ''
			s.delete(icons[12])
		elif 250 <= x <= 300:
			s.delete(labels[13])
			labels[13] = ''
			s.delete(icons[13])
		elif 300 <= x <= 350:
			s.delete(labels[14])
			labels[14] = ''
			s.delete(icons[14])
		
	elif 375 <= y <= 450:	
		if 100 <= x <= 150:
			s.delete(labels[15])
			labels[15] = ''
			s.delete(icons[15])
		elif 150 <= x <= 200:
			s.delete(labels[16])
			labels[16] = ''
			s.delete(icons[16])
		elif 200 <= x <= 250:
			s.delete(labels[17])
			labels[17] = ''
			s.delete(icons[17])
		elif 250 <= x <= 300:
			s.delete(labels[18])
			labels[18] = ''
			s.delete(icons[18])
		elif 300 <= x <= 350:
			s.delete(labels[19])
			labels[19] = ''
			s.delete(icons[19])
		
	elif 475 <= y <= 550:
		if 100 <= x <= 150:
			s.delete(labels[20])
			labels[20] = ''
			s.delete(icons[20])
		elif 150 <= x <= 200:
			s.delete(labels[21])
			labels[21] = ''
			s.delete(icons[21])
		elif 200 <= x <= 250:
			s.delete(labels[22])
			labels[22] = ''
			s.delete(icons[22])
		elif 250 <= x <= 300:
			s.delete(labels[23])
			labels[23] = ''
			s.delete(icons[23])
		elif 300 <= x <= 350:
			s.delete(labels[24])
			labels[24] = ''
			s.delete(icons[24])
	
	elif 575 <= y <= 625:
		if 100 <= x <= 150:
			s.delete(labels[25])
			labels[25] = ''
			s.delete(icons[25])
		elif 150 <= x <= 200:
			s.delete(labels[26])
			labels[26] = ''
			s.delete(icons[26])
		elif 200 <= x <= 250:
			s.delete(labels[27])
			labels[27] = ''
			s.delete(icons[27])
		elif 250 <= x <= 300:
			s.delete(labels[28])
			labels[28] = ''
			s.delete(icons[28])
		elif 300 <= x <= 350:
			s.delete(labels[29])
			labels[29] = ''
			s.delete(icons[29])
	
	elif 650 <= y <= 725:
		if 100 <= x <= 150:
			s.delete(labels[30])
			labels[30] = ''
			s.delete(icons[30])
		elif 150 <= x <= 200:
			s.delete(labels[31])
			labels[31] = ''
			s.delete(icons[31])
		elif 200 <= x <= 250:
			s.delete(labels[32])
			labels[32] = ''
			s.delete(icons[32])
		elif 250 <= x <= 300:
			s.delete(labels[33])
			labels[33] = ''
			s.delete(icons[33])
		elif 300 <= x <= 350:
			s.delete(labels[34])
			labels[34] = ''
			s.delete(icons[34])

s.bind("<Button-1>", removeFood)
