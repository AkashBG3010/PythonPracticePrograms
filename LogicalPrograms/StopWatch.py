import time    # Importing tile library


def time_convertion(sec):       # initiating time conversion function
    mins = sec // 60            # conversions
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60

    print("Total Time Lapsed = {0}:{1}:{2}".format(int(hours), int(mins), sec))  # Printing result


def startTimer(char):
    if (char == 'Y') | (char == 'y'):       # Validating
        print("The Stopwatch watch has started....")
        start_time = time.time()  # Starting Timer

        char = str(input("Press N/n Enter to stop the stopwatch: \n"))  # Reading User Input

        if (char == 'N') | (char == 'n'):
            print("<-----The Stopwatch has ended------>")
            end_time = time.time()  # Stopping Timer

            totalTime(start_time, end_time)      # Function calling

        else:
            print("Invalid! Please enter correct key (N,n)")

    else:
        print("Invalid! Please enter correct key (Y,y)")


def totalTime(start_time, end_time):    # Function to calculate total time elapsed
    time_lapsed = end_time - start_time     # Total time elapsed calculation
    time_convertion(time_lapsed)


char = str(input("Press Y/y to start the stopwatch: \n"))  # Reading User Input
startTimer(char)

print("----------End of Program--------------")













#####///////////////////////////////////###########################


    # import time
    #
    # second = 0
    # minute = 0
    # hours = 0
    #
    # while True:
    #      try:
    #          input("Press Enter to continue and ctrl+C to exit the stopwatch: \n")
    #          start_time=time.time()
    #          print("Stopwatch has started--------->")
    #          while True:
    #              print("Time elapsed:",round(time.time()-start_time,0),'secs',end='\n')
    #              time.sleep(1)
    #             break
    #       except KeyboardInterrupt:
    #          print("Stopwatch has stopped")
    #          end_time=time.time()
    #          print("The total time elapsed: ",round(end_time-start_time,2),'secs')
    #          break