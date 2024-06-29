from app import db
import sqlalchemy as sa
from typing import Optional, List
import sqlalchemy.orm as so
from datetime import datetime, timezone
from .association_tables import game_system_association as gsa

class System(db.Model):
    __tablename__ = 'systems'
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(80), unique=True, nullable=False)
    manufacturer: so.Mapped['Publisher'] = so.relationship('Publisher', back_populates='systems') # type: ignore
    publisher_id: so.Mapped[int] = so.mapped_column(sa.Integer, sa.ForeignKey('publishers.id'), index=True, nullable=False)
    release_year: so.Mapped[int] = so.mapped_column(sa.Integer, nullable=False)
    created_at: so.Mapped[Optional[datetime]] = so.mapped_column(
        sa.DateTime(timezone=True), default=sa.func.now())
    updated_at: so.Mapped[Optional[datetime]] = so.mapped_column(
        sa.DateTime(timezone=True), default=sa.func.now(), onupdate=sa.func.now())
    games: so.WriteOnlyMapped['Game'] = so.relationship( # type: ignore
        'Game', 
        secondary=gsa,
        back_populates='systems')
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'manufacturer': self.manufacturer.name if self.manufacturer else None,
            'publisher_id': self.publisher_id,
            'release_year': self.release_year,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
    def __repr__(self):
        return '<System {}>'.format(self.name)
