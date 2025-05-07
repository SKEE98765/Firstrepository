from datetime import datetime 
try:
    date_obj = datetime.strptime("31-02-2025", "%d-%m-%Y")
    print(date_obj.strftime("%Y-%m-%d"))
except ValueError as e:
    print("Invalid date format:", e)
