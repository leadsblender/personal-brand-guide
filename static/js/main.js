document.addEventListener('DOMContentLoaded', function() {
    // Global variables
    let selectedHero = null;
    let saveTimeout = null;
    const form = document.querySelectorAll('textarea, input');
    
    // Initialize hero selection
    initializeHeroSelection();
    
    // Track form changes for autosave
    form.forEach(input => {
        input.addEventListener('change', () => {
            updateProgress();
            autosave();
        });
        input.addEventListener('keyup', () => {
            autosave();
        });
    });

    function initializeHeroSelection() {
        const heroCards = document.querySelectorAll('.hero-card');
        heroCards.forEach(card => {
            card.addEventListener('click', () => {
                // Remove selected class from all cards
                heroCards.forEach(c => c.classList.remove('selected'));
                
                // Add selected class to clicked card
                card.classList.add('selected');
                selectedHero = card.dataset.hero;
                
                // Show customization form
                document.getElementById('hero-customization').style.display = 'block';
                
                // Pre-fill customization fields
                const heroDetails = card.querySelector('.hero-details');
                document.querySelector('textarea[name="stands_for"]').value = 
                    heroDetails.querySelector('p:nth-child(1)').textContent.replace('Staat voor: ', '');
                document.querySelector('textarea[name="stands_against"]').value = 
                    heroDetails.querySelector('p:nth-child(2)').textContent.replace('Staat tegen: ', '');
                document.querySelector('textarea[name="flaws"]').value = 
                    heroDetails.querySelector('p:nth-child(3)').textContent.replace('Gebreken: ', '');
                
                updateProgress();
                autosave();
            });
        });
    }

    function updateProgress() {
        const total = form.length;
        const completed = Array.from(form).filter(input => {
            return input.value.trim() !== '';
        }).length;
        
        const percentage = Math.round((completed / total) * 100);
        const progressBar = document.querySelector('.progress-bar');
        const progressText = document.querySelector('.progress-text');
        
        progressBar.style.width = `${percentage}%`;
        progressBar.setAttribute('aria-valuenow', percentage);
        progressText.textContent = `${percentage}% Voltooid`;
    }

    function autosave() {
        if (saveTimeout) {
            clearTimeout(saveTimeout);
        }
        
        saveTimeout = setTimeout(() => {
            saveDraft();
        }, 1000);
    }

    window.saveDraft = function() {
        const saveBtn = document.querySelector('.navbar .btn-primary');
        const originalText = saveBtn.innerHTML;
        saveBtn.innerHTML = '<i class="bi bi-hourglass-split"></i> Opslaan...';
        
        const formData = {
            // Ideale Klant
            ideal_client: document.querySelector('textarea[name="ideal_client"]').value,
            client_problem: document.querySelector('textarea[name="client_problem"]').value,
            client_goal: document.querySelector('textarea[name="client_goal"]').value,

            // Hero
            hero: selectedHero,
            hero_customization: {
                stands_for: document.querySelector('textarea[name="stands_for"]').value,
                stands_against: document.querySelector('textarea[name="stands_against"]').value,
                flaws: document.querySelector('textarea[name="flaws"]').value
            },

            // Brand Pillars
            brand_pillars: {
                stands_for: document.querySelector('textarea[name="brand_stands_for"]').value,
                stands_against: document.querySelector('textarea[name="brand_stands_against"]').value,
                principles: document.querySelector('textarea[name="principles"]').value
            },

            // Brand Identity
            tone_of_voice: document.querySelector('textarea[name="tone_of_voice"]').value,
            visual_identity: document.querySelector('textarea[name="visual_identity"]').value,
            visual_style: document.querySelector('textarea[name="visual_style"]').value,

            // Offer & Behavior
            offer: document.querySelector('textarea[name="offer"]').value,
            offer_principles: document.querySelector('textarea[name="offer_principles"]').value,
            behavior: document.querySelector('textarea[name="behavior"]').value,

            // Why & Mission
            why: document.querySelector('textarea[name="why"]').value,
            mission: {
                long: document.querySelector('textarea[name="mission_long"]').value,
                short: document.querySelector('textarea[name="mission_short"]').value
            },

            // Additional Elements
            enemies: document.querySelector('textarea[name="enemies"]').value,
            slogans: document.querySelector('textarea[name="slogans"]').value,
            brand_summary: document.querySelector('textarea[name="brand_summary"]').value
        };

        fetch('/api/save-draft', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData)
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                saveBtn.innerHTML = '<i class="bi bi-check-lg"></i> Opgeslagen';
                saveBtn.classList.add('btn-success');
                
                setTimeout(() => {
                    saveBtn.innerHTML = originalText;
                    saveBtn.classList.remove('btn-success');
                }, 2000);
            } else {
                throw new Error(data.error || 'Saving failed');
            }
        })
        .catch(error => {
            saveBtn.innerHTML = '<i class="bi bi-exclamation-triangle"></i> Fout';
            saveBtn.classList.add('btn-danger');
            
            setTimeout(() => {
                saveBtn.innerHTML = originalText;
                saveBtn.classList.remove('btn-danger');
            }, 2000);
            
            console.error('Error:', error);
        });
    };

    window.generatePDF = function() {
        const guide_id = window.location.pathname.split('/').pop();
        window.location.href = `/generate-pdf/${guide_id}`;
    };
});
