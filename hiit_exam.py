products = []

ent = input("Enter first item ")
low = ent.lower() 

products.append(low)

def cond():
    doa = input("Do you want to input another item Y/N? ")
    hk = doa.lower()

    if hk == "y":
        ent = input("Enter item ")
        low = ent.lower() 
        products.append(low)
        cond()
    elif hk == "n":
        print("Showing products : ", products)
    else:
        print("Invalid entry")
        cond()

cond()




def search():
    
    doa = input("Do you want to search an item Y/N? ")
    hk = doa.lower()

    if hk == "y":
        ent = input("What item do you want to search for? ")
        ent_low = ent.lower()

        if ent_low in products:
            count = products.count(ent_low)
            print("Product found!")
            print("Total number of ", ent_low ," in Product list is ", count)
            search()
        else:
            print(ent_low ,"not in Product list")
            search()
    elif hk == "n":
        print("Exiting... ")
    else:
        print("Invalid entry")
        search()
        
search()
