import gspread

gc = gspread.service_account(filename='schedule-401419-d4c2eaafc94d.json')
sh = gc.open("расписание копия")
print(sh.sheet1.get('E21'))