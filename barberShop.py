from datetime import datetime

waiting = []
arrivalTime = []

checkedIn = []
timeIn = []

def someoneIsHere():
    time = datetime.today().strftime("%I:%M %p") ##Used %I for regular hours instad of %H for 24 hour time
    name = input('Name?')
    waiting.append(name)
    arrivalTime.append(time)

def snip():
    time = datetime.today().strftime("%I:%M %p")
    name = input('Name?')
    customerIndex = waiting.index(name)
    waiting.pop(customerIndex)
    arrivalTime.pop(customerIndex)
    checkedIn.append(name)
    timeIn.append(time)

def leaving():
    name = input('Name?')
    customerIndex = checkedIn.index(name)
    checkedIn.pop(customerIndex)
    timeIn.pop(customerIndex)

def main():
    print('NittanyBarberShop')
    print('1) Customer has Arrived')
    print('2) Customer\'s Wating')
    print('3) Customer Check In')
    print('4) Currently Being Pampered')
    print('5) Customer Check Out')
    print('e) Exit Program')
    choice = input('Please choose option 1,2,3,4,5, or e.')
    if choice == '1':
        someoneIsHere()
    if choice == '2':
        for i in range(len(waiting)):
            print('Name:', waiting[i],'|','Arrived:', arrivalTime[i])
    if choice == '3':
        snip()
    if choice == '4':
        for i in range(len(checkedIn)):
            print('Name:', checkedIn[i],'|','Started:', timeIn[i])
    if choice == '5':
        leaving()
    if choice == 'e':
        exit()
    main()

main()