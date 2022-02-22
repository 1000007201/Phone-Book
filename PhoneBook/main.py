from Phone_Book import Book, json

book = Book(r"E:\CFP-Python_CoreStack\Phone-Book\PhoneBook\Book.json")
# book.display()
while True:
    option = int(input("Enter Value:\n1.Display Data\n2.Add Data\n3.Update data\n4.Delete Data"
                       "\n5.Exit to make changes\n"))
    if option == 1:
        book.display()
    if option == 2:
        book.add_entry()
    if option == 3:
        book.update_entry()
    if option == 4:
        book.delete_entry()
    if option == 5:
        break

out_file = open(r"E:\CFP-Python_CoreStack\Phone-Book\PhoneBook\Book.json",'w')
json.dump(book.json_data, out_file)
out_file.close()