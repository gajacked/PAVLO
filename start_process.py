from multiprocessing import Pool

import Agent1
import Agent2
##import Agentn

# Here n refers to the number of parallel voice recognition agents we have

# As soon as an Agent is made available the data will be updated here

def main():
    pool = Pool( process = n)


    Agent1 = pool.apply_async(Agent1, parameters)
    Agent2 = pool.apply_async(Agent2, parameters)
    #..........
    Agentn = pool.apply_async(Agentn, parameters)


    pool.close()
    pool.join()

    final = FinalProcess(Agent1.get(), Agent2.get(), Agentn.get())



if '__name__' == '__main__':
    main()
    
