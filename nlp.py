# This file is where all the natural language processing will take place

#  We have not completed this section yet
import mysql


def processing_set():
    try:
        con = mysql.connect('localhost', 'root', '######')
        cur = con.cursor()
        
        cur.execute("Select query from query_box")
        data = cur.fetchall()
        cur.execute("Delete * from query_box")
        con.commit()
        return data
    except:
        "RIP connection failed"
    finally:
        con.close()
