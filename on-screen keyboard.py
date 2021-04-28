from tkinter import *
import tkinter

def keyboard():
    kb = tkinter.Toplevel(root)
    global buttons
    buttons = [
        '~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '0', '_', '-',
        'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '\\', '7', '8', '9', 'BACK',
        'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', '[', ']', '4', '5', '6'
        , 'TAB',
        'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '?', '/', '1', '2', '3', 'ENTER', 'SPACE', 'CAPS'
    ]
    global caps_status
    caps_status = False

    def select(value):
        if value == "BACK":
            # allText = entry.get()[:-1]
            # entry.delete(0, tkinter,END)
            # entry.insert(0,allText)

            # content_text.delete(len(content_text.get()) - 1, tkinter.END)
            input_val = content_text.get("1.0", 'end-2c')
            content_text.delete("1.0", "end")
            content_text.insert("1.0", input_val, "end")

        elif value == "SPACE":
            content_text.insert(tkinter.END, ' ')
        elif value == "TAB":
            content_text.insert(tkinter.END, '\t')
        elif value == "ENTER":
            content_text.insert(tkinter.END, '\n')
        elif value == "CAPS":
            global caps_status
            global buttons
            if caps_status == True:
                caps_status = False
                buttons = [
                    '~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '0', '_', '-',
                    'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '\\', '7', '8', '9', 'BACK',
                    'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', '[', ']', '4', '5', '6'
                    , 'TAB',
                    'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '?', '/', '1', '2', '3', 'ENTER', 'SPACE', 'CAPS'
                ]
                HosoPop()
            elif caps_status == False:
                caps_status = True
                buttons = [
                    '~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '0', '_', '-',
                    'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '\\', '7', '8', '9', 'BACK',
                    'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', '[', ']', '4', '5', '6'
                    , 'TAB',
                    'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '?', '/', '1', '2', '3', 'ENTER', 'SPACE', 'CAPS'
                ]
                HosoPop()

        else:
            content_text.insert(tkinter.END, value)

    def HosoPop():
        varRow = 1
        varColumn = 0
        Font_tuple = ("Helvetica", 10, "bold")

        for button in buttons:
            command = lambda x=button: select(x)
            if button != "SPACE":
                but = Button(kb, text=button, font=Font_tuple, width=5, bg="#D1E7E0", fg="#5B8340",
                             highlightthickness=4,
                             activebackground="gray65", highlightcolor='red', activeforeground="#000000",
                             relief="raised", padx=8,
                             pady=4, bd=4, command=command)
                # buttonL[varRow - 1].append(but)
                but.grid(row=varRow, column=varColumn)

            if button == "SPACE":
                but = Button(kb, text=button, font=Font_tuple, width=60, bg="#D1E7E0", fg="#5B8340",
                             highlightthickness=4,
                             activebackground="gray65", highlightcolor='red', activeforeground="#000000",
                             relief="raised", padx=4,
                             pady=4, bd=4, command=command)
                # buttonL[varRow - 1].append(but)
                varRow += 1
                but.grid(row=varRow, columnspan=18)

            varColumn += 1
            if varColumn > 14:
                varColumn = 0
                varRow += 1
                # buttonL.append([])

    def main():
        kb.title("On-screen Keyboard")
        # global keyboard_icon
        kb.iconphoto(False, PhotoImage(file="icons/keyboard.png"))
        kb.resizable(0, 0)
        HosoPop()

        kb.mainloop()

    main()

root=Tk()
root.title("Keyboard")
root.iconbitmap('icons/keyboard.png')
content_text = Text(root,wrap='word')
content_text.pack(expand='yes', fill='both')
Button(root, text="TYPE", bg="#D1E7E0", fg="#5B8340",
                             highlightthickness=4,
                             activebackground="gray65", highlightcolor='red', activeforeground="#000000",
                             relief="raised", padx=4,
                             pady=4, bd=4, command=keyboard).pack()

root.mainloop()