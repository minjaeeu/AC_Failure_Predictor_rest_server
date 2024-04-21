from sqlalchemy.orm import declarative_base

# to avoid import reocurrance in both db & route files
Base = declarative_base()
