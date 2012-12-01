import webapp2

from google.appengine.api import users

class MainPage(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/plain'
		self.response.out.write('Hello, Udacity')

	
app = webapp2.WSGIApplication([('/', MainPage)],
				debug = True)
