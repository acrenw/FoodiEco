import Image
from tkinter import *
from time import *
import math
from PIL import Image, ImageTk
'''
the recipe = https://replit.com/@acrenw/test-1#main.py
the replacements = https://replit.com/@GayeunKim/replacements#main.py
https://devpost.com/software/foodieco/joins/uD2APhMDSpqKHrJsBfiKpA
 - our devpost join link
https://docs.google.com/presentation/d/1oN6PN-ohaBMreEuWXrN7jPsZ1jUQ7qGkFoqHxFetXZs/edit?usp=sharing
 - our pitch presentation
'''

root = Tk()
root.geometry("900x1600")
root.title('Foodieco')
s = Canvas(root, width= 900, height=1600, bg='#f3ebfc')
s.pack(fill = BOTH, expand=True)

def replacements():
	global root, s, replTitle, replType, replRatio, replRatioType, backBtn
	
	# Define Background Image for replacements
	replBg = ImageTk.PhotoImage(file = 'image/download.png')
	
	# Put the image on the canvas
	s.create_image(450, 800, image = (replBg), anchor= CENTER)


	#default replacements--------------------------------------
	replTitle = ['Stevia for Sugar', 'Broccoli for Asparagus', 'Whole Wheat for White Rice']
	replType = ['Low Calories Suggestion', 'Environmentally Friendlier Suggestion', 'Healthier Suggestion']
	replRatio = ['1:1', 'N/A', '1:1']
	replRatioType = ['Volume', 'Your Choice', 'Volume']
	
	
	#Search Box--------------------------------------
	def search():
		global searchBox
		searchBox = Entry(root, font=("Helvetica", 30), width=20, fg="#000000", borderwidth=0)
		searchBox.insert(0, "")
		#Add the search boxes to the canvas--------------------------------------
		searchBoxWindow = s.create_window(145, 155, anchor="nw", window=searchBox)
		
	def searchClick(event):
		x = event.x
		y = event.y
		if 690 <= x <= 800 and 130 <= y <= 230:
			searching()

	def searching():
		searchResult = []
		searchPlace = []
		Searched = searchBox.get()
		for i in range(len(replTitle)):
			if Searched in replTitle[i]:
				searchResult.append(replTitle[i])
				searchPlace.append(i)
				
		for i in range(len(replType)):
			if Searched in replType[i]:
				if replTitle[i] not in searchResult:
					searchResult.append(replTitle[i])
					searchPlace.append(i)
					
		s.delete('all')
		s.create_image(0,0, image=replBg, anchor= 'nw')
	
		search()
		searchBox.insert(0, Searched)
	
		i = 0	
		for n in searchPlace:
			replBoxSearch = s.create_rectangle(150, 300 + i * 250, 750, 500 + i * 250, fill = '#f4e9d2')
			replSearch = s.create_text(450, 340 + i*250 , text= replTitle[n], fill="black", font=('Helvetica Bold', 30))
			replUnderlineSearch = s.create_line(150, 380 + i*250, 750, 380 + i*250, fill = 'black')
			replDescripSearch = s.create_text(450, 415 + i*250 , text= replType[n], fill="black", font=('Helvetica', 20))
			replRatioDescripSearch = s.create_text(450, 460 + i*250 , text= ('Ratio when replacing : ' 
		+ replRatio[n] + ' (' + replRatioType[n] + ')'), fill="black", font=('Helvetica', 20))
		
			if i == (len(searchPlace)) - 1:
				uploadBtn = Button(root, text= 'Upload My Replacement', font = ('Helvetica', 25),fg= "#000000", background = '#f4e9d2', command = lambda: upload())
				uploadBtnWindow = s.create_window(150, 300 + (i+1)*250 , width=600, anchor = NW, window = uploadBtn)
				break
		
			else:
				i += 1
				
	#showing replacements--------------------------------------
	def createRepl():
		global replTitle, replType, replRatio, replRatio, backBtnWindow, uploadBtnWindow
		for i in range(len(replTitle)):
			replBox = s.create_rectangle(150, 300 + i * 250, 750, 500 + i * 250, fill = '#f4e9d2')
			repl = s.create_text(450, 340 + i*250 , text= replTitle[i], fill="black", font=('Helvetica Bold', 30))
			replUnderline = s.create_line(150, 380 + i*250, 750, 380 + i*250, fill = 'black')
			replDescrip = s.create_text(450, 415 + i*250 , text= replType[i], fill="black", font=('Helvetica', 20))
			replRatioDescrip = s.create_text(450, 460 + i*250 , text= ('Ratio when replacing : ' 
		 + replRatio[i] + ' (' + replRatioType[i] + ')'), fill="black", font=('Helvetica', 20))
		
			if i == (len(replTitle)) - 1:
				uploadBtn = Button(root, text= 'Upload My Replacement', font = ('Helvetica', 25),fg= "#000000", background = '#f4e9d2', command = lambda: upload())
				uploadBtnWindow = s.create_window(150, 300 + (i+1)*250 , width=600, anchor = NW, window = uploadBtn)
				
		
	
	def upload():
		global suggestionBar, ratioBar, suggestion_inside, ratioOptions_inside, replTitleBox, replRatioBox
		
		#upload tab setting--------------------------------------
		uploadSetting = s.create_rectangle(100,600,800,900, fill = 'white')
		uploadDesign = s.create_rectangle(100,600,800,650, fill = '#f4e9d2')
		uploadCancel = Button(root, text = 'X', font = ('Helvetica', 25),fg= "#000000", background = '#f4e9d2', command = lambda: cancel())
		uploadCancelWindow = s.create_window(100, 600, width=50, anchor = NW, window = uploadCancel)
		uploadDone = Button(root, text = 'Done', font = ('Helvetica', 25),fg= "#000000", background = '#f4e9d2', command = lambda: finish())
		uploadDoneWindow = s.create_window(800, 650, width=100, anchor = SE, window = uploadDone)
	
		#textbox for replTitle--------------------------------------
		replTitleBox = Entry(root, font=("Helvetica", 25), width=15, fg="#000000", borderwidth=0)
		replTitleBox.insert(0, "Replacement Title (ex: Stevia for Sugar)")
		replTitleoBoxWindow = s.create_window(110, 670, anchor="nw", window = replTitleBox)
		
		#options for replacement types -- make the options font bigger
		suggestion = ["Environmentally Friendlier Suggestion", "Healthier Suggestion", "Low Calories Suggestion"]
		suggestion_inside = StringVar()
		suggestion_inside.set("Replacement Types")
		suggestionBar = OptionMenu(s, suggestion_inside, *suggestion)
		suggestionBar.config(font = ('Helvetica', 25))
		suggestionBar.pack()
		suggestionBar.place(x=110, y=740,height=50,anchor=NW)

		#textbox for ratio--------------------------------------
		replRatioBox = Entry(root, font=("Helvetica", 25), width=17, fg="#000000", borderwidth=0)
		replRatioBox.insert(0, "ratio (ex: 1:1 or N/A)")
		replRatioBoxWindow = s.create_window(110, 820, anchor="nw", window=replRatioBox)
	
		#ratio type--------------------------------------
		ratioOptions = ["Volume", "Weight", "Your Choice"]
		ratioOptions_inside = StringVar()
		ratioOptions_inside.set("Ratio Types")
		ratioBar = OptionMenu(s, ratioOptions_inside, *ratioOptions)
		ratioBar.config(font = ('Helvetica', 25))
		ratioBar.pack()
		ratioBar.place(x=480, y=820 ,height=50,anchor=NW)
		
		#updating the canvas
		s.update()
		print('hi')
		
	def cancel():
		global suggestionBar, ratioBar
		s.delete('all')
		s.create_image(0,0, image=replBg, anchor="nw")
		suggestionBar.destroy()
		ratioBar.destroy()
		createRepl()
		search()
		
	def finish():
		global suggestionBar, ratioBar, suggestion_inside, ratioOptions_inside, replTitleBox, replRatioBox
		replTitle.append(replTitleBox.get())
		replType.append(suggestion_inside.get())
		replRatio.append(replRatioBox.get())
		replRatioType.append(ratioOptions_inside.get())
		s.delete('all')
		s.create_image(0,0, image=replBg, anchor="nw")
		suggestionBar.destroy()
		ratioBar.destroy()
		createRepl()
		search()

	
	def back():
		s.delete('all')
		s.unbind("<Button-1>")
		backBtn.destroy()
		startPage()

	backBtn = Button (root, text = 'Back', font = ('Helvetica', 25), fg = '#000000', background = '#af98d6', command = back)
	backBtn.pack()
	backBtn.place(x=450,y=1400,width=200,height=50,anchor=CENTER)
	
	createRepl()
	search()
	s.bind("<Button-1>",searchClick, add="+")
	root.mainloop()


def recipe():
	global bg, plusBtn, createBtnWindow, indexNum, textBoxArray, deleteBtnArray, counter, deleteBtnTextArray, foodNameEntry, recipes
	
	recipes = []
	
	def recipeInput():
		global bg, plusBtn, createBtnWindow, indexNum, textBoxArray, deleteBtnArray, counter, deleteBtnTextArray, foodNameEntry, recipes, recipeBookButton
		# Define Background Image
		bg = ImageTk.PhotoImage(file="images/receipt.gif")
	
		# Put the image on the canvas
		s.create_image(0,0, image=bg, anchor="nw")
	
		#back button
		def back(event):
			x = event.x
			y = event.y
	
			if 200 <= x <= 700 and 1460 <= y <= 1540:
				plusBtn.destroy()
				root.unbind("<Button-1>")
				foodNameEntry.destroy()
				recipeBookButton.destroy()
				enterButton.destroy()
				s.delete('all')
				startPage()
	
		def recipeBook():
			s.delete('all')
			root.unbind("<Button-1>")
			foodNameEntry.destroy()
			enterButton.destroy()
			recipeBookButton.destroy()
			plusBtn.destroy()
			recipeSaved()
						
		recipeBookButton = Button(root, text = "Go to Recipe Book", command = recipeBook, font="Arial 15", bg="#fbfcca",anchor = CENTER)
		recipeBookButton.pack()
		recipeBookButton.place(x=450, y=140,height=50,width=300,anchor=CENTER)
				
		#functions------------------------------------------
		
		def deleteBtnClick(event): 
			global counter, recipes
		
			xMouse = event.x
			yMouse = event.y
		
			for i in range(11):
				iHundred = i*100
				if 650 <= xMouse <= 745 and 277+iHundred <= yMouse <= 351+iHundred: 
					counter = i
					reset()
		
		
		def reset(): 
			global plusBtn, indexNum, textBoxArray, deleteBtnArray, deleteBtnTextArray, recipes
		
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
			3
			#make "+" button again at bottom
			plusBtn2 = Button(root, text="+", font=("Helvetica Bold", 40), width=2, fg="#000000", background = '#af98d6', command=lambda: createListItems())
			createBtnWindow = s.create_window(150, 277+(indexNum)*100, anchor="nw", window=plusBtn2)
		
			#destroy delete btn and text box
			plusBtn.destroy()
			#make new btn
			plusBtn = plusBtn2
			s.update()

		
		def createListItems():
			global indexNum, plusBtn, textBox, deleteBtn, plusBtn2, deleteBtnArray, deleteBtnTextArray, textBoxArray, recipes
		
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
	
		def enter():
			global foodName, ingredients, recipes
			foodName = foodNameEntry.get()
			
			#reset ingredients array
			ingredients = []
			
			for i in range(len(textBoxArray)):
				textBox = textBoxArray[i]
				ingredients.append(textBox.get())

			if str(foodName) not in foodNameArray:
				recipes.insert(-1, [foodName, ingredients])
				print(recipes)

			foodNameArray.append(foodName)
				
		#--------------------------------------------------
		#enter button
		enterButton = Button(root, text = "Enter", command = enter, font="Arial 15", bg="#d5aefc",anchor = CENTER)
		enterButton.pack()
		enterButton.place(x=450, y=1300,height=50,width=300, anchor=CENTER)
	
		yVal = 277
		indexNum = 0
		createBtnArray = []
		loopAmount = 10
		counter = None
		textBoxArray = [] 
		deleteBtnArray = []
		deleteBtnTextArray = []
		ingredients = []
		foodNameArray = []
		
		#bind the clicks to deleteBtnClick
		s.bind("<Button-1>", deleteBtnClick, add="+")
		s.bind("<Button-1>", back, add="+")
		
		#food name
		foodNameEntry= Entry(root, font=("Helvetica", 30), width=15, fg="#000000", borderwidth=0)
		foodNameEntry.pack()
		foodNameEntry.place(x=450,y=200,height=50,anchor=CENTER)
		
		#creating the add item buttons
		plusBtn = Button(root, text="+", font=("Helvetica Bold", 40), width=2, fg="#000000", background = '#af98d6', command=lambda: createListItems())
		
		createBtnWindow = s.create_window(150, yVal, anchor="nw", window=plusBtn)
		
		root.mainloop()
	
	
	def recipeSaved(): 
		global recipes, recipeButtons, foodName, ingredients, backButton
		
		def back():
			global recipe
			s.delete('all')
			s.unbind("<Button-1>")
			backButton.destroy()
			backToMainBtn.destroy()
			recipeInput()
			
		backButton = Button(root, text = "Go to Input Page", command = back, font="Arial 15", bg="#fbfcca",anchor = CENTER)
		backButton.pack()
		backButton.place(x=450, y=200,height=50,width=300,anchor=CENTER)

		def backToMain():
			global recipes
			s.delete('all')
			s.unbind("<Button-1>")
			backToMainBtn.destroy()
			backButton.destroy
			startPage()
		
		backToMainBtn = Button(root, text = "Go Home", command = backToMain, font="Arial 15", bg="#fbfcca",anchor = CENTER)
		backToMainBtn.pack()
		backToMainBtn.place(x=450, y=1400,height=50,width=300,anchor=CENTER)
	
		s.create_text(450,100,text="Recipe Book",font=("Arial","30","bold"),anchor=CENTER)
		recipeButtons = []
		foodName = []
		ingredients = []
		for i in range(15):
			recipe = s.create_rectangle(200,300+i*65,700,340+i*65,fill="#ffedf6",outline="#f5b5d5",width=2)
			recipeButtons.append(recipe)
	
		for i in range(len(recipes)):
			foodName.append(recipes[i][0])
			ingredients.append(recipes[i][1])
	
		for i in range(len(recipes)):
			s.create_text(450,325+i*65,text=foodName[i],anchor=CENTER,font="Arial 15")
		
		def recipeOpen(event):
			global foodName, ingredients, recipes
			x = event.x
			y = event.y
			if 200 <= x <= 650:
				for i in range(len(recipes)):
					if 300+i*50 <= y <= 340+i*50:
						s.delete('all')
						s.create_rectangle(200,300,700,900,fill="#f5e6fa")
						print(1)
						s.create_text(450,400,text=foodName[i],anchor=CENTER,font=("Arial","20","bold"))
	
						for a in range(len(ingredients)+1):
							s.create_text(450,450+(a*50),text=ingredients[i][a],anchor=CENTER,font="Arial 15")
	
						def back():
							s.delete('all')
							backButton.destroy()
							recipeSaved()
						
						backButton = Button(root, text = "Back", command = back, font="Arial 15", bg="#fbfcca",anchor = CENTER)
						backButton.pack()
						backButton.place(x=450, y=200,height=50,width=300,anchor=CENTER)
		s.bind("<Button-1>", recipeOpen, add="+")
	
	recipeSaved()

labels = []
labelsStored = []
icons = []
iconsStored = []
for i in range(35):
	labels.append('')
	icons.append('')
	labelsStored.append('')
	iconsStored.append('')

	
def fridgeOpen():
	global foodEntry, categoryBar, fridge, drinksCategory, veggiesCategory, legumesCategory, fruitsCategory, meatsCategory, enterButton, nFood, coordinates, closeButton, labels, labelsStored, iconsStored
	s.delete('all')
	foodEntry = Entry(s)
	foodEntry.insert(0, "Insert food name")
	foodEntry.delete(0, END)
	foodEntry.pack()
	foodEntry.place(x=450,y=80,height=50,width=300,anchor=CENTER)
	foodEntry.config(font="Arial 15")
	
	options = ["drink", "fruit", "legume", "meat", "veggie"]
	value_inside = StringVar()
	value_inside.set("Select an Option")
	categoryBar = OptionMenu(s, value_inside, *options)
	categoryBar.config(bg="#cafcf9",font="Arial 15")
	categoryBar.pack()
	categoryBar.place(x=450, y=140,height=50,width=300,anchor=CENTER)
	
	#import image
	fridge = PhotoImage(file="images/fridgeOpen.gif")
	drinksCategory = PhotoImage(file="images/drinksCategory.gif")
	veggiesCategory = PhotoImage(file="images/veggiesCategory.gif")
	legumesCategory = PhotoImage(file="images/legumesCategory.gif")
	fruitsCategory = PhotoImage(file="images/fruitsCategory.gif")
	meatsCategory = PhotoImage(file="images/meatsCategory.gif")
	
	coordinates = []
	y = 210
	for nFood in range(35):
		if (nFood/5) == int(nFood/5):
			x = 290
			y += 143
		else:
			x += 80
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
	
	enterButton = Button(root, text = "Enter", command = getEntry, font="Arial 15", bg="#fbfcca",anchor = CENTER)
	enterButton.pack()
	enterButton.place(x=450, y=200,height=50,width=300,anchor=CENTER)

	def labelFood(foodInput):
		nameLength = len(foodInput)

		if ' ' in foodInput:
			spaceIndex = foodInput.index(' ')
			label1 = foodInput[:spaceIndex]
			label2 = foodInput[spaceIndex+1:]

			label = label1+'\n'+label2

		else:
			if nameLength > 7:
				label1 = foodInput[:7]
				label2 = foodInput[7:]
	
				label = label1+'\n'+label2
			
			else:
				label = foodInput

		return label
	
	def labelDrinks():
		global foodInput, drinks, nFood, drinksCategory, label, coordinates, labelsStored, iconsStored
		index = labels.index('')
		coordinate = coordinates[index]
		x = coordinate[0]
		y = coordinate[1]
		icons[index] = s.create_image(x,y,image=drinksCategory,anchor=CENTER)
		label = labelFood(foodInput)
		labels[index] = s.create_text(x,y+47,text=label,font="Arial 10")
		iconsStored[index] = drinksCategory
		labelsStored[index] = label
		nFood += 1
	
	def labelVeggies():
		global foodInput, veggies, nFood, veggiesCategory, label, coordinates, labelsStored, iconsStored
		index = labels.index('')
		coordinate = coordinates[index]
		x = coordinate[0]
		y = coordinate[1]
		icons[index] = s.create_image(x,y,image=veggiesCategory,anchor=CENTER)
		label = labelFood(foodInput)
		labels[index] = s.create_text(x,y+47,text=label,font="Arial 10")
		iconsStored[index] = veggiesCategory
		labelsStored[index] = label
		nFood += 1
		
	def labelLegumes():
		global foodInput, legumes, nFood, xCoordinate, yCoordinate, label, coordinates, labelsStored, iconsStored
		index = labels.index('')
		coordinate = coordinates[index]
		x = coordinate[0]
		y = coordinate[1]
		icons[index] = s.create_image(x,y,image=legumesCategory,anchor=CENTER)
		label = labelFood(foodInput)
		labels[index] = s.create_text(x,y+47,text=label,font="Arial 10")
		iconsStored[index] = legumesCategory
		labelsStored[index] = label
		nFood += 1
	
	def labelFruits():
		global foodInput, fruits, nFood, xCoordinate, yCoordinate, label, coordinates, labelsStored, iconsStored
		index = labels.index('')
		coordinate = coordinates[index]
		x = coordinate[0]
		y = coordinate[1]
		icons[index] = s.create_image(x,y,image=fruitsCategory,anchor=CENTER)
		label = labelFood(foodInput)
		labels[index] = s.create_text(x,y+47,text=label,font="Arial 10")
		iconsStored[index] = fruitsCategory
		labelsStored[index] = label
		nFood += 1
	
	def labelMeats():
		global foodInput, meats, nFood, xCoordinate, yCoordinate, label, coordinates, labelsStored, iconsStored
		index = labels.index('')
		coordinate = coordinates[index]
		x = coordinate[0]
		y = coordinate[1]
		icons[index] = s.create_image(x,y,image=meatsCategory, anchor=CENTER)
		label = labelFood(foodInput)
		labels[index] = s.create_text(x,y+47,text=label,font="Arial 10")
		iconsStored[index] = meatsCategory
		labelsStored[index] = label
		nFood += 1
	
	s.create_image(450,800,image=fridge)

	index = labels.index('')
	for i in range(index):
		x = coordinates[i][0]
		y = coordinates[i][1]
		labels[i] = s.create_text(x,y+47,text=labelsStored[i],font="Arial 10")
		icons[i] = s.create_image(x,y,image=iconsStored[i], anchor=CENTER)
	s.update()
	
	#PLEASE DO NOT TOUCH#
	def removeFood(event):
		x = event.x
		y = event.y

		if 125 <= x <= 160 and 610 <= y <= 1010:
			enterButton.destroy()
			foodEntry.destroy()
			categoryBar.destroy()
			s.delete('all')
			fridgeClosed()
			
		if 310 <= y <= 430:
			if 250 <= x <= 330:
				s.delete(labels[0])
				labels[0] = ''
				s.delete(icons[0])
				icons[0] = ''
				labelsStored[0] = ''
				iconsStored[0] = ''
			elif 330 <= x <= 410:
				s.delete(labels[1])
				labels[1] = ''  
				s.delete(icons[1])
				icons[1] = ''
				labelsStored[1] = ''
				iconsStored[1] = ''
			elif 410 <= x <= 490:
				s.delete(labels[2])
				labels[2] = ''
				s.delete(icons[2])
				icons[2] = ''
				labelsStored[2] = ''
				iconsStored[2] = ''
			elif 490 <= x <= 570:
				s.delete(labels[3])
				labels[3] = ''
				s.delete(icons[3])
				icons[3] = ''
				labelsStored[3] = ''
				iconsStored[3] = ''
			elif 570 <= x <= 650:
				s.delete(labels[4])
				labels[4] = ''
				s.delete(icons[4])
				icons[4] = ''
				labelsStored[4] = ''
				iconsStored[4] = ''
			
		elif 450 <= y <= 570:
			if 250 <= x <= 330:
				s.delete(labels[5])
				labels[5] = ''
				s.delete(icons[5])
				icons[5] = ''
				labelsStored[5] = ''
				iconsStored[5] = ''
			elif 330 <= x <= 410:
				s.delete(labels[6])
				labels[6] = ''  
				s.delete(icons[6])
				icons[6] = ''
				labelsStored[6] = ''
				iconsStored[6] = ''
			elif 410 <= x <= 490:
				s.delete(labels[7])
				labels[7] = ''
				s.delete(icons[7])
				icons[7] = ''
				labelsStored[7] = ''
				iconsStored[7] = ''
			elif 490 <= x <= 570:
				s.delete(labels[8])
				labels[8] = ''
				s.delete(icons[8])
				icons[8] = ''
				labelsStored[8] = ''
				iconsStored[8] = ''
			elif 570 <= x <= 650:
				s.delete(labels[9])
				labels[9] = ''
				s.delete(icons[9])
				icons[9] = ''
				labelsStored[9] = ''
				iconsStored[9] = ''
			
		elif 590 <= y <= 710:
			if 250 <= x <= 330:
				s.delete(labels[10])
				labels[10] = ''
				s.delete(icons[10])
				icons[10] = ''
				labelsStored[10] = ''
				iconsStored[10] = ''
			elif 330 <= x <= 410:
				s.delete(labels[11])
				labels[11] = ''  
				s.delete(icons[11])
				icons[11] = ''
				labelsStored[11] = ''
				iconsStored[11] = ''
			elif 410 <= x <= 490:
				s.delete(labels[12])
				labels[12] = ''
				s.delete(icons[12])
				icons[12] = ''
				labelsStored[12] = ''
				iconsStored[12] = ''
			elif 490 <= x <= 570:
				s.delete(labels[13])
				labels[13] = ''
				s.delete(icons[13])
				icons[13] = ''
				labelsStored[13] = ''
				iconsStored[13] = ''
			elif 570 <= x <= 650:
				s.delete(labels[14])
				labels[14] = ''
				s.delete(icons[14])
				icons[14] = ''
				labelsStored[14] = ''
				iconsStored[14] = ''
			
		elif 730 <= y <= 850:	
			if 250 <= x <= 330:
				s.delete(labels[15])
				labels[15] = ''
				s.delete(icons[15])
				icons[15] = ''
				labelsStored[15] = ''
				iconsStored[15] = ''
			elif 330 <= x <= 410:
				s.delete(labels[16])
				labels[16] = ''  
				s.delete(icons[16])
				icons[16] = ''
				labelsStored[16] = ''
				iconsStored[16] = ''
			elif 410 <= x <= 490:
				s.delete(labels[17])
				labels[17] = ''
				s.delete(icons[17])
				icons[17] = ''
				labelsStored[17] = ''
				iconsStored[17] = ''
			elif 490 <= x <= 570:
				s.delete(labels[18])
				labels[18] = ''
				s.delete(icons[18])
				icons[18] = ''
				labelsStored[18] = ''
				iconsStored[18] = ''
			elif 570 <= x <= 650:
				s.delete(labels[19])
				labels[19] = ''
				s.delete(icons[19])
				icons[19] = ''
				labelsStored[19] = ''
				iconsStored[19] = ''
			
		elif 870 <= y <= 990:
			if 250 <= x <= 330:
				s.delete(labels[20])
				labels[20] = ''
				s.delete(icons[20])
				icons[20] = ''
				labelsStored[20] = ''
				iconsStored[20] = ''
			elif 330 <= x <= 410:
				s.delete(labels[21])
				labels[21] = ''  
				s.delete(icons[21])
				icons[21] = ''
				labelsStored[21] = ''
				iconsStored[21] = ''
			elif 410 <= x <= 490:
				s.delete(labels[22])
				labels[22] = ''
				s.delete(icons[22])
				icons[22] = ''
				labelsStored[22] = ''
				iconsStored[22] = ''
			elif 490 <= x <= 570:
				s.delete(labels[23])
				labels[23] = ''
				s.delete(icons[23])
				icons[23] = ''
				labelsStored[23] = ''
				iconsStored[23] = ''
			elif 570 <= x <= 650:
				s.delete(labels[24])
				labels[24] = ''
				s.delete(icons[24])
				icons[24] = ''
				labelsStored[24] = ''
				iconsStored[24] = ''
		
		elif 1010 <= y <= 1130:
			if 250 <= x <= 330:
				s.delete(labels[25])
				labels[25] = ''
				s.delete(icons[25])
				icons[25] = ''
				labelsStored[25] = ''
				iconsStored[25] = ''
			elif 330 <= x <= 410:
				s.delete(labels[26])
				labels[26] = ''  
				s.delete(icons[26])
				icons[26] = ''
				labelsStored[26] = ''
				iconsStored[26] = ''
			elif 410 <= x <= 490:
				s.delete(labels[27])
				labels[27] = ''
				s.delete(icons[27])
				icons[27] = ''
				labelsStored[27] = ''
				iconsStored[27] = ''
			elif 490 <= x <= 570:
				s.delete(labels[28])
				labels[28] = ''
				s.delete(icons[28])
				icons[28] = ''
				labelsStored[28] = ''
				iconsStored[28] = ''
			elif 570 <= x <= 650:
				s.delete(labels[29])
				labels[29] = ''
				s.delete(icons[29])
				icons[29] = ''
				labelsStored[29] = ''
				iconsStored[29] = ''
		
		elif 1150 <= y <= 1270:
			if 250 <= x <= 330:
				s.delete(labels[30])
				labels[30] = ''
				s.delete(icons[30])
				icons[30] = ''
				labelsStored[30] = ''
				iconsStored[30] = ''
			elif 330 <= x <= 410:
				s.delete(labels[31])
				labels[31] = ''  
				s.delete(icons[31])
				icons[31] = ''
				labelsStored[31] = ''
				iconsStored[31] = ''
			elif 410 <= x <= 490:
				s.delete(labels[32])
				labels[32] = ''
				s.delete(icons[32])
				icons[32] = ''
				labelsStored[32] = ''
				iconsStored[32] = ''
			elif 490 <= x <= 570:
				s.delete(labels[33])
				labels[33] = ''
				s.delete(icons[33])
				icons[33] = ''
				labelsStored[33] = ''
				iconsStored[33] = ''
			elif 570 <= x <= 650:
				s.delete(labels[34])
				labels[34] = ''
				s.delete(icons[34])
				icons[34] = ''
				labelsStored[34] = ''
				iconsStored[34] = ''


	s.bind("<Button-1>", removeFood, add="+")


def fridgeClosed():
	global fridge, openButton
	s.delete('all')
	fridge = PhotoImage(file="images/fridgeClosed.gif")
	s.create_image(450,800,image=fridge,anchor=CENTER)
	s.update()

	def open(event):
		x = event.x
		y = event.y
		if 610 <= x <= 700 and 545 <= y <= 1075:
			s.unbind("<Button-1>")
			backButton.destroy()
			fridgeOpen()
	
	def back():
		s.delete('all')
		backButton.destroy()
		startPage()
	
	backButton = Button(root, text = "Back to Home Screen", command = back,bg="#f7e8ff", font="Arial 20", anchor = CENTER)
	backButton.pack()
	backButton.place(x=450, y=1500,height=70,width=300,anchor=CENTER)
		
	s.bind("<Button-1>", open, add="+")
	
def startPage():
	global logo, fridgeButton, recipeButton, replacementButton, recipes
	
	logo = PhotoImage(file="images/logo.gif")
	s.create_image(450,500,image=logo, anchor=CENTER)

	def fridgeClick():
		s.delete('all')
		fridgeButton.destroy()
		recipeButton.destroy()
		replacementButton.destroy()

		fridgeClosed()

	fridgeButton = Button(root, text = "Fridge", command = fridgeClick,bg="#d7f7b5", font="Arial 20", anchor = CENTER)
	fridgeButton.pack()
	fridgeButton.place(x=450, y=800,height=70,width=300,anchor=CENTER)

	def recipeClick():
		s.delete('all')
		fridgeButton.destroy()
		recipeButton.destroy()
		replacementButton.destroy()

		recipe()

	recipeButton = Button(root, text = "Recipe", command = recipeClick, bg="#fbfcca",font="Arial 20", anchor = CENTER)
	recipeButton.pack()
	recipeButton.place(x=450, y=900,height=70,width=300,anchor=CENTER)

	def replacementClick():
		s.delete('all')
		fridgeButton.destroy()
		recipeButton.destroy()
		replacementButton.destroy()

		replacements()

	replacementButton = Button(root, text = "Replacement", command = replacementClick, bg="#b5cdf7", font="Arial 20", anchor = CENTER)
	replacementButton.pack()
	replacementButton.place(x=450, y=1000,height=70,width=300,anchor=CENTER)

startPage()
