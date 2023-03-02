from flask import Flask
from vsearch import acheletras
app = Flask(__name__)

@app.route('/')
def ola() -> str:
    return 'Olá mundo do Flask!'

@app.route('/achevogais')
def pesquise() -> str:
    return(str(acheletras('life, the universe, and evrything', 'eiru,!')))

app.run()