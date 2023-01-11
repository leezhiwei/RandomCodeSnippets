import faker
import secrets
import string
import genuine.fake
import random
def birthdaygen():
    year = random.randint(1600,3000)
    month = random.randint(1,12)
    thirtyone = [1,3,5,7,8,10,12]
    if month == 2:
        if year % 4 == 0:
            day = random.randint(1,29)
        else:
            day = random.randint(1,28)
        return f'{year}-{month}-{day}'
    if month in thirtyone:
            day = random.randint(1,31)
            return f'{year}-{month}-{day}'
    else:
        day = random.randint(1,30)
        return f'{year}-{month}-{day}'
def generator():
    multiple = False
    mprofile = []
<<<<<<< HEAD
    while len(mprofile) < 320:
=======
    for _ in range(1,2001):
>>>>>>> b90f7689031ecc566236c31c7a430f70bc21cc56
        profile = faker.Faker().simple_profile()
        uname = faker.Faker().unique.user_name()
        name = faker.Faker().unique.name()
        gender = profile['sex']
        address = faker.Faker().unique.address().replace('\n', ' ')
        email = faker.Faker().unique.email()
        birthday = profile['birthdate'].strftime("%d/%m/%Y")
        for p in mprofile:
            if p[0] == uname:
                multiple = True
            if p[4] == email:
                multiple = True
        if multiple:
            try:
                birthday = genuine.fake.GenuineFake.date_of_birth()
            except:
                birthday = birthdaygen()
            gender = random.choice(['M','F'])
            name = genuine.fake.GenuineFake.name()
            uname = name.replace(' ','').lower() + birthday.split('-')[0][-2:]
            address = genuine.fake.GenuineFake.address()
            email = genuine.fake.GenuineFake.email()
        for p in mprofile:
            if p[0] == uname:
                multiple = True
            if p[4] == email:
                multiple = True
        if multiple:
            continue
        prof = [uname, name, gender, address, email, birthday]
        mprofile.append(prof)
    print(f'Length of ProfileList is {len(mprofile)}')
    return mprofile
def passgen():
    letters = string.ascii_letters
    digits = string.digits
    spec_char = string.punctuation
    spec_char = spec_char.replace('"','')
    spec_char = spec_char.replace("'",'')
    spec_char = spec_char.replace("{",'')
    spec_char = spec_char.replace("}",'')
    charset = letters + digits + spec_char
    pwd_length = 30
    final_pass = ""
    for _ in range(pwd_length):
        final_pass += ''.join(secrets.choice(charset))
    return final_pass
