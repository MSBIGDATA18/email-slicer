def get_email():
   return input('Enter your email adress : ').strip()
    

def validate_email(email):
    if email.count('@') == 1 and '.' in email[email.index('@')+1:]:
        return True
    else: 
        return False


def main():
    email = get_email()
    if validate_email(email):
        username = email[:email.index('@')]
        domain = email[email.index('@')+1]
        print('Your username is', username)
        print('Your domain is ',  domain)
    else: 
        print('Invalid email adress')

if __name__ ==  "__main__":
    main()