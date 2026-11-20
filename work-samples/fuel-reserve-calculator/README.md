# Uçuş Yakıtı ve Rezerv Hesaplayıcısı

**Ders:** GEP1316 Kodlama Okuryazarlığı  
**Çalışma:** Ödev 3 – Python ile Kişisel Hesaplayıcı

## 1. Hesaplayıcının tanımı
Program, uçuş öncesinde uçakta bulunan yakıt miktarını, saatlik yakıt tüketimini, planlanan uçuş süresini ve ayrılacak rezerv süresini kullanıcıdan alır. Uçuş için gereken yakıtı hesaplar; uçuş sonunda kalması beklenen yakıtı rezerv ihtiyacıyla karşılaştırır.

## 2. Kullanılan formüller
- Uçuş yakıtı (L) = Saatlik tüketim × Uçuş süresi (dakika) / 60
- Rezerv yakıtı (L) = Saatlik tüketim × Rezerv süresi (dakika) / 60
- Kalan yakıt (L) = Uçaktaki yakıt − Uçuş yakıtı
- Rezerv kontrolü = Kalan yakıt ≥ Rezerv yakıtı

## 3. Veri tipleri ve programlama yapıları
- `int`: Uçuş ve rezerv süresi (dakika)
- `float`: Yakıt miktarı ve saatlik tüketim
- `str`: Kullanıcı mesajları ve durum açıklamaları
- `bool`: Rezerv yeterlilik sonucu
- `input()`, `int()` ve `float()`: Kullanıcı girdisi ve tür dönüşümü
- Aritmetik ve karşılaştırma operatörleri; biçimli çıktı için f-string

## 4. Çalıştırma
```bash
python main.py
```

## 5. Testler
```bash
python -m unittest -v
```

## 6. Sınırlar
Bu hesaplayıcı basitleştirilmiş, eğitim amaçlı bir programlama örneğidir. Gerçek uçuş planlamasında, yakıt planlamasında, uçuşa elverişlilik değerlendirmesinde veya operasyonel kararlarda kullanılamaz. Gerçek operasyonlar için onaylı dokümantasyon ve yetkili prosedürler esas alınmalıdır.
