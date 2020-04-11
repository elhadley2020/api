from flask import Flask, request
app = Flask(__name__)

'''

    Methods for database setup

'''


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Contact, User

engine = create_engine('sqlite:///contact-collection.db?checksame_thread=False')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


'''
    
    Methods for updating the model and database

 '''

# Methods for Contacts

from flask import jsonify

def get_contacts():
    contacts = session.query(Contact).all()
    return jsonify(contacts=[c.serialize for c in contacts])

def get_contact(contact_id):
    contacts = session.query(Contact).filter_by(id=contact_id).one()
    return jsonify(contacts=contacts.serialize)

def post_contact(first_name, last_name, phone, email, street, city, state, zip):
    post_contact = Contact(
        first_name = first_name,
        last_name = last_name,
        phone = phone,
        email = email,
        street = street,
        city = city,   
        state = state,
        zip = zip
    ) 
    session.add(post_contact)
    session.commit()
    return jsonify(Contact=post_contact.serialize)

def put_contact(contact_id, first_name, last_name, phone, email, street, city, state, zip):
    put_contact = session.query(Contact).filter_by(id=contact_id).one()
    if first_name:
        put_contact.first_name = first_name
    if last_name:
        put_contact.last_name = last_name
    if phone:
        put_contact.phone = phone
    if email:
        put_contact.email = email
    if street:
        put_contact.street = street
    if city:
        put_contact.city = city
    if state:
        put_contact.state = state
    if zip:
        put_contact.zip = zip
    
    session.add(put_contact)
    session.commit()
    return jsonify(Contact=put_contact.serialize)

def delete_contact(contact_id):
    delete_contact = session.query(Contact).filter_by(id=contact_id).one()
    session.delete(delete_contact)
    session.commit()
    
    contacts = session.query(Contact).all()
    return jsonify(contacts=[c.serialize for c in contacts])


# Methods for Users
def post_user(username,password,email):
    post_user = User(
        username = username,
        password = password,
        email = email
    )

    session.add(post_user)
    session.commit()
    return jsonify(User=post_user.serialize)

'''

    Methods for routes

'''

### Routes for contact

@app.route('/contacts')
def get_request_contacts():
    if request.method == "GET":
        return get_contacts()

@app.route('/contact', methods = ['POST'])
def post_request_contact():
    if request.method == "POST":
        first_name = request.args.get('first_name', '')
        last_name = request.args.get('last_name', '')
        phone = request.args.get('phone', '')
        email = request.args.get('email', '')
        street = request.args.get('street', '')
        city = request.args.get('city', '')
        state = request.args.get('state', '')
        zip = request.args.get('zip', '')
        return post_contact(first_name, last_name, phone, email, street, city, state, zip)

@app.route('/contact/<int:id>', methods = ['GET'])
def get_request_contact(id):
    if request.method == "GET":
        return get_contact(id)

@app.route('/contact/<int:id>' , methods = ['DELETE'])
def delete_request_contact(id):
    if request.method == "DELETE":
        return delete_contact(id)

@app.route('/contact/<int:id>', methods = ['PUT'])
def put_request_contact(id):
    if request.method == "PUT":
        first_name = request.args.get('first_name', '')
        last_name = request.args.get('last_name', '')
        phone = request.args.get('phone', '')
        email = request.args.get('email', '')
        street = request.args.get('street', '')
        city = request.args.get('city', '')
        state = request.args.get('state', '')
        zip = request.args.get('zip', '')
        return put_contact(id, first_name, last_name, phone, email, street, city, state, zip)

# Routes for Users
@app.route('/users', methods = ['GET'])
def get_request_users():
    if request.method == "GET":
        users = session.query(User).all()
        return jsonify(users=[u.serialize for u in users])

@app.route('/user', methods = ['POST'])
def post_request_user():
    if request.method == 'POST':
        username = request.args.get('username', '')
        password = request.args.get('password', '')
        email = request.args.get('email', '')
        return post_user(username,password,email)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=4996)