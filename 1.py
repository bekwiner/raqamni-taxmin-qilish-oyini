import random

print("Raqamni taxmin qilish o'yiniga xush kelibsiz!")
pastki = int(input("Oraliqning pastki chegarasini kiriting: "))
yuqori = int(input("Oraliqning yuqori chegarasini kiriting: "))

tasodifiy_son = random.randint(pastki, yuqori)
harakatlar = 0
maksimal_harakatlar = 5  

while harakatlar < maksimal_harakatlar:
    taxmin = int(input("Raqamni taxmin qiling: "))
    harakatlar += 1

    if taxmin > tasodifiy_son:
        print("Qayta urinib ko'ring! Siz juda yuqori taxmin qildingiz.")
    elif taxmin < tasodifiy_son:
        print("Qayta urinib ko'ring! Siz juda kichik taxmin qildingiz.")
    else:
        print(f"Tabriklaymiz! Siz {harakatlar} harakatda sonni taxmin qila oldingiz!")
        break
else:
    print("Keyingi safar omad tilaymiz!")