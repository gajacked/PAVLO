### After natural language processing is completed the data
### will be inserted using this module

import msyql




def insertdb(query_param):
    try:
            
        con =  mysql.connect('localhost','root','#####')

        cur = con.cursor()

        query = "Insert into query_box values (%s, %s, %s)"
        con.execute(query, query_param)

    except:
        "RIP connection has failed"

    finally:
        con.close()


    
