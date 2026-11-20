# Yapay Zekâ ile Çalışma Günlüğü

**Kullanılan araç:** ChatGPT (OpenAI)  
**Kullanım biçimi:** Ön yüz kodu için taslak üretimi, kod açıklaması, hata kontrolü, metin düzenleme ve test senaryosu oluşturma.

Aşağıdaki kayıtlar, geliştirme aşamalarında kullanılan istemlerin düzenlenmiş özetidir. Her üretilen çıktı doğrudan kabul edilmemiş; dosyalar çalıştırılarak, kod gözden geçirilerek ve yönerge maddeleriyle karşılaştırılarak son hâline getirilmiştir.

| No | Kullanılan istem | YZ'nin katkısı | Karar ve yapılan düzenleme |
|---|---|---|---|
| 1 | “Pilotaj ve bilgisayar mühendisliği alanlarını birleştiren, dört sayfalı ve Türkçe bir kişisel portfolyo için anlamsal HTML sayfa yapısı oluştur. Her sayfanın içeriğini ayrı tut.” | Ana sayfa, hakkımda, projeler ve iletişim için sayfa iskeletleri önerdi. | Kabul edildi. İçerik gerçek ders projelerine göre düzenlendi; iletişimde telefon ve adres kullanılmadı. |
| 2 | “Masaüstü, tablet ve telefon ekranlarında tutarlı görünecek, ortak CSS kullanan modern bir tasarım sistemi hazırla. En az iki medya sorgusu ekle.” | Renk değişkenleri, kart yerleşimleri, tipografi ve mobil düzen önerdi. | Büyük ölçüde kabul edildi. Mobil menü, kart sıralaması ve küçük ekran boşlukları ayrıca ayarlandı; harici font/kitaplık bağımlılığı kaldırıldı. |
| 3 | “JavaScript ile koyu mod ve mobil menü oluştur. Klavye ve ekran okuyucu durumlarını uygun ARIA nitelikleriyle belirt.” | Tema anahtarı ve açılır menü olaylarını oluşturdu. | Kabul edildi. `aria-pressed`, `aria-expanded`, Escape tuşuyla kapatma ve odak görünümü eklendi. Tema tercihi yalnızca tarayıcı depolamasında tutuldu. |
| 4 | “Proje kartlarına kategori filtreleme ve Türkçe arama ekle. Hiç sonuç yoksa kullanıcıya anlaşılır bir mesaj göster.” | Kart kategorisi, arama terimleri ve sonuç sayacı için filtreleme mantığı önerdi. | Kabul edildi. Filtre düğmelerinin durumları `aria-pressed` ile güncellendi; filtre sıfırlama işlevi eklendi. |
| 5 | “İletişim formunu ad, e-posta, konu ve mesaj alanlarıyla doğrula; hatalı alana odaklan ve başarılı doğrulama mesajı göster.” | Alan kontrolleri ve geri bildirim mekanizması önerdi. | İlk taslakta yalnızca yer tutucu metne güvenmenin etiket erişilebilirliğini zayıflatabileceği ve formun gerçekten gönderiliyormuş gibi algılanabileceği görüldü. Görünür `<label>`, hata metni, `aria-invalid`, canlı geri bildirim ve açık gizlilik notu eklendi. Formun ağ isteği göndermediği doğrulandı. |
| 6 | “Proje kartlarının açıklamalarını bu ders çalışmalarına göre düzenle: uçuş öncesi belge kontrol algoritması, GitHub ilk depo, uçuş yakıtı/rezerv hesaplayıcısı ve uçuş eğitim kayıt sistemi. Her biri için ‘ne öğrendim’ cümlesi ekle.” | Kart açıklamaları ve öğrenme çıktıları taslağı oluşturdu. | İçerik önceki ödev belgeleriyle karşılaştırıldı. Havacılık hesaplayıcısının ve kayıt yazılımının gerçek operasyonel karar aracı olmadığı açıkça belirtildi. |
| 7 | “Siteyi erişilebilirlik, gizlilik ve mobil görünüm açısından kontrol et. Üç ekran boyutu için test planı ve form test senaryoları hazırla.” | Kontrol maddeleri ve test örnekleri önerdi. | Kabul edildi ve gerçek tarayıcı testleriyle doğrulandı. Ekran görüntüleri masaüstü, tablet ve mobil boyutlarda alındı. |

## Tespit edilen erişilebilirlik/güvenlik riski ve düzeltme

İletişim formunun ilk tasarım değerlendirmesinde, yer tutucu metnin tek başına alan etiketi olarak kullanılmasının ekran okuyucu ve kullanıcı deneyimi açısından yetersiz kalabileceği görüldü. Her alan için görünür `<label>` eklendi; doğrulama hataları ayrı metinlerle gösterildi ve ilgili alana `aria-invalid` niteliği verildi. Ayrıca formun yalnızca istemci tarafında doğrulama yaptığı, verileri sunucuya göndermediği veya kaydetmediği açıkça yazıldı. Böylece kullanıcıya sahte bir gönderim veya veri saklama izlenimi verilmesi önlendi.

## Sorumluluk
YZ çıktıları öneri olarak kullanılmıştır. Son kod, metin, bağlantılar, testler ve teslim dosyalarının doğruluğunu kontrol etme sorumluluğu öğrencidedir.
