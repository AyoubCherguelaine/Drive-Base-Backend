from datetime import datetime
from app import db


class summary(db.Model):
    __tablename__ = "summaries"
    
    id = db.Column(db.Integer, primary_key=True)
    summary = db.Column(db.String())
    file_id = db.Column(db.ForeignKey("files.id"), nullable=False)
    model_id = db.Column(db.ForeignKey("models.id"), nullable=False)
    date = db.Column(db.DateTime(),default=datetime.utcnow)
    
    file = db.relationship("file", lazy='joined', foreign_keys=[file_id])
    model = db.relationship("model", lazy='joined', foreign_keys=[model_id])
    #attr
    data_keys = {'summary','file_id','model_id','date'}
    
    def __repr__(self) -> str:
        return "<category %r" % self.id
    
    def json_populate(self):
        return {
            "id": self.id,
            "summary": self.summary,
            "file": self.file.json(),
            "model": self.model.json(),
            "date": self.date
        } 
        
    def json(self):
        return {
            "id": self.id,
            "summary": self.summary,
            "file_id": self.file_id,
            "model_id": self.model_id,
            "date": self.date
        }