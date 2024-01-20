import tkinter as tk

def atbash(text):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    cipher = {alphabet[i]: alphabet[-i-1] for i in range(len(alphabet))}
    result = ''

    for l in text.upper():
        if l in cipher:
            result += cipher[l]
        else:
            result += l

    return result

def process_input():
    choice = var.get()
    user_input = text_input.get()
    if choice == 1:
        result = atbash(user_input)
    elif choice == 2:
        result = atbash(user_input)
    else:
        result = "Invalid choice"
    result_text.delete("1.0", tk.END) 
    result_text.insert(tk.END, result)  

r = tk.Tk()
r.title("Atbash Cipher")
var = tk.IntVar()
cipher_rb = tk.Radiobutton(r, text="Cipher", variable=var, value=1)
decipher_rb = tk.Radiobutton(r, text="Decipher", variable=var, value=2)
cipher_rb.pack()
decipher_rb.pack()

text_input = tk.Entry(r)
text_input.pack()

process_button = tk.Button(r, text="Process", command=process_input)
process_button.pack()

result_text = tk.Text(r, height=4, width=50)
result_text.pack()

r.mainloop()
