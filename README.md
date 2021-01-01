DATA STORE IMPLEMENTATION AND USAGE DOCUMENT

Key Value DataBase Definition:

A key-value database is a type of non relational database that uses a simple key-value method to store data. A key-value database stores data as a collection of key-value pairs in which a key serves as a unique identifier. Both keys and values can be anything, ranging from simple objects to complex compound objects.

As mentioned in the above definition, the data store is implemented using JSON as given in the Functional Requirement of the Problem Statement.

Language & Libraries Used :

Python 3
Python Libraries Used : json, os, JSONDecodeError, sys , datetime

Functional / Non Functional Requirements Adhered:

Optional File Path is requested from Client if not provided Default Storage Location (/home/user/….) is used.
The key is validated to be equal or lesser than 32 characters
Create operation on existing key throws appropriate error.
Read and Delete Operations is operated based on given key from the Client.
Time to live property implemented as expected.
Checks implemented such that Data File does not exceed 1 GB.
Multiple Client Processes are not allowed to access the same file simultaneously.

Implementation Details :
Approach 1

	Functions Implemented : 
	app() :
	''' A global variable stores the directory path. The directory is received  from the user. if not, the default file directory is stored. The directory is checked whether it is a default path or a new path. If the received file name has an extension other than ‘.json’ error message will be thrown. The file name can be without extension. By default it is considered as ‘.json’.'''
	
	file_existing_check():
	''' The function checks whether the file exists or not. If it exists it gets permission to access it.'''
	
	load_data():
	''' The function loads the json objects in the file into a python dictionary and makes it as a global dictionary. '''

	to_check_expiry_objects():
	''' The function checks the expiry time for the json objects and deletes the expired objects.'''

	file_size_check():
	''' The function checks whether the file exceeds 1GB of storage.'''
	
	action_in_file():
	''' The function receives what action is to be performed, CRD from the user.'''
	
	is_time_expired():
	''' The function takes the expiry time of the object and compares it with the current time.'''
	
	delete_value():
        ''' The function takes the key of the object and delete it from the global json data variable.'''
	
	data_update():
	''' The function updates the json file, dump the data into the json file.'''

	getting_key():
	''' The function receives the key from the user, checks whether the key exceeds 32 characters and whether the key exists in the json file or it got 	   expired.'''

	getting_value():
	''' The function receives the json object and checks if it exceeds 16KB.'''

	getting_time():
	''' The function receives the time to live for the json object to live from the user. If time is not given the objects will be present in the file forever.'''
	
	create():
	''' The function creates the json object in the desired file.'''
	
	read():
	''' The function displays the json object value using the key  and also checks if the key exists in the json file if not it throws a error message.'''

	delete():
	''' The function deletes the json object using the key and also checks if the key exists in the json file if not it throws a message.'''


Usage Guide :

The python program is used as a Datastore for storing the JSON objects. 
The file name or the path directory of the json.file is requested, if the file does not exist it will create a new file in the default path.
The file name can be with or without the extension.  By default it is considered as ‘.json’, other extensions are not allowed.
If the file name is not given it stores in the default file location.
The permission to access the json file is requested.  	
The action to be performed (CRD - Create,Read,Delete,Exit) is requested.  
For Create :
The key for creation is requested, if the key exceeds 32 characters or the key already exists in the file, an error message is thrown. 
The value for the json object is requested, if the value exceeds 16KB or the file exceeds 1GB, an error message is thrown.
The time is requested for the json object to be in the file. If it is skipped, the json object will be in the file permanently.
For Read :
The key is requested, if the json object was expired or the key is not available in the file, an error message is thrown.
If the key available in the file, the value of the object is displayed.
For Delete :
The key is requested, if the key is in the json file then the object is deleted.

Input Requested :

The file name for the action.
Permission to access the file. 
Input for the action to be performed ( CRD - Create,Read,Delete ) & (E - Exit)
Key for the action to be performed.
Value for creation.
Time for the creation.



Output Given:

Read Operation - If key exists, the value is gives as JSON Response.
Create Operation - On successful creation of a key-value pair, the entire JSON Object is given as response.
Delete Operation - Acknowledgement Messages.
	

Error Messages Displayed:

“The key exceeding 32 characters” - while the creation of the key.
“Already Exists” - when the key already exists while creating a key.
“The value size is exceeding 16kb” - when the value is above 16KB during creation.
“The key is not matched with any objects” -  When key not found while Reading.
“File exceeds 1GB storage limit” - when the json file is above 1GB.







		
