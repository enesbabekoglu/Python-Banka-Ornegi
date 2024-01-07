# Python Banka Sistemi Örneği
Python Dilinde Bir Banka Sistemi Örneği

![image](https://github.com/enesbabekoglu/Python-Banka-Ornegi/assets/92182480/70201478-63fd-4313-af5c-fe5c31f7d9f3)

## Özellikler

### Hesap Oluşturma
- Normal Hesap
- Tasarruf Hesap

![image](https://github.com/enesbabekoglu/Python-Banka-Ornegi/assets/92182480/219cbad5-0476-4a1a-91d1-954eac43fd37)

Hesap oluşturduktan sonraki hesaplar listemiz.
![image](https://github.com/enesbabekoglu/Python-Banka-Ornegi/assets/92182480/0c33977d-3644-4ae2-9c5e-f4ae68bfad4c)

### Hesap Kapatma
Tasarruf hesap kapatılırken hesap bakiyesi -%10 azalır.
Normal hesap kapatılırken herhangi bir kesinti olmaz.

![image](https://github.com/enesbabekoglu/Python-Banka-Ornegi/assets/92182480/ad8c4af6-a2fc-47c9-8dc5-fc345ab200f4)

### Hesapları Dosyadan Çekme (json dosyası)
Daha önceden hazırlanmış bir dosyadaki hesapları programa yükler. Bu hesaplar üzerinde değişiklik yapıldıktan sonra tekrar kaydedilebilir.

![image](https://github.com/enesbabekoglu/Python-Banka-Ornegi/assets/92182480/5d64cdc0-b150-4353-bf75-4b19613227fa)

Hesaplarımızı dosyadan yükledik.

![image](https://github.com/enesbabekoglu/Python-Banka-Ornegi/assets/92182480/80176e94-7c31-4d35-9552-9a0b272bbb75)

### Hesapları Dosyaya Kaydetme (json dosyası)
Programı başlattıktan sonra sistemde kayıtlı hesapları daha önceden belirlenmiş bir dosyaya kaydeder. Dosyada farklı hesaplar varsa o hesapları otomatik siler.

![image](https://github.com/enesbabekoglu/Python-Banka-Ornegi/assets/92182480/8ed5ecc5-c86a-4303-8fe5-306b53cef307)

### Para Çekme
Para çekme işlemleri hesapAdi:miktar şeklinde yapılabilir.
- Örnek => _BirikimHesap:500_ (Bu durumda BirikimHesap isimli hesaptan 500 TL çekilir.)

![image](https://github.com/enesbabekoglu/Python-Banka-Ornegi/assets/92182480/8d2b1386-8b3c-4059-91d6-3f24afe04ec1)

### Para Ekleme
Para ekleme işlemleri hesapAdi:miktar şeklinde yapılabilir.
- Örnek => _BirikimHesap:500_ (Bu durumda BirikimHesap isimli hesaba 500 TL eklenir.)

![image](https://github.com/enesbabekoglu/Python-Banka-Ornegi/assets/92182480/422bf0ca-876e-42b6-80ec-c23ab1639844)

### Hesapları Listeleme
- Program çalıştırıldıktan sonra dosyadan sisteme çekilen yada manuel oluşturulan hesapları listeler.
- Hesap adı, hesap tipi, hesap bakiyesi gibi bilgileri görebilirsiniz.

![image](https://github.com/enesbabekoglu/Python-Banka-Ornegi/assets/92182480/6c942b83-31df-44be-a2b8-33accfb634bd)

### Programdan Çıkış Yapma
- 0 Girdisi verildiğinde programı sonlandırır ve programdan çıkıldığına dair bilgi verir.

![image](https://github.com/enesbabekoglu/Python-Banka-Ornegi/assets/92182480/c0064517-4d27-485a-8f5d-0d66114e050f)
