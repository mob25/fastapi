import databases
import sqlalchemy

DATABASE_URL = "sqlite:///database.db"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table("users", metadata,
                         sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
                         sqlalchemy.Column("name", sqlalchemy.String(20)),
                         sqlalchemy.Column("surname", sqlalchemy.String(20)),
                         sqlalchemy.Column("email", sqlalchemy.String(30)),
                         sqlalchemy.Column("password", sqlalchemy.String(20)),
                         )

engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
metadata.create_all(engine)