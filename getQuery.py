#!/usr/bin/python
import pandas as pd
import MySQLdb
import sys

'''
Parameters
'''

# define access parameters to the database
host , user , passwd = sys.argv[ 1 : 4 ]

# define the filename
filename = sys.argv[ 4 ]

# define the query to execute
query = ' '.join( sys.argv[ 5: ] )

'''
Functions
'''

def getData( host , user , passwd , query , datab = 'nice264' ):

	# set up a connection with the database
	db = MySQLdb.connect( host = host , user = user , passwd = passwd , db = datab )

	# fetch the data as a dataframe
	df = pd.io.sql.read_sql( query , db )

	# close the connection
	db.close()

	# return the dataframe with NaN filled in as 0
	return df.fillna( 0 )

'''
Execution
'''

# add csv to the name if it is not there already
filename = filename.endswith( '.csv' ) and filename or '%s.csv' % filename

# fetch the data requested and save to a file
getData( host = host , user = user , passwd = passwd , query = query ).to_csv( filename , index = False )
