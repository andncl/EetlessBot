import time
from member_class import Member

name_list = ['isa', 'nemo', 'yara', 'nikki', 'yannick', 'andreas', 'paul', 'kaan', 'conor', 'robin',\
    'fons', 'frank','anna','luka','lukas', 'jules']

class Meal:
    ''' '''
    def __init__(self):
        self.cost = 0
        self.date = time.ctime(time.time())
        self.members = {}
        self.name_cook = ''
        self.open = True

    def print_date(self):
        return self.date

    def add_cook(self, cook: Member):
        self.members[cook.name] = cook
        self.name_cook = cook.name

    def add_member(self, member):
        self.members[member.name] = member

    def remove_member(self, member_name):
        del self.members[member_name]

    def calc_total_members(self):
        ''' Returns the total nr of participants.'''
        count = 0
        for member in self.members.values():
            count = count + 1 + member.nr_friends
        return count

    def show_member_list(self):
        ''' Prints snapshot of current meal. '''
        rsp = 'Status: OPEN\n' if self.open else 'Status: CLOSED\n'
        rsp += '-----------------\n'
        rsp += 'Cook: '
        for member in self.members.values():
            rsp += member.name + '\t+' + str(member.nr_friends) +'\n'
        rsp += '-----------------\n'
        rsp += 'Total members:\t'+str(self.calc_total_members())
        return rsp

    def set_cost(self, cost):
        self.cost = cost


    def calc_balance(self, payer_name: str, price: float):
        payer_name = payer_name.lower()
        self.cost += price
        nr_eaters = self.calc_total_members()
        rsp = 'BALANCE\n-----------------\n'
        if self.cost != 0:    
            for member in self.members.values():
                if member.name == payer_name:
                    member.price = price

                else:
                    member.price = -round((1+member.nr_friends)/nr_eaters*self.cost,2)
                rsp += member.name + '\t+' + str(member.nr_friends) +'\n'
                rsp += '\t' + str(member.price) +'€\n'

            rsp += '---------------' +'\n'
            rsp += 'Total members:\t'+str(self.calc_total_members())
            rsp += '\nTotal cost:\t' + str(self.cost) + '€'
        else:
            rsp = 'Let op! No cost has been entered yet.'
        return rsp


    def cmd_analyser(self,name:str, word: str):
        if word == 'k':
            if self.name_cook == '':
                rsp=name.upper() + ' is cooking.'
                self.add_cook(Member(name))
            else:
                rsp='Someone else is already cooking. But you may join.'

        elif word == 'e':
            if self.name_cook == '':
                rsp=r'Sorry no one is cooking.'
            else:
                if name == self.name_cook:
                    rsp = name.upper() + '... you cant join. You are the cook!'

                elif not self.open:
                    rsp = 'Sorry, inquiry is closed.'
                else:
                    self.add_member(Member(name))
                    rsp=name.upper() + ' is joining.'

        elif word == 'x' and self.open:
            if name in self.members:
                if name == self.name_cook:
                    rsp='Food is cancelled! The cook has left.'
                    Meal()
                    self.__init__()
                elif not self.open:
                    rsp = 'Ride or die! Inquiry is closed.'
                else:
                    self.remove_member(name)
                    rsp='You are not joining anymore.'
            else:
                return 'You can not leave if you have not joined yet.'

        elif word == 'si':
            if name == self.name_cook:
                if not self.open:
                    rsp = 'Inquiry already closed.'
                else:
                    self.open = False
                    rsp = 'Food inquiry closed now.'
            else:
                rsp='You are not cooking. So you cant close the inquiry.'

        elif len(word)>2:
            if word in name_list:
                if self.name_cook == '':
                    rsp = 'No one is cooking yet.'
                else:
                    if self.open:
                        self.add_member(Member(word))
                        rsp = word.upper() + ' added by: ' + name.upper() + ' (cook)'
                    elif name == self.name_cook:
                        rsp = word.upper() + ' added by: ' + name.upper()
                    else:
                        rsp = 'Sorry, inquiry is closed.'
            else:
                rsp='Sorry I do not know this command: ' + word

        elif len(word)>1:
            try:
                friends_to_add = int(word.split('+')[1])
            except:
                rsp='Sorry I do not know this command: ' + word
            else:
                if name in self.members:
                    if self.open:
                        rsp = 'Added '+str(friends_to_add)+' friends to '+name.upper()
                        self.members[name].nr_friends += friends_to_add
                    elif name == self.name_cook:
                        rsp = 'Added '+str(friends_to_add)+' friends to '+name.upper() + ' (cook)'
                        self.members[name].nr_friends += friends_to_add
                    else:
                        rsp = 'Sorry, inquiry is closed.'
                else:
                    rsp='You can only add friends if you join yourself.'

        else:
            rsp='Sorry I do not know this command: ' + word

        return rsp

    def message_analyser(self, name, sentence):
        '''Takes a sequence of words and splits it into readable commands.'''

        sentence = sentence.lower()
        name = name.lower()
        command_list = sentence.split(' ')
        print(command_list)
        reply_list = []

        for word in command_list:
            txt = self.cmd_analyser(name, word)
            reply_list.append(txt)

        return reply_list

    def log_meal(self):
        pass
