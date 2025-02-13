from datetime import datetime

while True:
    try:
        date_input = input("Enter the date (mm/dd/yyyy): ")
        date_object = datetime.strptime(date_input, "%m/%d/%Y")
        translated_date = date_object.strftime("%B %d, %Y")
        print("Date Output:", translated_date)
        break
    except ValueError:
        print("Invalid Format! Please enter a valid date in mm/dd/yyyy format.")
