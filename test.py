import cherrypy

import os.path

current_dir = os.path.dirname(os.path.abspath(__file__))

class Root(object):
	
	content = '''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/
   TR/html4/strict.dtd">
   <html>
   <head>
     <script type="text/javascript" src="static/jquery-1.4.2.js"
     ></script>
     <style>
       .light-grey { background-color: #e0e0e0; }
     </style>
   </head>
   <body>
     <table>
       <tr><td>one</td><td>line 1</td></tr>
       <tr><td>two</td><td>line 2</td></tr>
       <tr><td>three</td><td>line 3</td></tr>
       <tr><td>four</td><td>line 4</td></tr>
       <tr><td>five</td><td>line 5</td></tr>
       <tr><td>siz</td><td>line 6</td></tr>
     </table>
     <script type="text/javascript">
     $("tr:odd").addClass("light-grey");
     </script>
   </body>
   </html>
	'''
	
	@cherrypy.expose
	def index(self):
		return Root.content
	
if __name__ == "__main__":
	
	cherrypy.quickstart(Root(),config={
		'/static':
		{ 'tools.staticdir.on':True,
		  'tools.staticdir.dir':current_dir+"/static"
		}
	})
