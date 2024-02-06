from app.resource.models.access import Access
from app import db

def data_init():
    data_access= {'All':"""User Got All access to the ressource""",
                  'read':"""User Got read access to the ressource"""}
    access_list = Access.query.all()
    for access in access_list:
        if access.name in list(data_access.keys()):
            data_access.remove(access.name)
            
    for data in list(data_access.keys()):
        new_access= Access(data,data_access[data])
        db.session.add(new_access)
        db.session.commit()  
        
    
curl -X POST http://127.0.0.1:5000/access/ \
     -H "Content-Type: application/json" \
     -d '{"name": "read", "description": "User Got read access to the ressource"}'
