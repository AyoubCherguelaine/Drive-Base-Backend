

class endpoint:
    body_data_keys= {}
    @staticmethod
    def is_body_data_valide(data,body_data_keys=None,create=False)->bool:
        if create and set(data.keys()) == body_data_keys:
            return True
        elif not create and set(data.keys()) & body_data_keys:
            return True
        else:
            return False
        
    @staticmethod
    def create(data):
        pass
    
    @staticmethod
    def get_list(query):
        pass
    
    @staticmethod
    def get(id):
        pass
    
    @staticmethod
    def update(id,data):
        pass
    
    @staticmethod
    def delete(id):
        pass
    
    
        
    