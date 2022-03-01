import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# Reference:
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/
# https://docs.sqlalchemy.org/en/14/core/metadata.html#sqlalchemy.schema.Column
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/#many-to-many-relationships

class Teacher(db.Model):
    __tablename__ = 'teachers'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    gradelevel = db.Column(db.Integer, nullable=False)
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    years_teaching = db.Column(db.Integer, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'gradelevel': self.gradelevel,
            'years_teaching': self.years_teaching
        }


class Standard (db.Model):
    __tablename__ = 'standards'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    domain = db.Column(db.String(128), nullable=False)
    gradelevel = db.Column(db.Integer, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'domain': self.domain,
            'gradelevel': self.gradelevel
        }


tests_table = db.Table(
    'scores',
    db.Column(
        'teacher_id', db.Integer,
        db.ForeignKey('teachers.id'),
        primary_key=True
    ),
    db.Column(
        'student_id', db.Integer,
        db.ForeignKey('students.id'),
        primary_key=True
    ),
    db.Column(
        'standard_id', db.Integer,
        db.ForeignKey('standards.id'),
        primary_key=True
    ),
    db.Column(
        'score_id', db.Integer,
        nullable=False
    )
)


class Score (db.Model):
    __tablename__ = 'test_scores'
    id = id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    score = db.Column(db.Integer, nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey(
        'students.id'), nullable=False)
    standard_id = db.Column(db.Integer, db.ForeignKey(
        'standards.id'), nullable=False)

    tests = db.relationship(
        'Student', secondary=tests_table,
        lazy='subquery',
        backref=db.backref('scored_tests', lazy=True)
    )

    def serialize(self):
        return {
            'id': self.id,
            'student_id': self.student_id,
            'standard_id': self.standard_id,
            'score': self.score
        }


class Student (db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    gradelevel = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(128), nullable=False)
    iep = db.Column(db.Boolean, nullable=False)
    tag = db.Column(db.Boolean, nullable=False)
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)

    teacher_id = db.Column(db.Integer, db.ForeignKey(
        'teachers.id'), nullable=False)

    tests = db.relationship('Score', backref='student', cascade="all,delete")

    def serialize(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'gradelevel': self.gradelevel,
            'gender': self.gender,
            'iep': self.iep,
            'tag': self.tag
        }
