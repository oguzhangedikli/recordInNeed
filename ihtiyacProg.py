from tkinter import *
from PIL import ImageTk, Image
import sqlite3
	
	
root = Tk()
root.geometry('500x500')
root.title("İHTİYAÇ SAHİBİ BİLGİSİ")
path = "yardim.png"
img = ImageTk.PhotoImage(Image.open(path))
panel = Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "no")	

isim=StringVar()
eposta=StringVar()
kisiler=StringVar()
ihtcList=StringVar()
kisiAdres=StringVar()	

	

	

def database():
   isimSoyisim=isim.get()
   email=eposta.get()
   kisi=kisiler.get()
   ihtiyacListesi=ihtcList.get()
   adres=kisiAdres.get()
   conn = sqlite3.connect('kisiKaydi.db')
   with conn:
      cursor=conn.cursor()
   cursor.execute('CREATE TABLE IF NOT EXISTS ihtiyaclarListesi (isimSoyisim TEXT,email TEXT,kisi TEXT,ihtiyacListesi TEXT,adres TEXT)')
   cursor.execute('INSERT INTO ihtiyaclarListesi (isimSoyisim,email,kisi,ihtiyacListesi,adres) VALUES(?,?,?,?,?)',(isimSoyisim,email,kisi,ihtiyacListesi,adres))
   for row in cursor.execute('SELECT * FROM ihtiyaclarListesi'):
      print(row)
      conn.commit()
	   
	   
	             
label_0 = Label(root, text="İhtiyaç Sahibi Kayıt Formu",width=20,font=("bold", 20))
label_0.place(x=90,y=53)
	

	
label_1 = Label(root, text="Ad-Soyad",bg='lightblue',fg='black',width=20,font=("bold", 10))
label_1.place(x=70,y=130)
entry_1 = Entry(root,textvar=isim)
entry_1.place(x=260,y=130)
	

label_2 = Label(root, text="Email",bg='lightblue',fg='black',width=20,font=("bold", 10))
label_2.place(x=70,y=180)
	

entry_2 = Entry(root,textvar=eposta)
entry_2.place(x=260,y=180)
	

label_3 = Label(root, text="Kişi",bg='lightblue',fg='black',width=20,font=("bold", 10))
label_3.place(x=70,y=230)
	

Radiobutton(root, text="Aile",padx = 5, variable=kisiler, value='Aile').place(x=255,y=230)
Radiobutton(root, text="Tek Kişi",padx = 20, variable=kisiler, value='Tek Kişi').place(x=310,y=230)
	

label_4 = Label(root, text="İhtiyaç Listesi",bg='lightblue',fg='black',width=20,font=("bold", 10))
label_4.place(x=70,y=280)
list1 = ['Yiyecek','Giyecek','Isınma','Maddi'];
droplist=OptionMenu(root,ihtcList, *list1)
droplist.config(width=15)
ihtcList.set('İhtiyacınızı seçiniz') 
droplist.place(x=260,y=280)

label_5 = Label(root, text="Adres",bg='lightblue',fg='black',width=20,font=("bold", 10))
label_5.place(x=70,y=330)
entry_3 = Entry(root,textvar=kisiAdres)
entry_3.place(x=255,y=330)

Button(root, text='Kaydet',width=20,bg='green',fg='black',command=database).place(x=180,y=380)

	
root.mainloop()


