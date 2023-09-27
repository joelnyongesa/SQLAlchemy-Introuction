from faker import Faker
import random
from main import Student
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine


Base = declarative_base()
fake = Faker()
engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

students = [
    Student(
        name = fake.name(),
        index = random.randint(900, 1900)
    )
    for i in range(20)
]

session.bulk_save_objects(students)
session.commit()