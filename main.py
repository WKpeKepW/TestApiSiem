from mpsiemlib.common import Settings, Creds, MPSIEMAuth 
from mpsiemlib.modules import Filters, EventsAPI
import time

def get_credsTxt():
    with open('creds.txt','r') as txt:
        return txt.read()

if __name__ == '__main__':
    
    pass


def default():
    creds = Creds()
    creds.core_hostname = '172.17.250.66'
    creds.core_login = 'vakulik-dv'
    creds.core_auth_type = 0
    creds.core_pass = get_credsTxt()
    auth = MPSIEMAuth(creds, Settings())
    auth.get_session()
    events = EventsAPI(auth, Settings())
    filters = Filters(auth, Settings())
    filter_list = filters.get_filters_list()
    for uuid_filter in filter_list:
        if filter_list[uuid_filter]['name'] == '[malware] KES':
            print(filters[uuid_filter])
    filters.close()
    events.close() 