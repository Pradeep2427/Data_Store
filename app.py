# Libraries To Import 
import os
import json
from json.decoder import JSONDecodeError
from sys import getsizeof
from datetime import datetime,timedelta

def data_update():
    global data,path_directory
    f = open(path_directory,'w',encoding="utf-8")
    json.dump(data,f ,ensure_ascii=False) 
    f.close()
    return

def is_time_expired(exp_time):
    current_time = datetime.now()
    expiry_time = datetime.fromtimestamp(exp_time)
    if current_time > expiry_time:
        return True
    return False

def delete_value(key_to_delete):
    global data
    data.pop(key_to_delete)
    return

def getting_key(call_type):
    global data
    key = str(input("Enter the key for json\n>>> "))
    if (call_type == "create" and len(key) > 32): 
        print("The key is exceding 32 character")
        return getting_key(call_type)
            
    if key in data.keys():
        try :
            expiry_time = data.get(key , {}).get('expiry_time')
            if is_time_expired(expiry_time) : #checks for the expiry time
                delete_value(key)
                data_update()    
                if call_type == 'read':
                    print ("The key was expired and no longer available")
                    return None
                elif call_type == 'delete':
                    print ("The key was expired and no longer available")
                    return action_in_file()
            else:
                if call_type == 'create':
                    print ("Already exits")
                    return getting_key(call_type)
        except TypeError:
            if call_type == 'create':
                    print ("Already exits")
                    return getting_key(call_type)
    return key   

def getting_value():
    value = input("Enter valid json object for value\n>>> ")
    obj_value_size = getsizeof(value)
    if (obj_value_size > 16000): 
        print("The value size is exceeding 16kb")
        return getting_value()
    if file_size_check(obj_value_size): #to check the file exits 1GB after adding the value
        return value 

def getting_time():
    time_to_add = input("Enter the time in seconds\n>>> ")
    time = time_to_add
    if time_to_add == '':
        return None
    current_time = datetime.now()
    expiry_time = current_time + timedelta(seconds=int(time_to_add)) #add the given seconds with the current time
    expiry_time = datetime.timestamp(expiry_time) #converts to timestamp
    expiry_time_list = [expiry_time , time]
    return expiry_time_list            

def create():
    global data,path_directory
    key = getting_key("create")
    value = getting_value()
    expiry_time = getting_time()
    if expiry_time == None: #user does not gives the time
        value_dictionary = {"value" : value}
    else:
        value_dictionary = {"value" : value , "time_to_live" : expiry_time[1], 'expiry_time' : expiry_time[0]}
    data[key] = value_dictionary
    data_update()
    print("New object created : {",key + " : " ,value_dictionary,"}")
    return action_in_file()

def delete():
    global data
    key = getting_key('delete')
    if key in data.keys(): #deleting and updating values
       delete_value(key)
       data_update() 
       print("Deleted Successfully")
    else: 
       print ("The key is not matched with any objects")
    return action_in_file()

def read():
    global data
    key = getting_key("read")
    if key in data.keys():
        obj_value = data[key]
        print (obj_value['value'])
    elif key == None: #the key is expired in this condition
        pass
    else :
        print("The key is not matched with any objects")
    return action_in_file()

def action_in_file():
    print ("Mention the Action to be Performed")
    crd = input("To CREATE enter C/c \nTo READ enter R/r \nTo DELETE enter D/d  \nTo Exit enter E/e \n>>> ").lower()
    if(crd == "c"):
        create()
    elif(crd == "r"):
        read()
    elif(crd == "d"):
        delete()
    elif(crd == 'e'):
        quit()
    else:
        print("Enter the correct action to be performed")
        return action_in_file()

def file_size_check(input_size):
    file_size = os.path.getsize(path_directory) #to get the file size
    if input_size + file_size >= 1073741824: # 1GB check
        print ("File Exceeds 1GB storage limit")
        return app()
    return True

def to_check_expiry_objects():
    global data ,path_directory
    to_delete_lis = []
    for i in data.keys():
        try:
            expiry_time = data.get(i , {}).get('expiry_time') # to get the expiry timestamp
            if is_time_expired(expiry_time): #is_expired
                to_delete_lis.append(i) #delete_list
        except TypeError:
            pass
    for key in to_delete_lis:
        delete_value(key) #deleting expired objects
    data_update()   #update the new file
    if file_size_check(0):  # 0 is for the function to get the file size and add that and check.
        return 

def load_data(path):
    global data
    try:
        file_open = open (path ,'r',encoding="utf-8")
        data = json.load(file_open) #json objects is loaded into data as python dictionary
        file_open.close()
    except: #if file not exits, New file is created
        empty_dic = {}
        new_file = open (path , 'w' ,encoding="utf-8") #opening new file
        json.dump(empty_dic,new_file,ensure_ascii=False) #json dump is used bcoz dump methon accepts dictonary
        new_file.close()
        print ("\'''New File Created\''' ")
        load_data(path)
    to_check_expiry_objects()
    return action_in_file()

def file_existing_check(path,dirc):
    global path_directory
    path_directory = path + dirc
    existance_variable = os.path.isfile(path_directory) #getting file directories
    if existance_variable == True:
        print("The given file name already exist")
        option = input("Do you want to perform actions over it ? if yes enter Y/y or enter N/n \n>>> ").lower()
        if option == 'y':
            with open(path_directory,'r'):
                print ("File Opened")
                load_data(path_directory) 
        elif option == 'n':
            return app()
        else:
            print("Enter the correct action to perform")
        file_existing_check(path,dirc)
    else:
        load_data(path_directory)
       
def app():
    global path_directory
    parent_dir = "/home/pradeep/data_files/"
    directory = input("Enter the file Name \n>>>  ")  

    # Default Storage Location
    if directory == '':
        print ("Default storage location")
        path_directory = parent_dir + "default.json"
        load_data(path_directory)

    # To get file name with extension
    temp = []
    temp [:0] = directory
    if '.' in temp:  # To check Wheather the user gave .json extension
        file_name = directory
    else :
        file_name = directory +'.json'
    if '/' in temp:
        list_dir = directory.split('/')
        file_name = list_dir[-1] 
        if ( '.' in file_name ):
            pass
        else:
            file_name = list_dir[-1] + '.json'           

    # To get extension 
    extension = ''
    len_temp_var = []
    exten = []
    exten [:0] = file_name
    for i in file_name:
        if i == '.':
            len_temp_var.append(i)
        if ( len(len_temp_var) > 0 ):
            extension = extension + i 
    if extension == '':
        extension = '.json'
    if extension != '.json':
        print ("Not a Valid Extension")
        return app()

    # File Name 
    dirc = file_name 
    dir_lis = directory.split('/')
    file_path_to_check = dir_lis[1:-1]
    path = '/'
    for i in file_path_to_check:
        path = path + i + '/'
    if path == '/':
        file_existing_check(parent_dir , dirc)
    else:
        file_existing_check(path , dirc)

if __name__ == "__main__":
    app()
