# these functions are used in the routes in students.py 

# get data for all students to use in index and write alpha list there
def get_all_students(source):
    students = {}
    for record in source:
        id = record['id']['value']
        lastname = (record['name']['last']).title()
        students.update({id:lastname})
    return sorted(students.items(), key=lambda x: x[1])

# get data from one student based on idnum - use in student
def get_student(source, idnum):
    for record in source:
        if idnum == record['id']['value']:
            name = (record['name']['last']).title() + ", " + (record['name']['first']).title()
            photo = record["picture"]["large"]
            street = record["location"]["street"].title()
            city = record["location"]["city"].title()
            state = record["location"]["state"].title()
            postal = str(record["location"]["postcode"])
            address = street + ", " + city + ", " + state + " " + postal
            return name, photo, address
    # return these if id is not valid
    return "Unknown", "", "Unknown"
