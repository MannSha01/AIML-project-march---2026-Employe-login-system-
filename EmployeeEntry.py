from PIL import Image, ImageDraw, ImageFont, ImageTk, ImageFilter
import random, string, tkinter as tk, pyttsx3, _thread



v_engine = pyttsx3.init()
CURRENT_SECRET_CODE = "" 
tally_of_fails = 0 
waiting_on_second_enter = False

def talker_func(what_to_say):
    def _do_it():
        try:
            local_v = pyttsx3.init()
            local_v.say(what_to_say)
            local_v.runAndWait()
        except: 
            pass
    _thread.start_new_thread(_do_it, ())

def handle_keypress_logic(e):
    global waiting_on_second_enter, tally_of_fails
    
    val_in_box = BOX_FOR_TYPING.get()
    
    if not NAME_ENTRY.get() or not ID_ENTRY.get():
        talker_func("Please enter your name and office I D first")
        bottom_msg.config(text="ERROR: MISSING CREDENTIALS", fg="orange")
        return

    if waiting_on_second_enter == False:
        if len(val_in_box) == 0:
            talker_func("the box is empty type something")
        else:
            
            talker_func("yOu have typed: " + val_in_box + "press enter again to confirm,")
            waiting_on_second_enter = True
    else:
        user_guess = BOX_FOR_TYPING.get().strip().upper()
        
        if user_guess == CURRENT_SECRET_CODE:
            bottom_msg.config(text=" Captcha verified ", fg="green")
            talker_func("Captcha verified")
            
            talker_func("Welcome " + NAME_ENTRY.get())
            tally_of_fails = 0 
        else:
            tally_of_fails += 1
            bottom_msg.config(text=" Captcha Failed", fg="red")
            talker_func("captcha failed ")
            BOX_FOR_TYPING.delete(0, 'end')
            Draw_New_Image_Function() 
            
        waiting_on_second_enter = False



def Draw_New_Image_Function():
    global CURRENT_SECRET_CODE
    width, height = 220, 90
    chars = string.ascii_uppercase + string.digits
    CURRENT_SECRET_CODE = ''.join(random.choice(chars) for _ in range(4))
    
    main_img = Image.new("RGB", (width, height), (255, 255, 255))
    pen = ImageDraw.Draw(main_img)
    
    try:
        f = ImageFont.truetype("arial.ttf", 40)
    except:
        f = ImageFont.load_default()

    
    for i, ch in enumerate(CURRENT_SECRET_CODE):
        x = 20 + i * 45 + random.randint(-3, 3)
        y = 20 + random.randint(-5, 5)
        color = (random.randint(0, 150), random.randint(0, 150), random.randint(0, 150))
        pen.text((x, y), ch, font=f, fill=color)

    for _ in range(4):
        start = (random.randint(0, width), random.randint(0, height))
        end = (random.randint(0, width), random.randint(0, height))
        pen.line([start, end], fill=(0, 0, 0), width=2)

    for _ in range(80):
        px = random.randint(0, width)
        py = random.randint(0, height)
        pen.point((px, py), fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

    tk_img = ImageTk.PhotoImage(main_img)
    DISPLAY_LABEL.config(image=tk_img)
    DISPLAY_LABEL.image = tk_img 
    
    
    talker_func("Please type the following code in uppercase only: " + " ".join(CURRENT_SECRET_CODE))
    

# UI 
main_win = tk.Tk()
main_win.title("CAP Demo - Security Merge")
main_win.geometry("400x700")

tk.Label(main_win, text="EMPLOYEE VERIFICATION", font=("Verdana", 12, "bold")).pack(pady=10)

tk.Label(main_win, text="Full Name:").pack()
NAME_ENTRY = tk.Entry(main_win, font=("Arial", 12), width=25)
NAME_ENTRY.pack(pady=5)

tk.Label(main_win, text="Office ID:").pack()
ID_ENTRY = tk.Entry(main_win, font=("Arial", 12), width=25)
ID_ENTRY.pack(pady=5)

tk.Frame(main_win, height=2, bg="black").pack(fill='x', padx=50, pady=15)

DISPLAY_LABEL = tk.Label(main_win, bg="#f0f0f0")
DISPLAY_LABEL.pack(pady=10)

BOX_FOR_TYPING = tk.Entry(main_win, font=("Bold", 14), width=15, justify='center')
BOX_FOR_TYPING.pack(pady=5)
BOX_FOR_TYPING.bind("<Return>", handle_keypress_logic)

tk.Button(main_win, text="Verify", command=lambda: handle_keypress_logic(None)).pack(pady=5)
tk.Button(main_win, text="Refresh CAP", command=Draw_New_Image_Function).pack(pady=5)
tk.Button(main_win, text=" Speak CAPTCHA ", command=lambda: talker_func("Please type the following code in uppercase only: " + " ".join(CURRENT_SECRET_CODE))).pack(pady=5)

bottom_msg = tk.Label(main_win, text="", font=("Arial", 12))
bottom_msg.pack(pady=10)

Draw_New_Image_Function()
main_win.mainloop()
