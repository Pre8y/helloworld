import webapp2
import cgi

form = """
	<form method="post">
	<h1>
	Enter some text to ROT13:
	</h1>
	<br>
	<br>
	<textarea rows = "5" cols = "50" name="text" >
	%(result)s
	</textarea>
	<br>
	<input type="submit" value="submit">
	</form>
	"""

class MainPage(webapp2.RequestHandler):
	def write_form(self, result=""):
		self.response.write(form %{'result': result})
	
	def get(self):
		self.write_form()

	def post(self):
		text = self.request.get('text')
		result = rot13(text)
		self.write_form(result)
app = webapp2.WSGIApplication([('/', MainPage)], debug=True)



def rot13(text):
	result = ''
	if text:
		for i in text:
			if i.isalpha():
				c = i.lower()
				r = (ord(c)-ord('a')+13)%26
				if i.islower():
					result += chr(ord('a')+r)
				else :
					result += chr(ord('A')+r)
			else:
				result+= cgi.escape(i, quote=True)
	return result
