from PIL import Image , ImageDraw , ImageFont , ImageFilter , ImageTk
import random
import string 
import tkinter as tk
from PIL import ImageTk
import pyttsx3 
# creating captcha only







func = pyttsx3.init()
entcount = 0  # giving function for everytime enter press like for first time it will say what you have writtten (for blind) and ask you to press again to verify 
def eve (event):
    global entcount
    entcount += 1

    if entcount == 1:
        
        text = entry.get()
        if text:
            func.say("yOu have typed: " + text + "press enter again to confirm,")
            
    elif entcount == 2:
        # verify captcha
        checking ()
        entcount = 0 


def make_cap(len = 4 , width = 190 , height =70):
    chars = string.ascii_uppercase + string.digits
    cap_text = ''.join(random.choice(chars) for i in range(len ))


    imag = Image.new("RGB" , (width,height), (255,255,255))
    draw = ImageDraw.Draw(imag)
    font = ImageFont.truetype("arial.ttf", 40)
    


    for i , ch in enumerate(cap_text):
        x = 20 + i*25 + random.randint(-3,3)
        y = 20 + random.randint(-5, 5)
        color = (random.randint(0,150), random.randint(0,150), random.randint(0,150))
        draw.text((x, y), ch, font=font, fill=color)
    for _ in range(4):
        start = (random.randint(0, width), random.randint(0, height))
        end = (random.randint(0, width), random.randint(0, height))
        draw.line([start, end], fill=(0, 0, 0), width=2)

    for _ in range(80):
        x = random.randint(0, width)
        y = random.randint(0, height)
        draw.point((x, y), fill=(random.randint(0,255), random.randint(0,255), random.randint(0,255)))

    
    func.say("Please type the following code in uppercase only: " + " ".join(cap_text))
    func.runAndWait()


    return cap_text, imag
def RefRESh():
    global cap_text, cap_img, cap_tk
    cap_text, cap_img = make_cap()
    cap_tk = ImageTk.PhotoImage(cap_img)
    cap_label.config(image=cap_tk)
    cap_label.image = cap_tk
    func.say("New captcha code is: " + " ".join(cap_text))
    
  

  
def checking ():
    user_input = entry.get()
    if user_input == cap_text:
        result_label.config(text=" Captcha verified ")
        func.say("Captcha verified")
    else:
        result_label.config(text=" Captcha Failed")
        func.say("captcha failed ")

def speak_for_upcase():
    func.say("Please type the following code in uppercase only: " + " ".join(cap_text))
    



# Creating tkiner setup this will help us to open a userinterface in pythpn 

root = tk.Tk()
root.title("CAP Demo")

cap_text, cap_img = make_cap()
cap_tk = ImageTk.PhotoImage(cap_img)

cap_label = tk.Label(root, image=cap_tk)
cap_label.pack(pady=10)

entry = tk.Entry(root, font=("Bold", 14))
entry.pack(pady=5)
entry.bind("<Return>", eve)
tk.Button(root, text="Verify", command=checking ).pack(pady=5)
tk.Button(root, text="Refresh CAP", command=RefRESh).pack(pady=5)
tk.Button(root, text=" Speak CAPTCHA ", command=speak_for_upcase).pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()

