from flask import Flask, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import LoginForm, RegistrationForm
import os

app = Flask(__name__)
app.config.from_object('config.Config')
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    nome_completo = db.Column(db.String(100), nullable=False)
    rua = db.Column(db.String(100), nullable=False)
    numero = db.Column(db.String(10), nullable=False)
    complemento = db.Column(db.String(100), nullable=True)
    bairro = db.Column(db.String(100), nullable=False)
    cidade = db.Column(db.String(100), nullable=False)
    estado = db.Column(db.String(2), nullable=False)
    cep = db.Column(db.String(9), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    cpf = db.Column(db.String(11), nullable=False)

    def __repr__(self):
        return f"User('{self.email}', '{self.nome_completo}')"

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login solicitado para o email {form.email.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('login.html', form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, password=form.password.data, 
                    nome_completo=form.nome_completo.data, rua=form.rua.data, 
                    numero=form.numero.data, complemento=form.complemento.data, 
                    bairro=form.bairro.data, cidade=form.cidade.data, 
                    estado=form.estado.data, cep=form.cep.data, 
                    telefone=form.telefone.data, cpf=form.cpf.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Conta criada para {form.email.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

if __name__ == '__main__':
    if not os.path.exists('site.db'):
        with app.app_context():
            db.create_all()
    app.run(debug=True)
