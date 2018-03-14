import json
from os import path
from sys import argv
import signal

YEAR = argv[1]
AGENDA_FILE = "../agendas_" + YEAR + ".json"
AGENDA_FILE_TAGS = "./agendas_" + YEAR + "_tags.json"

with open(AGENDA_FILE, 'r') as agendas:
    AGENDA_JSON = json.load(agendas)
if (path.exists(AGENDA_FILE_TAGS)):
    with open(AGENDA_FILE_TAGS, 'r') as tagged:
        TAG_JSON = json.load(tagged)
else:
    TAG_JSON = dict()


def signal_handler(signal, frame):
    TAG_JSON[AGENDA][secondary].pop()
    print()
    print("Quitting... saving state, thanks!")
    terminate()


signal.signal(signal.SIGINT, signal_handler)


def terminate():
    with open(AGENDA_FILE_TAGS, 'w') as tagged:
        json.dump(TAG_JSON, tagged)
    exit()


tags_dict = {
    "0": "Community",
    "1": "Learning",
    "2": "Health",
    "3": "Economic opportunity",
    "4": "Responsive government",
    "5": "Environment",
    "6": "Sustainability",
    "7": "Public Safety",
    "8": "Parks and Recreation",
    "9": "Free Speech",
    "10": "Housing",
    "11": "Mobility",
    "12": "Pets",
    "13": "Zoning",
    "14": "Infrastructure",
    "15": "Sanitation"
}
for AGENDA in AGENDA_JSON:
    if (AGENDA not in TAG_JSON):
        TAG_JSON[AGENDA] = []
    secondary = 0
    print(AGENDA)
    # 2 layers of arrays? What was I thinking?
    for AGENDA_2 in AGENDA_JSON[AGENDA]:
        if len(TAG_JSON[AGENDA]) <= secondary:
            TAG_JSON[AGENDA].append([])
        item_number = 0
        for AGENDA_ITEM in AGENDA_2:
            if len(TAG_JSON[AGENDA][secondary]) <= item_number:
                TAG_JSON[AGENDA][secondary].append(dict())
            else:
                item_number += 1
                continue
            print("SECONDARY:" + str(secondary) + " ITEM#:" + str(item_number))
            print(AGENDA_ITEM["Title"])
            print("0=Community")
            print("1=Learning")
            print("2=Health")
            print("3=Economic opportunity")
            print("4=Responsive government")
            print("5=Environment")
            print("6=Sustainability")
            print("7=Public Safety")
            print("8=Parks and Recreation")
            print("9=Free Speech")
            print("10=Housing")
            print("11=Mobility")
            print("12=Pets")
            print("13=Zoning")
            print("14=Infrastructure")
            print("15=Sanitation")
            tags = input(
                "Comma separated values (m for more info, q to quit):")
            if ("m" in tags or "M" in tags):
                if ("Recommendations" in AGENDA_ITEM):
                    print(AGENDA_ITEM["Recommendations"])
                else:
                    if ("Body" in AGENDA_ITEM):
                        print(AGENDA_ITEM['Body'])
                    else:
                        print("No more information")
                tags = input("Comma separated values (q to quit):")
            if ("q" in tags or "Q" in tags):
                TAG_JSON[AGENDA][secondary].pop()
                terminate()
            tags = tags.split(",")
            tags_full = []
            for tag in tags:
                stripped = tag.strip()
                if not (stripped == "") and stripped in tags_dict:
                    tags_full.append(tags_dict[stripped])
            TAG_JSON[AGENDA][secondary][item_number]["Tags"] = tags_full
            item_number += 1
        secondary += 1
terminate()
