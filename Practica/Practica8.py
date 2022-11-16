from flask import Flask, render_template


app = Flask(__name__)

libros = {
    1: {"Titulo": "Emma", "Autor": "Jane Austen", "Editorial": "Paidos"},
    2: {"Titulo": "1984", "Autor": "George Orwell", "Editorial": "Planeta"},
}

audio_libros = {
    1: {"Titulo": "Los Miserables", "Autor": "Victor Hugo", "Editorial": "Planeta"},
    2: {"Titulo": "Un mundo feliz", "Autor": "Aldous Huxley", "Editorial": "Alfaguara"},
}

revistas = {
    1: {"Titulo": "Vouge", "Editorial": "Anagrama"},
    2: {"Titulo": "Forbes", "Editorial": "Atlas"},
}

@app.get("/")
def home():
    return render_template("home.html")


@app.get("/libros/")
def get_libros():
    return render_template("libros.html", libros=libros.items())

@app.get("/audio_libros/")
def get_audio_libros():
    return render_template("audio_libros.html", audio_libros=audio_libros.items())

@app.get("/revistas/")
def get_revistas():
    return render_template("revistas.html", revistas=revistas.items())