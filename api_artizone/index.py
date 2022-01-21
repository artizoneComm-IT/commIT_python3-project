"""Script to run flask webserver for routing views."""
from flask import Flask, request
from flask_cors import CORS
from .models.models import *


app = Flask(__name__)
# cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
CORS(app)

@app.route('/api/login')
def authentifier():
    """S'authentifier pour l'artisant."""
    demande = Login()
    if(request.form['identifiant'] != '' and request.form['password'] != ''):
        donnees = (request.form['identifiant'], request.form['identifiant'], request.form['identifiant'], request.form['password'])
        resultats = authentifier(donnees)
    else:
        resultats = {'message': 'Les identifiants ne sont pas vides ...!'}
    return resultats, 200, {'Access-Control-Allow-Origin': '*', 'content-type':'application/json'}


#  ************************ PRENDRE DES DONNEES DANS LA BASE  DE DONNÉES ************************
@app.route('/api/get/identities/<identifiant>')
def obtenir_identities(identifiant):
    """Route to go to get identities of personnes"""
    demande = Identities()
    donnees = (identifiant, identifiant)
    return demande.getIdentities(donnees), 200, {'Access-Control-Allow-Origin': '*', 'content-type':'application/json'}
    

@app.route('/api/get/formations/<identifiant>')
def obtenir_formations(identifiant):
    demande = Formations()
    donnees = (identifiant, identifiant)
    return demande.getFormations(donnees), 200, {'Access-Control-Allow-Origin': '*', 'content-type':'application/json'}


@app.route('/api/get/experiences/<identifiant>')
def obtenir_experiences(identifiant):
    demande = Experiences()
    donnees = (identifiant, identifiant)
    return demande.getExperiences(donnees), 200, {'Access-Control-Allow-Origin': '*', 'content-type':'application/json'}


# *********************** INSERTION DANS LA BASE DE DONNÉES **************************
@app.route('/api/add/identities')
def inserer_personnes():
    demande = Identities()
    donnees = (request.form['nom'], request.form['prenoms'], request.form['pseudo'], request.form['birthday'],
     request.form['phone1'], request.form['phone2'], request.form['adresse'], request.form['email'],
     request.form['password'], request.form['id_categorie'])
    demande.addPersons(donnees)


@app.route('/api/add/formations')
def inserer_formations():
    demande = Formations()
    donnees = (request.form['places'], request.form['dates'], request.form['objects'],
     request.form['descriptions'], request.form['id_identity'])
    demande.addFormations(donnees)


@app.route('/api/add/experiences')
def inserer_experiences():
    demande = Experiences()
    donnees = (request.form['experience'], request.form['dates'], request.form['descriptions'], request.form['id_identity'])
    demande.addExperiences(donnees)


# ************************ For making update in database **********************
@app.route('api/update/identities')
def update_identities():
    demande = Identities()
    donnees = (request.form['pseudo'], request.form['phone1'], request.form['phone2'],
     request.form['adresse'], request.form['identifiant'], request.form['identifiant'])
    demande.updatePersons(donnees)


@app.route('/api/update/formations')
def update_formations():
    demande = Formations()
    donnees = (request.form['places'], request.form['dates'], request.form['objects'],
     request.form['descriptions'], request.form['identifiant'])
    demande.updateFormations(donnees)


@app.route('/api/update/experiences')
def update_experiences():
    demande = Experiences()
    donnees = (request.form['experiences'], request.form['dates'], request.form['descriptions'], request.form['identifiant'])
    demande.updateExperiences(donnees)


# ****************************** For deleting some informations **************************
@app.route('/api/delete/formations')
def delete_formations():
    demande = Formations()
    donnees = (request.form['identifiant'], )
    demande.deleteFormations(donnees)


@app.route('/api/delete/experiences')
def delete_experiences():
    demande = Experiences()
    donnees = (request.form['identifiant'], )
    demande.deleteExperiences(donnees)


if __name__ == '__main__':
    app.run()
