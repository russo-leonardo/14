from flask import Flask, render_template, request, redirect, url_for #imparare memoria

lista = []

app = Flask(__name__)#imparare a memoria, è il nome dell'app Flask che dò io.

x = 'ciao'

@app.route('/') #visitiamo l'url (`/`), la funzione home() viene eseguita.  #imparare a memoria
def home():#definisco funzione home
    return render_template("index.html", paperino = x, lista=lista) 


@app.route('/aggiungi', methods=['POST'])
def aggiungi():
    #ottiene elemento dal form
    elemento = request.form['elemento']
    #aggiunge alla lista
    if elemento:
        lista.append(elemento)
    return redirect(url_for('home'))

   
@app.route('/rimuovi/<int:indice>', methods=['POST'])
def rimuovi(indice):
    if 0 <= indice < len(lista):
       lista.pop(indice)
    return redirect(url_for('home'))

@app.route('/elimina tutto/<int:indice>',methods=['POST'])
def elimina_tutto():
        lista.clear()
        return redirect(url_for('home'))













if __name__ == '__main__':#imparare a memoria
   app.run(debug=True)