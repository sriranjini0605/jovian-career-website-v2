from sqlalchemy import create_engine, text
import os
#creating an engine
db_connection_string = os.environ['DB_Connection_String']
engine = create_engine(db_connection_string,
                       connect_args={
                      "ssl": {
                          "ssl_ca": "/etc/ssl/cert.pem"
                      }})


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(dict(row._mapping))
    return jobs

def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(
       text(f"SELECT * FROM jobs WHERE id={id}")
      )
    rows = []
    for row in result.all():
      rows.append(row._mapping)
    if len(rows) == 0:
      return None
    else:
      return rows[0] if rows else None

