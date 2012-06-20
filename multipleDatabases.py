import random 

class MasterSlaveRouter(object):
    """A router that sets up a simple master/slave configuration"""

    def db_for_read(self, model, **hints):
        "Point all read operations to a random slave"
        if(model._meta.app_label != 'osm'):
            return random.choice(['default'])
        else:
            return 'osm'

    def db_for_write(self, model, **hints):
        "Point all write operations to the master"
        if(model._meta.app_label != 'osm'):
            return 'default'
        else:
            return 'osm'

    def allow_relation(self, obj1, obj2, **hints):
        "Allow any relation between two objects in the db pool"
        db_list = ('default')
        if obj1._state.db in db_list and obj2._state.db in db_list:
            return True
        return None

    def allow_syncdb(self, db, model):
        "Explicitly put all models on all databases."
        if(model._meta.app_label != 'osm'):
            return True
        else:
            return False
