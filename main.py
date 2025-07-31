from pprint import pprint
import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
#pprint(contacts_list)
lst_return = []
# TODO 1: выполните пункты 1-3 ДЗ

def merge_duplicates(data):
  headers = data[0]
  merged_rows = {}
  for row in data[1:]:
    lastname, firstname = row[0], row[1]
    key = (lastname, firstname)
    if key not in merged_rows:
      merged_rows[key] = row.copy()
    else:    
      existing_row = merged_rows[key]
      for i in range(len(row)):
        if not existing_row[i] and row[i]:  
          existing_row[i] = row[i]
  return [headers] + list(merged_rows.values())

for contact in contacts_list[1:]:
  cont = ' '.join(contact[:3]).replace('  ',' ').split(' ')
  contact[:3] = cont[:3]
  
for contact in contacts_list:
  phone = contact[-2]  
  if not phone:  
    continue

  main_pattern = r"(?:\+7|8)\s*\(?(\d{3})\)?[\s-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})"
  phone = re.sub(main_pattern, r"+7(\1)\2-\3-\4", phone)
  ext_pattern = r"(?:\s*\(?(?:доб)\.?\s*(\d+)\)?)"
  phone = re.sub(ext_pattern, r" доб.\1", phone)
  contact[-2] = phone.strip()
  
contacts_list = merge_duplicates(contacts_list)  
pprint(contacts_list)
  
# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8", newline='') as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(contacts_list)