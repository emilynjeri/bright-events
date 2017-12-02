from app import app
from flask import request, jsonify
from models import User, Events

user = User()
event = Events()

@app.route('/')
def index():
    '''Index page endpoint'''
    return("My API Index")

@app.route('/api/v1/auth/register', methods=['POST'])
def register():
    '''User register API endpoint'''
    data = request.get_json()
    response = user.register(data.firstname, data.lastname, data.email, data.password)
    return jsonify({'message', response})

@app.route('/api/v1/auth/login', methods=['POST'])
def login():
    '''user login API endpoint'''
    data = request.get_json()
    response = user.login(data.email, data.password)
    return jsonify({'message', response})

@app.route('/api/v1/events', methods=['GET'])
def events():
    '''Gets all events API endpoint'''
    response = event.view_event()
    return jsonify({'message', response})

@app.route('/api/v1/auth/logout', methods=['POST'])
def logout():
    '''user logout API endpoint'''

@app.route('/api/v1/auth/reset-password', methods=['POST'])
def reset_password():
    '''user reset-password API endpoint'''

@app.route('/api/v1/events', methods=['POST'])
def create_event():
    '''user can create an event'''
    data = request.json()
    response = event.create()
    return jsonify({'message', response})  

@app.route('/api/v1/events/<eventId>', methods=['PUT'])
def update_event():
    '''user can update an event'''
    data = request.json():
    response = event.edit_event(data.eventid,data.event,data.starttime,data.finishtime,data.place)
    retun jsonify({'message', response})

@app.route('/api/v1/events/<eventId>', methods=['DELETE'])
def delete_event():
    '''user can delete an event'''
    data = request.json():
    response = event(data.eventid)
    return jsonify({'message',response})

@app.route('api/v1/events/<eventId>/rsvp',methods=['POST'])
def rsvp_event():
    '''user can be able to rsvp event'''
    data =request.json():
    response = rsvp(data.eventid, data.email)
    return jsonify({'message', response})
