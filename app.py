from flask import Flask
from flask_restful import Api, Resource, abort, reqparse, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contact.db'
db = SQLAlchemy(app)


class ContactDb(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(30),unique=True, nullable = False )
    phone_no = db.Column(db.Integer, unique = True, nullable = False)
    email = db.Column(db.String(50))

    def __repr__(self):
        return  f"name = {name}, phone_no = {phone_no}, email = {email}"

contact_args = reqparse.RequestParser()
contact_args.add_argument('name', type =str, help = 'Input right name of contact', required = True)
contact_args.add_argument('phone_no', type =int, help = 'Input phone No.', required = True)
contact_args.add_argument('email', type =str, help = 'Input the email')

contact_field = {
    'id':fields.Integer,
    'name' : fields.String,
    'phone_no' : fields.Integer,
    'email' : fields.String

}

class contact(Resource):
    @marshal_with(contact_field)
    def post(self):
        #if name:
        #    return('Name already taken')
        args = contact_args.parse_args()
        contact = ContactDb(name = args['name'], phone_no = args['phone_no'], email = args['email'])
        db.session.add(contact)
        db.session.commit()
        return contact, 201
    @marshal_with(contact_field)
    def get(self, name):
        result = ContactDb.query.filter_by(name = name)
        if not result:
            abort(404, 'contact not found')
        return result
    @marshal_with(contact_field)   
    def patch(self):
        args = contact_args.parse_args()
        result = ContactDb.query.filter_by(name = name)
        if args['name']:
            result.name = args['name']
        if args['phone_no']:
            result.phone_no = args['phone_no']
        if args['email']:
            result.email = args['email']
        return result
        
        
    def delete(self, name):
        result = ContactDb.query.filter_by(name = name)
        if not result:
            abort(404, 'Contact does not exist')
        del result
        return '', 201
api.add_resource(contact,'/')


if __name__ == '__main__':
    app.run(debug=True)