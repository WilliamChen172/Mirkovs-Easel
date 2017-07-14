'''
Created on Jul 23, 2015

@author: Matthew
'''
from cx_Freeze import setup, Executable  # @UnresolvedImport

copyDependentFiles=True
silent = True
includes = ["pygame","sys"]
setup(name='Markovs Easel',
     version = "1.0",
     options = {
       "build_exe" : {
           "includes": includes,
           },
       },
     executables=[Executable('Palette.py')],) 
