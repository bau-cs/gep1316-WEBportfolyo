"""GEP1316 Odev 2 - Ad ve dogum yilina gore kisisel karsilama."""

from datetime import date


def get_birth_year() -> int:
    """Gecerli bir dogum yili alinana kadar kullanicidan tekrar ister."""
    current_year = date.today().year
    while True:
        raw_year = input("Dogum yilinizi girin: ").strip()
        try:
            birth_year = int(raw_year)
        except ValueError:
            print("Lutfen sadece tam sayi girin. Ornek: 2006")
            continue
        if birth_year < 1900 or birth_year > current_year:
            print(f"Dogum yili 1900 ile {current_year} arasinda olmalidir.")
            continue
        return birth_year


def main() -> None:
    """Programin giris ve cikis akislarini calistirir."""
    print("=" * 48)
    print("KISISEL KARSILAMA PROGRAMI")
    print("=" * 48)
    name = ""
    while not name:
        name = input("Adinizi girin: ").strip()
        if not name:
            print("Ad alani bos birakilamaz.")

    birth_year = get_birth_year()
    age = date.today().year - birth_year
    print("\n" + "-" * 48)
    print(f"Merhaba {name}! {age} yasindasin.")
    print("Kodlama yolculugunda basarilar dilerim.")
    print("-" * 48)
    input("Programi kapatmak icin Enter tusuna basin...")


if __name__ == "__main__":
    main()
