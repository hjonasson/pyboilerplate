#!/usr/bin/python
import sys
import os

'''
Parameters
'''

filename , args = sys.argv[ 1 ] , sys.argv[ 2: ]
keysImports = { 'plt' : 'seaborn as sns\nimport matplotlib.pylab as plt ' ,
				'pd' : 'pandas as pd' ,
				'np' : 'numpy as np' ,
				'ss' : 'scipy.stats as ss'
				}

'''
Functions
'''

# flattening a list of lists
flatten = lambda l: [ item for sublist in l for item in sublist ]

# make values into an import string
stringer = lambda l : 'import ' + ' '.join( map( lambda _: '%s' , l[ 0 ] if isinstance( l[ 0 ] , tuple ) else [ None ] ) ) + '\n'

def parts( l = [ 'Parameters' , 'Functions' , 'Execution' ] ):

	# define the string that sections off parts of the code
	return "\n\n'''\n" + "\n'''\n\n\n\n'''\n".join( l ) + "\n'''\n\n"

def writer( f , l ):

	# make string needed for formatting
	st = stringer( l )
	for i in l:

		# write to the file with string formatting
		f.write( st % i )

	# file return
	return f

'''
Execution
'''

# filter the keys that are both in args and keysImports
reqImports = [ keysImports[ i ] for i in filter( lambda j : j in args , keysImports ) ]

# get indices of 'as' in requested to find all values that should have a pseudonym
reqPseuInds = map( lambda i : i[ 0 ] , filter( lambda ( i , j ) : j == 'as' , enumerate( args ) ) )

# get modules and pseudonyms
modPseu = map( lambda i : tuple( args[ i - 1 : i + 2 ] ) , reqPseuInds )

# filter requested imports that are not predefined
rINP = filter( lambda a : a not in keysImports.keys() + flatten( modPseu ) , args )

# create file with the requested filename
f = open( filename.endswith( '.py' ) and filename or '%s.py' % filename , 'w' )

# iterate over all imports to add
for reqs in filter( lambda i : i , [ reqImports , rINP , modPseu ] ):

	# call writer function defined above
	f = writer( f , reqs )

# write the areas for functionality
f.write( parts() )

# save the file
f.close()

# open the file in sublime
os.system( filename.endswith( '.py' ) and 'subl %s' % filename or 'subl %s.py' % filename )







