#!/usr/bin/python
import os
import sys
import datetime
import argparse

#Server constants
server = '127.0.0.1'
db = 'mysql'

parser = argparse.ArgumentParser()
parser.add_argument("-d", metavar="Database-Name", nargs="?", help="Select the database to use")
parser.add_argument("-s", metavar="Server-Name", nargs="?", help="Input the IP or domain name of the server")
parser.add_argument("-v", "--verbose", help="Increase output verbosity", action="store_true")
args = parser.print_help()

'''
# Getting current datetime to create separate backup folder like "12012013-071334".
DATETIME = time.strftime('%Y%m%d')

TODAYBACKUPPATH = BACKUP_PATH + DATETIME

# Checking if backup folder already exists or not. If not exists will create it.
# print "creating backup folder"
if not os.path.exists(TODAYBACKUPPATH):
    os.makedirs(TODAYBACKUPPATH)
mod = "chmod 777 " + TODAYBACKUPPATH
os.system(mod)

# Starting actual database backup process.
db = DB_NAME
TODAYBACKUPFILE = TODAYBACKUPPATH + "/IC.SQL.tar.gz"
dumpcmd = "mysqldump -u root --lock-tables=FALSE --verbose --tab=" + TODAYBACKUPPATH + " " + db
#tarcmd = "tar cvzf " + TODAYBACKUPFILE + " " + TODAYBACKUPPATH + "/* --remove-files"
tarcmd = "tar cvzf " + TODAYBACKUPFILE + " " + TODAYBACKUPPATH + "/*"
scpcmd = "scp " + TODAYBACKUPFILE + " dclark@10.10.101.7:IC_Backups/IC.SQL." + DATETIME + ".tar.gz"

#print dumpcmd
#print tarcmd
#print scpcmd

os.system(dumpcmd)
os.system(tarcmd)
os.system(scpcmd)
delsql = "rm -rf " + TODAYBACKUPPATH + "/*.sql"
deltxt = "rm -rf " + TODAYBACKUPPATH + "/*.txt"
os.system(delsql)
os.system(deltxt)

databasename = raw_input('Enter the database name to restore: ')
filedate = raw_input('Enter the date to restore (YYYYMMDD): ')
#user = raw_input('Enter MySQL Username: ')
#pw = getpass.getpass()
path = "/home/dclark/IC_Backups/"
zipfile =  path + "IC.SQL." + filedate + ".tar.gz"
unzipcmd = "zcat " + zipfile + " > " + zipfile[0:-3]
untarcmd = "tar -C / -xvf " + zipfile[0:-3]

#print file
#print unzipcmd
#print untarcmd
os.system(unzipcmd)
os.system(untarcmd)
restorepath = path + filedate
files = os.listdir(restorepath)

for file in files:
    if file[-3:] == "sql":
        sql="mysql -u root " + databasename + " < " + path + filedate + "/" + file
        #print sql
        os.system(sql)
for file in files:
    if file[-3:] == "txt":
        sql="mysqlimport -u root " + databasename + " " + path + filedate + "/" + file
        #print sql
        os.system(sql)

cleanup = "rm -rf " + restorepath + "; rm -f " + zipfile[0:-3]
print cleanup
os.system(cleanup)
'''
