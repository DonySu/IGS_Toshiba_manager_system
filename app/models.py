from app import db

#账户信息条目定义
class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),index=True,unique=True)
    password = db.Column(db.String(20),index=True)
    workid = db.Column(db.String(6),index=True,unique=True)
    email = db.Column(db.String(64),index=True,unique=True)
    phone = db.Column(db.String(11),index=True,unique=True)
    section = db.Column(db.String(6))
    gender = db.Column(db.String(6))
    user_img = db.Column(db.String(64),default='Panda.gif')
    
    old_password = db.Column(db.String(20),default="")
    old_email = db.Column(db.String(64),default="")
    old_phone = db.Column(db.String(11),default="")
    old_section = db.Column(db.String(6),default="")
    old_user_img = db.Column(db.String(64),default="")
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False
 
    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return '<User %r>' % (self.__dict__)

#通告条目定义
class Notices(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(512),index=True,unique=True)
    author = db.Column(db.String(128),index=True)
    content = db.Column(db.String(1024),index=True)
    species = db.Column(db.String(128),index=True)
    create_date = db.Column(db.String(128),index=True)

    old_title = db.Column(db.String(512),index=True,unique=True)
    old_content = db.Column(db.String(1024),index=True)
    old_species = db.Column(db.String(128),index=True)
    latest_modify_date = db.Column(db.String(128),index=True)
    
#LOM条目定义
class Loms(db.model):
    id = db.Column(db.Integer,primary_key=True)
    worker_name = db.Column(db.String(512),index=True)
    author = db.Column(db.String(128),index=True)
    content = db.Column(db.String(1024),index=True)
    species = db.Column(db.String(128),index=True)
    create_date = db.Column(db.String(128),index=True)

    old_title = db.Column(db.String(512),index=True,unique=True)
    old_content = db.Column(db.String(1024),index=True)
    old_species = db.Column(db.String(128),index=True)
    latest_modify_date = db.Column(db.String(128),index=True)
