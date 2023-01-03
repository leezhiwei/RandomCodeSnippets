import faker
import secrets
import string
def generator():
    multiple = False
    mprofile = []
    for _ in range(1,1001):
        profile = faker.Faker().simple_profile()
        uname = profile['username']
        name = profile['name']
        gender = profile['sex']
        address = profile['address']
        email = profile['mail']
        birthday = profile['birthdate'].strftime("%d/%m/%Y")
        if _ != 1:
            for p in mprofile:
                if p[4] == email:
                    multiple = True
                    break
                if p[0] == uname:
                    multiple = True
                    break
        if multiple:
            continue
        prof = [uname, name, gender, address, email, birthday]
        mprofile.append(prof)
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
