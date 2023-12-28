from app import db
from datetime import datetime


class summary(db.Model):
    __tablename__ = "summaries"
    
    id = db.Column(db.Integer, primary_key=True)
    summary = db.Column(db.String())
    file_id = db.Column(db.ForeignKey("file.id"), nullable=False)
    model_id = db.Column(db.ForeignKey("model.id"), nullable=False)
    date = db.Column(db.Datetime())
    
    file = db.relationship("file", lazy='joined', foreign_keys=[file_id])
    model = db.relationship("file", lazy='joined', foreign_keys=[model_id])
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