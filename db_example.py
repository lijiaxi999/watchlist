from app import db, User, Movie

user = User(name='Grey Li')
m1 = Movie(title='Leon',year='1994')
m2 = Movie(title='Mahjong', year='1996')
db.session.add(user)
db.session.add(m1)
db.session.add(m2)
db.session.commit()