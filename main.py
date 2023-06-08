import json
import string
import random
import tkinter
from tkinter import Frame


class Encrypting_stuff:

    def create_password(*self):
        alphabet = list(string.ascii_letters)
        random.shuffle(alphabet)
        password = {letter: replace for letter, replace in zip(string.ascii_letters, alphabet)}
        return password


    def encrypt(password, sentence):
        encrypted_sentence = "".join(password.get(letter, letter) for letter in sentence)
        return encrypted_sentence


    def decrypt(password, encrypted_sentence):
        reverse_password = {v: k for k, v in password.items()}
        decrypted_sentence = "".join(reverse_password.get(letter, letter) for letter in encrypted_sentence)
        return decrypted_sentence


    def save_password(password, file_path):
        with open(file_path, 'w') as file:
            json.dump(password, file)


    def load_password(file_path):
        with open(file_path, 'r') as file:
            password = json.load(file)
        return password


def execute_replace_alphabet():
    sentence = text.get("1.0", 'end-1c')
    password = Encrypting_stuff.create_password()
    encrypted_sentence = Encrypting_stuff.encrypt(password, sentence)
    text.delete("1.0", tkinter.END)
    text.insert("1.0", encrypted_sentence)
    save_path = name.get()
    Encrypting_stuff.save_password(password, save_path)


def execute_decrypt():
    sentence = text.get("1.0", 'end-1c')
    load_path = name.get()
    password = Encrypting_stuff.load_password(load_path)
    decrypted_sentence = Encrypting_stuff.decrypt(password, sentence)
    text.delete("1.0", tkinter.END)
    text.insert("1.0", decrypted_sentence)


root = tkinter.Tk()
root.geometry("1280x720")
root.title("Message Coder/Decoder")
frame = Frame(root)
text = tkinter.Text(root, width=20, font=('Arial', 16))
text.pack(side="left", fill="both", expand=True)
text.pack(padx=10, pady=10)
frame.pack(side="right", fill="both", expand=False)
label = tkinter.Label(frame, text='''
Hello and welcome to the encryptor/decryptor.
1. Enter some text on the left.
2. Select the desired action.
Please note that the passwords are saved 
in the project's directory.
''', font=('Arial', 18))
label2 = tkinter.Label(frame, text='Enter the name of the password')
button1 = tkinter.Button(frame, text="Encrypt", font=('Arial', 16), command=execute_replace_alphabet)
button2 = tkinter.Button(frame, text="Decrypt", font=('Arial', 16), command=execute_decrypt)
frame.pack(side="right", fill="both", expand=False)
name = tkinter.Entry(frame)

label.grid(row=0, padx=10, column=0, pady=10)
button1.grid(row=1, padx=10, column=0, pady=10)
button2.grid(row=2, padx=10, column=0, pady=10)
label2.grid(row=3, padx=10, column=0, pady=10)
name.grid(row=4, padx=10, column=0, pady=10)

frame.grid_rowconfigure(100, weight=1)
frame.grid_columnconfigure(2, weight=1)

root.mainloop()
