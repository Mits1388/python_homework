import csv

import models
from models import OrderItems, Orders, Products, Statuses, Users, Categories
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine, select

# file = 'bhcorp.csv'


engine = create_engine('postgresql://mits16:1616@localhost:5432/bhcorp')
session = sessionmaker(bind=engine)

with session() as session:
    with open('bhcorp.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            print(row)
            db_record = models.Base(
                id=[row],
                name=[row],
                user_id=[row],
                status_id=[row],
                email=[row],
                order_id=[row],
                product_id=[row],
                title=[row],
                description=[row],
                category_id=[row],
            )
            # print(row['name'])
            session.add(db_record)
        session.commit()
    session.close()