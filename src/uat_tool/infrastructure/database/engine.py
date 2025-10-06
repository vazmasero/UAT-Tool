from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

DB_NAME = "uat_tool.db"
DB_URL = f"sqlite:///{DB_NAME}"

# Motor SQLAlchemy
engine = create_engine(DB_URL, echo=False)

# Scoped session para seguridad de hilos
Session = scoped_session(sessionmaker(bind=engine))
