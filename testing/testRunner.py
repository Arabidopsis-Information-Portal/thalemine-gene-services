import main
import time

def test():
    testQuery = "AT5G01010"
    #testQuery = "AT2G01008"
    #testQuery = "AT3G01010"
    #testQuery = "AT4G00005"
    #testQuery = "AT5G01010"

    for i in range(0,5):
        start_time = time.time()
        print "Current date "  + time.strftime("%x")
        print "Current time " + time.strftime("%X")
        main.search(testQuery)
        print("--- %s seconds ---" % (time.time() - start_time))
        print(".")
        time.sleep(5)
