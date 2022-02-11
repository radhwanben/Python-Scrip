
from ftplib import FTP




#small logo :v
logo='''
**********************************************************
###########
##
##     TP ATTCKER V1
##
#########  		{**Coded By Radhwan Benyoussef**}
##   		
##			{**greetz to alah**}
##			
***********************************************************
'''
print(logo) ;


wlist = raw_input("enter hosts list plz ...\n")
w = open(wlist,"r")
for i in w.readlines():
	i=i.rstrip("\n")
print ("trying to conect with",i)

ftp = FTP(i)
try:
  ftp.login()
  files = ftp.dir()
  print files
  print 'Working: %s' % (i)
  write = open('Ftp.txt', "a+")
  write.write(i + '\n')
  write.close()  
  ftp.quit() 
except ftplib.all_errors: 
	print 'Not Working: %s' % (i) 
               
