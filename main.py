#!/usr/bin/env python3



from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    # table columns
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    index = Column(Integer())

    def __repr__(self):
        return f"Student {self.name}, "\
            + f"Index {self.index}"

if __name__ == "__main__":
    engine = create_engine('sqlite:///database.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # max = Student(
    #     name = "Max",
    #     index = 10
    # )
    # medrine = Student(
    #     name = "Medrine",
    #     index = 3
    # )
    # session.bulk_save_objects([max, medrine])
    # session.commit()

    students = session.query(Student).all()
    names = [name for name in session.query(Student.name)]
    # print(names)

    # Deleting data
    studentID = session.query(Student).filter(Student.name.like("%Max%")).first()
    session.delete(studentID)
    session.commit()