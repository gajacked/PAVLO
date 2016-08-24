import Voice_Recognition_1
import microphone
import db_insert
import datetime
from random import randint



def get_time():
    current_time = datetime.datetime.now().time()
    return current_time.isoformat()

def key_generator():
    range_start == 10**9
    range_end == (10**10)-1
    return randint(range_start, range_end)


def start_recognition():
    timer = 10000
    sentence = Voice_recongiton_1.start(timer)
    
    db_insert.insertdb((key_generator,sentence, get_time()), querybox) 

