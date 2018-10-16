from base import db, Puppy

# creates all tables
db.create_all()

sam = Puppy('Sam', 3)
frank = Puppy('Frank', 4)

db.session.add_all([sam, frank])
db.session.commit()

print(sam.id)
print(frank.id)