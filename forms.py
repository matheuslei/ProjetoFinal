from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    nome_completo = StringField('Nome Completo', validators=[DataRequired()])
    rua = StringField('Rua', validators=[DataRequired()])
    numero = StringField('Número', validators=[DataRequired()])
    complemento = StringField('Complemento')
    bairro = StringField('Bairro', validators=[DataRequired()])
    cidade = StringField('Cidade', validators=[DataRequired()])
    estado = StringField('Estado', validators=[DataRequired(), Length(min=2, max=2)])
    cep = StringField('CEP', validators=[DataRequired()])
    telefone = StringField('Telefone', validators=[DataRequired()])
    cpf = StringField('CPF', validators=[DataRequired()])
    submit = SubmitField('Cadastrar')
