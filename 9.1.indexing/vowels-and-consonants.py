p = input()
g = s = 0
for c in p:
    if c in 'aeiouAEIOU' # 'ауоыиэяюёеАУОЫИЭЯЮЁЕ':
        g += 1
    if c in 'bcdfghjklmnpqrstvwxyBCDFGHJKLMNPQRSTVWXY' # 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ':
        s += 1
print(f"Number of vowels is {g}")
print(f"Number of consonants is {s}")
