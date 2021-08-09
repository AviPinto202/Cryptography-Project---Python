import tkinter as tk
from tkinter import filedialog as fd, filedialog
from tkinter.messagebox import showinfo


def rot47_enc(text, key, output_label, choice):
    """Function of encrypt"""
    # get the text and the key from the user
    text = text.get("1.0", "end")
    text = str(text).replace("\n", "").strip()  # fix bug in text widget
    key = key.get("1.0", "end")
    key = key.replace("\n", "").strip()

    encrypt_text = ""
    # check if the key is not number show error message
    if not str(key).isdigit():
        showinfo(title='Error', message="Key must be numbers !!!")
    # else do the encrypt
    else:
        for i in range(len(text)):
            temp = ord(text[i]) + int(key)  # get the num of ascii and addition with the key number
            if ord(text[i]) == 32:  # if the num of the ascii table == 32
                encrypt_text += " "
            elif temp > 126:
                temp -= 94
                encrypt_text += chr(temp)
            else:
                encrypt_text += chr(temp)

    # Check what user selected (clicked) and prints according to the choice he made
    if choice == "Encrypt":
        output_label["text"] = encrypt_text
    if choice == "Encrypt to file" and str(key).isdigit():
        f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")  # open dialog to save the file
        if f is None:  # if the file save canceled show error message
            showinfo(title='Error', message="Save file not completed")
            return
        f.write(encrypt_text)
        f.close()
        output_label["text"] = "Successes write to file"
    else:
        pass


def rot47_dec(text, key, output_label, choice):
    """Function of Decrypt"""
    # get the text and the key from the user
    try:
        text = text.get("1.0", "end")
        text = str(text).replace("\n", "").strip()  # fix bug in text widget
        key = key.get("1.0", "end")
        key = key.replace("\n", "").strip()

    except:
        text = str(text)
        text = str(text).replace("\n", "").strip()  # fix bug in text widget
        key = str(key)

    decrypt_text = " "
    # check if the key is not number show error message
    if not str(key).isdigit():
        showinfo(title='Error', message="Key must be numbers !!!")
    # else do the encrypt
    else:
        for i in range(len(text)):
            temp = ord(text[i]) - int(key)
            if ord(text[i]) == 32:
                decrypt_text += " "
            elif temp < 32:
                temp += 94
                decrypt_text += chr(temp)
            else:
                decrypt_text += chr(temp)

    # Check what user selected And prints according to the choice he made
    if choice == "BruteForce":
        return decrypt_text
    if choice == "Decrypt":
        output_label["text"] = decrypt_text
        print(choice)
    if choice == "Decrypt to file":
        print(choice)
        f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")  # open dialog to save the file
        if f is None:  # if the file save canceled show error message
            showinfo(title='Error', message="Save file not completed")
            return
        f.write(decrypt_text)
        f.close()
        output_label["text"] = "Successes write to file"
    else:
        pass

    return decrypt_text


def brute_Force(text_enc, text_dec, output_label):
    """function of brute force"""
    # output_label.delete('1.0', "end")
    # get the encrypt text and the original text from the user
    text_enc = text_enc.get("1.0", "end")
    text_enc = str(text_enc).replace("\n", "").strip()
    text_dec = text_dec.get("1.0", "end")
    text_dec = str(text_dec).replace("\n", "").strip()

    count_key = 1
    found = False

    while not count_key == 100:
        res = rot47_dec(text_enc, str(count_key).strip(), output_label, "BruteForce")
        if text_dec in res:
            output_label["text"] = "key = " + str(count_key) + " " + res + "= successes " + "\n"
            return
        count_key = count_key + 1
    if not found:
        output_label.insert(tk.INSERT, "Not Found")


def select_file(text):
    """function of select file of text to encrypt or decrypt"""
    # try to open the file and insert the text in to the text widget
    try:
        text.delete("1.0", "end")
        filetypes = (('text files', '*.txt'), ('All files', '*.*'))
        filename = fd.askopenfilename(title='Open a file', initialdir='/', filetypes=filetypes)
        f = open(filename, "r")
        text.insert("1.0", f.read())
    # if not selected file show error message
    except:
        showinfo(title='Selected File', message="not file selected")


def brute_Force_window():
    """function to create new window for the brute force"""
    root2 = tk.Tk()
    root2.geometry("500x500")
    root2.title("Brute Force")
    root2.configure(bg='#e5e5e5')

    titleTextEnter = tk.Label(root2, text="Enter Encrypt Text", font=('Helvetica', 10, "bold"), bg='#e5e5e5')
    titleTextEnter.pack(pady=5)
    # text widget to enter the encrypt text
    encrypt_Text = tk.Text(root2, font='Arial 10', bg='#e5383b', width=45, height=5)
    encrypt_Text.pack()

    titleTextEnter2 = tk.Label(root2, text="Enter Decrypt Text", font=('Helvetica', 10, "bold"), bg='#e5e5e5')
    titleTextEnter2.pack(pady=5)
    # text widget to enter the decrypt text
    decrypt_text = tk.Text(root2, font='Arial 10', bg='#e5383b', width=45, height=5)
    decrypt_text.pack(pady=5)

    bruteforce_btn = tk.Button(root2, text="Brute Force",
                               command=lambda: brute_Force(encrypt_Text, decrypt_text, output_label),
                               font=('Helvetica', 10, "bold"))
    bruteforce_btn.pack(pady=5)

    Result_label = tk.Label(root2, text="Result :", height=2, font=('Helvetica', 10, "bold"), bg='#e5e5e5')
    Result_label.pack()

    output_label = tk.Label(root2, text="", font='Arial 10', bg="#e5383b", width=40, height=5)
    output_label.pack(pady=0)


def help_window():
    """function to create the help window"""
    root3 = tk.Tk()
    root3.geometry("600x250")
    root3.title("Help")
    root3.configure(bg='#e5e5e5')

    help_txt = tk.Label(root3, text="ROT 47 Chipper\n \nEnter Text or Chose file to encrypt or decrypt " +
                                    "\nand then chose a key number. \nThere is also an option to\n encrypt or decrypt "
                                    "the text "
                                    "into a new text file.\n"
                                    "You can also to find the key with the help of Brute Force.",
                        font=('Helvetica', 12, "bold"), bg="#e5e5e5", width=60, height=7)
    help_txt.pack(pady=5)

    name_txt = tk.Label(root3, text="Avi Pinto ",
                        font=('Helvetica', 12, "bold"), bg="#e5e5e5", width=60, height=7)
    name_txt.pack(pady=20)


def main():
    """ create the main window"""
    root = tk.Tk()
    root.geometry("800x600")
    root.title("Rot 47 Chipper")
    root.configure(bg='#e5e5e5')
    selection = tk.StringVar()
    # vigenere_enc()

    # the top menu
    menuBar = tk.Menu(root)
    menuBar.add_command(label="Brute Force", command=brute_Force_window)
    menuBar.add_command(label="Help",
                        command=help_window)
    menuBar.add_command(label="Quit", command=root.quit)
    root.config(menu=menuBar)

    titleTextEnter = tk.Label(root, text="Enter Text", font=('Helvetica', 10, "bold"), bg='#e5e5e5')
    titleTextEnter.pack(pady=0)

    # text widget to enter the text you want the encrypt or decrypt
    text = tk.Text(root, font='Arial 10', bg='#e5383b', width=45, height=4)
    text.pack(pady=5)

    titleKeyEnter = tk.Label(root, text="Enter Key (Numbers only)", font=('Helvetica', 10, "bold"), bg='#e5e5e5')
    titleKeyEnter.pack(pady=0)

    # text widget to enter the key (shift)
    key = tk.Text(root, font='Arial 10', bg='#e5383b', width=45, height=4)
    key.pack()

    titleKeyEnter = tk.Label(root, text="Open file to Encrypt or Decrypt", font=('Helvetica', 10, "bold"), bg='#e5e5e5')
    titleKeyEnter.pack(pady=0)

    # button to select file to encrypt or decrypt
    OpenFile_btn = tk.Button(root, text="Open File",
                             command=lambda: select_file(text),
                             font='Arial 10')
    OpenFile_btn.pack()

    Select_label = tk.Label(text="Select Encrypt or Decrypt :", height=2, width=45, font=('Helvetica', 10, "bold"),
                            bg='#e5e5e5')
    Select_label.pack()
    selection.set('null')

    Encrypt_btn = tk.Radiobutton(root, text="Encrypt", value='Encrypt', variable=selection,
                                 command=lambda: rot47_enc(text, key, output_label, "Encrypt"),
                                 font='Arial 10', bg='#e5e5e5')
    Encrypt_btn.pack()

    Decrypt_btn = tk.Radiobutton(root, text="Decrypt", value='Decrypt', variable=selection,
                                 command=lambda: rot47_dec(text, key, output_label, "Decrypt"),
                                 font='Arial 10', bg='#e5e5e5')
    Decrypt_btn.pack()

    Select_label2 = tk.Label(text="Select Encrypt or Decrypt to file:", height=2, width=45,
                             font=('Helvetica', 10, "bold"),
                             bg='#e5e5e5')
    Select_label2.pack()

    # button to activate the functions of Encrypt or Decrypt
    EncryptToFile_btn = tk.Radiobutton(root, text="Encrypt to file", font='Arial 10', value='Encrypt to file',
                                       variable=selection, bg='#e5e5e5',
                                       command=lambda: rot47_enc(text, key, output_label, "Encrypt to file"))
    EncryptToFile_btn.pack(padx=5, pady=5)

    DecryptToFile_btn = tk.Radiobutton(root, text="Decrypt to file", font='Arial 10', value='Decrypt to file',
                                       variable=selection, bg='#e5e5e5',
                                       command=lambda: rot47_dec(text, key, output_label, "Decrypt to file"))
    DecryptToFile_btn.pack()

    Result_label = tk.Label(text="Result :", height=2, font=('Helvetica', 10, "bold"), bg='#e5e5e5')
    Result_label.pack()

    output_label = tk.Label(font=('Helvetica', 10, "bold"), bg="#e5383b", width=45, height=5, relief="ridge",
                            borderwidth=2)
    output_label.pack()

    # button to open the brute force window
    BruteForce_btn = tk.Button(root, text="Brute Force", bg="#f25c54",
                               command=brute_Force_window,
                               font=('Helvetica', 10, "bold"))
    BruteForce_btn.pack(pady=5)

    tk.mainloop()


if __name__ == "__main__":
    main()
