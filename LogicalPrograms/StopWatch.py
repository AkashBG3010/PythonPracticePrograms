import time    # Importing tile library

def time_convertion(sec):       # initiating time conversion function
    mins = sec // 60            # conversions
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60

    input("Press Enter to start the stopwatch: \n")     # Reading User Input
    print("The Stopach watch has started....")
    start_time = time.time()        # Starting Timer

    input("Press Enter to stop the stopwatch: \n")      # Reading User Input
    print("-----The Stopach watch has ended------")
    end_time = time.time()      # Stopping Timer

    time_lapsed = end_time - start_time     # Total time elapsed calculation
    time_convertion(time_lapsed)
    print("Total Time Lapsed = {0}:{1}:{2}".format(int(hours), int(mins), sec))     # Printing result






















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
    #      except KeyboardInterrupt:
    #          print("Stopwatch has stopped")
    #          end_time=time.time()
    #          print("The total time elapsed: ",round(end_time-start_time,2),'secs')
    #          break