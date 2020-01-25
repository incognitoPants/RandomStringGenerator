#!/usr/bin/env python3
"""
Random String Generator
Python Version: 3.7 or 3.8

Generates a random alphanumeric string of 12 characters on user click. String is automatically copied to the user's
clipboard.

Notes:
    - Requires compilation using pyinstaller or something similar. Running on script on console may generate unintended
    results

    - You can change the length of the output by modifying the range of the for loop from 12 to your desired length

    - Destroying Label1 and Label2 creates issues when compiled on Windows; The string will be copied, but neither
    labels will display
"""

import random
import tkinter as tk

root = tk.Tk()
root.title("Random String Generator")
canvas1 = tk.Canvas(root, width=300, height=300)
canvas1.pack()


# 12-character random number generator
def random_string_gen():
    random.seed()
    r_string = ""
    # change range number into your desired string length
    for x in range(12):
        r_type = random.randint(1, 3)
        if r_type == 1:
            r_chr = random.randint(48, 57)

        if r_type == 2:
            r_chr = random.randint(65, 90)

        if r_type == 3:
            r_chr = random.randint(97, 122)

        r_string = r_string + chr(r_chr)

    label1 = tk.Label(root, text=r_string, fg="black", font=("helvetica", 12, "bold"))
    canvas1.create_window(150, 200, window=label1)
    label2 = tk.Label(root, text="Copied to clipboard!", font=("helvetica", 12))
    canvas1.create_window(150, 225, window=label2)
    clip = tk.Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append(r_string)
    clip.update()
    clip.destroy()

    # remove these if compiling for Windows
    label1.destroy()
    label2.destroy()


button1 = tk.Button(text="Click Me", command=random_string_gen, fg="black", bg ="white")
canvas1.create_window(150, 150, window=button1)


root.mainloop()
