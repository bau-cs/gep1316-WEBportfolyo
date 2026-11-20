"""GEP1316 Odev 3 - Egitim amacli ucus yakiti ve rezerv hesaplayicisi."""


def calculate_fuel(
    onboard_fuel_l: float,
    hourly_consumption_lph: float,
    flight_minutes: int,
    reserve_minutes: int,
) -> dict[str, float | bool]:
    """Verilen girdilerden yakit miktarlarini hesaplar.

    Bu fonksiyon yalnizca ders icin basit bir matematik modelidir.
    Gercek operasyonel yakit planlamasi icin kullanilamaz.
    """
    if onboard_fuel_l <= 0:
        raise ValueError("Uctaki yakit miktari sifirdan buyuk olmalidir.")
    if hourly_consumption_lph <= 0:
        raise ValueError("Saatlik tuketim sifirdan buyuk olmalidir.")
    if flight_minutes <= 0:
        raise ValueError("Ucus suresi sifirdan buyuk olmalidir.")
    if reserve_minutes < 0:
        raise ValueError("Rezerv suresi negatif olamaz.")

    flight_fuel_l = hourly_consumption_lph * flight_minutes / 60
    reserve_fuel_l = hourly_consumption_lph * reserve_minutes / 60
    remaining_fuel_l = onboard_fuel_l - flight_fuel_l
    reserve_sufficient = remaining_fuel_l >= reserve_fuel_l

    return {
        "flight_fuel_l": flight_fuel_l,
        "reserve_fuel_l": reserve_fuel_l,
        "remaining_fuel_l": remaining_fuel_l,
        "reserve_sufficient": reserve_sufficient,
    }


def read_positive_float(prompt: str) -> float:
    """Sifirdan buyuk bir ondalikli sayi alinana kadar tekrar ister."""
    while True:
        raw_value = input(prompt).strip().replace(",", ".")
        try:
            value = float(raw_value)
        except ValueError:
            print("Gecersiz giris. Lutfen sayisal bir deger girin.")
            continue
        if value <= 0:
            print("Deger sifirdan buyuk olmalidir. Tekrar deneyin.")
            continue
        return value


def read_minutes(prompt: str, allow_zero: bool = False) -> int:
    """Tam sayi dakika alir; negatif ve uygun olmayan degerleri reddeder."""
    while True:
        raw_value = input(prompt).strip()
        try:
            value = int(raw_value)
        except ValueError:
            print("Gecersiz giris. Dakikayi tam sayi olarak yazin.")
            continue
        if value < 0 or (value == 0 and not allow_zero):
            minimum = "0 veya daha buyuk" if allow_zero else "0'dan buyuk"
            print(f"Dakika {minimum} olmalidir. Tekrar deneyin.")
            continue
        return value


def main() -> None:
    print("=" * 58)
    print("        UCUS YAKITI VE YEDEK YAKIT HESAPLAYICISI")
    print("=" * 58)
    print("Bu program yalnizca egitim amacli basit bir hesaplama ornegidir.")
    print("Gercek ucus operasyonlarinda kullanilamaz.\n")

    while True:
        try:
            onboard_fuel = read_positive_float("Uctaki yakit miktari (L): ")
            hourly_consumption = read_positive_float("Saatlik yakit tuketimi (L/saat): ")
            flight_minutes = read_minutes("Planlanan ucus suresi (dakika): ")
            reserve_minutes = read_minutes("Ayrilacak rezerv suresi (dakika): ", allow_zero=True)
            result = calculate_fuel(
                onboard_fuel,
                hourly_consumption,
                flight_minutes,
                reserve_minutes,
            )
            break
        except ValueError as error:
            print(f"Girdi hatasi: {error} Lutfen tekrar deneyin.\n")

    print("\n" + "-" * 58)
    print(f"Planlanan ucus icin gereken yakit : {result['flight_fuel_l']:.2f} L")
    print(f"Ayrilan rezerv icin gereken yakit : {result['reserve_fuel_l']:.2f} L")
    print(f"Ucus sonunda beklenen kalan yakit : {result['remaining_fuel_l']:.2f} L")
    print("-" * 58)
    reserve_status: bool = bool(result["reserve_sufficient"])
    if reserve_status:
        print("Egitim modeline gore rezerv miktari yeterli gorunuyor.")
    else:
        print("Egitim modeline gore rezerv miktari yeterli degil.")
    print("NOT: Bu cikti operasyonel ucus yakit karari degildir.")
    input("Programi kapatmak icin Enter tusuna basin...")


if __name__ == "__main__":
    main()
