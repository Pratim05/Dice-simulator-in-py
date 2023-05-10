import tkinter as tk
from PIL import Image, ImageTk
import random
window = tk.Tk()
window.geometry("500x360")
window.title("Pratim's Dice simulator")



dice =  ["inverted-dice-1.png", "inverted-dice-2.png", "inverted-dice-3.png", "inverted-dice-4.png", "inverted-dice-5.png", "inverted-dice-6.png"]

#TO RESIZE THE IMAGE 100 x 100
# for i in dice:
#     img = i
#     r_image = Image.open(img)
#     r_image = r_image.resize((100,100))
#     r_image.save(img)


image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

label1 = tk.Label(window,image=image1)
label2 = tk.Label(window,image=image2)

label1.image  = image1
label2.image  = image2

label1.place(x= 100, y=100)
label2.place(x= 300, y=100)


def roll_dice():
   image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
   label1.configure(image = image1)
   label1.image = image1

   image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
   label2.configure(image = image2)
   label2.image = image2




button =  tk.Button(window,text='ROLL', bg = "green", fg = "white" , font = ("Comic Sans MS", 15 ,"bold"), activebackground= "red", relief="ridge",borderwidth=5 , width= 10, command = roll_dice)
button.place(x =190, y=10)
window.mainloop()