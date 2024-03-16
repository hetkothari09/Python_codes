def mailchk(mail):
    if '.com' and '@' in mail:
        return True
    else:
        return False

def check(i):
    switcher={
        True: "Valid Email ID!",
        False: "Invalid Email ID!"
    }
    print(switcher.get(i, "Not Appropriate Email!"))

check(mailchk("hetkothari1907@gmail.com"))
