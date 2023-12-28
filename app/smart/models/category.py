from app import db

class category(db.Model):
    __tablename__ = "categories"
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(55))
    description = db.Column(db.String(500))
    
    
    data_keys = {'label','description'}
    
    def __repr__(self) -> str:
        return "<category %r" % self.id
    
    def json_populate(self):
        return {
            "id":self.id,
            "label":self.label,
            "description":self.description
        }
        
    def json(self):
        return {
            "id":self.id,
            "label":self.label,
            "description":self.description
        }