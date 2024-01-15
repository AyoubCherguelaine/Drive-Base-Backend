
from app import db
from flask import request, jsonify, abort

class endpoint:
    def __init__(self,model, model_name,details=False):
        self.model = model
        self.model_name = model_name
        self.details = details
        self.__rename_functions(model_name)
        
    def __rename_functions(self, suffix):
        for attr_name in dir(self):
            attr = getattr(self, attr_name)
            if callable(attr) and hasattr(attr, '__call__') and not attr_name.startswith("__"):
                setattr(self, f"{attr_name}_{suffix}", attr)
        
    def __is_body_data_valide(self, data, create=True):
        if create and set(data.keys()) == self.model.data_keys:
            return True
        elif not create and set(data.keys()) & self.model.data_keys:
            return True
        else:
            return False
    
    def create(self):
        data = request.json
        if self.__is_body_data_valide(data,create=True):
            model = self.model(**data)
            try:
                db.session.add(model)
                db.session.commit()  
                return jsonify(model.json())
            except Exception as e :
                abort(500,e)
        else:
            abort(400, {"message": "Invalid % data" % self.model_name })
    
    def get_list(self):
        models = self.model.query.order_by(self.model.id).all()
        models_json = [model.json() for model in models]
        return jsonify(models_json)
    
    def get(self, id):
        model = self.model.query.get_or_404(id)
        return jsonify(model.json()) 
    
    def update(self, id):
        data = request.json
        model = self.model.query.get_or_404(id)
        if self.__is_body_data_valide(data):
            for key in list(data.keys()):
                setattr(model, key, data[key])
            try:
                db.session.commit()
                return jsonify(model.json())
            except Exception as e :
                abort(500,e)
        else:
            abort(400,{"Invalid % data" % self.model_name})
    
    def delete(self, id):
        model = self.model.query.get_or_404(id)
        try:
            db.session.delete(model)
            db.session.commit()
            return {"result":f"Deleted {model.id} "}
        except Exception as e : 
            abort(500,e)
            
    def get_list_details(self):
        if not self.details:
            return False
        list_models = self.model.query.order_by(self.model.id).all()
        models = [model.json_populate() for model in list_models] 
        return jsonify(models)
    
    def get_details(self, id):
        
        if not self.details:
            return False
        
        model = self.model.query.get_or_404(id)
        return jsonify(model.json_populate())
    
    @staticmethod
    def get_endpoint(obj,function_name):
        if hasattr(obj, function_name):
            return getattr(obj, function_name)