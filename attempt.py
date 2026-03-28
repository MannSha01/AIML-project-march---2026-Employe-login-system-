# this is the first attempt of making this project


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
            talker_func("You wrote " + val_in_box + ". press enter again to confirm")
            waiting_on_second_enter = True
    else:
        user_guess = BOX_FOR_TYPING.get().strip().upper()
        
        if user_guess == CURRENT_SECRET_CODE:
            bottom_msg.config(text=f"WELCOME {NAME_ENTRY.get().upper()}! (ID: {ID_ENTRY.get()})", fg="green")
            talker_func("Verified. Welcome " + NAME_ENTRY.get())
            tally_of_fails = 0 
        else:
            tally_of_fails += 1
            bottom_msg.config(text="WRONG - Attempt #" + str(tally_of_fails), fg="red")
            talker_func("that is wrong. making a new one")
            BOX_FOR_TYPING.delete(0, 'end')
            Draw_New_Image_Function() 
            
        waiting_on_second_enter = False

def Draw_New_Image_Function():
    global CURRENT_SECRET_CODE
    width, height = 220, 90
    chars = string.ascii_uppercase + "23456789"
    CURRENT_SECRET_CODE = ''.join(random.choice(chars) for _ in range(4))
    
    main_img = Image.new("RGB", (width, height), (255, 255, 255))
    pen = ImageDraw.Draw(main_img)
    
    try:
        f = ImageFont.truetype("arial.ttf", 38)
    except:
        f = ImageFont.load_default()

    for i, ch in enumerate(CURRENT_SECRET_CODE):
        x = 25 + i * 45 + random.randint(-5, 5)
        y = random.randint(15, 25)
        color = (random.randint(0, 150), random.randint(0, 100), random.randint(0, 150))
        pen.text((x, y), ch, font=f, fill=color)

    for _ in range(5):
        start = (random.randint(0, width), random.randint(0, height))
        end = (random.randint(0, width), random.randint(0, height))
        pen.line([start, end], fill=(150, 150, 150), width=1)

    for _ in range(100):
        px = random.randint(0, width)
        py = random.randint(0, height)
        pen.point((px, py), fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

    tk_img = ImageTk.PhotoImage(main_img)
    DISPLAY_LABEL.config(image=tk_img)
    DISPLAY_LABEL.image = tk_img 
    talker_func("new code is: " + " ".join(CURRENT_SECRET_CODE))

main_win = tk.Tk()
main_win.title("Internal Security v0.9 - 2AM Build")
main_win.geometry("400x700")

tk.Label(main_win, text="EMPLOYEE VERIFICATION", font=("Verdana", 12, "bold")).pack(pady=10)

tk.Label(main_win, text="Full Name:").pack()
NAME_ENTRY = tk.Entry(main_win, font=("Arial", 12), width=25)
NAME_ENTRY.pack(pady=5)

tk.Label(main_win, text="Office ID:").pack()
ID_ENTRY = tk.Entry(main_win, font=("Arial", 12), width=25)
ID_ENTRY.pack(pady=5)

hr = tk.Frame(main_win, height=2, bg="black")
hr.pack(fill='x', padx=50, pady=15)

DISPLAY_LABEL = tk.Label(main_win, bg="#f0f0f0", bd=2, relief="sunken")
DISPLAY_LABEL.pack(pady=5)

tk.Label(main_win, text="Enter Captcha Below:", font=("Arial", 8, "italic")).pack()
BOX_FOR_TYPING = tk.Entry(main_win, font=("Consolas", 26), width=12, justify='center')
BOX_FOR_TYPING.pack(pady=10)
BOX_FOR_TYPING.bind("<Return>", handle_keypress_logic)

tk.Button(main_win, text="[ CHECK ACCESS ]", command=lambda: handle_keypress_logic(None), bg="#e1e1e1", width=20).pack(pady=5)
tk.Button(main_win, text="cant read? refresh", command=Draw_New_Image_Function, font=("Arial", 9), bd=0).pack()
tk.Button(main_win, text="Speak Code", command=lambda: talker_func("The code is " + " ".join(CURRENT_SECRET_CODE)), font=("Arial", 8)).pack()

bottom_msg = tk.Label(main_win, text="system ready...", font=("Courier", 10))
bottom_msg.pack(side="bottom", pady=20)

Draw_New_Image_Function()
main_win.mainloop()
