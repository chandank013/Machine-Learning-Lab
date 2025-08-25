'''
| **GET**     | Retrieve data from the server (read-only, no side-effects)             | Fetch a webpage, search query result       |
| **POST**    | Send data to the server to create a new resource                       | Submit form, register user                 |
| **PUT**     | Update an existing resource (or create if it doesn’t exist)            | Update user profile info in database       |
| **PATCH**   | Partially update an existing resource                                  | Change just the user's email               |
| **DELETE**  | Delete a resource from the server                                      | Remove a user account                      |
| **HEAD**    | Same as GET but only retrieves headers (no body/content)               | Check if a resource exists (metadata only) |
| **OPTIONS** | Get the allowed HTTP methods for a specific resource                   | Check allowed methods for an API endpoint  |
| **CONNECT** | Establish a tunnel to the server (mostly used for HTTPS proxy servers) | Secure connections, proxies                |
| **TRACE**   | Perform a message loop-back test along the path to the target resource | Debugging network routes  
'''


from flask import Flask,render_template,request
'''
 It creates an instance of the Flask class, 
 which will be your WSGI (Web Server Gateway Interface) application.
'''
###WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>Welcome to the flask course</H1></html>"

@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/form',methods=['GET','POST'])
def form():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')

@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')


if __name__=="__main__":
    app.run(debug=True)