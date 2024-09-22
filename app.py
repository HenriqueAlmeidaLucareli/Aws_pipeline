from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<center><h1><font color=red>Oi, nova atualização via pipeline, ajuste feito, ajuste feito para a aws e o  render ao mesmo tempo  mais um ajuste 📈📈📈📈📈📈</font></h1></center> '

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)