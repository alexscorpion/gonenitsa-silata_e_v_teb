import random
import time

daljina_pole = 50
moya_poziciya = 0

while True:
    zar = random.randint(1, 6)
    print(zar)

    if moya_poziciya == 0:
        if zar == 6:
            moya_poziciya = 1
            zar = 0

    if moya_poziciya != 0:
        while zar == 6:
            print(" Допълнително Хвърляне! ")
            if moya_poziciya + zar <= daljina_pole:
                moya_poziciya = moya_poziciya + zar
            zar = random.randint(1, 6)
            print("  ", zar)
        
        if moya_poziciya + zar <= daljina_pole:
                moya_poziciya = moya_poziciya + zar


    for tekushta_poziciya in range(1, daljina_pole+1):
        if tekushta_poziciya == moya_poziciya:
            print("i", end="")
        else:
            print("_", end="")
        print(" ", end="")
    # край на for tekushta_poziciya
    time.sleep(0.3)

    if moya_poziciya == daljina_pole:
        break
print("Specheli!")