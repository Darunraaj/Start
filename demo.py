
ask = ""
started = False
while True:
    ask = input('> ').lower()
    if ask == "quit":
        break
    elif ask == "start":
        if started :
            print('Car already started !')
        else:
            started = True
            print ("Car started...Ready to go!")
    elif ask == "stop":
        if not started :
            print('Car is already stopped!')
        else:
            started = False
            print("Car stopped!")
    elif ask == 'help':
        print('''
start - start the car
stop - stop the car 
quite - to exit car
              ''')
    else:
        print("I don't understand that...")

