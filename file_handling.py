try:
    with open("not.txt",'r') as file:
        content=file.read()
        print(content)
except:
    print("file not found")
