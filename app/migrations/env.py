from models import db

def run_migrations():
    with db.engine.connect() as connection:
        db.create_all()

if __name__ == '__main__':
    run_migrations()
