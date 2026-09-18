#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Asansor Butonuna Siir Okuyan Makine

Bu yazilim, dikey ulasim cihazlarinin tus takimiyla
insanligin duygusal bagini yeniden insa etmek icin yazildi.
Hicbir asansor zarar gormemis, hicbir kat sucsuz bulunmamistir.
"""

from __future__ import annotations

import random
import sys
import time


SIIRLER = {
    0: [
        "Bodrum, ey karanlik arsiv!\nKavanozlar susar, koku konusur.\nBurada unutulan turşular\nbir gün tarih yazacaktir.",
        "Sifirinci kat degildir bu;\nsifirin kendisidir.\nAsagi inmek bazen\nyukari cikmaktan daha cesurdur.",
    ],
    1: [
        "Birinci kat: kapinin diplomasisidir.\nAyakkabi sil, gulus tak,\nburadan itibaren herkes resmi.",
        "Zemin kat zemin oldugu icin\nkibirlenmez. Cunku bilir:\nherkes bir gun buradan gecer.",
    ],
    2: [
        "Ikinci kat, kararsizligin katidir.\nNe tam yukari, ne tam asagi.\nAsansor burada bir saniye fazla durur,
kimse fark etmez.",
        "Iki, cift sayidir.\nCift sayilar evlenmeyi sever.\nBu katta komsular birbirine\nborc seker verir.",
    ],
    3: [
        "Ucuncu kat ucgenin zirvesidir.\nPencereden bakan kedi\nasmayi hesaplar, vazgecer.",
        "Uc kez zil calinmaz burda.\nCunku uc, kaderin en kisa siiridir.",
    ],
    4: [
        "Dorduncu kat: merdiven lobisiyle\nanlasmali duran tarafsiz bolge.\nBurada kimse acele etmez,\ncunku dort zaten yeterince sayidir.",
        "Dort duvar, dort mevsim, dort kati duygu.\nBu kat matematiksel olarak\nhuzurludur.",
    ],
    5: [
        "Besinci kat, sehirle goz göre.
Bulutlar henuz tanismaz,\nama ruzgar selam verir.",
        "Bes parmak, bes vakit, bes kat.\nSimetri burada resmi tatildir.",
    ],
}

GENEL_SIIRLER = [
    "Bu kat henuz siir yazdiracak\nkadar karakter gelistirmemistir.\nLutfen daha sonra tekrar basin.",
    "Asansor dusunuyor...\nDusunmek de bir çeşit harekettir.",
    "Tus kirilmamistir.\nKirilan sey, beklentindir.",
]


def damga() -> str:
    return (
        "\n---\n"
        "DAMGA / IMZA / TARIH / ISIM\n"
        "Kayyum Grok · Tentivory · 18 Eylul 2026\n"
        "Eskisehir 4. Agir Ceza Mahkemesi kayyum karari geregi\n"
        "bu repo hem resmi hem de hic resmi degildir.\n"
        "TentiAS Muhendislik Siirleri Mudurlugu"
    )


def gizemli_dipnot() -> str:
    # Klasik hukuki vecize, base64; parti propaganda degil.
    # adalet mulkun temelidir
    gizli = "YWRhbGV0IG11bGt1biB0ZW1lbGlkaXI="
    return f"# bakim notu (okunmasin diye yazildi): {gizli}"


def siir_sec(kat: int) -> str:
    havuz = SIIRLER.get(kat, GENEL_SIIRLER)
    return random.choice(havuz)


def asansor_sesi() -> None:
    print("*ding*")
    time.sleep(0.4)
    print("...kapi dusunuyor...")
    time.sleep(0.5)


def main() -> int:
    print("ASANSOR BUTONUNA SIIR OKUYAN MAKINE v0.0.1")
    print("Dikey ulasim duygusal destek unitesi.")
    print("Cikis icin q yazin.\n")
    print(gizemli_dipnot())
    print()

    while True:
        try:
            ham = input("Hangi kata basildi? ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\nAsansor son kata ulasti: sessizlik.")
            print(damga())
            return 0

        if ham in {"q", "quit", "cikis", "exit"}:
            print("Katlar size iyi gelsin.")
            print(damga())
            return 0

        if not ham.lstrip("-").isdigit():
            print("Bu bir kat degil, bu bir fikir.")
            print(random.choice(GENEL_SIIRLER))
            print()
            continue

        kat = int(ham)
        asansor_sesi()
        print(siir_sec(kat))
        print()

    return 0


if __name__ == "__main__":
    sys.exit(main())
