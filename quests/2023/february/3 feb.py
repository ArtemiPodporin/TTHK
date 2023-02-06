import datetime

ikodid = []
arvud = []

for i in range(4):
  KOOD = input("Andke isikukood palun!: ")
  if len(KOOD) != 11:
    print("Andke palun 11-length isikukood.")
    arvud.append(KOOD)
    continue
  
  if KOOD[0] not in ["1", "2", "3", "4", "5", "6"]:
    print("Esimene number peab olema 1-st kuni 6-ni.")
    arvud.append(KOOD)
    continue

  SUNNIPAEV = datetime.datetime.strptime(KOOD[1:7], '%d%m%y').date()

  # Control number calculation
  KAAL1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
  KAAL2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
  sum = 0
  for j in range(10):
    sum += int(KOOD[j]) * KAAL1[j]
  
  KONTROLLNUMBER = sum % 11
  if KONTROLLNUMBER == 10:
    sum = 0
    for j in range(10):
      sum += int(KOOD[j]) * KAAL2[j]
    KONTROLLNUMBER = sum % 11

  if KONTROLLNUMBER != int(KOOD[10]):
    print("Invalid control number. Please enter a valid personal code.")
    arvud.append(KOOD)
    continue

  if KOOD[0] in ["1", "3", "5"]:
    SUGU = "MEES"
  else:
    SUGU = "NAINE"

  HAIGLA = ""
  if KOOD[7:10] == "001":
    HAIGLA = "Kuressaare Hospital"
  elif KOOD[7:10] == "011":
    HAIGLA = "Tartu University Women's Clinic, Tartu County, Tartu"
  elif KOOD[7:10] >= "021" and KOOD[7:10] <= "220":
    HAIGLA = "Ida-Tallinn Central Hospital, Pelgulinna Maternity Hospital, Hiiumaa, Keila, Rapla Hospital, Loksa Hospital"
  elif KOOD[7:10] >= "221" and KOOD[7:10] <= "270":
    HAIGLA = "Ida-Viru Central Hospital (Kohtla-Järve)"
  elif KOOD[7:10] >= "271" and KOOD[7:10] <= "370":
    HAIGLA = "Tartu clinic, Riverva Hospital"
  elif KOOD[7:10] >= "371" and KOOD[7:10] <= "420":
    HAIGLA = "Narva Hospital"
  elif KOOD[7:10] >= "421" and KOOD[7:10] <= "470":
    HAIGLA = "Pärnu Hospital"
  elif KOOD[7:10] >= "471" and KOOD[7:10] <= "490":
    HAIGLA = "Tallinn Pelgulinna Maternity Hospital, Haapsalu Hospital"
  elif KOOD[7:10] >= "491" and KOOD[7:10] <= "520":
    HAIGLA = "Järvamaa Hospital (Paide)"
  elif KOOD[7:10] >= "521" and KOOD[7:10] <= "570":
    HAIGLA = "Rakvere, Tapa Hospital"
  elif KOOD[7:10] >= "571" and KOOD[7:10] <= "600":
    HAIGLA = "Valga Hospital"
  elif KOOD[7:10] >= "601" and KOOD[7:10] <= "650":
    HAIGLA = "Viljandi Hospital"
  elif KOOD[7:10] >= "651" and KOOD[7:10] <= "700":
    HAIGLA = "Lõuna-Eesti Haigla (Võru), Põlva Haigla"
