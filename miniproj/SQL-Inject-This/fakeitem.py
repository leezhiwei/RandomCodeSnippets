from faker import Faker
import faker_commerce
fake = Faker() #faker object
fake.add_provider(faker_commerce.Provider) #add commerce module
def fakeitemname():
    name = fake.ecommerce_name() # get random name of product
    return name
