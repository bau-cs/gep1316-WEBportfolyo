# Uçuş Öncesi Belge Kontrol Listesi

**Ders:** GEP1316 Kodlama Okuryazarlığı  
**Çalışma:** Ödev 1 – Günlük Hayattan Bir Problemin Algoritması ve Akış Şeması

## Problem
Pilotun uçuş öncesinde kontrol etmesi gereken belgelerin mevcut ve geçerli olup olmadığını sırayla gözden geçirmek. Algoritma, eksik veya geçerli olmadığı bildirilen belgeleri ayrı bir listede toplar.

## Girdi – İşlem – Çıktı
- **Girdi:** Pilot lisansı, sağlık sertifikası, kimlik belgesi ve uçuş için gerekli evrakların mevcut/geçerli bilgisi.
- **İşlem:** Belgeler bir döngüyle tek tek değerlendirilir. Durumu eksik olan belge, eksik listesine eklenir.
- **Çıktı:** Eksik belgelerin listesi veya eksik belge bulunmadığını bildiren mesaj.

## Sözde kod
```text
BAŞLA
GerekliBelgeler = [Pilot lisansı, Sağlık sertifikası, Kimlik belgesi, Gerekli uçuş evrakı]
EksikBelgeler = boş liste

HER belge İÇİN GerekliBelgeler:
    BelgeDurumunu al
    EĞER BelgeDurumu = "H" İSE:
        Belgeyi EksikBelgeler listesine ekle
    SON
SON

EĞER EksikBelgeler boş İSE:
    "Kontrol listesinde eksik belge yok." yaz
DEĞİLSE:
    EksikBelgeler listesini yaz
SON
"Bu çıktı yalnızca hatırlatma amaçlıdır; uçuş izni değildir." yaz
BİTİR
```

## Öğrenme çıktısı
Koşul ve döngülerin bir arada kullanılması; eksik girdinin nasıl bir sonuç listesine dönüştürüldüğünün anlaşılması.

> **Emniyet sınırı:** Bu algoritma yalnızca eğitim ve hatırlatma amaçlıdır. Gerçek uçuş izni, uçuşa elverişlilik veya operasyonel karar vermez. Resmî kontrol listelerinin ve yetkili personelin yerine geçmez.
