import mysql.connector
import json


# ************************* CONNEXION À LA BASE DE DONNÉES ************************
class Database: 

    def db_connect(self):
        try:
            return mysql.connector.connect(host = 'localhost', user = 'jitiy',
             password = '01Lah_tr*@ro0t/*', database = 'artizone')
        
        except:
            print(json.dumps({'message': "Nous n'avons pas pu connecter à la base de données !"}, indent=3))


# ************************** CRÉER DU JSON **********************
class CreateJson:
    def sendJson(self, reponses, nomColonne):
        resultats = {} 
        resultat = {}
        for reponse in reponses:
            for ligne, donnee in zip(nomColonne, reponse):
                resultat[ligne] = donnee
            resultats[reponses.index(reponse)] = resultat
        return resultats


# ************************ DEMANDE ET MODIFICATION DANS LA TABLE IDENTITIES *************************
class Identities(Database, CreateJson):
    def __init__(self):
        self.identities = 'artizone'


# ******************** For geting all data used *****************
    def getIdentities(self, donnees):
        try:
            database = Database.db_connect(self)
            demande = database.cursor()
            demande.execute("""
                SELECT id, names, last_names, birthday, pseudo, phone1, phone2, addresses, email, 
                    linkedin, facebook, work, work_description, profile_link, id_categorie 
                    FROM identities WHERE email = %s OR id = %s
                """, donnees)
            reponses = demande.fetchall()
            nomColonne = ['id', 'nom', 'prenoms', 'birthday', 'pseudo', 'phone1', 'phone2', 'adresse',
                'email', 'linkedin', 'facebook', 'work', 'work_description', 'profile_link', 'id_categorie']
            return CreateJson.sendJson(self, reponses, nomColonne)

        except:
            print(json.dumps({'message': "Erreur sur le chargement des donnees de l'artisant...!"}, indent=3))

        database.close()

    
# ************************* For adding personnes ************************
    def addPersons(self, donnees):
        try:
            database = Database.db_connect(self)
            demande = database.cursor()
            demande.execute("""
                INSERT INTO identities(names, last_names, pseudo, birthday,
            	phone1, phone2, addresses, email, passwords, id_categorie)
                VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, donnees)
            database.commit()

        except:
            database.rollback()
            print(json.dumps({'message': "Nous n'avons pas pu ajouter de personnes ...!"}, indent=3))
        
        database.close()


# ********************** For updating data's persons ********************
    def updatePersons(self, donnees):
        try:
            database = Database.db_connect(self)
            demande = database.cursor()
            demande.execute("""
                UPDATE identities SET pseudo = %s, phone1 = %s, phone2 = %s, addresses = %s
                WHERE id = %s OR email = %s
            """, donnees)
            database.commit()
        
        except:
            database.rollback()
            print(json.dumps({'message': "Nous n'avons pas pu faire de la mise à jour ...!"}, indent=3))

        database.close()


# ****************************** DEMANDE ET MODIFICATION DANS LA TABLE FORMATIONS ****************************
class Formations(Database, CreateJson):
    def __init__(self):
        self.formations = 'artizone'
    

    def getFormations(self, donnees):
        try:
            database = Database.db_connect(self)
            demande = database.cursor()
            demande.execute("""
                SELECT f.id, f.places, f.dates, f.objects, f.descriptions 
                FROM formations f 
                JOIN identities i ON f.id_identity = i.id
                WHERE i.id = %s OR i.email = %s
            """, donnees)
            reponses = demande.fetchall()
            nomColonne = ['id', 'places', 'dates', 'objects', 'descriptions']
            return CreateJson.sendJson(self, reponses, nomColonne)
        
        except:
            print(json.dumps({'message': "Nous n'avons pas pu prendre des données formations ... !"}, indent=3))
    
        database.close()


    def addFormations(self, donnees):
        try:
            database = Database.db_connect(self)
            demande = database.cursor()
            demande.execute("""
                INSERT  INTO formations(places, dates, 
                    objects, descriptions, id_identity)
                    VALUES(%s, %s, %s, %s, %s)
            """, donnees)
            database.commit()

        except:
            database.rollback()
            print(json.dumps({'message': "Nous n'avons pas pu ajouter les formations ...!"}, indent=3))
        
        database.close()

    
    def updateFormations(self, donnees):
        try:
            database = Database.db_connect(self)
            demande = database.cursor()
            demande.execute("""
                UPDATE formations SET places = %s, dates = %s, objects = %s, descriptions = %s
                WHERE id = %s
            """, donnees)
            database.commit()
        
        except:
            print(json.dumps({'message': "Nous n'avons pas pu mettre à jours les formations ...!"}, indent=3))

        database.close()


# ********************* For deleting formations ********************
    def deleteFormations(self, donnees):
        try:
            database = Database.db_connect(self)
            demande = database.cursor()
            demande.execute("""
                DELETE FROM formations WHERE id = %s
            """, donnees)
            database.commit()
        
        except:
            database.rollback()
            print(json.dumps({'message': "Nous n'avons pas pu supprimer une formation ...!"}, indent=3))

        database.close()

    
class Experiences(Database, CreateJson):
    def __init__(self):
        self.experience = 'artizone'

    
    def getExperiences(self, donnees):
        try:
            database = Database.db_connect(self)
            demande = database.cursor()
            demande.execute("""
                SELECT e.id, e.experience_name, e.dates, e.descriptions
                FROM experiences e 
                JOIN identities i ON e.id_identity = i.id
                WHERE i.id = %s OR i.email = %s
            """, donnees)
            reponses = demande.fetchall()
            nomColonne = ['id', 'experience_name', 'dates', 'descriptions']
            return CreateJson.sendJson(self, reponses, nomColonne)
        
        except:
            print(json.dumps({'message': "Nous n'avons pas pu prendre des experiences ...!"}, indent=3))

        database.close()

    
    def addExperiences(self, donnees):
        try:
            database = Database.db_connect(self)
            demande = database.cursor()
            demande.execute("""
                INSERT INTO experiences(experience_name, 
            	dates, descriptions, id_identity)
                VALUES(%s, %s, %s, %s)
            """, donnees)
            database.commit()

        except:
            database.rollback()
            print(json.dumps({'message': "Nous n'avons pas pu ajouter des experiences ...!"}, indent=3))

        database.close()


    def updateExperiences(self, donnees):
        try:
            database = Database.db_connect(self)
            demande = database.cursor()
            demande.execute("""
                UPDATE experiences SET experience_name = %s, dates = %s, descriptions = %s
                WHERE id = %s
            """, donnees)
            database.commit()
        
        except:
            database.rollback()
            print(json.dumps({'message': "Nous n'avons pas pu mettre à jours une expérience ...!"}, indent=3))

        database.close()
    

    def deleteExperiences(self, donnees):
        try:
            database = Database.db_connect(self)
            demande = database.cursor()
            demande.execute("""
                DELETE FROM experiences WHERE id = %s
            """, donnees)
            database.commit()
        
        except:
            database.rollback()
            print(json.dumps({'message': "Nous n'avons pas pu supprimer une experience ...!"}, indent=3))
        
        database.close()


# ************************* FOR LOGGING IN AS ADMIN **************************
class Login(Database, CreateJson):
    def __init__(self):
        self.login = 'artizone'


    def authentifier(self, donnees):
        try:
            database = Database.db_connect(self, donnees)
            demande = database.cursor()
            demande.execute("""
                SELECT True, id, email
                FROM identities
                WHERE (email = %s OR phone1 = %s OR phone2 = %s) AND passwords = %s
            """, donnees)
            reponses = demande.fetchall()
            nomColonne = ['TRUE', 'id', 'email']
            return CreateJson.sendJson(self, reponses, nomColonne)

        except:
            print(json.dumps({'message': "Nous n'avons pas pu créer de la connexion ...!"}, indent=3))
            
        database.close()
