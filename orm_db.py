from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
confi={
     "host" : "localhost",
     "port":"3306",
    "user": "root",
    "passwd":"12345678",
    "database":"Student"
}

def get_db():
  DB_URL = f"mysql://{confi['user']}:{confi['passwd']}@{confi['host']}:{confi['port']}/
{confi['database']}"
  print(DB_URL)
  engine = create_engine(DB_URL,echo=True)
  SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
  db_session = SessionLocal() 
  return db_session
