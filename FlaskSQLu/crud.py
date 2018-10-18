from base import db, Puppy

## CREATE ##
my_puppy = Puppy('Rufus', 5)
db.session.add(my_puppy)
db.session.commit()

## READ ##
all_puppies = Puppy.query.all()
print(all_puppies)

## SELECT BY ID ##
one_puppy = Puppy.query.get(1)
print(one_puppy.name)

## FILTER ##
puppy_frank = Puppy.query.filter_by(name='Frank')
print(puppy_frank.all())

## UPDATE ##
first_puppy = Puppy.query.get(1)
first_puppy.age = 10
db.session.add(first_puppy)
db.session.commit()

## delete ##
second_pup = Puppy.query.get(2)
db.session.delete(second_pup)
db.session.commit()

#all
print(Puppy.query.all())