
from mechanize  import Browser
from bs4 import BeautifulSoup
import cookielib
import mechanize
import random
logo='''
Hi I <3 evry Musslim and You

	         (__)
                 (oo)
           /------\/
          / |    ||
         *  /\---/\\


..."You Want Create Twitter  Account Let's Go"...

'''
print (logo) ;
br = Browser()
cj = cookielib.LWPCookieJar()
br.set_handle_robots(False)
br.set_handle_equiv(True)
br.set_handle_referer(True)
br.set_handle_redirect(True)
br.set_cookiejar(cj)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
headers =[('user-agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246')]
br.addheaders = [('user-agent',random.choice(headers))]
email = raw_input("Email Please ...\n")
fullname = raw_input("FullName Please ... \n")
password = raw_input("Password Please ... \n")
print ("trying please wait .....")
site = "https://twitter.com/signup"
br.open(site)
formcount=0
for frm in br.forms():
  if "id" in frm.attrs:
    if str(frm.attrs["id"])=="phx-signup-form":
      break
  formcount=formcount+1
br.select_form(nr=formcount)
br.form["user[name]"]=fullname
br.form["user[email]"]=email
br.form["user[user_password]"]=password
br.submit()
verisite = br.geturl()
if verisite is not site:
    print("account has been create Go And Complete The Settings........")
else:
    print("N0t create......")
