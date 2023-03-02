import csv
import models
from database import SessionLocal, engine

db = SessionLocal()

models.Base.metadata.create_all(bind=engine)

with open("bhcorp.csv", "r") as f:
    csv_reader = csv.DictReader(f)

    for row in csv_reader:
        db_record = models.Record(
            id=row["id"],
            name=row["name"],
            user_id=row["user_id"],
            status_id=row["status_id"],
            email=row["email"],
            order_id=row["order_id"],
            product_id=row["product_id"],
            title=row["title"],
            description=row["description"],
            category_id=row["description"],
        )
        db.add(db_record)

    db.commit()

db.close()
