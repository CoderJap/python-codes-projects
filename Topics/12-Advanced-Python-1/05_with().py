# Using multiple context managers to open files with the new syntax

with (
    open('file1.txt', 'r') as file1,
    open('file2.txt', 'r') as file2
):
    # Reading from the first file
    content1 = file1.read()
    print("Content of file1.txt:")
    print(content1)
    
    # Reading from the second file
    content2 = file2.read()
    print("Content of file2.txt:")
    print(content2)
