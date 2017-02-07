#!/usr/bin/python
import pandas as pd
import sys
import glob
import os
from datetime import date , timedelta as td

'''
Parameters
'''

# get beginning date, end date, access to database and the base for the query to be run
d0 , d1 , host , user , passwd , query_base = sys.argv[ 1 : ]

'''
Functions
'''

def iterDates( i ):

	# get the current beginning and end time
	d0i , d1i = d0 + td( days = i ) , d0 + td( days = i + 1 )

	# convert them back to string format
	d0i , d1i = d0i.strftime( '%Y-%m-%d' ) , d1i.strftime( '%Y-%m-%d' )

	# let them know!
	print 'Fetching data for %s' % d0i

	# filename for the current date data
	f = filename( system , d0i )
	
	# if the data already exists there is no need to fetch it, if you are changing the query either the old data is not what you wanted or if you want to keep it, your current project should be in a different folder yall
	if not os.path.isfile( f ):

		# call the python script getQuery from /usr/local/bin/, what are you doing with your life if you dont have it???
		os.system( "getQuery '%s' '%s' '%s' '%s' '%s'" % ( host , user , passwd , f , query( d0i , d1i ) ) )

# base name for data files as defined by the boss
filename = lambda system , d : '%s/data-%s000000.csv' % ( system , ''.join( d.split( '-' ) ) )

# for formatting of dates
formatDate = lambda d : tuple( [ int( i ) for i in d.split( '-' ) ] )

# adding dateslicing to the base query
query = lambda d0 , d1 : '%s where init_at > "%s" and init_at < "%s"' % ( query_base , d0 , d1 )

'''
Execution
'''

# get the system ID as NPAW constructs databases
system = query_base.split( 'log_')[ -1 ].split( ' ' )[ 0 ]

# format the start and end dates
d0 , d1 = date( *formatDate( d0 ) ) , date( *formatDate( d1 ) )

# find how many days they are apart
delta = d1 - d0

# in case this is the first time fetching data for this system in this folder
if not os.path.exists( system ): os.mkdir( system )

# call iterdates for each day
map( iterDates , range( delta.days ) )
