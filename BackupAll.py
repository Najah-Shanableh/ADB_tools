#!python3
'''
This module backs up the 5 main Salesforce tables and saves to CSV
'''
from botutils.ADB import ssf
from botutils.tabletools import tabletools as tt
import datetime
import os
from botutils.fileutils import zipup #for compressing the output file at the end

dataDir = os.path.abspath('../SalesforceExports/KIPP_Chicago')
if not os.path.exists(dataDir):
    os.makedirs(dataDir)

ends =datetime.datetime.now().strftime('%m_%d_%Y')
outDir = os.path.join(dataDir,ends)
if not os.path.exists(outDir):
    os.makedirs(outDir)

sf = ssf.getSF()
objects = ['Contact',
           'Account',
           'Enrollment__c',
           'Contact_Note__c',
           'Relationship__c']
for obj in objects:
    exec('oj = sf.' + obj)
    table = ssf.getAll(sf, oj)
    tt.table_to_csv(outDir+'/'+obj+'_'+ends+'.csv', table)

zipup.compress(outDir) #Compresses the output directory into a single zip file
