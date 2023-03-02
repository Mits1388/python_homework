import csv
from database import SessionLocal, engine
import models

db = SessionLocal()

models.Base.metadata.create_all(bind=engine)

file = open("bhcorp.csv", "r", encoding='utf-8')
print(file.read())
db.close()
