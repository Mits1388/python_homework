from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('postgresql://mits16:1616@localhost:5432/bhcorp.csv')
SessionLocal = sessionmaker(bind=engine)

