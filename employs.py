from intialsettings import *
import json

db = SQLAlchemy(app)

class employtable(db.Model):
    __tablename__ = 'employtable'  
    id = db.Column(db.Integer, primary_key=True) 
    empid = db.Column(db.Integer, nullable=False)
    empname = db.Column(db.String(80), nullable=False)
    yearofjoining = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(80), nullable=False)
    position = db.Column(db.String(80), nullable=False)

    def json(self):
        return {'id': self.id, 'empid': self.empid,'empname':self.empname,
                'yearofjoining': self.yearofjoining, 'gender': self.gender, 'position':self.position}
        

    def add_employ(_empid, _empname , _yearofjoining, _gender, _position):
        new_employ = employtable(empid=_empid, empname = _empname,yearofjoining=_yearofjoining, gender=_gender, position= _position)
        db.session.add(new_employ)  
        db.session.commit() 

    def get_all_employs():
        return [employtable.json(emp) for emp in employtable.query.all()]

    def get_employbyid(_id):
        return [employtable.json(employtable.query.filter_by(id=_id).first())]

    def get_employbyempid(_empid):
        return [employtable.json(employtable.query.filter_by(empid=_empid).first())]

    def get_employbyyearofjoining(_yearofjoining):
        return [employtable.json(emp) for emp in employtable.query.filter_by(yearofjoining=_yearofjoining)]
       

    def update_employ(_id, _empid, _empname, _yearofjoining, _gender, _position):
        emp_to_update = employtable.query.filter_by(id=_id).first()
        emp_to_update.empid = _empid
        emp_to_update.empname = _empname
        emp_to_update.yearofjoining = _yearofjoining
        emp_to_update.gender = _gender
        emp_to_update.position = _position
        db.session.commit()

    def delete_employ(_id):
        employtable.query.filter_by(id=_id).delete()
        db.session.commit()  
