# first install PyMySQL with - pip install PyMySQL
# start XAMPP and start all services - NOTE: not XAMPP-VM
# this does not work with XAMPP-VM, but does work with plain XAMPP
# see https://github.com/PyMySQL/PyMySQL

import pymysql.cursors

# connect to the local database
conn = pymysql.connect(host='localhost',
                    user='root',
                    password=None,
                    db='myshoutbox',
                    charset='utf8',
                    cursorclass=pymysql.cursors.DictCursor)

# variables for new record - used below
name = "Monty"
shout = "Python rules!"
mydate = "12:12:12 pm 02-24-2018"

try:
    with conn.cursor() as cursor:
        # create a new record in the database
        sql = "INSERT INTO `shouts` (`name`, `shout`, `date`) VALUES (%s, %s, %s)"
        # format strings in Python: string (%s), integer (%d),
        # float (%f), and float restricted to 2 decimal places (%.2f)
        cursor.execute(sql, (name, shout, mydate))

    # the connection is not autocommit by default - you must commit to
    # save your changes
    conn.commit()

    with conn.cursor() as cursor:
        # read a single record that exists in the database
        # note, this is a record in MY local databse, not yours
        sql = "SELECT `name`, `shout` FROM `shouts` WHERE `date`=%s"
        cursor.execute(sql, ('01:26:00 pm 01-22-2018',))
        result = cursor.fetchone()
        print(result)

finally:
    conn.close()
