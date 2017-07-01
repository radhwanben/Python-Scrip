import mechanize

br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.addheaders = [('user-agent','Nokia6630/1.0 (2.3.129) SymbianOS/8.0 Series60/2.6 Profile/MIDP-2.0 Configuration/CLDC-1.1')]


def login(user, pwd):
	global br
	br.open('https://mobile.twitter.com/login')
	br.select_form(nr=0)
	br.form['session[username_or_email]'] = user
	br.form['session[password]'] = pwd
	br.submit()
	return br.geturl() == "https://mobile.twitter.com/"

def tweet(text):
	global br
	br.open('https://mobile.twitter.com/compose/tweet')
	br.select_form(nr=0)
	br.form['tweet[text]'] = text
	try:
		br.submit()
	except:
		#To escape the 302 Exception : mechanize._response.httperror_seek_wrapper: HTTP Error 302: Found
		pass
	

print "You need to login to your twitter accoutn first"
user = raw_input("Your login /Email:")
pwd = raw_input("Your Password")

if(login(user, pwd)):
	print "Authenticated Successfuly"
	print "Write a tweet ^^"
	text=  raw_input("What do you want to say?")
	while (len(text) > 140 or len(text)==0):
		print "Sorry but you need to type a tweet with text between 0/140 characters"
		text = raw_input("re-type your tweet")
	tweet(text)
	print "Done your tweet was updated successfuly"
else:
	print "Sorry but i guess you frogot your password!"
 	
