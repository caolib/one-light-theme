import os

def show():
    print('---------------------------------------------------------')
    print('enter ---> git status')
    print('1     ---> git add .')
    print('2     ---> git commit -m "message"')
    print('3     ---> git push')
    print('4     ---> git pull')
    print('5     ---> git add . & git commit -m "message" & git push')
    print('6     ---> git log')
    print('else  ---> exit')
    print('---------------------------------------------------------')

while True:
    try:
        show()
        choice = int(input('chioce: '))
        if choice == None:
            os.system('git status')
        elif choice == 1:
            os.system('git add .')
        elif choice == 2:
            message = input('Enter your message: ')
            os.system(f'git commit -m "{message}"')
            print(f'message:{message}')
        elif choice == 3:
            os.system('git push')
        elif choice == 4:
            os.system('git pull')
        elif choice == 5:
            message = input('Enter your message: ')
            os.system(f'git add .')
            os.system(f'git commit -m "{message}"')
            os.system(f'git push')
            print(f'message:{message}')
        elif choice == 6:
            os.system('git glog')
        else:
            exit()
    except Exception as e:
        if isinstance(e, ValueError):
            os.system('git status')
        print('Invalid choice')
