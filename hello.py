from flask import Flask
from flask import request

from flask import Flask,render_template

import easygui as g

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    import os
    
    #x=str(dir(os.environ))
   # with open('2.txt',"a") as f1:
        #f.write(request.environ.get('REMOTE_USER'))
    #    f1.write('hello')
    #print (content)
    #return request.environ.get('REMOTE_USER')+request.form['username']+request.environ.get('REMOTE_USER')
    return "hello"

@app.route('/signin', methods=['GET'])
def signin_form():
    with open('1.txt',"r") as f:
        content=f.readlines()
    a='I am chinese'    
    return render_template('item.html',a=a,content=content)


@app.route('/history')
def history():
    with open('1.txt',"r") as f:
        content0=f.readlines()
    a='I am chinese'    
    return render_template('history.html',a=a,content=content0)


@app.route('/signin', methods=['POST'])
def signin():
    #g.msgbox(request.form['username'])
    with open('1.txt',"a") as f:
        #f.write(request.environ.get('REMOTE_USER'))
        f.write(request.environ.get('REMOTE_USER')[9:]+':'+request.form['username']+'\n')
    #with open('1.txt',"r") as f:
    #    content1=f.readlines()

    return render_template('item.html')
@app.route('/signin', methods=['POST'])
def signin1(methods=['POST']):
    with open('1.txt',"a") as f:
        f.write(request.form['username']+'\n')

    return render_template('item.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5002,debug=True)
