from mongoengine import *
from settings import DBNAME
connect(DBNAME)

class EmployeDetails(EmbeddedDocument):

    employee_designation = StringField()
    employee_phone = StringField()
    employee_name = StringField()
    employee_link = StringField()
    employee_mail = StringField()

class Discoverorgdata(Document):
    website = StringField(max_length=120, required=True)
    description = StringField(max_length=1500, required=True)
    url = StringField(max_length=120, required=True)
    company_name = StringField(max_length=100)
    address  = StringField(max_length=100)
    phone = StringField(max_length=15)
    company_details = DictField()
    employee_details =ListField(EmbeddedDocumentField(EmployeDetails))

class Companylist(Document):
    count = IntField()
    text = StringField(max_length=100)






