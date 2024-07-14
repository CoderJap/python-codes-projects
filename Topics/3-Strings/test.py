import re
from datetime import datetime

def extract_date(input_str):
    # Regular expression pattern to match dates in the format dd month
    date_pattern = r'(\d{1,2})\s+(january|february|march|april|may|june|july|august|september|october|november|december)\b'
    
    # Match the date pattern in the input string
    match = re.search(date_pattern, input_str.lower())
    
    if match:
        # Extract day and month from the matched groups
        day = match.group(1)
        month_str = match.group(2)
        
        # Convert month string to a month number
        month = datetime.strptime(month_str, "%B").strftime("%m")
        
        # Format the date as dd-mm
        date_str = f"{day}-{month}"
        return date_str
    
    elif 'today' in input_str.lower():
        # If "today" is in the input string, return today's date in dd-mm format
        today_date = datetime.now().strftime("%d-%m")
        return today_date
    
    else:
        return None  # Return None if no valid date or "today" is found in the input

# Example usage:
input_str1 = "What's celebrated on 12 january?"
input_str2 = "Tell me about today's celebrations."
input_str3 = "Any special event today?"

print(extract_date(input_str1))  # Output: 12-01
print(extract_date(input_str2))  # Output: Today's date in dd-mm format
print(extract_date(input_str3))  # Output: Today's date in dd-mm format
