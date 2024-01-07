import json # json dosya işlemlerini yapmak için kullanılan kütüphanemiz

class Transaction: # Transaction sınıfının yapıcı metodu hesap ve miktar bilgilerini alır
    def __init__(self, account, amount):
        self.account = account
        self.amount = amount

    def paraDondur(self): # Eklenen/Çekilen Para Değerini Kontrol Eder
        if self.amount > 0: # Eğer miktar pozitifse para ekleyelim veya çekelim
            return self.amount
        else: # Eğer miktar 0 veya negatifse hata mesajı verelim
            raise ValueError("❌ HATA OLUŞTU! Geçersiz para miktarı. Pozitif bir değer giriniz.")

class Account:
    def __init__(self, account_type, account_name, balance): # Hesap sınıfının yapıcı metodu hesap türü, hesap adı ve başlangıç bakiyesi alır
        self._account_type = account_type
        self._account_name = account_name
        if balance < 0: # Başlangıç bakiyesi negatifse
            raise ValueError("❌ HATA OLUŞTU! Başlangıç bakiyesi negatif olamaz.")
        self._balance = balance

    @property
    def account_type(self): # Hesap türünü getirir
        return self._account_type

    @property
    def account_name(self): # Hesap adını getirir
        return self._account_name

    @property
    def balance(self): # Hesap bakiyesini getirir
        return self._balance

    @balance.setter
    def balance(self, value): # Hesap bakiyesini ayarlar ancak negatif bir değer verilirse hata verir
        if value < 0:
            raise ValueError("❌ HATA OLUŞTU! Bakiye 0 TL altına düşürülemez.")
        self._balance = value

class SavingAccount(Account): 
    def __init__(self, account_name, balance): # Tasarruf Hesabı sınıfının yapıcı metodudur hesap adı ve başlangıç bakiyesi alır
        super().__init__("Saving", account_name, balance)

    def kapat(self): # Tasarruf hesabını kapatırken bakiyeden %10 kesilir
        self.balance -= self.balance * 0.10
        return self.balance

class NormalAccount(Account):
    def __init__(self, account_name, balance): # Normal Hesap sınıfının yapıcı metodudur hesap adı ve başlangıç bakiyesi alır
        super().__init__("Normal", account_name, balance)

    def kapat(self): # Normal Hesap kapatılırken herhangi bir kesinti olmaz
        return self.balance

def paraCek(transaction):
    def wrapper(amount): # Para çekme işlemi için bir wrapper fonksiyonu
        if amount < 0:
            raise ValueError("❌ HATA OLUŞTU! Negatif değerli para çekilemez.")
        return transaction(amount)
    return wrapper

def paraEkle(transaction):
    def wrapper(amount): # Para ekleme işlemi için bir wrapper fonksiyonu
        if amount <= 0:
            raise ValueError("❌ HATA OLUŞTU! Eklenecek para miktarı 0 veya daha küçük olamaz.")
        return transaction(amount)
    return wrapper

def mesajBas(text): # Belirli bir metni çevreleyen dekoratif bir mesajın oluşturulmasında kullanılır
    return ("\n" + "-" * 100 + "\n" + str(text) + "\n" + "-" * 100)

class HesapManager:
    def __init__(self): # Hesap yöneticisi sınıfının yapıcı metodudur hesaplar isimli bir dictionary oluşturur
        self.hesaplar = {}

    def hesapOlustur(self, hesap_tipi, hesap_adi, bakiye): # Yeni bir hesap oluşturan metod
        if hesap_adi in self.hesaplar: # Hesap adı zaten mevcutsa hata mesajı verilir
            print(mesajBas("❌ HATA OLUŞTU! Aynı isimde bir hesap zaten var."))
            return
        if bakiye < 0: # Başlangıç bakiyesi negatifse hata mesajı verilir
            print(mesajBas("❌ HATA OLUŞTU! Başlangıç bakiyesi negatif olamaz."))
            return

        if hesap_tipi == '1': # Hesap türü Normal ise NormalAccount nesnesi oluşturulur
            hesap = NormalAccount(hesap_adi, bakiye)
        elif hesap_tipi == '2': # Hesap türü Saving ise SavingAccount nesnesi oluşturulur
            hesap = SavingAccount(hesap_adi, bakiye)
        else: # Geçersiz hesap türü girişi durumunda hata mesajı verilir
            print(mesajBas("❌ HATA OLUŞTU! Geçersiz hesap tipi girdiniz. Sadece Normal/Saving değerleri girilebilir."))
            return

        hesap_tipi = "Normal" if hesap_tipi == '1' else "Saving"

        self.hesaplar[hesap_adi] = hesap  # Yeni hesap hesaplar isimli sözlüğe eklenir
        print(mesajBas("✅ HESAP OLUŞTURMA İŞLEMİ BAŞARILI!"))
        print(f"Hesap Adı: {hesap_adi} | Tip: {hesap_tipi} Hesap")
        print("-" * 100)
        print(f"Başlangıç Bakiyesi: {bakiye} TL")
        print("-" * 100)

    def hesapKapat(self, hesap_adi): # Belirli bir hesabı kapatma işlemini gerçekleştiren metod

        if hesap_adi not in self.hesaplar: # Hesap adı mevcut değilse hata mesajı verilir
            print(mesajBas("❌ HATA OLUŞTU!\nSistemde bu hesap adına sahip bir hesap bulunmamaktadır."))
            return

        # Hesap kapatma işlemi ve bilgilerin görüntülenmesi
        hesap = self.hesaplar.pop(hesap_adi)
        hesap_turu = hesap.account_type
        sonBakiye = hesap.balance
        bakiye = hesap.kapat()

        print(mesajBas("✅ HESAP KAPATMA İŞLEMİ BAŞARILI!"))
        print(f"Kapatılan Hesap Adı: {hesap_adi} | Tip: {hesap_turu} Hesap")
        print("-" * 100)
        print(f"Kapatılmadan Önceki Bakiye: {sonBakiye} TL | Kapatıldıktan Sonraki Bakiye: {bakiye} TL")
        print("-" * 100)

    def kaydetYukle(self, islem_tipi): # Hesapları dosyaya kaydetme veya dosyadan yükleme işlemini gerçekleştiren metod
        if islem_tipi == "1":
            with open("hesaplar.json", "w") as file: # Hesapları dosyaya kaydetme işlemi
                json.dump({hesap_adi: {"tip": hesap.account_type, "bakiye": hesap.balance} for hesap_adi, hesap in self.hesaplar.items()}, file)
            print(mesajBas("✅ İŞLEM BAŞARILI! Sistemdeki güncel hesaplar dosyaya kaydedildi."))
        elif islem_tipi == "2":
            with open("hesaplar.json", "r") as file: # Hesapları dosyadan yükleme işlemi
                data = json.load(file)
                self.hesaplar = {hesap_adi: NormalAccount(hesap_adi, bilgiler["bakiye"]) if bilgiler["tip"] == "Normal" else SavingAccount(hesap_adi, bilgiler["bakiye"]) for hesap_adi, bilgiler in data.items()}
            print(mesajBas("✅ İŞLEM BAŞARILI! Dosyadaki hesaplar sisteme yüklendi."))
        else: # Geçersiz işlem tipi durumunda hata mesajı verilir
            print(mesajBas("❌ HATA OLUŞTU! Geçersiz bir işlem tipi seçtiniz."))

    def paraCek(self, girdi): # Belirli bir hesaptan para çekme işlemini gerçekleştiren metod
        try:
            hesap_adi, miktar = girdi.split(":")
            hesap_adi = hesap_adi.strip()
            miktar = float(miktar.strip())

            if hesap_adi not in self.hesaplar: # Hesap adı mevcut değilse hata mesajı verilir
                print(mesajBas("❌ HATA OLUŞTU! Sistemde böyle bir hesap bulunmamaktadır."))
                return

            hesap = self.hesaplar[hesap_adi]
            transaction = Transaction(hesap, miktar)
            eski_bakiye = hesap.balance
            cekilen_miktar = transaction.paraDondur()
            hesap.balance -= cekilen_miktar  # Bakiyeyi güncelle
            print(mesajBas("✅ PARA ÇEKME İŞLEMİ BAŞARILI!"))
            print(f"Hesap Adı: {hesap_adi} | Tip: {hesap.account_type} Hesap")
            print("-" * 100)
            print(f"Önceki Bakiye: {eski_bakiye} TL | Çekilen Tutar: -{cekilen_miktar} TL | Güncel Bakiye: {hesap.balance} TL")
            print("-" * 100)
        except ValueError as e:  # Geçersiz giriş formatı durumunda hata mesajı verilir
            print(mesajBas("❌ HATA OLUŞTU! Geçersiz giriş formatı. Hesap adı ve miktarı ayrıca giriniz. Örneğin: KrediHesabi:500"))

    def paraEkle(self, girdi): # Belirli bir hesaba para ekleme işlemini gerçekleştiren metod
        try:
            hesap_adi, miktar = girdi.split(":")
            hesap_adi = hesap_adi.strip()
            miktar = float(miktar.strip())

            if hesap_adi not in self.hesaplar: # Hesap adı mevcut değilse hata mesajı verilir
                print(mesajBas("❌ HATA OLUŞTU! Sistemde böyle bir hesap bulunmamaktadır."))
                return

            hesap = self.hesaplar[hesap_adi]
            if miktar < 0:
                raise ValueError("❌ HATA OLUŞTU! Eklenen para miktarı negatif olamaz.")
            transaction = Transaction(hesap, miktar)
            eski_bakiye = hesap.balance
            hesap.balance += miktar  # Bakiyeyi güncelle

            print(mesajBas("✅ PARA EKLEME İŞLEMİ BAŞARILI!"))
            print(f"Hesap Adı: {hesap_adi} | Tip: {hesap.account_type} Hesap")
            print("-" * 100)
            print(f"Önceki Bakiye: {eski_bakiye} TL | Eklenen Tutar: +{miktar} TL | Güncel Bakiye: {hesap.balance} TL")
            print("-" * 100)
        except ValueError as e:
            print(mesajBas("❌ HATA OLUŞTU! Geçersiz giriş formatı. Hesap adı ve miktarı ayrıca giriniz. Örneğin: KrediHesabi:500"))

    def goster(self):
        print("\n>>>>>>MEVCUT HESAPLAR<<<<<<\n")
        print("-" * 100)
        i = 0
        for hesap_adi, hesap in self.hesaplar.items():
            i += 1

            print(f"{i}) Hesap Adı: {hesap_adi} | Tip: {hesap.account_type} Hesap | Bakiye: {hesap.balance} TL")
            print("-" * 100)

        if i == 0:
            print("Sistemde hiç hesap bulunmamaktadır.")
        else:
            print(f"Sistemde kayıtlı {i} hesap bulunmaktadır.")

        print("-" * 100)

def main():
    hesapManager = HesapManager()

    while True:
        print("\n>>>>>>İŞLEM MENÜSÜ<<<<<<\n")
        print("1. Hesap Oluştur")
        print("2. Hesap Kapat")
        print("3. Dosyaya Kaydet veya Yükle")
        print("4. Para Çek")
        print("5. Para Ekle")
        print("6. Hesapları Göster")
        print("0. Programı Kapat")

        secim = input("\nYapmak İstediğiniz İşlemi Seçiniz: ")

        if secim == "1":
            print("\n>>>>>>HESAP OLUŞTUR<<<<<<\n")
            print("1. Normal Hesap")
            print("2. Saving Hesap")
            hesap_tipi = input("\nHesap Tipini Giriniz: ")
            hesap_adi = input("\nHesap Adını Giriniz: ")
            bakiye = float(input("\nBaşlangıç Bakiyesi Giriniz: "))
            hesapManager.hesapOlustur(hesap_tipi, hesap_adi, bakiye)
        elif secim == "2":
            print("\n>>>>>>HESAP KAPAT<<<<<<\n")
            hesap_adi = input("Kapatmak İstediğiniz Hesabın Adını Giriniz: ")
            hesapManager.hesapKapat(hesap_adi)
        elif secim == "3":
            print("\n>>>>>>DOSYAYA KAYDET VEYA YÜKLE<<<<<<\n")
            print("1. Güncel Verileri Dosyaya Kaydet")
            print("2. Dosyadaki Verileri Sisteme Yükle")
            islem_tipi = input("\nYapmak İstediğiniz İşlemi Seçiniz: ")
            hesapManager.kaydetYukle(islem_tipi)
        elif secim == "4":
            print("\n>>>>>>PARA ÇEK<<<<<<\n")
            girdi = input("Hesap Adı:Miktar Giriniz: ")
            hesapManager.paraCek(girdi)
        elif secim == "5":
            print("\n>>>>>>PARA EKLE<<<<<<\n")
            girdi = input("Hesap Adı:Miktar Giriniz: ")
            hesapManager.paraEkle(girdi)
        elif secim == "6":
            hesapManager.goster()
        elif secim == "0":
            print(mesajBas("🕒 Çıkış Yapılıyor..."))
            break
        else:
            print(mesajBas("❌ HATA OLUŞTU! Seçtiğiniz işlem türü sistemimizde bulunmamaktadır. Lütfen tekrar deneyiniz."))

if __name__ == "__main__":
    main()

    print(mesajBas("✅ Çıkış Başarılı!")+"\n")
