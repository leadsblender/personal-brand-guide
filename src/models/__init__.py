from .. import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    guides = db.relationship('BrandGuide', backref='user', lazy=True)

class BrandGuide(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False, default="My Brand Guide")
    language = db.Column(db.String(10), nullable=False, default="nl")
    
    # Hero information
    hero_name = db.Column(db.String(100))
    hero_stands_for = db.Column(db.Text)
    hero_stands_against = db.Column(db.Text)
    hero_flaws = db.Column(db.Text)
    
    # Brand information
    ideal_client = db.Column(db.Text)
    brand_pillars = db.Column(db.Text)
    tone_of_voice = db.Column(db.Text)
    visual_identity = db.Column(db.Text)
    offer_principles = db.Column(db.Text)
    behavior = db.Column(db.Text)
    why = db.Column(db.Text)
    enemies = db.Column(db.Text)
    slogans = db.Column(db.Text)
    brand_summary = db.Column(db.Text)
    mission_statement = db.Column(db.Text)
    mission_statement_short = db.Column(db.String(255))
    
    # Metadata
    is_draft = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(),
                          onupdate=db.func.current_timestamp())

    def __repr__(self):
        return f'<BrandGuide {self.title}>'

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'hero_name': self.hero_name,
            'hero_stands_for': self.hero_stands_for,
            'hero_stands_against': self.hero_stands_against,
            'hero_flaws': self.hero_flaws,
            'ideal_client': self.ideal_client,
            'brand_pillars': self.brand_pillars,
            'tone_of_voice': self.tone_of_voice,
            'visual_identity': self.visual_identity,
            'offer_principles': self.offer_principles,
            'behavior': self.behavior,
            'why': self.why,
            'enemies': self.enemies,
            'slogans': self.slogans,
            'brand_summary': self.brand_summary,
            'mission_statement': self.mission_statement,
            'mission_statement_short': self.mission_statement_short,
            'is_draft': self.is_draft,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }