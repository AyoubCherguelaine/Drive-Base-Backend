from app import db

class model(db.Model):
    __tablename__ = "models"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(55))
    provider = db.Column(db.String(55))
    
    #attr
    data_keys = {'name','provider'}
    
    def __repr__(self) -> str:
        return "<model %r" % self.id

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "provider": self.provider
        }