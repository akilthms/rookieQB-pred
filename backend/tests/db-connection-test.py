from backend.entities.entity import Session, engine, Base
from backend.entities.rookieQbs import RookieQbs

# generate database schema
Base.metadata.create_all(engine)

# start session
session = Session()

# check for existing data
rookieQbs = session.query(RookieQbs).all()

if len(rookieQbs) == 0:
    # create and persist dummy exam
    test = RookieQbs("Test QB", "Test your knowledge about SQLAlchemy.", "script")
    session.add(test)
    session.commit()
    session.close()

    # reload exams
    rookieQbs = session.query(RookieQbs).all()

# show existing exams
print('### Quaterbacks:')
for qb in rookieQbs:
    print(f'({qb.id}) {qb.title} - {qb.description}')