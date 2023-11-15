from tkinter import *
class KartuKredit:
    def __init__(self, kredit):
        self.kredit = kredit
        self.balance = 0
        self.maxpay = 0
        self.minpay = 0
        kredit.title("Tugas Kartu Kredit")
        kredit.geometry("740x480")
        kredit.configure(bg='green')

        self.nomor_kartu = IntVar()
        self.nama_kartu = StringVar()
        self.maxpay = IntVar()
        self.minpay = IntVar()
        self.label_nomor_kartu = Label(kredit, text= "Masukkan nomor Kartu anda =")
        self.label_nomor_kartu.pack(padx=10, pady=10, side='left')
        self.label_nomor_kartu.place(y = 25)

        self.field_nomor_kartu = Entry(kredit, textvariable=self.label_nomor_kartu, width = 40)
        self.field_nomor_kartu.pack()

        self.label_nama_kartu = Label(kredit, text= "Nama anda = ")
        self.label_nama_kartu.pack(padx=10, pady=10, side='left')
        self.label_nama_kartu.place(y = 50)

        self.field_nama_kartu = Entry(kredit, textvariable=self.label_nama_kartu, width = 40)
        self.field_nama_kartu.pack()

        self.label_maxpay = Label(kredit, text= "Maximum payment = ")
        self.label_maxpay.pack(padx=10, pady=10, side='left')
        self.label_maxpay.place(y = 75)

        self.field_maxpay = Entry(kredit, textvariable=self.label_maxpay, width=40)
        self.field_maxpay.pack()

        self.label_minpay = Label(kredit, text = "Minimum payment = ")
        self.label_minpay.pack(padx=10, pady=10, side='left')
        self.label_minpay.place(y = 100)

        self.field_minpay = Entry(kredit, textvariable=self.label_minpay, width = 40)
        self.field_minpay.pack()

root = Tk()
my_gui = KartuKredit(root)
root.mainloop()
