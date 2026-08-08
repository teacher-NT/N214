import os
os.system("cls")
from translate import Translator


tillar = {
    "O'zbekcha": "uz",
    "Turkcha": "tr",
    "Qozoqcha": "kk",
    "Inglizcha": "en",
    "Ruscha": "ru",
    "Nemischa": "de",
    "Fransuzcha": "fr",
    "Ispancha": "es",
    "Yaponcha": "ja",
    "Koreyscha": "ko",
    "Arabcha": "ar",
    "Forscha": "fa"
}

print("TARJIMON DASTURIGA XUSH KELIBSIZ")

next = "yes"
while next == 'yes':
    print("Qaysi tildan tajima qilamiz?")
    for i, k in enumerate(tillar.keys()):
        print("| ", i, k)
    from_lang = int(input(">>> "))
    from_lang = tillar[list(tillar.keys())[from_lang]]
    os.system("cls")
    print("Qaysi tilga tajima qilamiz?")
    for i, k in enumerate(tillar.keys()):
        print("| ", i, k)
    to_lang = int(input(">>> "))
    to_lang = tillar[list(tillar.keys())[to_lang]]
    os.system("cls")
    tarjimon = Translator(from_lang=from_lang, to_lang=to_lang)
    text = input("Matn kiriting: ")
    text = tarjimon.translate(text)
    print("Tarjimasi:\n", text, end="\n\n")

    next = input("Yana tarjima qilasizmi? (yes/no): ").lower()
    os.system("cls")

