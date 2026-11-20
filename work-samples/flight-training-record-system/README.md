# Uçuş Eğitim Kayıt ve Saat Takip Sistemi

**Ders:** GEP1316 Kodlama Okuryazarlığı  
**Çalışma:** Ara Değerlendirme Ödevi 1

## Amaç
Pilotaj eğitimi sırasında gerçekleştirilen Dual Flight, Solo Flight ve Simulator oturumlarının tarihini, süresini ve konusunu tek bir yerde düzenli olarak kaydetmek.

## Temel işlevler
- Yeni eğitim kaydı ekleme.
- Mevcut kayıtları listeleme.
- Toplam uçuş/eğitim süresi özetini görme.
- Bir kaydı silmeden önce kullanıcıdan onay alma.
- Kayıtları CSV dosyasında saklama ve program yeniden açıldığında yükleme.

## Veri modeli
Her kayıt bir sözlük olarak tutulur ve kayıtlar bir liste içinde yönetilir. CSV alanları: `date`, `duration`, `hours`, `topic`. Eğitim türleri Dual Flight, Solo Flight ve Simulator olarak ayrılır.

## Öğrenme çıktısı
Python'da fonksiyonlara ayırma, liste ve sözlük kullanımı, dosya okuma/yazma, giriş doğrulama ve test senaryosu tasarlama konularını pekiştirdim.

## GitHub
[Flight Training Record Management System](https://github.com/bau-cs/Flight-Training-Record-Management-System)

> Bu proje eğitim kayıtlarını düzenlemek içindir. Resmî uçuş kayıt sisteminin, uçuş planlamasının veya operasyonel kararların yerine geçmez.
