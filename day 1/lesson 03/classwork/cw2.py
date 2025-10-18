



products = []  

product = ""  

while product != "exit":  
    product = input("შეიყვანე პროდუქტი (ჩაწერე 'exit' გასასვლელად): ")
    if product != "exit":
        products.append(product)  

print("შენი პროდუქტებია:", products)  
