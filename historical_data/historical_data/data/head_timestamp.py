from datetime import datetime

import sqlalchemy

from data.sqlalchemy_base import SqlAlchemyBase


class HeadTimestamp(SqlAlchemyBase):
    __tablename__ = "head_timestamp"

    con_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    symbol = sqlalchemy.Column(sqlalchemy.String, nullable=False, index=True)
    head_timestamp = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    symbol = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    insert_date = sqlalchemy.Column(sqlalchemy.DateTime, nullable=False, default=datetime.now)


