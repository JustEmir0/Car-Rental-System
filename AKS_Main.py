import tkinter as tk
from tkinter import ttk, messagebox

app = tk.Tk()
app.geometry("1366x768")
app.title("Araç Kiralama Sistemi")

class Arac:
    def __init__(self, marka, model, yil, yakit, vites):
        self.marka = marka
        self.model = model
        self.yil = yil
        self.yakit = yakit
        self.vites = vites

class Musteri:
    def __init__(self, ad, soyad):
        self.ad = ad
        self.soyad = soyad   

kiralanan_araclar = []

def kiralama_yap():
    musteri_ad = ad_entry.get()
    musteri_soyad = soyad_entry.get()

    # Combobox'lardan herhangi birinin değerinin boş olup olmadığını kontrol et
    if not (marka_combobox.get() and model_combobox.get() and yil_combobox.get() and yakit_combobox.get() and vites_combobox.get() and
            sehir_combobox.get() and alis_yeri_combobox.get() and alis_tarihi_combobox.get() and alis_saati_combobox.get() and
            sehir_combobox_donus.get() and donus_yeri_combobox.get() and donus_tarihi_combobox.get() and donus_saati_combobox.get()):
        messagebox.showerror("Hata", "Lütfen tüm bilgileri doldurun!")
        return

    if not musteri_ad or not musteri_soyad:
        messagebox.showerror("Hata", "Müşteri adı ve soyadı boş bırakılamaz!")
        return

    kiralanan_arac = Arac(marka_combobox.get(), model_combobox.get(), yil_combobox.get(), yakit_combobox.get(), vites_combobox.get())
    kiralanan_arac.musteri = Musteri(ad_entry.get(), soyad_entry.get())
    kiralanan_arac.alis_bilgileri = (sehir_combobox.get(), alis_yeri_combobox.get(), alis_tarihi_combobox.get(), alis_saati_combobox.get())
    kiralanan_arac.donus_bilgileri = (sehir_combobox_donus.get(), donus_yeri_combobox.get(), donus_tarihi_combobox.get(), donus_saati_combobox.get())
    
    kiralanan_araclar.append(kiralanan_arac)
    messagebox.showinfo("Başarılı", "Kiralama işlemi başarıyla tamamlandı!")

def bilgi_göster_pencere():
    # Yeni bir pencere oluştur
    belirli_musteri_penceresi = tk.Toplevel(app)
    belirli_musteri_penceresi.title("Belirli Müşteri Bilgileri")

    # Etiketler ve giriş alanları oluştur
    ad_label = tk.Label(belirli_musteri_penceresi, text="Müşteri Adı:", font=('Century Gothic', 16))
    ad_label.grid(row=0, column=0, padx=10, pady=10)
    ad_entry = tk.Entry(belirli_musteri_penceresi, font=('Century Gothic', 14))
    ad_entry.grid(row=0, column=1, padx=10, pady=10)

    soyad_label = tk.Label(belirli_musteri_penceresi, text="Müşteri Soyadı:", font=('Century Gothic', 16))
    soyad_label.grid(row=1, column=0, padx=10, pady=10)
    soyad_entry = tk.Entry(belirli_musteri_penceresi, font=('Century Gothic', 14))
    soyad_entry.grid(row=1, column=1, padx=10, pady=10)

    def bilgi_göster():
        # Müşteri adı ve soyadını giriş alanlarından al
        musteri_ad = ad_entry.get()
        musteri_soyad = soyad_entry.get()

        # Belirtilen müşteriye ait kiralama bilgilerini bul
        bulunan_kiralama_bilgisi = None
        for kiralanan_arac in kiralanan_araclar:
            if kiralanan_arac.musteri.ad == musteri_ad and kiralanan_arac.musteri.soyad == musteri_soyad:
                bulunan_kiralama_bilgisi = kiralanan_arac
                belirli_musteri_penceresi.destroy()
                break
            
            # Eğer müşteriye ait kiralama bilgisi bulunduysa göster
        if bulunan_kiralama_bilgisi:
            bilgi_penceresi = tk.Toplevel(app)
            bilgi_penceresi.title("Müşteri Kiralama Bilgileri")
                
                
            kiralama_bilgisi = f"""{musteri_ad} {musteri_soyad} adlı müşterinin kiralama bilgileri:

            Araç Bilgileri:
            Marka: {bulunan_kiralama_bilgisi.marka}
            Model: {bulunan_kiralama_bilgisi.model}
            Yıl: {bulunan_kiralama_bilgisi.yil}
            Yakıt: {bulunan_kiralama_bilgisi.yakit}
            Vites: {bulunan_kiralama_bilgisi.vites}

            Alış Bilgileri:
            Şehir: {bulunan_kiralama_bilgisi.alis_bilgileri[0]}
            Alış Yeri: {bulunan_kiralama_bilgisi.alis_bilgileri[1]}
            Alış Tarihi: {bulunan_kiralama_bilgisi.alis_bilgileri[2]}
            Alış Saati: {bulunan_kiralama_bilgisi.alis_bilgileri[3]}

            Dönüş Bilgileri:
            Şehir: {bulunan_kiralama_bilgisi.donus_bilgileri[0]}
            Dönüş Yeri: {bulunan_kiralama_bilgisi.donus_bilgileri[1]}
            Dönüş Tarihi: {bulunan_kiralama_bilgisi.donus_bilgileri[2]}
            Dönüş Saati: {bulunan_kiralama_bilgisi.donus_bilgileri[3]}
                """

            bilgi_text = tk.Text(bilgi_penceresi, height=20, width=80)
            bilgi_text.insert(tk.END, kiralama_bilgisi)
            bilgi_text.pack(padx=20, pady=20)
            bilgi_text.config(state=tk.DISABLED)
        else:
            messagebox.showerror("Hata", "Belirtilen müşteriye ait kiralama bilgisi bulunamadı.")
        
    göster_btn = tk.Button(belirli_musteri_penceresi, text="Göster", font=('Century Gothic', 14), command=bilgi_göster)
    göster_btn.grid(row=2, columnspan=2, padx=10, pady=10)
    

def kiralama_iptal_et():
    iptal_penceresi = tk.Toplevel(app)
    iptal_penceresi.title("Kiralama İptal Et")

    ad_label_iptal = tk.Label(iptal_penceresi, text='Müşteri Adı:', font=('Century Gothic', 16))
    ad_label_iptal.grid(row=0, column=0, padx=10, pady=10)
    ad_entry_iptal = tk.Entry(iptal_penceresi, font=('Century Gothic', 14))
    ad_entry_iptal.grid(row=0, column=1, padx=10, pady=10)

    soyad_label_iptal = tk.Label(iptal_penceresi, text='Müşteri Soyadı:', font=('Century Gothic', 16))
    soyad_label_iptal.grid(row=1, column=0, padx=10, pady=10)
    soyad_entry_iptal = tk.Entry(iptal_penceresi, font=('Century Gothic', 14))
    soyad_entry_iptal.grid(row=1, column=1, padx=10, pady=10)

    def kiralama_iptal():
        musteri_ad_iptal = ad_entry_iptal.get()
        musteri_soyad_iptal = soyad_entry_iptal.get()

        kiralanan_arac = None
        for arac in kiralanan_araclar:
            if arac.musteri.ad == musteri_ad_iptal and arac.musteri.soyad == musteri_soyad_iptal:
                kiralanan_arac = arac
                break

        if kiralanan_arac:
            kiralanan_araclar.remove(kiralanan_arac)
            messagebox.showinfo("Başarılı", "Kiralama işlemi başarıyla iptal edildi.")
            iptal_penceresi.destroy()
        else:
            messagebox.showerror("Hata", "Müşteriye ait bir kiralama bulunamadı.")

    iptal_btn = tk.Button(iptal_penceresi, text="İptal Et", font=('Century Gothic', 14), command=kiralama_iptal)
    iptal_btn.grid(row=2, columnspan=2, padx=10, pady=10)

def marka_secme(event):
    secilen_marka = marka_combobox.get()
    if secilen_marka in model:
        model_combobox.config(values=model[secilen_marka])
    else:
        model_combobox.config(values=[])

def lokasyon_secme_alıs(event):
    secilen_sehir = sehir_combobox.get()
    if secilen_sehir in alıs_yer:
        alis_yeri_combobox.config(values=alıs_yer[secilen_sehir])
    else:
        alis_yeri_combobox.config(values=[])

def lokasyon_secme_donus(event):
    secilen_sehir = sehir_combobox_donus.get()
    if secilen_sehir in varıs_yer:
        donus_yeri_combobox.config(values=varıs_yer[secilen_sehir])
    else:
        donus_yeri_combobox.config(values=[])


alıs_sehir = ["İstanbul", "İzmir", "Ankara"]
alıs_yer = {
    "İstanbul": ["İstanbul Otel"],
    "İzmir": ["İzmir Otel"],
    "Ankara": ["Ankara Otel"]
}
varıs_Sehir = ["İstanbul", "İzmir", "Ankara"]
varıs_yer = {
    "İstanbul": ["İstanbul Otel"],
    "İzmir": ["İzmir Otel"],
    "Ankara": ["Ankara Otel"]}
tarih = ["05.04.2024", "06.04.2024", "07.04.2024", "08.04.2024", "09.04.2024"]
saat = ["09.00", "10.00", "11.00", "12.00", "13.00", "14.00", "15.00", "16.00"]

marka = ["Audi", "Honda", "Renault","Toyota"]
model = {
    "Audi": ["A3", "A4"],
    "Honda": ["City", "Civic"],
    "Renault": ["Fluence", "Clio"],
    "Toyota": ["Corolla","Yaris"]
}

frame = tk.Frame(app, width=1000, height=300, bg="darkgrey", highlightbackground="black", highlightthickness=2)
frame.place(x=20, y=250)

frame2 = tk.Frame(app, width=400, height=175, bg="darkgrey", highlightbackground="black", highlightthickness=2)
frame2.place(x=20, y=30)

musteri_label = tk.Label(frame2, text='Müşteri Bilgileri', font=('Century Gothic', 20), bg="darkgrey")
musteri_label.place(x=90, y=14)

ad_label = tk.Label(frame2, text='Ad:', font=('Century Gothic', 16), bg="darkgrey")
ad_label.place(x=18, y=75)
ad_entry = tk.Entry(frame2, font=('Century Gothic', 14))
ad_entry.place(x=90, y=75)

soyad_label = tk.Label(frame2, text='Soyad:', font=('Century Gothic', 16), bg="darkgrey")
soyad_label.place(x=8, y=120)
soyad_entry = tk.Entry(frame2, font=('Century Gothic', 14))
soyad_entry.place(x=90, y=120)

arac_label = tk.Label(frame, text='Araç Bilgileri', font=('Century Gothic', 20), bg="darkgrey")
arac_label.place(x=40, y=10)

marka_label = tk.Label(frame, text='Marka', font=('Century Gothic', 16), bg="darkgrey")
marka_label.place(x=20, y=50)
marka_combobox = ttk.Combobox(frame, values=marka)
marka_combobox.place(x=100, y=55)

model_label = tk.Label(frame, text='Model', font=('Century Gothic', 16), bg="darkgrey")
model_label.place(x=20, y=90)
model_combobox = ttk.Combobox(frame)
model_combobox.place(x=100, y=95)

yil_label = tk.Label(frame, text='Yıl', font=('Century Gothic', 16), bg="darkgrey")
yil_label.place(x=20, y=130)
yil_combobox = ttk.Combobox(frame, values=["2019", "2020", "2021"])
yil_combobox.place(x=100, y=135)

yakit_label = tk.Label(frame, text='Yakıt', font=('Century Gothic', 16), bg="darkgrey")
yakit_label.place(x=20, y=170)
yakit_combobox = ttk.Combobox(frame, values=["Benzin", "Dizel", "Hibrit"])
yakit_combobox.place(x=100, y=175)

vites_label = tk.Label(frame, text='Vites', font=('Century Gothic', 16), bg="darkgrey")
vites_label.place(x=20, y=210)
vites_combobox = ttk.Combobox(frame, values=["Manuel", "Otomatik"])
vites_combobox.place(x=100, y=215)

alis_label = tk.Label(frame, text='Araç Alış Bilgileri', font=('Century Gothic', 20), bg="darkgrey")
alis_label.place(x=340, y=10)

sehir_label = tk.Label(frame, text='Şehir', font=('Century Gothic', 16), bg="darkgrey")
sehir_label.place(x=310, y=50)
sehir_combobox = ttk.Combobox(frame, values=alıs_sehir)
sehir_combobox.place(x=410, y=55)

alis_yeri_label = tk.Label(frame, text='Alış Yeri', font=('Century Gothic', 16), bg="darkgrey")
alis_yeri_label.place(x=310, y=90)
alis_yeri_combobox = ttk.Combobox(frame)
alis_yeri_combobox.place(x=410, y=95)

alis_tarihi_label = tk.Label(frame, text='Alış Tarihi', font=('Century Gothic', 16), bg="darkgrey")
alis_tarihi_label.place(x=310, y=130)
alis_tarihi_combobox = ttk.Combobox(frame, values=tarih)
alis_tarihi_combobox.place(x=410, y=135)

alis_saati_label = tk.Label(frame, text='Alış Saati', font=('Century Gothic', 16), bg="darkgrey")
alis_saati_label.place(x=310, y=170)
alis_saati_combobox = ttk.Combobox(frame, values=saat)
alis_saati_combobox.place(x=410, y=175)

donus_label = tk.Label(frame, text='Araç Dönüş Bilgileri', font=('Century Gothic', 20), bg="darkgrey")
donus_label.place(x=600, y=10)

sehir_label_donus = tk.Label(frame, text='Şehir', font=('Century Gothic', 16), bg="darkgrey")
sehir_label_donus.place(x=590, y=50)
sehir_combobox_donus = ttk.Combobox(frame, values=varıs_Sehir)
sehir_combobox_donus.place(x=730, y=55)

donus_yeri_label = tk.Label(frame, text='Dönüş Yeri', font=('Century Gothic', 16), bg="darkgrey")
donus_yeri_label.place(x=590, y=90)
donus_yeri_combobox = ttk.Combobox(frame)
donus_yeri_combobox.place(x=730, y=95)

donus_tarihi_label = tk.Label(frame, text='Dönüş Tarihi', font=('Century Gothic', 16), bg="darkgrey")
donus_tarihi_label.place(x=590, y=130)
donus_tarihi_combobox = ttk.Combobox(frame, values=tarih)
donus_tarihi_combobox.place(x=730, y=135)

donus_saati_label = tk.Label(frame, text='Dönüş Saati', font=('Century Gothic', 16), bg="darkgrey")
donus_saati_label.place(x=590, y=170)
donus_saati_combobox = ttk.Combobox(frame, values=saat)
donus_saati_combobox.place(x=730, y=175)

btn1 = tk.Button(app, text="Kiralama İşlemini Onayla", width=30, height=2, font=('Century Gothic', 16), command=kiralama_yap)
btn1.place(x=200, y=615, anchor=tk.CENTER)

btn2 = tk.Button(app, text="Kiralama Bilgilerini Göster", width=30, height=2, font=('Century Gothic', 16), command=bilgi_göster_pencere)
btn2.place(x=580, y=615, anchor=tk.CENTER)

btn3 = tk.Button(app, text="Kiralama İptal Et", width=30, height=2, font=('Century Gothic', 16), command=kiralama_iptal_et)
btn3.place(x=960, y=615, anchor=tk.CENTER)

# Seçeneklerini güncelle
marka_combobox.bind("<<ComboboxSelected>>", marka_secme)
sehir_combobox.bind("<<ComboboxSelected>>", lokasyon_secme_alıs)
sehir_combobox_donus.bind("<<ComboboxSelected>>",lokasyon_secme_donus)


app.mainloop()