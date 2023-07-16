from werkzeug.security import check_password_hash, generate_password_hash
from Models import *
from database import db


#Funcion para agregar gafetes


def agregarGafetes(inicio, fin, tipo):
    if inicio > fin or inicio == fin :
        print("Error, el inicio no puede ser mas grande o igual que el fin")
    elif len(tipo) < 3:
        print("Introduzca un tipo valido")
    else:
        nuevo_gafete = Gafetes(tipo="prueba", numero="1", prestado="0")
        db.session.add(nuevo_gafete)
        db.session.commit()

        
#for i in range(fin + 1 - inicio):
#objGafete = Gafetes.query.filter_by()
#nuevoGafete = Gafetes(tipo=tipo, numero=inicio+1)
#gafete = Gafetes.query.filter_by(numero=inicio+1 , tipo=tipo)
#db.session.add(nuevoGafete)
#db.session.commit()

#agregarGafetes(1, 5, "staff")






