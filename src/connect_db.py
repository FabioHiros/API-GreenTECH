from sqlalchemy import create_engine

def connect():
    dbsensores = create_engine('mysql+mysqlconnector://estufa:estufa@localhost:3306/dadosensores')
    print("Connected to MySQL database successfully.")
    return dbsensores