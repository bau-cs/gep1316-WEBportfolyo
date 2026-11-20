# Hüseyin Can Sevinç — Kişisel Web Portfolyosu

**Ders:** GEP1316 Kodlama Okuryazarlığı  
**Ödev:** Ara Değerlendirme Ödevi 2 — Kişisel Web Portfolyosu (GitHub Pages)  
**Dönem:** 2026-2027 Güz  
**Öğrenci:** Hüseyin Can Sevinç

## Canlı site

GitHub Pages yayını açıldıktan sonra bağlantı şu biçimde olacaktır:

`https://<GITHUB-KULLANICI-ADIN>.github.io/gep1316-portfolyo/`

> Bu paket henüz herhangi bir GitHub hesabına yüklenmediği için canlı bağlantı henüz oluşmamıştır. Depo `gep1316-portfolyo` adıyla oluşturulup GitHub Pages etkinleştirildiğinde yukarıdaki kullanıcı adı alanı gerçek hesap adıyla değiştirilmelidir.

## Site sayfaları

1. `index.html` — Ana sayfa, kısa tanıtım, avatar ve gezinme.
2. `about.html` — Eğitim, ilgi alanları ve kodlama/yapay zekânın havacılıktaki yeri.
3. `projects.html` — Dört proje kartı, GitHub bağlantıları, kategori filtresi ve arama.
4. `contact.html` — Doğrulamalı iletişim formu ve profesyonel bağlantılar.

## Dosya yapısı

```text
GEP1316_Odev2_HuseyinCanSevinc/
├── index.html
├── about.html
├── projects.html
├── contact.html
├── style.css
├── script.js
├── README.md
├── work-samples/
│   ├── document-checklist/
│   ├── github-first-repository/
│   ├── fuel-reserve-calculator/
│   └── flight-training-record-system/
├── docs/
│   ├── GEP1316_Odev2_HuseyinCanSevinc_Rapor.docx
│   ├── GEP1316_Odev2_HuseyinCanSevinc_Rapor.pdf
│   ├── PROMPT_GUNLUGU.md
│   └── ERISILEBILIRLIK_KONTROL_LISTESI.md
└── screenshots/
    ├── desktop.png
    ├── tablet.png
    └── mobile.png
```

## GitHub'a yükleme ve Pages yayını

1. GitHub hesabınıza giriş yapın ve **New repository** seçeneğini açın.
2. Repository name alanına `gep1316-portfolyo` yazın ve depoyu **Public** olarak oluşturun.
3. Bu klasörün içindeki dosya ve klasörlerin tamamını deponun ana dizinine yükleyin. `index.html` dosyası doğrudan kök dizinde bulunmalıdır.
4. GitHub deposunda **Settings → Pages** bölümüne girin.
5. **Build and deployment** altında **Deploy from a branch** seçin.
6. Branch olarak `main`, klasör olarak `/(root)` seçip **Save** düğmesine basın.
7. Pages bölümünde gösterilen canlı adresi kopyalayın ve bu README'deki canlı site alanına ekleyin.
8. `projects.html` sayfasını açıp dört GitHub bağlantısının doğru hedeflere gittiğini kontrol edin. GitHub Pages alan adı `kullaniciadi.github.io` olduğunda ilk üç proje bağlantısı otomatik olarak bu deponun `work-samples/` klasörlerine yönlendirilir.

## Yerel çalıştırma

HTML sayfaları doğrudan açılabilir. Yerel bir sunucu kullanmak için proje ana dizininde:

```bash
python -m http.server 8000
```

Ardından tarayıcıda `http://localhost:8000` adresini açın.

## Örnek Python çalışmalarını çalıştırma

İlk depo örneği:

```bash
python work-samples/github-first-repository/merhaba.py
```

Yakıt/rezerv hesaplayıcısı:

```bash
python work-samples/fuel-reserve-calculator/main.py
```

Hesaplayıcı testleri:

```bash
cd work-samples/fuel-reserve-calculator
python -m unittest -v
```

## JavaScript etkileşimleri

- Koyu/açık tema değiştirme (tercih tarayıcıda saklanır).
- Mobil gezinme menüsünü açma/kapatma.
- Proje kartlarını kategoriye göre filtreleme.
- Projelerde metin arama ve sonuç bulunamadığında boş durum mesajı.
- İletişim formunda ad, e-posta, konu ve mesaj doğrulaması; karakter sayacı ve geri bildirim.
- Form gönderimi sunucuya yapılmaz; veriler saklanmaz.

## Duyarlı tasarım

`style.css` dosyasında masaüstü/tablet ve mobil yerleşimler için birden fazla `@media` kuralı, ayrıca kullanıcının `prefers-reduced-motion` tercihini dikkate alan bir kural bulunur.

## Erişilebilirlik ve gizlilik

- Sayfalarda `header`, `nav`, `main`, `section` ve `footer` gibi anlamsal HTML öğeleri kullanılır.
- Klavye kullanıcıları için atlama bağlantısı ve belirgin odak görünümü vardır.
- Form kontrollerinin görünen etiketleri, zorunlu alanları ve hata mesajları bulunur.
- Tema ve mobil menü durumları `aria-pressed` / `aria-expanded` ile duyurulur.
- Üçüncü taraf izleyici veya harici JavaScript kütüphanesi kullanılmaz.
- İletişim formu yalnızca ön yüz doğrulama demosudur; mesaj göndermez veya kaydetmez.

## Önemli not

Yakıt hesaplayıcısı ve uçuş eğitim kayıt sistemi yalnızca akademik/öğrenme amaçlı örneklerdir. Gerçek uçuş planlaması, yakıt planlaması, uçuşa elverişlilik veya operasyonel kararlar için kullanılmamalıdır.
