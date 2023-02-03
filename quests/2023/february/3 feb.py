from math import *
import datetime

ikoodid = []
arvud = []

# Counter for number of attempts
count = 0

while count < 5:
  personal_code = input("Enter your personal code: ")
  
  # Check if the personal code is 11 characters long
  if len(personal_code) != 11:
    print("Error: Incorrect number of digits. Please try again.")
    arvud.append(personal_code)
    count += 1
    continue
  
  # Check the first character
  if personal_code[0] not in "123456":
    print("Error: Incorrect first character. Please try again.")
    arvud.append(personal_code)
    count += 1
    continue
  
  # Extract the date of birth from the personal code
  day = personal_code[5:7]
  month = personal_code[3:5]
  year = personal_code[1:3]
  
  # Check if the date of birth is valid
  try:
    datetime.datetime.strptime(day + "-" + month + "-" + year, '%d-%m-%y')
  except ValueError:
    print("Error: Incorrect date of birth. Please try again.")
    arvud.append(personal_code)
    count += 1
    continue
  
  # Check the control number
  # ...
  
  # If the control number is correct, add the personal code to the ikoodid list
  ikoodid.append(personal_code)
  
  # Display the information
  gender = "male" if personal_code[0] in "135" else "female"
  dob = day + "/" + month + "/19" + year
  place_of_birth = "Idavir Keshaigla (Kohtla-Järve, endine Jõhvi)"
  print(f"This is a {gender}, his/her birthday is {dob} and place of birth is {place_of_birth}.")
  break

# Display the arvud list sorted from lowest to highest
arvud.sort()
print("List of incorrect codes:", arvud)

# Display the ikoodid list, first for women and then for men
ikoodid_women = [code for code in ikoodid if code[0] in "246"]
ikoodid_men = [code for code in ikoodid if code[0] in "135"]
print("List of correct codes for women:", ikoodid_women)
print("List of correct codes for men:", ikoodid_men)
