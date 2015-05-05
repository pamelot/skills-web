from flask import Flask, request

app = Flask(__name__)

@app.route("/application-request", method = "POST")
def form_request():
    name = request.args.get('firstname')
    lastname = request.args.get('lastname')
    salary = request.args.get('salaryask')
    position = request.args.get('job')
    
	return render_template("application.html", name=name, lastname=lastname, salary=salary, position=position)
   
	##### Why is it giving me an unexpected indent error?### AHHHH!!!!!!!!!

	
    # return "<html><body>This is the homepage.</body></html>"

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)