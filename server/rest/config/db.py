from sqlalchemy import create_engine,MetaData

engine = create_engine("sqlite:///database.sqlite")
meta = MetaData()
conn = engine.connect()