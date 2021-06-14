from sqlalchemy.orm import mapper, relationship
from sqlalchemy.schema import MetaData, Table
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, String
import model

metadata = MetaData()

order_lines = Table(
    'order_lines', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('sku', String(255)),
    Column('qty', Integer, nullable=False),
    Column('orderid', String(255)),
)


def start_mappers():
    line_mapper = mapper(model.OrderLine, order_lines)
