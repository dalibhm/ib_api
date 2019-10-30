import sqlalchemy

from data.sqlalchemy_base import SqlAlchemyBase


class Exchange(SqlAlchemyBase):
    __tablename__ = "exchanges"

    code = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String,  nullable=False)
    security_type = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    opening_hours = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    link = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    @staticmethod
    def from_json(json_exchange):
        # try:
        return Exchange(**json_exchange)
        # except:
        #     raise ValidationError('Contract cannot be constructed')

    def to_json(self):
        json_exchange = {
            'code': self.code,
            'name': self.name,
            'security_type': self.security_type,
            'opening_hours': self.opening_hours,
            'link': self.link
        }
        return json_exchange
