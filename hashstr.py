from argon2 import PasswordHasher
from database import (local_session, create_tables, User)


ph = PasswordHasher()


def user_inputs():
    username = input("Username: ") # will change later due to the inputs being on a web app
    master_key = input("Password: ") # passwd will be hidden on web app
    
    is_passwd_valid(master_key)
    
    return username, master_key


def hash_passwd(master_key):
    my_hash = ph.hash(str(master_key))
    
    return my_hash


def is_passwd_valid(passwd):
    # add more input validation for passwd
    if len(passwd) < 12:
        raise Exception("Password is less than 12 characters")
    
    
def is_uname_valid(uname):
    # add more input validation for passwd
    if len(uname) < 12:
        raise Exception("Password is less than 12 characters")


def main():
    try:
        create_tables()
        
        username, master_key = user_inputs()
        
        my_hash = hash_passwd(master_key)

        with local_session as session:
            my_user = User(
                    username = username,
                    hash_string = my_hash,
            )
            
            session.add(my_user)
            
            session.commit()
            
    
    except ValueError as e:
        print(f"Error: {e}")
        
        
    except Exception as e:
        print(f"Unexpected error occured: {e}")
        

if __name__ == "__main__":
    main()