DATA = [
{"gender":"male","name":{"title":"mr","first":"brian","last":"watts"},"location":{"street":"8966 preston rd","city":"des moines","state":"virginia","postcode":15835},"dob":"1977-03-11 11:43:34","id":{"name":"SSN","value":"003-73-8821"},"picture":{"large":"https://randomuser.me/api/portraits/men/68.jpg","medium":"https://randomuser.me/api/portraits/med/men/68.jpg","thumbnail":"https://randomuser.me/api/portraits/thumb/men/68.jpg"}},
{"gender":"female","name":{"title":"miss","first":"terra","last":"jimenez"},"location":{"street":"1989 taylor st","city":"roseburg","state":"illinois","postcode":86261},"dob":"1987-05-08 18:18:06","id":{"name":"SSN","value":"896-95-9224"},"picture":{"large":"https://randomuser.me/api/portraits/women/17.jpg","medium":"https://randomuser.me/api/portraits/med/women/17.jpg","thumbnail":"https://randomuser.me/api/portraits/thumb/women/17.jpg"}},
{"gender":"female","name":{"title":"mrs","first":"jeanette","last":"thomas"},"location":{"street":"7446 hickory creek dr","city":"caldwell","state":"wyoming","postcode":73617},"dob":"1959-03-21 14:19:01","id":{"name":"SSN","value":"578-92-7338"},"picture":{"large":"https://randomuser.me/api/portraits/women/56.jpg","medium":"https://randomuser.me/api/portraits/med/women/56.jpg","thumbnail":"https://randomuser.me/api/portraits/thumb/women/56.jpg"}},
{"gender":"male","name":{"title":"mr","first":"darrell","last":"ramos"},"location":{"street":"4002 green rd","city":"peoria","state":"new york","postcode":62121},"dob":"1960-03-09 16:44:53","id":{"name":"SSN","value":"778-73-1993"},"picture":{"large":"https://randomuser.me/api/portraits/men/54.jpg","medium":"https://randomuser.me/api/portraits/med/men/54.jpg","thumbnail":"https://randomuser.me/api/portraits/thumb/men/54.jpg"}}
]

# get data for all students to use in index and write a list
def get_all_students(source):
    # new dictionary
    students = {}
    # write id as key and lastname as value into dict
    for record in source:
        id = record['id']['value']
        # .title() capitalizes the first letter of each word in string
        lastname = (record['name']['last']).title()
        students.update({id:lastname})
    # return a list of tuples sorted in alpha order by lastname
    # see https://pybit.es/dict-ordering.html - great resource! 
    return sorted(students.items(), key=lambda x: x[1])

print(get_all_students(DATA))
