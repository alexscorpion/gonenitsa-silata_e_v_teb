import random

daljina_pole = 50
moya_poziciya = 0

while True:
    zar = random.randint(1, 6)

    if moya_poziciya + zar <= daljina_pole:
        moya_poziciya = moya_poziciya + zar

    for tekushta_poziciya in range(1, daljina_pole+1):
        if tekushta_poziciya == moya_poziciya:
            print("i"),
        else:
            print("_"),
    # край на for tekushta_poziciya

    print(zar)

    if moya_poziciya == daljina_pole:
        break
print("Specheli!")