"""Bir klasördeki (alt klasörler dahil) dosyaları uzantıya göre sayar.

Yalnızca okuma yapar; hiçbir dosyayı taşımaz, silmez veya değiştirmez.

Kullanım:
    python dosya_say.py              -> Masaüstü\\deneme klasörünü sayar
    python dosya_say.py "<klasör>"   -> verilen klasörü sayar
"""

import sys
from collections import Counter
from pathlib import Path

VARSAYILAN_KLASOR = Path.home() / "Desktop" / "deneme"


def dosyalari_say(klasor: Path) -> Counter:
    sayac = Counter()
    for yol in klasor.rglob("*"):
        if yol.is_file():
            uzanti = yol.suffix.lower() or "(uzantısız)"
            sayac[uzanti] += 1
    return sayac


def main() -> int:
    klasor = Path(sys.argv[1]) if len(sys.argv) > 1 else VARSAYILAN_KLASOR

    if not klasor.is_dir():
        print(f"Hata: klasör bulunamadı: {klasor}")
        return 1

    sayac = dosyalari_say(klasor)
    print(f"Klasör: {klasor}\n")

    if not sayac:
        print("Hiç dosya bulunamadı.")
        return 0

    genislik = max(len(u) for u in sayac) + 4
    for uzanti, adet in sorted(sayac.items(), key=lambda x: (-x[1], x[0])):
        print(f"{uzanti:<{genislik}}{adet:>5}")
    print("-" * (genislik + 5))
    print(f"{'Toplam':<{genislik}}{sum(sayac.values()):>5}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
