from flask import Flask, render_template, request
from flask.views import MethodView

app = Flask(__name__)

@app.route("/")
def hello():
    # return render_template('index.html')
    return "Hello"

@app.route("/products")
def prod():
    return "Products"

# uuid - it's a data type
# int, str, bool
@app.route("/user/<uuid:uuid>")
def user(uuid):
    return str(uuid) + "\n"

# Query param
@app.route("/user", methods=['GET', 'POST'])
def users():
    resp_dic = dict()
    if request.method == 'GET':
        if 'FirstName' in request.args:
            resp_dic['FirstName'] = request.args.get('FirstName')
        if 'LastName' in request.args:
            resp_dic['LastName'] = request.args.get('LastName')
        return resp_dic

    elif request.method == "POST":
        body = request.get_json()
        resp_dic["FirstName"] = body.get("FirstName", "")
        resp_dic["LastName"] = body.get("LastName", "")
        return resp_dic

# Post method
@app.route('/method', methods=['GET', 'POST'])
def method():
    return "Method"


class ProjectAPI(MethodView):
    def get(self):
        return "Project List"
    
app.add_url_rule('/project', view_func=ProjectAPI.as_view)

if __name__ == "__main__":
    app.run(debug=True, port=8000) 