import time
from tkinter import messagebox, Toplevel
from tkinter import ttk
from customtkinter import CTkFont
import customtkinter as ctk
from dataBase import *
from typing import List
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

def main():

    def submitSell():
        new_window = ctk.CTkToplevel(root)
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        new_window.geometry(f"{screen_width}x{screen_height}+0+0")

        new_window.columnconfigure(0, weight=1)
        new_window.columnconfigure(1, weight=0)

        topLabel = ctk.CTkLabel(new_window,text="ثبت فروش",
                                font=("IranNastaliq", 60),
                                fg_color="#426DE6",
                                height=55)
        topLabel.grid(row=0,column=0,sticky="ew",padx=5,pady=15)

        nameVar = ctk.StringVar()
        entryName = ctk.CTkEntry(new_window,
                                 font=("Arial", 45),
                                 height=40,
                                 border_color="white",
                                 border_width=1,
                                 textvariable=nameVar,
                                 justify="right"
                                 )
        entryName.grid(row=1, column=0, sticky="ew", padx=5, pady=15)
        nameLabel = ctk.CTkLabel(new_window, text="نام کالا",
                                 font=("IranNastaliq", 45))
        nameLabel.grid(row=1, column=1, sticky="e", padx=10, pady=15)

        # Label and Entry for Price
        priceVar = ctk.StringVar()
        entryPrice = ctk.CTkEntry(new_window,
                                  font=("IranNastaliq", 45),
                                  height=40,
                                  border_color="white",
                                  border_width=1,
                                  textvariable=priceVar,
                                  justify='right'
                                  )
        entryPrice.grid(row=2, column=0, sticky="ew", padx=10, pady=15)
        priceLabel = ctk.CTkLabel(new_window, text="مبلغ دریافتی",
                                  font=("IranNastaliq", 45))
        priceLabel.grid(row=2, column=1, sticky="e", padx=5, pady=15)

        # Label and Entry for Color
        colorVar = ctk.StringVar()
        entryColor = ctk.CTkEntry(new_window,
                                  font=("IranNastaliq", 45),
                                  height=40,
                                  border_color="white",
                                  border_width=1,
                                  textvariable=colorVar,
                                  justify='right'
                                  )
        entryColor.grid(row=3, column=0, sticky="ew", padx=5, pady=15)
        colorLabel = ctk.CTkLabel(new_window, text="رنگ",
                                  font=("IranNastaliq", 45))
        colorLabel.grid(row=3, column=1, sticky="e", padx=10, pady=15)

        # Label and Entry for Number
        numVar = ctk.StringVar()
        entryNumber = ctk.CTkEntry(new_window,
                                   font=("Arial", 45),
                                   height=40,
                                   border_color="white",
                                   border_width=1,
                                   textvariable=numVar,
                                   justify='right'
                                   )
        entryNumber.grid(row=4, column=0, sticky="ew", padx=5, pady=15)
        numberLabel = ctk.CTkLabel(new_window, text="شماره موبایل",
                                   font=("Arial", 45))
        numberLabel.grid(row=4, column=1, sticky="e", padx=10, pady=15)

        # Label and ComboBox for Tag
        tagVariable = ctk.StringVar()
        with open("tags.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
        entryTag = ctk.CTkComboBox(new_window,
                                   values=lines,
                                   variable=tagVariable,
                                   font=("Arial", 45),
                                   height=40,
                                   border_color="white",
                                   border_width=1,
                                   justify='right'
                                   )
        entryTag.grid(row=5, column=0, sticky="ew", padx=5, pady=15)
        tagLabel = ctk.CTkLabel(new_window, text="تگ",
                                font=("IranNastaliq", 45))
        tagLabel.grid(row=5, column=1, sticky="e", padx=10, pady=15)
        entryTag.set(lines[-1].strip())

        # Create the main window
        submitBut = ctk.CTkButton(new_window,
                                  text=" ثبت فروش ",
                                  command=lambda:submit(nameVar,priceVar,colorVar,numVar,tagVariable),
                                  width=40,
                                  height=10
                                  )
        submitBut.grid(row=6, column=0, columnspan=2)
        new_window.lift()
        new_window.focus_set()
        new_window.attributes('-topmost', True)
        new_window.attributes('-topmost', False)
        def submit(entryName:ctk.StringVar,entryPrice:ctk.StringVar,entryClolor:ctk.StringVar,entrynum:ctk.StringVar,entryTag:ctk.StringVar):
            try:
                add_row(entryName.get(),entryPrice.get(),entryTag.get(),entrynum.get(),entryClolor.get())
                time.sleep(2)
                new_window.destroy()
            except:
                messagebox.showerror("اضافه کردن با شکست مواجه شد")
    def Tag():
        new_window = ctk.CTkToplevel()
        new_window.geometry("500x500")
        new_window.lift()
        new_window.focus_force()
        tagvar = ctk.StringVar()
        entryTag = ctk.CTkEntry(new_window, placeholder_text=":تگ", textvariable=tagvar)
        entryTag.grid(row=0, column=0, padx=5, pady=15)

        AddBut = ctk.CTkButton(new_window,text = "تگ افزودن", command=lambda : writeTag(tagvar.get()))
        AddBut.grid(row=0, column=1,sticky="e")


        with open("tags.txt", "r", encoding="utf-8") as file:
            lines =file.readlines()
        comboVar = ctk.StringVar()
        comboDel = ctk.CTkComboBox(new_window,values =lines,variable=comboVar)
        comboDel.grid(row=2, column=0, sticky="e")

        ButDel = ctk.CTkButton(new_window,text="تگ حذف", command= lambda : delTag(comboVar.get()))
        ButDel.grid(row=2, column=1, padx=5, pady=15)

        def delTag(text):
            with open("tags.txt", "r", encoding="utf-8") as file:
                lines = file.readlines()
            for i in lines:
                if i == text:
                    del i
            with open("tags.txt", "w", encoding="utf-8") as file:
                file.writelines(lines)
            new_window.destroy()
        def writeTag(text):
            with open("tags.txt", "a", encoding="utf-8") as file:
                file.write(text + "\n")
            new_window.destroy()



    root =ctk.CTk()
    root.title("Shop")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"{screen_width}x{screen_height}+0+0")

    root.columnconfigure(0, weight=1)
    lblTitle = ctk.CTkLabel(root,text="مدیریت فروشگاه",
                            font=("IranNastaliq", 60),
                            fg_color="#426DE6",
                            height=55)
    lblTitle.grid(row=0,column=0,sticky="ew",columnspan=2,padx=5,pady=25)

    butSell = ctk.CTkButton(root,text="ثبت فروش",
                            font=("IranNastaliq", 45),
                            height=40,
                            corner_radius=40,
                            fg_color="#3244E6",
                            border_color="white",
                            border_width=1,
                            command=submitSell
                            )
    butSell.grid(row=1,column=0,sticky="ew",padx=5,pady=15)

    butAnalys = ctk.CTkButton(root,text="آنالیز",
                            font=("IranNastaliq", 45),
                            height=40,
                            corner_radius=40,
                            fg_color="#3244E6",
                            border_color="white",
                            border_width=1,
                            )
    butAnalys.grid(row=2,column=0,sticky="ew",padx=5,pady=15)

    butShow = ctk.CTkButton(root,text="نمایش فروش ها",
                            font=("IranNastaliq", 45),
                            height=40,
                            corner_radius=40,
                            fg_color="#3244E6",
                            border_color="white",
                            border_width=1
                            )
    butShow.grid(row=3,column=0,sticky="ew",padx=5,pady=15)

    butShow = ctk.CTkButton(root, text="ارسال پیام به کاربران",
                            font=("IranNastaliq", 45),
                            height=40,
                            corner_radius=40,
                            fg_color="#3244E6",
                            border_color="white",
                            border_width=1
                            )
    butShow.grid(row=4, column=0, sticky="ew", padx=5, pady=15)

    butCredit = ctk.CTkButton(root, text="بخش نسیه",
                            font=("IranNastaliq", 45),
                            height=40,
                            corner_radius=40,
                            fg_color="#3244E6",
                            border_color="white",
                            border_width=1
                            )
    butCredit.grid(row=5, column=0, sticky="ew", padx=5, pady=15)

    tag = ctk.CTkButton(root,text="مدیریت تگ",
                        font=("IranNastaliq", 45),
                        height=40,
                        corner_radius=40,
                        fg_color="#3244E6",
                        border_color="white",
                        border_width=1,
                        command=Tag
                        )
    tag.grid(row=6, column=0, sticky="ew", padx=5, pady=15)
    

    root.mainloop()

main()

