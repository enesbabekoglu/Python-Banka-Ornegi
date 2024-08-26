# (EN) Python Bank System Example

This project is a simple bank system example developed in Python. It demonstrates how to manage bank accounts, including creating, closing, saving, and loading accounts, as well as handling transactions like deposits and withdrawals.

![Bank System Example](https://github.com/enesbabekoglu/Python-Banking-App/assets/92182480/70201478-63fd-4313-af5c-fe5c31f7d9f3)

## Features 🌟

### Account Creation
- **Normal Account:** Standard bank account creation.
- **Savings Account:** Savings account with special conditions.

![Account Creation](https://github.com/enesbabekoglu/Python-Banking-App/assets/92182480/219cbad5-0476-4a1a-91d1-954eac43fd37)

After creating accounts, you can view the list of created accounts.
![Account List](https://github.com/enesbabekoglu/Python-Banking-App/assets/92182480/0c33977d-3644-4ae2-9c5e-f4ae68bfad4c)

### Account Closure
- **Savings Account:** Closing a savings account reduces the balance by 10%.
- **Normal Account:** No deduction is applied when closing a normal account.

![Account Closure](https://github.com/enesbabekoglu/Python-Banking-App/assets/92182480/ad8c4af6-a2fc-47c9-8dc5-fc345ab200f4)

### Loading Accounts from a File (JSON)
- Load accounts from a pre-existing JSON file into the program. These accounts can be modified and saved back to the file.

![Load Accounts](https://github.com/enesbabekoglu/Python-Banking-App/assets/92182480/5d64cdc0-b150-4353-bf75-4b19613227fa)

After loading accounts from a file:

![Loaded Accounts](https://github.com/enesbabekoglu/Python-Banking-App/assets/92182480/80176e94-7c31-4d35-9552-9a0b272bbb75)

### Saving Accounts to a File (JSON)
- Save the current accounts to a predefined JSON file after starting the program. If the file contains different accounts, they will be automatically replaced.

![Save Accounts](https://github.com/enesbabekoglu/Python-Banking-App/assets/92182480/8ed5ecc5-c86a-4303-8fe5-306b53cef307)

### Withdraw Money
- Withdrawals can be made using the format `accountName:amount`.
  - Example: _SavingsAccount:500_ (This will withdraw 500 units from the SavingsAccount.)

![Withdraw Money](https://github.com/enesbabekoglu/Python-Banking-App/assets/92182480/8d2b1386-8b3c-4059-91d6-3f24afe04ec1)

### Deposit Money
- Deposits can be made using the format `accountName:amount`.
  - Example: _SavingsAccount:500_ (This will deposit 500 units into the SavingsAccount.)

![Deposit Money](https://github.com/enesbabekoglu/Python-Banking-App/assets/92182480/422bf0ca-876e-42b6-80ec-c23ab1639844)

### List Accounts
- After the program is started, it lists all accounts that have been loaded from the file or created manually.
- You can view details such as account name, account type, and account balance.

![List Accounts](https://github.com/enesbabekoglu/Python-Banking-App/assets/92182480/6c942b83-31df-44be-a2b8-33accfb634bd)

### Exit the Program
- The program terminates when the input is `0`, and it provides confirmation of the exit.

![Exit Program](https://github.com/enesbabekoglu/Python-Banking-App/assets/92182480/c0064517-4d27-485a-8f5d-0d66114e050f)

## Installation 🚀

Follow these steps to run this project on your local machine:

### Requirements 📋
- **Python 3.x** or higher 🐍

### Step 1: Clone the Repository
First, clone the project to your local machine:

```bash
git clone https://github.com/enesbabekoglu/Python-Banking-App.git
cd Python-Banking-App
```

### Step 2: Install Required Libraries
Install the required Python libraries:

```bash
pip install -r requirements.txt
```

### Step 3: Run the Program
To run the program:

```bash
python main.py
```

## License 📄

This project is licensed under the MIT License. For more details, please refer to the `LICENSE` file.

## Contributing 🤝

If you would like to contribute to this project, please submit a **pull request** or open an **issue**. Your feedback and contributions are welcome!

# (TR) Python Banka Sistemi Örneği

Bu proje, Python dilinde geliştirilmiş basit bir banka sistemi örneğidir. Banka hesaplarının oluşturulması, kapatılması, dosyadan yüklenmesi, dosyaya kaydedilmesi ve para çekme/yatırma işlemlerinin nasıl yapılacağını gösterir.

![Banka Sistemi Örneği](https://github.com/enesbabekoglu/Python-Banking-App/assets/92182480/70201478-63fd-4313-af5c-fe5c31f7d9f3)

## Özellikler 🌟

### Hesap Oluşturma
- **Normal Hesap:** Standart banka hesabı oluşturma.
- **Tasarruf Hesabı:** Özel şartlarla tasarruf hesabı oluşturma.

![Hesap Oluşturma](https://github.com/enesbabekoglu/Python-Banking-App/assets/92182480/219cbad5-0476-4a1a-91d1-954eac43fd37)

Hesap oluşturduktan sonra, oluşturulan hesaplar listelenebilir.
![Hesap Listesi](https://github.com/enesbabekoglu/Python-Banking-App/assets/92182480/0c33977d-3644-4ae2-9c5e-f4ae68bfad4c)

### Hesap Kapatma
- **Tasarruf Hesabı:** Tasarruf hesabı kapatıldığında bakiye %10 azalır.
- **Normal Hesap:** Normal hesap kapatıldığında herhangi bir kesinti olmaz.

![Hesap Kapatma](https://github.com/enesbabekoglu/Python-Banking-App/assets/92182480/ad8c4af6-a2fc-47c9-8dc5-fc345ab200f4)

### Hesapları Dosyadan Yükleme (JSON)
- Daha önce oluşturulmuş bir JSON dosyasından hesapları programa yükleyin. Bu hesaplar üzerinde değişiklik yapıldıktan sonra tekrar kaydedilebilir.

![Hesapları Yükleme](https://github.com/enesbabekoglu/Python-Banking-App/assets/92182480/5d64cdc0-b150-4353-bf75-4b19613227fa)

Dosyadan hesapları yükledikten sonra:
![Yüklenmiş Hesaplar](https://github.com/enesbabekoglu/Python-Banking-App/assets/92182480/80176e94-7c31-4d35-9552-9a0b272bbb75)

### Hesapları Dosyaya Kaydetme (JSON)
- Program çalıştırıldıktan sonra mevcut hesapları bir JSON dosyasına kaydeder. Dosyada farklı hesaplar varsa, bu hesaplar otomatik olarak silinir.

![Hesapları Kaydetme](https://github.com/enesbabekoglu/Python-Banking-App/assets/92182480/8ed5ecc5-c86a-4303-8fe5-306b53cef307)

### Para Çekme
- Para çekme işlemleri `hesapAdi:miktar` formatında yapılabilir.
  - Örnek: _BirikimHesap:500_ (Bu işlem, BirikimHesap isimli hesaptan 500 TL çeker.)

![Para Çekme](https://github.com/enesbabekoglu/Python-Banking-App/assets/92182480/8d2b1386-8b3c-4059-91d6-3f24afe04ec1)

### Para Yatırma
- Para yatırma işlemleri `hesapAdi:miktar` formatında yapılabilir.
  - Örnek: _BirikimHesap:500_ (Bu işlem, BirikimHesap isimli hesaba 500 TL ekler.)

![Para Yatırma](https://github.com/enesbabekoglu/Python-Banking-App/assets/92182480/422bf0ca-876e-42b6-80ec-c23ab1639844)

### Hesapları Listeleme
- Program çalıştırıldıktan sonra dosyadan yüklenen ya da manuel olarak oluşturulan hesapları listeler.
- Hesap adı, hesap tipi, hesap bakiyesi gibi bilgileri görüntüleyebilirsiniz.

![Hesapları Listeleme](https://github.com/enesbabekoglu/Python-Banking-App/assets/92182480/6c942b83-31df-44be-a2b8-33accfb634bd)

### Programdan Çıkış Yapma
- 0 girdisi verildiğinde program sonlandırılır ve çıkış yapıldığına dair bilgi verilir.

![Çıkış Yapma](https://github.com/enesbabekoglu/Python-Banking-App/assets/92182480/c0064517-4d27-485a-8f5d-0d66114e050f)

## Kurulum 🚀

Bu projeyi kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyin:

### Gereksinimler 📋
- **Python 3.x** veya üstü 🐍

### Adım 1: Projeyi Klonlayın
Öncelikle projeyi bilgisayarınıza klonlayın:

```bash
git clone https://github.com/enesbabekoglu/Python-Banking-App.git
cd Python-Banking-App
```

### Adım 2: Gerekli Kütüphaneleri Yükleyin
Gerekli Python kütüphanelerini yükleyin:

```bash
pip install -r requirements.txt
```

### Adım 3: Programı Çalıştırın
Programı çalıştırmak için:

```bash
python main.py
```

## Lisans 📄

Bu proje MIT Lisansı ile lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına göz atabilirsiniz.

## Katkıda Bulunma 🤝

Bu projeye katkıda bulunmak isterseniz, bir **pull request** gönderin veya bir **issue** açın. Geri bildirimleriniz ve katkılarınız memnuniyetle karşılanacaktır!
