from app import db
import sqlalchemy as sa
from sqlalchemy import select
from sqlalchemy.schema import CheckConstraint
import uuid
from typing import Optional
import sqlalchemy.orm as so
from datetime import datetime
from .association_tables import game_publisher_association as gpa, game_genre_association as gga, game_system_association as gsa

class Game(db.Model):
    __tablename__ = 'games'
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    title: so.Mapped[str] = so.mapped_column(sa.String(120), unique=True)
    release_year: so.Mapped[Optional[int]] = so.mapped_column(sa.Integer)
    publisher: so.WriteOnlyMapped['Publisher'] = so.relationship('Publisher', secondary='game_publisher', back_populates='games') # type: ignore
    genre: so.WriteOnlyMapped['Genre'] = so.relationship('Genre', # type: ignore    
        secondary='game_genre', back_populates='games') 
    systems: so.WriteOnlyMapped['System'] = so.relationship('System', # type: ignore
        secondary=gsa,
        back_populates='games')
    pc: so.Mapped[bool] = so.mapped_column(sa.Boolean, default=False)
    mac: so.Mapped[bool] = so.mapped_column(sa.Boolean, default=False)
    created_at: so.Mapped[Optional[datetime]] = so.mapped_column(
        sa.DateTime(timezone=True), default=sa.func.now())
    updated_at: so.Mapped[Optional[datetime]] = so.mapped_column(
        sa.DateTime(timezone=True), default=sa.func.now(), onupdate=sa.func.now())
    image_url: so.Mapped[Optional[str]] = so.mapped_column(sa.String(255), default='https://gamefaqs.gamespot.com/a/box/8/1/2/14812_front.jpg')
    __table_args__ = (
        CheckConstraint('release_year >= 1940 AND release_year <= 2024', name='release_year_check'),
        )
 
    def to_dict_with_systems(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_year': self.release_year,
            'pc': self.pc,
            'mac': self.mac,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
            'image_url': self.image_url,
            'systems': [system.to_dict() for system in self.systems]
        }