"""Ucusa hazirlik evraklari icin egitim amacli hatirlatma algoritmasi."""


def find_missing_documents(document_status: dict[str, bool]) -> list[str]:
    """Mevcut/gecerli olarak isaretlenmeyen belgeleri liste halinde dondurur."""
    return [document for document, is_valid in document_status.items() if not is_valid]


def main() -> None:
    required_documents = [
        "Pilot lisansi",
        "Saglik sertifikasi",
        "Kimlik belgesi",
        "Ucus icin gerekli evrak",
    ]
    document_status: dict[str, bool] = {}

    print("UCUS ONCESI BELGE KONTROLU - EGITIM DEMOSU")
    print("Her belge icin E (mevcut/gecerli) veya H (eksik/gecerli degil) girin.\n")
    for document in required_documents:
        while True:
            answer = input(f"{document}: ").strip().upper()
            if answer in {"E", "H"}:
                document_status[document] = answer == "E"
                break
            print("Gecersiz cevap. Lutfen E veya H girin.")

    missing = find_missing_documents(document_status)
    if not missing:
        print("Kontrol listesinde eksik belge bildirilmedi.")
    else:
        print("Eksik/gecerli olmadigi bildirilen belgeler:")
        for document in missing:
            print(f"- {document}")
    print("Bu program yalnizca hatirlatmadir; ucus izni veya ucusa elverislilik karari degildir.")


if __name__ == "__main__":
    main()
