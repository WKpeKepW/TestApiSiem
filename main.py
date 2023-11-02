from mpsiemlib.common import Settings, Creds, MPSIEMAuth 
from mpsiemlib.modules import Filters, EventsAPI
import time


def default():
    ini = Initialize()
    filter_list = ini.filters.get_filters_list()

    for uuid_filter in filter_list:
        if filter_list[uuid_filter]['name'] == 'src_distinct_dst_SMB_bot':
            #print(ini.filters.get_filter_info(uuid_filter)['query']['aggregate'])
            #print(ini.filters.get_filter_info(uuid_filter)['query']['select'])
            print(ini.events.get_events_by_filter_aggregation(
                filter=ini.filters.get_filter_info(uuid_filter)['query']['where'],
                fields=ini.filters.get_filter_info(uuid_filter)['query']['select'],
                groupBy=ini.filters.get_filter_info(uuid_filter)['query']['group'],
                aggregateBy=ini.filters.get_filter_info(uuid_filter)['query']['aggregate'],
                time_from=time.time()-3600,
                time_to=time.time(),
                limit=10,
                offset=0
            ))

    ini.close()

class Initialize:
    def close(self):
        self.filters.close()
        self.events.close()

    def get_credsTxt(self):
        with open('creds.txt','r') as txt:
            return txt.read()
        
    def __init__(self) -> None:
        creds = Creds()
        creds.core_hostname = '10.81.41.5'
        creds.core_login = 'vols_3'
        creds.core_auth_type = 0
        creds.core_pass = self.get_credsTxt()
        auth = MPSIEMAuth(creds, Settings())
        auth.get_session()
        self.events = EventsAPI(auth, Settings())
        self.filters = Filters(auth, Settings())
        
        
if __name__ == '__main__':
    default()
    pass
