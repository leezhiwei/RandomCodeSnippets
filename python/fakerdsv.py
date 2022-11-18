from faker import Faker 
from bs4 import BeautifulSoup
import requests
import re           #Import modules including product faker
import random
import faker_commerce
fake = Faker() #faker object
fake.add_provider(faker_commerce.Provider) #add commerce module
csvfile = open("Inventory.dsv","w",encoding="utf-8") # open the final file
usedname = [] # list for usedname
csvfile.write("ItemID.ProductName.UnitPrice.Description.RemainingInventory\n") # write header
for x in range(1, 200): # for loop from 1 to 200
    name = fake.ecommerce_name() # get random name of product
    if name in usedname: # if name is used before
        continue # continue loop (avoid duplicates)
    usedname.append(name) # append the name to uselist
    print(name) # print out the name
    price = random.randint(1,9999) # random price between 1 to 9999
    stockamt = random.randint(1,10000) # amount of stock between 1 to 10000
    r = requests.get(f"https://www.google.com/search?q={name}").text # get the html text
    soup = BeautifulSoup(r, "html.parser").select(".s3v9rd.AP7Wnd") # used BeautifulSoup to parse it
    description = soup[2].getText(strip=True) # description and strip the unusual text?
    if ',' or '.' in description: # if comma or dot
        finaldesc1 = description.replace(',','') # replace all comma with blank
        finaldesc = finaldesc1.replace('.','') # replace all dot with blank
    else: # else
        finaldesc = description # no processing
    print(finaldesc) # print description
    csvfile.write(f'{x}.{name}.{price}.{finaldesc}.{stockamt}\n') # put inside the DSV file
csvfile.close() # at end of loop, close the file
