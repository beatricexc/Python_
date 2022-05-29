from flask import Flask
app = Flask(_name_)
@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"
if _name_ == '_main_':
    app.run(host='0.0.0.0', port=105)