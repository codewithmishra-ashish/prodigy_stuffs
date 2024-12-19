from customtkinter import *
from CTkMessagebox import CTkMessagebox

# function to change properties of button on hover
def changeOnHover(button, colorOnHover, colorOnLeave):

	# adjusting backgroung of the widget
	# background on entering widget
	button.bind("<Enter>", func=lambda e: button.config(
		background=colorOnHover))

	# background color on leving widget
	button.bind("<Leave>", func=lambda e: button.config(
		background=colorOnLeave))


root = CTk()
root.title("Temp_Converter")
root.geometry("320x250")
root.resizable(0,0)
root._set_appearance_mode("dark")

value=0
active = False


#Button Functions OnCLick
def zero():
	if (active==True):
		value = value + 0.1
		return
	else:
	    value = value*10 +0	
def one():
	value = value*10 +1
	return
def two():
	value = value*10 +2	
	return
def three():
	value = value*10 +3	
	return
def four():
	value = value*10 +4	
	return
def five():
	value = value*10 +5	
	return
def six():
	value = value*10 +6	
	return
def seven():
	value = value*10 +7	
	return
def eight():
	value = value*10 +8	
	return
def nine():
	
	value = value*10 +9	
	return
def clear():
	value=0
	return
def dot():
	value = value+ 0.0
	active=True
	return
def delete():
	
	return
def convert():
	unit = optionmenu.get()
	if (unit =="Kelvin"):
		k = entry.get()
		
		return
	elif (unit=="Celcius"):
		return
	elif (unit=="Farenheit"):
		return
	else:
		CTkMessagebox(width=200,height=100,title="Error", message="Please enter the correct unit !!", icon="warning")
	print(unit)	
	return



gap1 = CTkLabel(root,
                text="",
                width=300,
                height=10,
                fg_color="transparent",
                bg_color="transparent")
gap1.grid(row=0,column=0,columnspan=3)



#Data Entry Section
frame = CTkFrame(root,
                 cursor="hand2")
frame.grid(row=1,column=0,columnspan=3, padx=5)

entry = CTkEntry(frame,
                 width=190,
                 corner_radius=0,
                 fg_color="white",
                 text_color="black",
                 placeholder_text="0",
                 placeholder_text_color="black")
entry.grid(row=0,column=0)

optionmenu = CTkOptionMenu(frame,
                           fg_color="black",
                           width=120,
                           corner_radius=0,
                           values=["Celcius", "Farenheit", "Kelvin"],
                           font=("Goudy Old Style", 20))
optionmenu.set("unit")
optionmenu.grid(row=0,column=1)



gap2 = CTkLabel(root, text="", width=300,fg_color="transparent",bg_color="transparent")
gap2.grid(row=2,column=0,columnspan=3)



#Button Initialization
but_C = CTkButton(root,
                  width=90, 
                  text="C",
                  text_color="black",
                  fg_color="white",
                  font=("Goudy Old Style", 20, "bold"))
but_convert = CTkButton(root, 
                        width=195, 
                        text="Convert",
                        text_color="black",
                        fg_color="white",
                        font=("Goudy Old Style", 20, "bold"),
						command=convert)
but_7 = CTkButton(root, 
                  width=90, 
                  text="7",
                  text_color="black",
                  fg_color="white", 
                  font=("Goudy Old Style", 20, "bold"))
but_8 = CTkButton(root, 
                  width=90, 
                  text="8",
                  text_color="black",
                  fg_color="white", 
                  font=("Goudy Old Style", 20, "bold"))
but_9 = CTkButton(root,
                  width=90, 
                  text="9",
                  text_color="black",
                  fg_color="white", 
                  font=("Goudy Old Style", 20, "bold"))
but_4 = CTkButton(root, 
                  width=90, 
                  text="4",
                  text_color="black",
                  fg_color="white", 
                  font=("Goudy Old Style", 20, "bold"))
but_5 = CTkButton(root, 
                  width=90, 
                  text="5",
                  text_color="black",
                  fg_color="white", 
                  font=("Goudy Old Style", 20, "bold"))
but_6 = CTkButton(root, 
                  width=90, 
                  text="6",
                  text_color="black",
                  fg_color="white", 
                  font=("Goudy Old Style", 20, "bold"))
but_1 = CTkButton(root, 
                  width=90, 
                  text="1",
                  text_color="black",
                  fg_color="white", 
                  font=("Goudy Old Style", 20, "bold"))
but_2 = CTkButton(root, 
                  width=90, 
                  text="2",
                  text_color="black",
                  fg_color="white", 
                  font=("Goudy Old Style", 20, "bold"))
but_3 = CTkButton(root, 
                  width=90, 
                  text="3",
                  text_color="black",
                  fg_color="white", 
                  font=("Goudy Old Style", 20, "bold"))
but_0 = CTkButton(root, 
                  width=90, 
                  text="0",
                  text_color="black",
                  fg_color="white", 
                  font=("Goudy Old Style", 20, "bold"))
but_dot = CTkButton(root, 
                  width=90, 
                  text=".",
                  text_color="black",
                  fg_color="white", 
                  font=("Goudy Old Style", 20, "bold"),
                  hover=False,
                  cursor="hand2")
but_del = CTkButton(root, 
                  width=90, 
                  text="Del",
                  text_color="black",
                  fg_color="white", 
                  font=("Goudy Old Style", 20, "bold"))



#Button Hover Effect 
but_C.bind("<Enter>", lambda event: but_C.configure(text_color="white",fg_color="blue")) 
but_C.bind("<Leave>", lambda event: but_C.configure(text_color="black",fg_color="white"))  
but_convert.bind("<Enter>", lambda event: but_convert.configure(text_color="white",fg_color="blue")) 
but_convert.bind("<Leave>", lambda event: but_convert.configure(text_color="black",fg_color="white"))  
but_7.bind("<Enter>", lambda event: but_7.configure(text_color="white",fg_color="blue")) 
but_7.bind("<Leave>", lambda event: but_7.configure(text_color="black",fg_color="white"))  
but_8.bind("<Enter>", lambda event: but_8.configure(text_color="white",fg_color="blue")) 
but_8.bind("<Leave>", lambda event: but_8.configure(text_color="black",fg_color="white"))  
but_9.bind("<Enter>", lambda event: but_9.configure(text_color="white",fg_color="blue")) 
but_9.bind("<Leave>", lambda event: but_9.configure(text_color="black",fg_color="white"))  
but_4.bind("<Enter>", lambda event: but_4.configure(text_color="white",fg_color="blue")) 
but_4.bind("<Leave>", lambda event: but_4.configure(text_color="black",fg_color="white"))  
but_5.bind("<Enter>", lambda event: but_5.configure(text_color="white",fg_color="blue")) 
but_5.bind("<Leave>", lambda event: but_5.configure(text_color="black",fg_color="white"))  
but_6.bind("<Enter>", lambda event: but_6.configure(text_color="white",fg_color="blue")) 
but_6.bind("<Leave>", lambda event: but_6.configure(text_color="black",fg_color="white"))  
but_1.bind("<Enter>", lambda event: but_1.configure(text_color="white",fg_color="blue")) 
but_1.bind("<Leave>", lambda event: but_1.configure(text_color="black",fg_color="white"))  
but_2.bind("<Enter>", lambda event: but_2.configure(text_color="white",fg_color="blue")) 
but_2.bind("<Leave>", lambda event: but_2.configure(text_color="black",fg_color="white"))  
but_3.bind("<Enter>", lambda event: but_3.configure(text_color="white",fg_color="blue")) 
but_3.bind("<Leave>", lambda event: but_3.configure(text_color="black",fg_color="white"))  
but_0.bind("<Enter>", lambda event: but_0.configure(text_color="white",fg_color="blue")) 
but_0.bind("<Leave>", lambda event: but_0.configure(text_color="black",fg_color="white"))  
but_dot.bind("<Enter>", lambda event: but_dot.configure(text_color="white",fg_color="blue")) 
but_dot.bind("<Leave>", lambda event: but_dot.configure(text_color="black",fg_color="white"))  
but_del.bind("<Enter>", lambda event: but_del.configure(text_color="white",fg_color="blue")) 
but_del.bind("<Leave>", lambda event: but_del.configure(text_color="black",fg_color="white"))  


#Button Grid
but_C.grid(row=3, column=0,padx=2,pady=3)
but_convert.grid(row=3, column=1,columnspan=2,padx=2,pady=3)
but_7.grid(row=4,column=0,padx=2,pady=3)
but_8.grid(row=4,column=1,padx=2,pady=3)
but_9.grid(row=4,column=2,padx=2,pady=3)
but_4.grid(row=5,column=0,padx=2,pady=3)
but_5.grid(row=5,column=1,padx=2,pady=3)
but_6.grid(row=5,column=2,padx=2,pady=3)
but_1.grid(row=6,column=0,padx=2,pady=3)
but_2.grid(row=6,column=1,padx=2,pady=3)
but_3.grid(row=6,column=2,padx=2,pady=3)
but_0.grid(row=7,column=0,padx=2,pady=3)
but_dot.grid(row=7,column=1,padx=2,pady=3)
but_del.grid(row=7,column=2,padx=2,pady=3)


root.mainloop()