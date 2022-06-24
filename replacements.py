#initializing--------------------------------------
from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.geometry("900x1600")
#make sure app can't be resized--------------------------------------
root.resizable(width=False, height=False)
root.title('search')

#Define Canvas--------------------------------------
s = Canvas(root, width=900, height=1600, bd=0, highlightthickness=0, background = '#af98d6')
s.pack(fill="both", expand=True)

# Define Background Image
replBg = ImageTk.PhotoImage(file="images/download.png")
# Put the image on the canvas
s.create_image(0,0, image=replBg, anchor="nw")

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
	s.create_image(0,0, image=replBg, anchor="nw")

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
	global replTitle, replType, replRatio, replRatio
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
	replRatioBox = Entry(root, font=("Helvetica", 25), width=15, fg="#000000", borderwidth=0)
	replRatioBox.insert(0, "ratio (ex: 1:1 or N/A)")
	replRatioBoxWindow = s.create_window(110, 820, anchor="nw", window=replRatioBox)

	#ratio type--------------------------------------
	ratioOptions = ["Volume", "Weight", "Your Choice"]
	ratioOptions_inside = StringVar()
	ratioOptions_inside.set("Ratio Types")
	ratioBar = OptionMenu(s, ratioOptions_inside, *ratioOptions)
	ratioBar.config(font = ('Helvetica', 25))
	ratioBar.pack()
	ratioBar.place(x=450, y=820,height=50,anchor=NW)
	
	#updating the canvas
	s.update()
	
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

createRepl()
search()
s.bind("<Button-1>",searchClick)
root.mainloop()
