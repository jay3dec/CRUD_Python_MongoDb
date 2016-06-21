from pymongo import MongoClient

# creating connectioons for communicating with Mongo DB
client = MongoClient('localhost:27017')
db = client.EmployeeData

def main():

    while(1):
	# chossing option to do CRUD operations
        selection = raw_input('\nSelect 1 to insert, 2 to update, 3 to read, 4 to delete\n')
    
        if selection == '1':
	    insert()
    	elif selection == '2':
	    update()
    	elif selection == '3':
	    read()
    	elif selection == '4':
	    print 'delete'
	    delete()
    	else:
	    print '\n INVALID SELECTION \n'


# Function to insert data into mongo db
def insert():
    try:
	employeeId = raw_input('Enter Employee id :')
	employeeName = raw_input('Enter Name :')
	employeeAge = raw_input('Enter age :')
	employeeCountry = raw_input('Enter Country :')
        
	db.Employees.insert_one(
	    {
		"id": employeeId,
	        "name":employeeName,
		"age":employeeAge,
		"country":employeeCountry
	    })
        print '\nInserted data successfully\n'
	
    except Exception, e:
        print str(e)
	
# Function to update record to mongo db
def update():
    try:
	criteria = raw_input('\nEnter id to update\n')
	name = raw_input('\nEnter name to update\n')
	age = raw_input('\nEnter age to update\n')
	country = raw_input('\nEnter country to update\n')

	db.Employees.update_one(
	    {"id": criteria},
	    {
		"$set": {
		    "name":name,
		    "age":age,
		    "country":country
		}
	    }
	)
	print "\nRecords updated successfully\n"	
	
    except Exception, e:
	print str(e)

# function to read records from mongo db
def read():
    try:
	empCol = db.Employees.find()
	print '\n All data from EmployeeData Database \n'
	for emp in empCol:
	    print emp

    except Exception, e:
	print str(e)

# Function to delete record from mongo db
def delete():
    try:
	criteria = raw_input('\nEnter employee id to delete\n')
        db.Employees.delete_many({"id":criteria})
	print '\nDeletion successful\n'	
    except Exception, e:
	print str(e)

main()
