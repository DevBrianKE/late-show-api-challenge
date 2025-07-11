from app import create_app, db
from models.guest import Guest
from models.episode import Episode

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    g1 = Guest(name="Brian Kipcchumba", occupation="Engineer")
    g2 = Guest(name="John Gitonga", occupation="Developer")

    e1 = Episode(date="2025-06-01", number=101)
    e2 = Episode(date="2025-06-15", number=102)

    db.session.add_all([g1, g2, e1, e2])
    db.session.commit()

    print("Database seeded with initial data.")