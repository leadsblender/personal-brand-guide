from flask import Blueprint, render_template, jsonify, request
from ..models import BrandGuide, db
from ..config.heroes import SUPERHEROES

brand_guide_bp = Blueprint('brand_guide', __name__)

@brand_guide_bp.route('/')
def index():
    """Render the main page with superhero selection."""
    return render_template('index.html', superheroes=SUPERHEROES)

@brand_guide_bp.route('/api/save-draft', methods=['POST'])
def save_draft():
    """Save the brand guide draft."""
    try:
        data = request.get_json()
        guide_id = data.get('guide_id')
        
        if guide_id:
            guide = BrandGuide.query.get(guide_id)
            if not guide:
                return jsonify({'success': False, 'error': 'Guide not found'})
        else:
            guide = BrandGuide()
        
        # Update Ideale Klant
        guide.ideal_client = data.get('ideal_client')
        guide.client_problem = data.get('client_problem')
        guide.client_goal = data.get('client_goal')
        
        # Update Hero
        guide.hero_id = data.get('hero')
        guide.hero_stands_for = data.get('hero_customization', {}).get('stands_for')
        guide.hero_stands_against = data.get('hero_customization', {}).get('stands_against')
        guide.hero_flaws = data.get('hero_customization', {}).get('flaws')
        
        # Update Brand Pillars
        guide.brand_stands_for = data.get('brand_pillars', {}).get('stands_for')
        guide.brand_stands_against = data.get('brand_pillars', {}).get('stands_against')
        guide.brand_principles = data.get('brand_pillars', {}).get('principles')
        
        # Update Brand Identity
        guide.tone_of_voice = data.get('tone_of_voice')
        guide.visual_identity = data.get('visual_identity')
        guide.visual_style = data.get('visual_style')
        
        # Update Offer & Behavior
        guide.offer = data.get('offer')
        guide.offer_principles = data.get('offer_principles')
        guide.behavior = data.get('behavior')
        
        # Update Why & Mission
        guide.why = data.get('why')
        guide.mission_long = data.get('mission', {}).get('long')
        guide.mission_short = data.get('mission', {}).get('short')
        
        # Update Additional Elements
        guide.enemies = data.get('enemies')
        guide.slogans = data.get('slogans')
        guide.brand_summary = data.get('brand_summary')
        
        if not guide_id:
            db.session.add(guide)
        
        db.session.commit()
        
        return jsonify({
            'success': True,
            'guide_id': guide.id
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

@brand_guide_bp.route('/api/load-draft/<int:guide_id>')
def load_draft(guide_id):
    """Load a saved brand guide draft."""
    guide = BrandGuide.query.get_or_404(guide_id)
    
    hero = SUPERHEROES.get(guide.hero_id, {})
    
    return jsonify({
        'success': True,
        'data': {
            'ideal_client': guide.ideal_client,
            'client_problem': guide.client_problem,
            'client_goal': guide.client_goal,
            'hero': guide.hero_id,
            'hero_customization': {
                'stands_for': guide.hero_stands_for,
                'stands_against': guide.hero_stands_against,
                'flaws': guide.hero_flaws
            },
            'brand_pillars': {
                'stands_for': guide.brand_stands_for,
                'stands_against': guide.brand_stands_against,
                'principles': guide.brand_principles
            },
            'tone_of_voice': guide.tone_of_voice,
            'visual_identity': guide.visual_identity,
            'visual_style': guide.visual_style,
            'offer': guide.offer,
            'offer_principles': guide.offer_principles,
            'behavior': guide.behavior,
            'why': guide.why,
            'mission': {
                'long': guide.mission_long,
                'short': guide.mission_short
            },
            'enemies': guide.enemies,
            'slogans': guide.slogans,
            'brand_summary': guide.brand_summary,
            'hero_data': hero
        }
    })