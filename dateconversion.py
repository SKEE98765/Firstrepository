from datetime import datetime

# Example: Converting from string to a valid format
input_date = "07-05-2025"  # Input in DD-MM-YYYY
date_obj = datetime.strptime(input_date, "%d-%m-%Y")  # Parse the string to datetime object

# Convert to different valid formats
print(date_obj.strftime("%Y-%m-%d"))  # Output: 2025-05-07 (ISO format)
print(date_obj.strftime("%d %B, %Y")) # Output: 07 May, 2025
print(date_obj.strftime("%A, %d %b %Y")) # Output: Wednesday, 07 May 2025
