import math


def macht(getal, macht=2):
    return int(getal) ** int(macht)


def delen(deeltal, deler):
    return int(deeltal) / int(deler)


if __name__ == "__main__":
    verder = True
    while (verder):
        try:
            wat = input(
                "Wat wil u doen? (macht, vierkantswortel, maal, delen, plus, stop): ")
            if (wat == "macht"):
                getallen = input("Het grondtal: ")
                getallen += ":" + input("De macht: ")
                result = macht(getallen.split(":")[0], getallen.split(":")[1])
                print(f"Het resultaat is {result}.")
            elif (wat == "vierkantswortel"):
                getallen = input("Het grondtal: ")
                result = math.sqrt(int(getallen))
                print(f"Het resultaat is {result}.")
            elif (wat == "maal"):
                result = 1
                last = int(
                    input("Geef een getal in dat u wilt vermenigvuldigen: "))
                while (last != 0):
                    result *= last
                    last = int(input(
                        "Geef een getal in dat u wilt vermenigvuldigen. Type '0' om te annuleren: "))
                print(f"Het resultaat is {result}")
            elif (wat == "delen"):
                getallen = input("Het deeltal: ")
                getallen += ":" + input("De deler: ")
                result = delen(getallen.split(":")[0], getallen.split(":")[1])
                print(f"Het resultaat is {result}.")
            elif (wat == "plus"):
                result = 0
                last = int(input("Geef een getal in dat u wilt optellen: "))
                while (last != 0):
                    result += last
                    last = int(input(
                        "Geef een getal in dat u wilt optellen. Type '0' om te annuleren: "))
                print(f"Het resultaat is {result}")
            elif (wat == "stop"):
                verder = False
        except:
            print("Foute invoer! Probeer opnieuw.")
