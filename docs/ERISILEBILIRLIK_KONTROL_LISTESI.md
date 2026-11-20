# Erişilebilirlik, Gizlilik ve Test Kontrol Listesi

## Erişilebilirlik kontrolü

| Kontrol | Durum | Uygulama |
|---|---|---|
| Anlamsal HTML kullanımı | Tamamlandı | `header`, `nav`, `main`, `section`, `article`, `footer` kullanıldı. |
| Sayfa başına tek ana `h1` | Tamamlandı | Her sayfada bir ana başlık yer alır. |
| Klavye ile gezinme | Tamamlandı | Bağlantı ve düğmeler doğal sekme sırasındadır; odak göstergesi görünürdür. |
| Ana içeriğe atlama bağlantısı | Tamamlandı | Her sayfanın başında “Ana içeriğe geç” bağlantısı bulunur. |
| Form etiketleri | Tamamlandı | Her giriş alanının görünür `label` etiketi vardır. |
| Form hata mesajları | Tamamlandı | Alan bazlı mesajlar ve `aria-invalid` durumu kullanılır. |
| Canlı geri bildirim | Tamamlandı | Sonuç alanlarında `aria-live` / `role="status"` kullanılır. |
| Mobil menü durumu | Tamamlandı | `aria-expanded` ve açıklayıcı `aria-label` kullanılır. |
| Tema düğmesi durumu | Tamamlandı | `aria-pressed` niteliği güncellenir. |
| Görsel alternatifleri | Tamamlandı | Avatarlar için rol/etiket; dekoratif SVG'ler için `aria-hidden="true"` kullanılır. |
| Renk kontrastı | Kontrol edildi | Açık temada gövde metni (#17283E) / arka plan (#F7F9FC) ve vurgu metni (#08777E) / arka plan çiftleri 4.5:1 üstündedir; koyu tema metin çiftleri de kontrol edildi. |
| Hareket azaltma tercihi | Tamamlandı | `prefers-reduced-motion` medya sorgusu eklendi. |

## Gizlilik ve güvenlik

- Telefon numarası, ev adresi veya gereksiz kişisel veri istenmez.
- İletişim formu bir sunucuya istek göndermez; girilen verileri kaydetmez.
- Üçüncü taraf analiz/izleme betiği veya harici JavaScript kitaplığı bulunmaz.
- E-posta, isim ve mesaj alanları yalnızca örnek doğrulama için tarayıcıda işlenir.
- Proje açıklamalarında yakıt/rezerv hesaplayıcısının gerçek uçuş operasyonlarında kullanılamayacağı belirtilir.

## Tarayıcı ve cihaz testleri

| Test | Görünüm / girdi | Beklenen sonuç | Sonuç |
|---|---|---|---|
| Ana sayfa açılışı | Masaüstü 1440 × 1000 | İçerik taşmadan iki sütunlu giriş alanı görünür. | Başarılı |
| Ana sayfa açılışı | Tablet 768 × 1024 | Başlık ve görsel alanı taşmadan yerleşir. | Başarılı |
| Ana sayfa açılışı | Mobil 390 × 844 | Tek sütunlu görünüm; yatay kaydırma yoktur. | Başarılı |
| Koyu mod | Tema düğmesine tıklama | Tema değişir, `aria-pressed` güncellenir. | Başarılı |
| Mobil menü | 390 px ekranda menü düğmesi | Menü açılır/kapanır; `aria-expanded` değişir. | Başarılı |
| Proje filtresi | “Python” filtresi | Python etiketli kartlar kalır. | Başarılı |
| Proje araması | “rezerv” ifadesi | Yakıt/rezerv hesaplayıcısı görünür. | Başarılı |
| Boş arama | Eşleşmeyen ifade | “Eşleşen proje bulunamadı” mesajı görünür. | Başarılı |
| Form zorunlu alan | Tüm alanlar boş | Alan hataları gösterilir; ilk hatalı alana odaklanılır. | Başarılı |
| Form e-posta | `abc` | E-posta biçim hatası gösterilir. | Başarılı |
| Form mesaj | 5 karakter | En az 10 karakter uyarısı gösterilir. | Başarılı |
| Form geçerli veri | Geçerli ad/e-posta/konu/10+ karakter mesaj | Doğrulama başarılı mesajı görünür; veri gönderilmez ve saklanmaz. | Başarılı |

**Not:** Bu testler yerel tarayıcı testidir. GitHub Pages'e yükleme sonrasında canlı bağlantı, kaynak dosyalar ve harici bağlantılar yeniden kontrol edilmelidir.
