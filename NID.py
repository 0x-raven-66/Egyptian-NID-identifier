def getBearthDate(centry, YY, MM, DD, year=0):
    if int(centry) == 2:
        year = "19"+YY
    elif int(centry) == 3:
        year = "20"+YY
    BearthDate = f"{year}/{MM}/{DD}"
    return BearthDate


def getGov(govNum):
    govs = {
        "01": "Cairo",
        "02": "Alexandria",
        "03": "Port Said",
        "04": "Suez",
        "11": "Damietta",
        "12": "Dakahlia",
        "13": "Sharqia",
        "14": "Qalyubia",
        "15": "Kafr El-Sheikh",
        "16": "Gharbia",
        "17": "Menoufia",
        "18": "Beheira",
        "19": "Ismailia",
        "21": "Giza",
        "22": "Bani Sweif",
        "23": "Fayoum",
        "24": "Minya",
        "25": "Asyut",
        "26": "Sohag",
        "27": "Qena",
        "28": "Aswan",
        "29": "Luxor",
        "31": "Red Sea",
        "32": "The new Valley",
        "33": "Matrouh",
        "34": "North Sinaa",
        "35": "South Sinaa",
        "88": "Outside the republic"
    }
    return govs.get(govNum, "Invalid governorate code")


def getGender(genderNum):
    return "Female" if int(genderNum) % 2 == 0 else "Male"


NID = input("NID:")
if len(NID) == 14:
    centry = NID[0]
    YY = NID[1:3]
    MM = NID[3:5]
    DD = NID[5:7]
    govNum = NID[7:9]
    uniqueNum = NID[9:12]
    genderNum = NID[12]
    checkNum = NID[13]
    print(f"Berath Date => {getBearthDate(centry, YY, MM, DD)}")
    print(f"Governorate => {getGov(govNum)}")
    print(f"Gender => {getGender(genderNum)}")
    print(f"Birth unique number => {uniqueNum}")
    print(f"Validation number => {checkNum}")
else:
    print("NID is not a valid")
