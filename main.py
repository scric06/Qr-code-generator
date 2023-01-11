import qrcode
import customtkinter

error = False

def generate_qr():
    global error
    if (len(data.get()) > 0):
        img = qrcode.make(str(data.get()))
        img.save("image.png")
        print(data.get())
        if error:
            error.destroy()

        complete = customtkinter.CTkLabel(master=root,
        text="generate!", font=('Arial',25), text_color="green")

        complete.pack()

    else:
        error = True
        error = customtkinter.CTkLabel(master=root, 
        text="insert data!", font=('Arial',25), text_color="red")

        error.pack()

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x150")
root.title("Qr Code Generator")

data = customtkinter.CTkEntry(master=root, placeholder_text="data")
data.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=root, text="generate", 
command=generate_qr)

button.pack(pady=12, padx=10)

root.mainloop()
