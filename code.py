import sys
import threading
from threading import *
import time

dictionary = {}  #dictionary= to store data


def create(key, district,state, timeout=0):
    if key not in dictionary:
        if len(dictionary) < (1024 * 1020 * 1024) and sys.getsizeof(district) + sys.getsizeof(state) <= (
                16 * 1024 * 1024):  # constraints for file size less than 1GB and sizeof(name + phno) value less than 16KB
            if timeout == 0:
                l = [district, state, timeout]
            else:
                l = [district, state, time.time() + timeout]
            if len(key) <= 32:  # constraints for input key_name capped at 32chars
                dictionary[key] = l
                print("successfully created")
        else:
            print("error: Memory limit exceeded!! ")  # error message2

    else:
        print("error: this key already exists")  # error message1



def read(key):
    if key not in dictionary:
        print("error: given key does not exist in database. Please enter a valid key")  # error message4
    else:
        d_copy = dictionary[key]
        if d_copy[2] != 0:
            if time.time() < d_copy[2]:  # comparing the present time with expiry time
                output = "{" + "district" + ":" + str(d_copy[0]) + "," + "state" + ":" + str(
                    d_copy[1]) + "}"  # to return the value in the format of JasonObject (for example "key_value:district,state")
                return output
            else:
                print("error: time-to-live of", key, "has expired")  # error message5
        else:
            output = "{" + "district" + ":" + str(d_copy[0]) + "," + "state" + ":" + str(d_copy[1]) + "}"
            return output



def delete(key):
    if key not in dictionary:
        print("error: given key does not exist in database. Please enter a valid key")  # error message4
    else:
        d_copy = dictionary[key]
        if d_copy[2] != 0:
            if time.time() < d_compy[2]:  # comparing the current time with expiry time
                del dictionary[key]
                print("key is successfully deleted")
            else:
                print("error: time-to-live of", key, "has expired")  # error message5
        else:
            del dictionary[key]
            print("key is successfully deleted")



