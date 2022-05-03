from datetime import datetime

checkedIn = []
customerTimeIn = []
employee = []
employeeTimeIn = []

def customerHere():
    now = datetime.now()
    today745pm = now.replace(hour=19, minute=45, second=0, microsecond=0)
    today8pm = now.replace(hour=20, minute=0, second=0, microsecond=0)
    today8am = now.replace(hour=8, minute=0, second=0, microsecond=0)
    if (now < today8am) or (now >= today8pm):
        print('Closed')
        main()
    if (now > today745pm) and (now < today8pm):
        print('Sorry we\'re closing soon.')
        main()
    if len(employee) == 0: ##No barbers!
        print('We are waiting for a barber, sorry for the inconvience.')
        main()
    else:
        time = datetime.now()
        name = input('Name?')
        if name in checkedIn:
            print('It appears this customer is already checked in.')
            main()
        checkedIn.append(name)
        customerTimeIn.append(time)
        waitTime = int((len(checkedIn)-1)*12/(len(employee)))
        print('Your wait is currently', waitTime, 'minutes.')

def customerLeft():
    try:
        name = input('Name?')
        customerTimeIndex = checkedIn.index(name)
    except:
        print('No customer in the system with that name.')
        main()
    timeWorkedSec = datetime.now() - customerTimeIn[customerTimeIndex] ##Calculates difference in timeIn and timeOut
    timeWorkedMin = int(timeWorkedSec.total_seconds()/60) ##Calculates minutes
    print(timeWorkedMin, "Minutes Waited")

    checkedIn.pop(customerTimeIndex)
    customerTimeIn.pop(customerTimeIndex)

def clockIn():
    time = datetime.now()
    name = input('Name?')
    if name in employee:
        print('It appears you are already clocked in.')
        staff()
    employee.append(name)
    employeeTimeIn.append(time)

def clockOut():
    try:
        name = input('Name?')
        employeeIndex = employee.index(name)
    except:
        print('No Employee Currently clocked in with that name.')
        staff()
    timeWorkedSec = datetime.now() - employeeTimeIn[employeeIndex] ##Calculates difference in timeIn and timeOut
    timeWorkedMin = int(timeWorkedSec.total_seconds()/60) ##Calculates minutes
    print(timeWorkedMin, "Minutes Worked")
    employee.pop(employeeIndex)
    employeeTimeIn.pop(employeeIndex)

def staff():
    print('1) Clock In')
    print('2) Clock Out')
    print('3) Staff Clocked In')
    print('r) Return to Main Menu')
    choice = input('Please choose option 1,2,3, or r.')
    if choice == '1':
        clockIn()
    if choice == '2':
        clockOut()
    if choice == '3':
        for i in range(len(employee)):
            print('Name:', employee[i],'|','Arrived:', employeeTimeIn[i].strftime("%I:%M %p"))
    if choice == 'r':
        main()

def main():
    print('NittanyBarberShop')
    print('1) Checkin a Customer')
    print('2) Checkout a Customer')
    print('3) Customer\'s Currently Being Pampered')
    print('4) Staff')
    print('e) Exit Program')
    choice = input('Please choose option 1,2,3,4, or e.')
    if choice == '1':
        customerHere()
    if choice == '2':
        customerLeft()
    if choice == '3':
        for i in range(len(checkedIn)):
            print('Name:', checkedIn[i],'|','Arrived:', customerTimeIn[i].strftime("%I:%M %p"))
    if choice == '4':
        staff()
    if choice == 'e':
        exit()
    main()

main()
