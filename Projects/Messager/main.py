import time
import pywhatkit as kit
import phoneLibrary

def send_whatsapp_msg(contact_name , message):

  # fetching contact number from dictionary
  contacts = phoneLibrary.contacts
  contact_number  = contacts.get(contact_name.lower())

  if not contact_number:
    print(f"Contact {contact_name} not found.")
    return 
  
  contact_number = "+91" + contact_number

  # Schedule the message from a min from now

  hour = time.localtime().tm_hour
  minute = time.localtime().tm_min + 2

  kit.sendwhatmsg(contact_number,message,hour,minute)
  print(f"Message sent to {contact_name}")

if __name__ == "__main__":
    contact_name = input("Enter the contact name: ")
    message = input("Enter the message: ")
    send_whatsapp_msg(contact_name, message)