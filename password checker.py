# w a p program to check a valid  password 
import time
password='dushi2037h'
attempt=5
while True:
    user_password=input('\nEnter the password')
    if user_password==password:
        print('Login Succesfull')
        break
    else:
        print('Wrong Password,Try Again')
        attempt-=1
        if attempt<=0:
            print('Failed to Login')
            count=10
            while count!=0:
                print(count,end=' ')
                time.sleep(1)
                count-=1
            attempt=5