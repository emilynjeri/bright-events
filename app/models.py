
import re 
import uuid


class User():
    '''The class handle activities related to user'''
    def __init__(self):

        self.user_list =[]

    def register(self,firstname,lastname,password,email):
        '''A method to register users with correct and valid details'''

        #empty dict to store details that user create
        user_details ={}

        for user in self.user_list:
            if email == user['email']:
                return "email already taken,create another email"
            else:
                if not match("^[a-zA-Z0-9_]*$", firstname):
                     return "Name should only contain alpanumeric character" 
        
                 if not re.match("^[a-zA-Z0-9_]*$", lastname):
                     return "Name should only contain alpanumeric character"
                elif len(password) <8:
                    return "password must contain more 8 characters"
                else:
                    #register user if all the details are valid
                    user_details['firstname'] = firstname
                    user_details['lastname'] = lastname
                    user_details['password'] = password
                    user_details['email'] = email
                    user_details['id'] = uuid.uuid1()
                    self.user_list.append(user_details)
                    return "You have successfully registered to bright events"

                def login(self,email,password):
                    '''Login user with valid user details'''
                    for user in self.user_details:
                        if email == user['email']:
                            if password == ['password']:
                                return "login successful"
                            else:
                                return "wrong password or email"

                def find _user_by_id(self,user_id):
                    '''Retrieve user given a user id'''
                    for user in self.user_list:
                        if user['id'] == user_id:
                            return user 


    class Events():

        def __init__(self):
            '''Allow user to create event'''
            self.event_list = []
    def create(self,id,event,starttime,finishtime,place)
        self.event_particulars = {}
        self.event_particulars['id'] = id
        self.event_prticulars['event'] = event
        self.event_particulars[starttime] = starttime
        self.event_particulars[finishtime] = finishtime
        self.rsvp = []
        self.event_particulars.append(self.event_particulars)
        return "event has been created"

    def view_event(self):
        '''allow user to events that exist'''
        return self.event_list

    def place_filter(self,place):
        '''allow to search event by venue ot the event'''
        new_event_list = [event for in self.event_list if event['place'] == place]
        
    def edit_event(self,eventid,event,starttime,finishtime,place)
        for event in self. event_list:
                        event['id'] = eventid
						event['event'] = event
						event['starttime'] = starttime
						event['finishtime'] = finishtime
						event['place'] = place_filter
						self.event_list.append(self.event_partucals)
                        return "update success"

    def delete(self, eventid):
		for event in self.event_list:
			if event['id'] == eventid:
				self.event_list.remove(event)
            return " event deleted"
    
    def rsvp(self, eventid,email):
        for event in self.event_list:
            if event['id'] == eventid:
                event['rsvp'].append(email)
    
    def view_rsvps(self, eventid):
        for event in self.event_list:
            if event['id'] == eventid:
                att_users = event['rsvp']

	