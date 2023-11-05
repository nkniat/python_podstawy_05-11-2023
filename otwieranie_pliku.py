with open('my_file.txt', 'r') as file1:
    content = file1.read()

print(content)

content = content.lower().replace(',', '').replace('.','').replace('(','').replace(')','.').split()
print(content)
print("Liczba słów: ", len(set(content)))
