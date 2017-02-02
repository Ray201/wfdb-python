import numpy as np
import re
import os
import sys
from collections import OrderedDict
from calendar import monthrange



# Class with header method definitions. 
# To be inherited by WFDBrecord from records.py. (May split this into multi and single header)
class Headers_Mixin():

    # Write a wfdb header file. The signals fields are not used. 
    def wrheader(self):

        # Get all the fields used to write the header
        writefields = self.getwritefields()

        # Check the validity of individual fields used to write the header 
        for f in writefields:
            self.checkfield(f) 
        
        # Check the cohesion of fields used to write the header
        self.checkfieldcohesion(writefields)
        
        # Write the header file using the specified fields
        self.wrheaderfile(writefields)



    # Get the list of fields used to write the header. (Does NOT include d_signals.)
    # Returns the default required fields, the user defined fields, and their dependencies.
    def getwritefields(self):

        # Record specification fields
        writefields=self.getreqsubset(sreversed(list(recfieldspecs.items())))
        writefields.remove('nseg')

        # Determine whether there are signals. If so, get their required fields.
        self.checkfield('nsig')
        if self.nsig>0:
            writefields=writefields+self.getwritesubset(reversed(list(fieldspeclist[2].items())))

        # Comments
        if self.comments !=None:
            writefields.append('comments')
        return writefields

    # Helper function for getwritefields
    def getwritesubset(self, fieldspecs):
        writefields=[]
        for f in fieldspecs:
            if f in writefields:
                continue
            # If the field is required by default or has been defined by the user
            if f[1].write_req or self.f!=None:
                rf=f
                # Add the field and its recursive dependencies
                while rf!=None:
                    writefields.append(rf)
                    rf=fieldspecs[rf].dependency

        return writefields


    # Check the cohesion of fields used to write the header
    def checkfieldcohesion(self, writefields):

        # If there are no signal specification fields, there is nothing to check. 
        if nsig>0:
            # The length of all signal specification fields must match nsig
            for f in writefields:
                if f in sigfieldspecs:
                    if length(getattr(self, f)) != self.nsig:
                        sys.exit('The length of field: '+f+' does not match field nsig.')

            # Each filename must correspond to only one fmt, and only one blocksize if defined. 
            datfmts = {}
            datoffsets = {}
            for ch in range(0, self.nsig):
                if self.filename[ch] not in datfmts:
                    datfmts[self.filename[ch]] = self.fmt[ch]
                else:
                    if datfmts[self.filename[ch]] != self.fmt[ch]:
                        sys.exit('Each filename (dat file) specified must have the same fmt')
                    
                if self.filename[ch] not in datoffsets:
                    datoffsets[self.filename[ch]] = self.byteoffset[ch]
                else:
                    if datoffsets[self.filename[ch]] != self.byteoffset[ch]:
                        sys.exit('Each filename (dat file) specified must have the same byte offset')

    # Write a header file using the specified fields
    def writeheaderfile(self, writefields):

        # Record specification line
        recordline = ''
        # Traversing the ordered dictionary
        for field in recfieldspecs:
            # Add the field with its delimiter
            if field in writefields:
                recordline = recordline + recfieldspecs[field].delimiter + fieldstring = lambda getattr(self, field)




        # Signal specification fields

        # Comment fields
        commentlines = None
        if 'comments' in writefields














































    
            
   
    
    
    
    





# The useful summary information contained in a wfdb record.
# Note: NOT a direct subset of WFDBrecord's fields. 
infofields = [['recordname',
               'nseg',
               'nsig',
               'fs',
               'siglen',
               'basetime',
               'basedate'],
              
              ['filename',
               'maxresolution',
               'sampsperframe',
               'units',
               'signame'],
              
              ['segname',
               'seglen'],
              
              ['comments']]





        
# Write a multi-segment wfdb header file. 
def wrmultiheader(recinfo, targetdir=os.cwd(), setinfo=0):
    
    # Make sure user is not trying to write single segment headers. 
    if getattr(recinfo, 'nseg')!=None:
        if type(getattr(recinfo, 'nseg'))!= int:
            
            sys.exit("The 'nseg' field must be an integer.")
            
        if getattr(recinfo, 'nseg')==0:
            
            sys.exit("The 'nseg' field is 0. You cannot write a multi-segment header with zero segments.")
            
        elif getattr(recinfo, 'nseg')==1:
            
            print("Warning: The 'nseg' field is 1. You are attempting to write a multi-segment header which encompasses only one segment.\nContinuing ...")
            
    else:
        sys.exit("Missing input field 'nseg' for writing multi-segment header.\nFor writing regular WFDB headers, use the 'wrheader' function.")
                  
    
    WFDBfieldlist = [recfields.copy(), segfields.copy(), comfields.copy()]
                  
    
    keycheckedfields = _checkheaderkeys(inputfields, WFDBfieldlist, setsigreqs, 1)
    
    # Check the header values
    valuecheckedfields = checkheadervalues(keycheckedfields, WFDBfields, setsigreqs, 0)
    
    # check that each signal component has the same fs and the correct number of signals. 
    
    # Write the header file
    
    
# Merge the ordered dictionaries in a list into one ordered dictionary. 
# Belongs to the module
def _mergeODlist(ODlist):
    mergedOD=ODlist[0].copy()
    for od in ODlist[1:]:
        mergedOD.update(od)
    return mergedOD
                  

            