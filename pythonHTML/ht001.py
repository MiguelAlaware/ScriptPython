
from flask import Flask, render_template, request, escape
from vsearch import acheletras
app = Flask(__name__)

def log_request (req : 'flask_request', res : str) -> None:
    with open('vsearch.log', 'a') as log:
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|' )
@app.route('/search4', methods=['POST'])

def pesquise() -> 'html':
    frase = request.form['phrase']
    letras = request.form['letters']
    title = 'here are your results:'
    results = str(acheletras(frase, letras))
    log_request(request, results)
    return render_template('results.html',
    the_phrase = frase,
    the_letters = letras,
    the_title = title,
    the_results = results,)

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
     the_title='Bem vindo ao acheletras na web!')

@app.route('/viewlog')
def view_the_log() -> str:
    with open('vsearch.log') as log:
        contents = log.read()
    return escape(contents)


if __name__ =='__main__':
    app.run(debug=True)