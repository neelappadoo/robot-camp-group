

def solution_station_5(name: str) -> int:
    groups = {
        "1": [
            "Ainas", "Tobit", "Yasmin", "Zoë",
            "Iuliia", "Klementyna", "Markus", "Mufang", "Oumaima",
            "Ebony", "Nandini", "Nathan", "Tiara", "Yurui",
            "Ben", "Christopher", "Lula", "Muni", "Yuvraj",
        ],
        "2": [
            "Huy", "Iris", "Katharina", "Minseo", "Sade",
            "Alex", "Arwen", "Rajko", "Sylwia", "Zeno",
            "Christina", "Helen", "Mark", "Mats", "Vadim",
            "David", "Lora", "Quinn", "Tarling",
        ],
        "3": [
            "Elizabeth", "Gabriel", "Jakub", "Luc", "Soelie",
            "Aleksandra", "Arnav", "Donna", "Milan", "Rongze",
            "Cris", "Jingqi", "Oliver", "Vaayu", "Yusef",
            "Afua", "Anna", "Daniel", "Nataly", "Rafael",
        ],
        "4": [
            "Jeremy", "Krishiv", "Neel", "Yujie", "yutong",
            "An", "Heer", "Paige", "Samir",
            "Amalia", "Douwe", "Illya", "Maria", "Rakin",
            "Lara", "Lucas", "Michelle", "Oliwia", "Tom",
        ]
    }


    if name in groups['1']:
        return 1
    elif name in groups['2']:
        return 2
    elif name in groups['3']:
        return 3
    elif name in groups['4']:
        return 4
