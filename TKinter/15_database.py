from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title("Databases in Tkinter")
root.geometry("400x600")

# Create table (uncomment if running for the first time)
# conn = sqlite3.connect('address_book.db')
# c = conn.cursor()
# c.execute("""CREATE TABLE addresses (
#           first_name text,
#           last_name text,
#           address text,
#           city text,
#           state text,
#           zipcode integer
#           )
# """)
# conn.commit()
# conn.close()

def update():
    def save():
        conn = sqlite3.connect('address_book.db')
        c = conn.cursor()

        record_id = delete_box.get()
        c.execute("""UPDATE addresses SET
                  first_name = :first,
                  last_name = :last,
                  address = :address,
                  city = :city,
                  state = :state,
                  zipcode = :zipcode
                  WHERE oid = :oid""",
                  {
                      'first': f_name_editor.get(),
                      'last': l_name_editor.get(),
                      'address': address_editor.get(),
                      'city': city_editor.get(),
                      'state': state_editor.get(),
                      'zipcode': zipcode_editor.get(),
                      'oid': record_id
                  })
        conn.commit()
        conn.close()
        editor.destroy()

    editor = Tk()
    editor.title("Update A Record")
    editor.geometry("400x300")

    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    record_id = delete_box.get()

    # Query the database
    c.execute("SELECT * FROM addresses WHERE oid=?", (record_id,))
    records = c.fetchall()

    # Create text boxes
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1)
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1)
    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1)
    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1)
    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1)

    # Create Text Box Labels
    f_name_label = Label(editor, text="First Name")
    f_name_label.grid(row=0, column=0, pady=(10, 0))
    l_name_label = Label(editor, text="Last Name")
    l_name_label.grid(row=1, column=0)
    address_label = Label(editor, text="Address")
    address_label.grid(row=2, column=0)
    city_label = Label(editor, text="City")
    city_label.grid(row=3, column=0)
    state_label = Label(editor, text="State")
    state_label.grid(row=4, column=0)
    zipcode_label = Label(editor, text="Zipcode")
    zipcode_label.grid(row=5, column=0)

    # Loop through results
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])

    # Create Save Button
    save_btn = Button(editor, text="Save Record", command=save)
    save_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=143)

# Create a function to delete a record
def delete():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    c.execute("DELETE from addresses WHERE oid=?", (delete_box.get(),))
    conn.commit()
    conn.close()

# Create submit function
def submit():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
              {
                  'f_name': f_name.get(),
                  'l_name': l_name.get(),
                  'address': address.get(),
                  'city': city.get(),
                  'state': state.get(),
                  'zipcode': zipcode.get()
              })
    conn.commit()
    conn.close()

    # Clear the text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

# Create query function
def query():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    conn.close()

    print_records = ''
    for record in records:
        print_records += f"Id: {record[6]}\nFirst Name: {record[0]}\nLast Name: {record[1]}\nAddress: {record[2]}\nCity: {record[3]}\nState: {record[4]}\nZipcode: {record[5]}\n\n"

    my_label = Label(root, text=print_records)
    my_label.grid(row=12, column=0, columnspan=2)

# Create text boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)

address = Entry(root, width=30)
address.grid(row=2, column=1)

city = Entry(root, width=30)
city.grid(row=3, column=1)

state = Entry(root, width=30)
state.grid(row=4, column=1)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)

delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1, pady=5)

# Create Text Box Labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0, pady=(10, 0))

l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)

address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)

city_label = Label(root, text="City")
city_label.grid(row=3, column=0)

state_label = Label(root, text="State")
state_label.grid(row=4, column=0)

zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)

delete_box_label = Label(root, text="Select ID:")
delete_box_label.grid(row=9, column=0, pady=5)

# Create Submit Button
submit_btn = Button(root, text="Add Record to Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create a query button
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# Create a Delete Button
delete_btn = Button(root, text="Delete Record", command=delete)
delete_btn.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=135)

# Create an update button
update_btn = Button(root, text="Update Record", command=update)
update_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=143)

root.mainloop()
