from datetime import datetime
from .. import db

class BrandGuide(db.Model):
    __tablename__ = 'brand_guide'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Ideale Klant
    ideal_client = db.Column(db.Text)
    client_problem = db.Column(db.Text)
    client_goal = db.Column(db.Text)

    # Hero Information
    hero_id = db.Column(db.String(100))
    hero_stands_for = db.Column(db.Text)
    hero_stands_against = db.Column(db.Text)
    hero_flaws = db.Column(db.Text)

    # Brand Pillars
    brand_stands_for = db.Column(db.Text)
    brand_stands_against = db.Column(db.Text)
    brand_principles = db.Column(db.Text)

    # Brand Identity
    tone_of_voice = db.Column(db.Text)
    visual_identity = db.Column(db.Text)
    visual_style = db.Column(db.Text)

    # Offer & Behavior
    offer = db.Column(db.Text)
    offer_principles = db.Column(db.Text)
    behavior = db.Column(db.Text)

    # Why & Mission
    why = db.Column(db.Text)
    mission_long = db.Column(db.Text)
    mission_short = db.Column(db.String(255))

    # Additional Elements
    enemies = db.Column(db.Text)
    slogans = db.Column(db.Text)
    brand_summary = db.Column(db.Text)

    def to_dict(self):
        """Convert model to dictionary."""
        return {
            'id': self.id,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
            'ideal_client': self.ideal_client,
            'client_problem': self.client_problem,
            'client_goal': self.client_goal,
            'hero_id': self.hero_id,
            'hero_stands_for': self.hero_stands_for,
            'hero_stands_against': self.hero_stands_against,
            'hero_flaws': self.hero_flaws,
            'brand_stands_for': self.brand_stands_for,
            'brand_stands_against': self.brand_stands_against,
            'brand_principles': self.brand_principles,
            'tone_of_voice': self.tone_of_voice,
            'visual_identity': self.visual_identity,
            'visual_style': self.visual_style,
            'offer': self.offer,
            'offer_principles': self.offer_principles,
            'behavior': self.behavior,
            'why': self.why,
            'mission_long': self.mission_long,
            'mission_short': self.mission_short,
            'enemies': self.enemies,
            'slogans': self.slogans,
            'brand_summary': self.brand_summary
        }
