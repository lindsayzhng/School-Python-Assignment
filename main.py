import logging
logging.basicConfig(filename='log.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

logging.info("Start of program")

#Finds how long it will take to travel a certain distance, using speed
def timeUntilDestination(speed,distance):
  '''
  Calculates the amount of time it takes to reach a destination 

  Receives distance length and speed. Calculates the time it takes to reach if the speed and distance is more than 0.

  Parameters
  ----------
  speed: int/float
    Speed in km/h
  
  distance: int/float
    legnth to destination km
  
  Returns
  ---------
  int
    Time in minutes
  NoneType
    Returns None if parameters are the wrong type or if their value is less than 0

  '''
  minuteCounter=0

  if not isinstance(speed,(float,int)) or not isinstance(distance,(float,int)):
    logging.error("Invalid parameters, must be a float or int")
    return None

  logging.info("Parameters are valid")
  if speed==0:
    logging.warning("Invalid value, speed cannot equal 0")
    return None
  
  time=distance/speed
  minuteCounter=int(time*60)

  if speed<0 or distance<0:
    logging.warning("Invalid value, speed and distance must be greater than 0")
    return None
  else:
    logging.debug("the time in minutes is calculated to be "+str(minuteCounter))
    return minuteCounter


#Gets the distance of two points following horizontal and vertical lines (not the hypotenuse)
def distanceUntilDestination(x1,y1,x2,y2):
  '''
  Calculates the distance between current position and desired destination

  Receives current coordinates and coordinates of another destination. Calculates the length of the two coordinates if they aren't negaitve.

  Parameters
  -----------
  x1: int
    x coordinate in (x,y) for starting position
  y1: int
    y coordinate in (x,y) for starting position
  x2: int
    x coordinate in (x,y) for end position
  y2: int
    y coordinate in (x,y) for end position

  Returns
  ----------
  int
    length in km
  NoneType
    Returns None if parameters are wrong type or value is below 0
  '''
  xDistance=0
  yDistance=0

  if not isinstance(x1,(int)) or not isinstance(y1,(int)) or not isinstance(x2,(int)) or not isinstance(y2,(int)):
    logging.error("Invalid parameters, must be an int")
    return None
  logging.info("Valid parameters, fucntion continues")
  if x1<0 or y1<0 or x2<0 or y2<0:
    logging.warning("Invalid value, must be greater than 0")
    return None
  else:
    if x1>x2:
      xDistance=x1-x2
    elif x2>x1:
      xDistance=x2-x1
    elif x1==x2:
      xDistance=0
      
    if y1>y2:
      yDistance=y1-y2
    elif y2>y1:
      yDistance=y2-y1
    elif y1==y2:
      yDistance=0
    logging.debug("The distance is calculated to be "+str(xDistance+yDistance))
    return xDistance+yDistance


assert timeUntilDestination(50,25)==30, "The time it will take to reach the destination is expected to be 30 minutes"
assert timeUntilDestination(-5,45)==None, "If the speed or distance are below 0 it should return None"
assert timeUntilDestination (60,"abc")==None, "If the data type isn't an int it should return None"

assert distanceUntilDestination(0,5,6,8)==9, "The distance to reach the destination is expected to be 9 km"
assert distanceUntilDestination(-8,9,4,7)==None, "If the coordinates are below 0 it should return None"
assert distanceUntilDestination (8,"abc",9,0)==None, "If the data type isn't an int it should return None"

arrivalTime=""
departureTime=""
numberOfAddresses=0
addressList=[]

#Gets the arrival time
#Loops until the input is valid
print("Please use military time.")
i=0
while i<1:
  arrivalTime=input("Time of arrival: ")
  formatCheck=list(arrivalTime)
  logging.debug("The input time is "+str(arrivalTime))
 
  counterOne=0
  counterTwo=0

  #checking the amount of digits there are 
  #and if there is a colon
  for i in range(0,len(formatCheck)):
    if formatCheck[i]==":":
      counterOne+=1
    if formatCheck[i]=="0" or formatCheck[i]=="1" or formatCheck[i]=="2" or formatCheck[i]=="3" or formatCheck[i]=="4" or formatCheck[i]=="5" or formatCheck[i]=="6" or formatCheck[i]=="7" or formatCheck[i]=="8" or formatCheck[i]=="9":
      counterTwo+=1

  logging.debug("The colon counter == "+str(counterOne)+" , The number counter == "+str(counterTwo))

  if counterOne==1 and counterTwo==3:
    arrivalTime=list(arrivalTime.split(":"))
    arrivalTime[0]=int(arrivalTime[0])
    arrivalTime[1]=int(arrivalTime[1])

    logging.debug("The hour == "+str(arrivalTime[0])+" , The minutes == "+str(arrivalTime[1]))

    #checking if the hour time is valid, and if the minute time is valid 
    # hours cant be 24 or greater, or less than 0
    # minutes can't be 60 or greater, or less than 0
    if 24>arrivalTime[0]>=0 and 60>arrivalTime[1]>=0:
      logging.info("Time is valid, code continues")
      print("Thank you, your time has been recorded.")
      i+=1
      print()
    else:
      logging.warning("The time value is invalid, must be within 23:59 ")
      print ("Error: time input not valid. Try again.")
      i=0
      print()

  elif counterOne==1 and counterTwo==4:
    arrivalTime=list(arrivalTime.split(":"))
    arrivalTime[0]=int(arrivalTime[0])
    arrivalTime[1]=int(arrivalTime[1])

    logging.debug("The hour == "+str(arrivalTime[0])+" , The minutes == "+str(arrivalTime[1]))

    #checking if the hour time is valid, and if the minute time is valid 
    # hours cant be 24 or greater, or less than 0
    # minutes can't be 60 or greater, or less than 0
    if 24>arrivalTime[0]>=0 and 60>arrivalTime[1]>=0:
      logging.info("Time is valid, code continues")
      print("Thank you, your time has been recorded.")
      i+=1
      print()
    else:
      logging.warning("The time value is invalid, must be within 23:59 ")
      print ("Error: time input not valid. Try again.")
      i=0
      print()
  #doesn't consist of 3-4 digits and a colon
  else:
    logging.error("The time format is invalid")
    print ("Error: time input not valid. Try again.")
    i=0
    print()

#Gets the amount of houses that need to be visited and their postal code
#If any input is invalid, the code will loop until it is valid
j=0
while j<1:
  numberOfAddresses=input("Houses you have to deliver to today: ")
  logging.debug("The number of addresses == "+str(numberOfAddresses))

  if numberOfAddresses.lstrip('-').isnumeric():
    numberOfAddresses=int(numberOfAddresses)

    # 0 addresses means no need for an input of its ZIP code
    if numberOfAddresses==0:
      logging.info("Valid input, code continues")
      print("You have no packages to deliver. You are done for the day.")
      print()
      j+=1

    #Can't visit a negative amount of addresses
    elif numberOfAddresses<0:
      logging.warning("Invalid input, cannot be negative")
      print("Invalid amount of addresses. Cannot be negative, try again. ")
      print()
      j==0
    
    #A valid number of addresses that need a ZIP code input
    elif numberOfAddresses>0:
      logging.info("Valid input, code continues")
      print("What are the ZIP codes for these deliveries?")
      print()
      j+=1
      x=1

      #Loops the amount of addresses that need to be visited to add each ZIP code to the list
      while x <=numberOfAddresses:
        addressInput=input()
        logging.debug("ZIP code == "+str(addressInput))

        # if the address isn't an int, it isn't a USA ZIP code
        if addressInput.lstrip('-').isnumeric():
          addressInput=int(addressInput)

          # ZIP codes don't have negative values
          if addressInput<0:
            logging.warning("ZIP codes cannot be negative")
            print ("Error: Invalid ZIP code")
            print()

          #Length of ZIP codes are 6, otherwise it isn't a ZIP code
          elif len(str(addressInput))!=6:
            logging.error("Invalid format, ZIP code must consist of 6 digits")
            print ("Error: Invalid ZIP code, must be six digits")
            print()

          #Positive, six digit code
          else:
            logging.info("Valid zip code, code continues")

            #Adds valid address into list
            addressList.append(addressInput) 

            x+=1
            #Loop can get closer to finishing (Marking off the ZIP codes)
            print("ZIP Code have been recorded.")
            print()

        #Isn't an int
        else:
          print("Error: Invalid data type, must be a six digit code")
          print()
      
        #sort all the addresses
        logging.debug("Unsorted address list == "+str(addressList))
        addressList.sort()
        logging.debug("Sorted address list == "+str(addressList))

  #Amount of addresses aren't an Int
  else:
    logging.info("Invalid input")
    print("Error: Invalid data type, must be an integer. Try again.")
    print()


#The menu to access all the actions you can take in this code
actionMenu=0
while actionMenu<1:

  print('''
  PLEASE CHOOSE ONE OF THE FOLLOWING ACTIONS

    MENU:

        A: Get the length of time it will take to reach the address
        B: Determine which address is closer to you
        C: Get your list of addresses
        D: Add an address to your list
        E: Remove an address off your list
        F: Leave the menu

  ''')

  #Get the action the user wants to use
  choice= input()
  logging.debug("The choice == "+str(choice))

  #Gets an estimation of the time it will take to get to a destination using speed and distance
  if choice=='A' or choice=='a':
    
    driveSpeed=input("The speed (km/h) you are driving at: ")
    destinationDistance=input("The distance to the address: ")

    logging.debug("The driving speed == "+str(driveSpeed)+" , and the distance to the destination == "+str(destinationDistance))

    #Checking if the inputs are integers
    if driveSpeed.lstrip('-').isnumeric():
      driveSpeed=int(driveSpeed)
    if destinationDistance.lstrip('-').isnumeric():
      destinationDistance=int(destinationDistance)
    
    timeOfDestination=(timeUntilDestination(driveSpeed,destinationDistance))
    logging.debug("Function returns "+str(timeOfDestination))

    if timeOfDestination==0:
      print("You're already at your destination")
    elif timeOfDestination==None:
        print("Error: Invalid distance, speed, or data types")
    else:
      print("It will take "+str(timeOfDestination)+" minutes to reach the destination.")

    logging.info("End of choice 'A' action")

    print()

  #Prints the remaining ZIP codes from the list of addresses
  elif choice=='C' or choice=='c':
    if len(addressList)==0:
      #Can't print a list of nothing (No ZIP codes in list)
      logging.info("No addresses in the list of ZIP codes to visit, cannot view list")
      print("There are no more addresses to deliver to.")

    else:
      for i in range (0,len(addressList),1):
        logging.debug("Address from address list == "+str(addressList[i]))

        #Print the remaining addresses one by one
        print(addressList[i])
    print()
    logging.info("End of choice 'B' action")
  
  #Adds a ZIP code to the list of addresses
  elif choice=='D' or choice=='d':
    newAddress=input("The new ZIP code you would like to add: ")
    logging.debug("The new ZIP code == "+str(newAddress))

    #checking if it is valid, similar format to inital ZIP code adding (in the beginning of the code)
    if newAddress.lstrip('-').isnumeric():
      newAddress=int(newAddress)

      if newAddress<=0:
        logging.warning("Invalid value, ZIP codes cannot be negative")
        print("Error: Invlaid ZIP code")
        print()

      elif len(str(newAddress)) !=6:
        logging.error("Invalid format, ZIP codes must consist of six digits")
        print("Error: Invalid ZIP code, must be a length of six digits")
        print()

      else:
        logging.info("ZIP code is valid, code continues")
        addressList.append(newAddress)

        logging.debug("New address list == "+str(addressList))
        addressList.sort()
        logging.debug("New sorted address list == "+str(addressList))

        print("Postal code as been added and sorted into the list of addresses.")

    else:
      logging.error("Invalid data type, must be an integer")
      print("Error: Invalid data type.")
      print()
    logging.info("End of choice 'D' action")
  
  #Removing a postal code from the list of addresses
  elif choice=='E' or choice=='e':
    removeZIPCode=input("The postal code you delivered to: " )
    logging.debug("The ZIP code that wants to be removed == "+str(removeZIPCode))

    #Making sure the ZIP code is an integer
    if removeZIPCode.lstrip('-').isnumeric():
      removeZIPCode=int(removeZIPCode)

      #Can't remove ZIP code from an empty list
      if len(addressList)==0:
        logging.warning("Cannot remove from an empty list")
        print("There are no more addresses to cross off the list.")

      #Checking if the code is in the current list codes 
      #Can't remove a code if it isn't there
      elif int(removeZIPCode) in addressList:
        logging.info("The ZIP code is found in the list")
        addressList.remove(int(removeZIPCode))

        logging.debug("New address list == "+str(addressList))
        print ("Address has been removed from the list.")
      else:
        logging.warning("Cannot remove a ZIP code that doesn't exist in the list")
        print ("Error: Address does not exist.")
      print()
    else:
      logging.error("Invalid data type, must be an integer")
      print("Error: Invalid data type. The ZIP code must consist of six digits.")
      print()
    logging.info("End of choice 'E' action")
      
  
  #Finding which destination will take quicker using coordinates
  elif choice=='B' or choice=='b':

    #Getting all the variables
    startCoorOne=input("Your current x coordinate: ")
    startCoorTwo=input("Your current y coordinate: ")
    print()

    endCoorOne=input("One of the address's x coordinate: ")
    endCoorTwo=input("One of the address's y coordinate: ")
    print()

    secondEndCoorOne=input("Another one of the address's x coordinate: ")
    secondEndCoorTwo=input("Another one of the address's y coordinate: ")
    print()

    #Making them an integer if they are one
    if startCoorOne.isnumeric():
      startCoorOne=int(startCoorOne)
    if startCoorTwo.isnumeric():
      startCoorTwo=int(startCoorTwo)
    if endCoorOne.isnumeric():
      endCoorOne=int(endCoorOne)
    if endCoorTwo.isnumeric():
      endCoorTwo=int(endCoorTwo)
    if secondEndCoorOne.isnumeric():
      secondEndCoorOne=int(secondEndCoorOne)
    if secondEndCoorTwo.isnumeric():
      secondEndCoorTwo=int(secondEndCoorTwo)

    logging.debug("The first distance returns "+str(distanceUntilDestination(startCoorOne,startCoorTwo,endCoorOne,endCoorTwo))+" , the second distance returns "+str(distanceUntilDestination(startCoorOne,startCoorTwo,secondEndCoorOne,secondEndCoorTwo)))

    if distanceUntilDestination(startCoorOne,startCoorTwo,endCoorOne,endCoorTwo)==None or distanceUntilDestination(startCoorOne,startCoorTwo,secondEndCoorOne,secondEndCoorTwo)==None:
      logging.info("Function returned None")
      print("Error: Invalid coordinates or data types")
      print()

    elif distanceUntilDestination(startCoorOne,startCoorTwo,endCoorOne,endCoorTwo)<distanceUntilDestination(startCoorOne,startCoorTwo,secondEndCoorOne,secondEndCoorTwo):
      logging.debug(str(distanceUntilDestination(startCoorOne,startCoorTwo,endCoorOne,endCoorTwo))+" is smaller than "+str(distanceUntilDestination(startCoorOne,startCoorTwo,secondEndCoorOne,secondEndCoorTwo)))
      print("The first destination is closer, head there first.")
      print()

    elif distanceUntilDestination(startCoorOne,startCoorTwo,endCoorOne,endCoorTwo)>distanceUntilDestination(startCoorOne,startCoorTwo,secondEndCoorOne,secondEndCoorTwo):
      logging.debug(str(distanceUntilDestination(startCoorOne,startCoorTwo,secondEndCoorOne,secondEndCoorTwo))+" is smaller than "+str(distanceUntilDestination(startCoorOne,startCoorTwo,endCoorOne,endCoorTwo)))
      print("The second destination is closer, head there first.")
      print()

    elif distanceUntilDestination(startCoorOne,startCoorTwo,endCoorOne,endCoorTwo)==distanceUntilDestination(startCoorOne,startCoorTwo,secondEndCoorOne,secondEndCoorTwo):
      logging.info(str(distanceUntilDestination(startCoorOne,startCoorTwo,endCoorOne,endCoorTwo))+' == '+str(distanceUntilDestination(startCoorOne,startCoorTwo,secondEndCoorOne,secondEndCoorTwo)))
      print("They are the same distance from you. It doesn't matter which address you go to first.")
      print()
    logging.info("End of choice 'B' action")


  #Leaving the action menu
  elif choice=='F' or choice =='f':

    #can't leave when there's still work to do 
    if len(addressList)>0:
      logging.error("Cannot leave action menu when there are addresses in the list")
      print("You still have packages to deliver.")
      print()
    else:
      logging.info("Leaving the action menu, code continues")
      print("You no longer need to use the menu.")
      actionMenu+=1
      print()
    logging.info("End of choice 'F' action")
    
  else:
    logging.error("Invalid input, must be between A-F")
    print("You input an invalid choice of action. Please select one of the available actions.")
    print("Try Again.")
    print()


#Get the time that the worker leaves work at
m=0
while m<1: 
  leaveTime=input("Time of departure:")
  logging.debug("Departure time == "+str(leaveTime))

  departureTime=leaveTime
  formatCheck=list(departureTime)

  counterOne=0
  counterTwo=0

  #checks formatting
  for i in range(0,len(formatCheck)):
    if formatCheck[i]==":":
      counterOne+=1
    elif formatCheck[i]=="0" or formatCheck[i]=="1" or formatCheck[i]=="2" or formatCheck[i]=="3" or formatCheck[i]=="4" or formatCheck[i]=="5" or formatCheck[i]=="6" or formatCheck[i]=="7" or formatCheck[i]=="8" or formatCheck[i]=="9":
      counterTwo+=1

  logging.debug("Colon counter == "+str(counterOne)+" , number counter == "+str(counterTwo))

  if counterOne==1 and counterTwo==3:
    newTime=list(departureTime.split(":"))
    newTime[0]=int(newTime[0])
    newTime[1]=int(newTime[1])

    logging.debug("Hour == "+str(newTime[0])+" , Minute == "+str(newTime[1]))

    #checks if the end time is earlier than the start time

    departureTime=list(departureTime)
    colon = departureTime.index(":")
    del(departureTime[colon])
    departureTime="".join(departureTime)

    timeInt=str(arrivalTime[0])+str(arrivalTime[1])

    if departureTime.isnumeric() and timeInt.isnumeric():
      timeInt=int(timeInt)
      timeIntTwo=int(departureTime)
    else:
      timeInt=timeInt
      timeIntTwo=departureTime

    logging.debug("The arrival time == "+str(timeInt)+" , Departure time == "+str(timeIntTwo))

    if not isinstance(timeInt,(int)) or not isinstance(timeIntTwo, (int)):
      logging.error("Input is invalid")
      print("Error: Invalid data type ")
      m=0
    elif int(timeInt)>int(timeIntTwo):
      logging.warning("Invalid value, departure time cannot be earlier than arrival time")
      print("Error: End time is earlier than when you started. Please try again.")
      m=0
      print()
    else:
      logging.info("Departure time is later than arrival time, code continues")
      if 24>newTime[0]>=0 and 60>newTime[1]>=0:
        logging.info("Valid value, code continues")
        print("Thank you, your time has been recorded.")
        m+=1
        print()

      else:
        logging.warning("Time format is invalid")
        print ("Error: time input not valid. Try again.")
        m=0
        print()

  elif counterOne==1 and counterTwo==4:
    newTime=list(departureTime.split(":"))
    newTime[0]=int(newTime[0])
    newTime[1]=int(newTime[1])

    logging.debug("Hour == "+str(newTime[0])+" , Minute == "+str(newTime[1]))

    #checks if the end time is earlier than the start time

    departureTime=list(departureTime)
    colon = departureTime.index(":")
    del(departureTime[colon])
    departureTime="".join(departureTime)

    timeInt=str(arrivalTime[0])+str(arrivalTime[1])

    if departureTime.isnumeric() and timeInt.isnumeric():
      timeInt=int(timeInt)
      timeIntTwo=int(departureTime)
    else:
      timeInt=timeInt
      timeIntTwo=departureTime

    logging.debug("The arrival time == "+str(timeInt)+" , Departure time == "+str(timeIntTwo))

    if not isinstance(timeInt,(int)) or not isinstance(timeIntTwo, (int)):
      logging.error("Input is invalid")
      print("Error: Invalid data type ")
      m=0
    elif int(timeInt)>int(timeIntTwo):
      logging.warning("Invalid value, departure time cannot be earlier than arrival time")
      print("Error: End time is earlier than when you started. Please try again.")
      m=0
      print()
    else:
      logging.info("Departure time is later than arrival time, code continues")
      if 24>newTime[0]>=0 and 60>newTime[1]>=0:
        logging.info("Valid value, code continues")
        print("Thank you, your time has been recorded.")
        m+=1
        print()

      else:
        logging.warning("Time format is invalid")
        print ("Error: time input not valid. Try again.")
        m=0
        print()
    
#Finding how long the delivery man has worked
hoursWorkedTwo=list(leaveTime.split(":"))

#converting the time into only minutes
hoursWorkedInMinutesOne=int(arrivalTime[0])*60+int(arrivalTime[1])
hoursWorkedInMinutesTwo=int(hoursWorkedTwo[0])*60+int(hoursWorkedTwo[1])

logging.debug("Arrival time in minutes == "+str(hoursWorkedInMinutesOne)+" , Departure time in minutes == "+str(hoursWorkedInMinutesTwo))

hoursWorkedInMinutes=int(hoursWorkedInMinutesTwo-hoursWorkedInMinutesOne)

logging.debug("Minutes worked == "+str(hoursWorkedInMinutes))

#turning the minutes back into hours/minutes
print("You worked "+str(int(hoursWorkedInMinutes/60))+" hour(s) and "+str(hoursWorkedInMinutes%60)+" minutes today.")
print("Goodbye!")
logging.info("End of program")
