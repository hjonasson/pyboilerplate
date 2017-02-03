#!/usr/bin/python
import sys

'''
Parameters
'''

filename , args = sys.argv[ 1 ] , sys.argv[ 2: ]
keysImports = { 'plt' : 'import seaborn as sns\nimport matplotlib.pylab as plt ' ,
				'pd' : 'import pandas as pd' ,
				'glob' : 'from glob import glob' ,
				'np' : 'import numpy as np'
				}

'''
Functions
'''

def reqImports():

	# filter the keys that are both in args and keysImports
	return { i : keysImports[ i ] for i in filter( lambda j : j in args , keysImports ) }

def parts( l = [ 'Parameters' , 'Functions' , 'Execution' ] ):

	return "\n\n'''\n" + "\n'''\n\n\n\n'''\n".join( l ) + "\n'''\n\n"

'''
Execution
'''

# create file with the requested filename
f = open( filename.endswith( '.py' ) and filename or '%s.py' % filename , 'w' )

# filter the requested imports and how to import them
rI = reqImports()

# write the requested imports
for i in rI: 
	f.write( '%s\n' % rI[ i ] )

# filter requested imports that are not predefined
rINP = filter( lambda a : a not in rI.keys() , args )

# write those imports
for i in rINP:
	f.write( 'import %s\n' % i )

# write the areas for functionality
f.write( parts() )

# save the file
f.close()








