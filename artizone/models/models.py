import mysql.connector


class ConnectDB:
    """
        Classe pour se connecter à la base de données
    """
    def db_connect(self):
        try:
            ldatabase = mysql.connector.connect(host='localhost', user = 'root', 
            	password = '', database = 'artizone')
            return ldatabase

        except:
            print("Erreur sur la connexion à la base de données...!")


class InsererInformationArtisant(ConnectDB):
    def fill_identities(self, donnees):
        try:
            database = ConnectDB.db_connect()
            requete = database.cursor()
            requete.execute("""INSERT INTO identities(names, last_names, pseudo, 
            	phone1, phone2, addresses, email, passwords, id_categorie)
                VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)""", donnees)
            database.commit()

        except:
            database.rollback()
            print("Erreur sur l'insertion dans la table 'identities'...!")

        database.close()


    def fill_formations(self, donnees):
        try:
            database = ConnectDB.db_connect()
            requete = database.cursor()
            requete.execute("""INSERT  INTO formations(places, dates, 
            	objects, descriptions, id_identity)
                VALUES(%s, %s, %s, %s, %s)""", donnees)
            database.commit()

        except:
            database.rollback()
            print("Erreur sur l'insertion dans la table 'formations'...!")

        database.close()


    def fill_experiences(self, donnees):
        try:
            database = ConnectDB.db_connect()
            requete = database.cursor()
            requete.execute("""INSERT INTO experiences(experience_name, 
            	dates, descriptions, id_identity)
                VALUES(%s, %s, %s, %s)""", donnees)
            database.commit()

        except:
            database.rollback()
            print("Erreur sur l'insertion dans la table 'experiences'...!")

        database.close()


class InsertFiles(ConnectDB):
    def fill_link_file(self, donnees):
        try:
            database = ConnectDB.db_connect()
            requete = database.cursor()
            requete.execute("""INSERT INTO files(links, comments, dates, id_identity)
                VALUES(%s, %s, NOW(), %s)""", donnees)
            database.commit()

        except:
            database.rollback()
            print("Erreur sur l'insertion dans la table 'files'...!")

        database.close()


class InsertMessages(ConnectDB):
    def fill_messages(self, donnees):
        try:
            database = ConnectDB.db_connect()
            requete = database.cursor()
            requete.execute("""INSERT INTO messengers(messages, dates, id_identity)
                VALUES(%s, NOW(), %s)""", donnees)
            database.commit()

        except:
            database.rollback()
            print("Erreur sur l'insertion dans la table 'messengers'...!")

        database.close()


class Login(ConnectDB):
    def get_info_artisant(self, donnees):
        try:
            database = ConnectDB.db_connect()
            reponse = database.cursor()
            reponse.execute("""SELECT True, id FROM identities 
                WHERE (email = %s OR phone1 = %s) AND passwords = SHA2(%s, 256)""", donnees)
            data = reponse.fecthone()
            return list(data)

        except:
            print("Nous n'avons pas pu obtenir les donnees d'authentification...!")

        database.close()


class UpdateIdentities(ConnectDB):
    def update_informations(self, donnees):
        try:
            database = ConnectDB.db_connect()
            requete = database.cursor()
            requete.execute("""UPDATE identities SET pseudo = %s, linkedin = %s,
                facebook = %s, work = %s, work_description = %s WHERE id = %s""", donnees)
            requete.commit()

        except:
            database.rollback()
            print("Erreur sur la mise à jours des informations dans la table 'identities'...!")

        database.close()


    def update_link_profile(self, donnees):
        try:
            database = ConnectDB.db_connect()
            requete = database.cursor()
            requete.execute("""UPDATE identities SET profile_link = %s 
                WHERE id = %s""", donnees)
            requete.commit()

        except:
            database.rollback()
            print("Erreur sur la mise à jours du profile_link dans la table 'identities'...!")

        database.close()


class GetInformationsArtisant(ConnectDB):
    def get_identities(self, donnees):
        try:
            database = ConnectDB.db_connect()
            reponse = database.cursor()
            reponse.execute("""SELECT names, last_names, pseudo, phone1,phone2, addresses, email, 
                linkedin, facebook, work, work_description, profile_link, id_categorie 
                FROM identities WHERE id = %s""", donnees)
            data = reponse.fecthall()
            return list(data)

        except:
            print("Erreur sur le chargement des donnees de l'artisant...!")

        database.close()


    def get_formations(self, donnees):
        try:
            database = ConnectDB.db_connect()
            reponse = database.cursor()
            reponse.execute("""SELECT f.places, f.dates, f.objects, f.descriptions 
                FROM formations f JOIN identities i ON f.id_identity = i.id 
                WHERE i.id = %s""", donnees)
            data = reponse.fecthall()
            return list(data)

        except:
            print("Erreur sur le chargement des donnees dans la table 'formations'...!")

        database.close()


    def get_experiences(self, donnees):
        try:
            database = ConnectDB.db_connect()
            reponse = database.cursor()
            reponse.execute("""SELECT e.experience_name, e.dates, e.descriptions
                FROM experiences e JOIN identities i ON e.id_identity = i.id
                WHERE i.id = %s""", donnees)
            data = reponse.fecthall()
            return list(data)

        except:
            print("Erreur sur le chargement des donnees dans la table 'experiences'...!")

        database.close()


    def get_messengers(self, donnees):
        try:
            database = ConnectDB.db_connect()
            reponse = database.cursor()
            reponse.execute("""SELECT m.messages, m.dates 
                FROM messengers m JOIN identities i ON m.id_identity = i.id
                WHERE i.id = %s""", donnees)
            data = reponse.fecthall()
            return list(data)

        except:
            print("Erreur sur le chargement des donnees dans la table 'messengers'...!")

        database.close()


    def get__files(self, donnees):
        try:
            database = ConnectDB.db_connect()
            reponse = database.cursor()
            reponse.execute("""SELECT 
                FROM files f JOIN identities i ON f.id_identities = i.id
                WHERE i.id = %s""", donnees)
            data = reponse.fecthall()
            return list(data)

        except:
            print("Erreur sur le chargement des donnees dans la table 'files'...!")

        database.close()


class UpdatePasswords(ConnectDB):
    def verify_email(self, donnees):
        try:
            database = ConnectDB.db_connect()
            reponse = database.cursor()
            reponse.execute("""SELECT True, id, names FROM identities
                WHERE email = %s""", donnees)
            data = reponse.fecthall()
            return list(data)

        except:
            print("Erreur sur la vérification de l'adresse email...!")

        database.close()


    def update_forgot_password(self, donnees):
        try:
            database = ConnectDB.db_connect()
            requete = database.cursor()
            requete.execute("""UPDATE identities 
                SET passwords = SH2('mybestfriends', 256)
                WHERE id = %s""", donnees)
            database.commit()

        except:
            database.rollback()
            print("Erreur sur la mise à jours du mot de passe oublié...!")

        database.close()


    def change_password(self, donnees):
        try:
            database = ConnectDB.db_connect()
            requete = database.cursor()
            requete.execute("""UPDATE identities
                SET passwords = SHA2(%s, 256)
                WHERE id = %s""", donnees)
            database.commit()

        except:
            database.rollback()
            print("Erreur sur la mise à jours du mot de passe...!")
