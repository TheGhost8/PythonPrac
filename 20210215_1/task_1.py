from bottle import route, run, template, request
import pyfiglet

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

@route('/zapros')
def zapros():
	name = request.query.name
	return template('<b>Hello</b>, <i>{{name}}</i>!', name=name)

@route('/figlet_text')
def pyfiglet_text():
	return template('<b>Hello</b>, <i>world</i>!')

@route('/abc/<string>')
def alphabet(string):
	return template('''
	<ol>
	%for c in string:
		<li>{{c}}</li>
	% end
	</ol>
	''', string=pyfiglet.FigletFont.getFonts())

run(host='localhost', port=8080)