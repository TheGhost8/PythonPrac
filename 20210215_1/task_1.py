from bottle import route, run, template, request
import pyfiglet

@route('/figlet_text')
def pyfiglet_text():
	return template('''
	<form action="/login" method="post">
		String:
		<input name="text" value="Test Text">
		<select name="font">
		%for font in fonts:
			<option>{{font}}</option>
		% end
		</select>
		<input type="submit">
	</form>
	''', fonts=pyfiglet.FigletFont.getFonts())

@route('/login', method='POST')
def do_pyfiglet_text():
	string = pyfiglet.figlet_format(request.forms.get("text"), font=request.forms.get("font"))
	return "<pre>" + string + "</pre>"

run(host='localhost', port=8080)