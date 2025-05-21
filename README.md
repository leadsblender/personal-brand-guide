# Personal Brand Guide Generator

Een interactieve web applicatie voor het maken van een professional personal brand guide met behulp van superhelden archetypes.

## 🌟 Features

- **Superheld Archetypes**: Kies uit verschillende superhelden en pas hun eigenschappen aan voor jouw brand
- **Stapsgewijs Proces**: Volg een gestructureerd proces om je brand te ontwikkelen
- **Automatisch Opslaan**: Je voortgang wordt automatisch opgeslagen terwijl je werkt
- **PDF Export**: Genereer een professionele PDF van je brand guide
- **Responsive Design**: Werkt perfect op zowel desktop als mobiele apparaten

## 🚀 Installatie

1. Clone de repository:
```bash
git clone https://github.com/yourusername/personal-brand-guide.git
cd personal-brand-guide
```

2. Maak een virtuele omgeving aan:
```bash
python -m venv venv
```

3. Activeer de virtuele omgeving:
```bash
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

4. Installeer de benodigde packages:
```bash
pip install -r requirements.txt
```

5. Start de applicatie:
```bash
python run.py
```

De applicatie is nu beschikbaar op http://localhost:5002

## 🛠 Technische Vereisten

- Python 3.8+
- Flask
- SQLAlchemy
- WeasyPrint (voor PDF generatie)
- Bootstrap 5
- Modern webbrowser

## 🏗 Project Structuur

```
personal_brand_guide/
├── src/
│   ├── config/
│   │   └── heroes.py         # Superhelden configuratie
│   ├── models/
│   │   └── __init__.py      # Database models
│   ├── routes/
│   │   ├── brand_guide.py   # Hoofdroutes
│   │   └── pdf.py          # PDF generatie routes
│   └── __init__.py          # App configuratie
├── static/
│   ├── css/
│   │   └── style.css       # Applicatie styling
│   └── js/
│       └── main.js         # Frontend logica
├── templates/
│   ├── index.html          # Hoofdtemplate
│   └── pdf_template.html   # PDF export template
├── instance/               # Database directory
├── requirements.txt        # Python dependencies
└── run.py                 # Start script
```

## 📝 Gebruik

1. Start de applicatie en ga naar http://localhost:5002
2. Kies een superheld die jouw brand vertegenwoordigt
3. Definieer je ideale klant
4. Vul de brand guide secties in:
   - Brand pilaren
   - Tone of voice
   - Visuele identiteit
   - Aanbod principes
   - Gedrag
   - Waarom/Missie
   - Vijanden
   - Slogans
5. Download je brand guide als PDF

## 🤝 Bijdragen

1. Fork het project
2. Maak een feature branch (`git checkout -b feature/nieuw-feature`)
3. Commit je wijzigingen (`git commit -am 'Voeg nieuw feature toe'`)
4. Push naar de branch (`git push origin feature/nieuw-feature`)
5. Open een Pull Request

## 📄 License

Dit project is gelicenseerd onder de MIT License - zie het [LICENSE](LICENSE) bestand voor details.

## 👏 Credits

- Superhelden informatie gebaseerd op DC Comics en Marvel Comics
- Bootstrap voor de frontend styling
- WeasyPrint voor PDF generatie

## 📞 Support

Als je problemen tegenkomt of vragen hebt:
1. Check de [Issues](https://github.com/yourusername/personal-brand-guide/issues) pagina
2. Open een nieuwe issue met een duidelijke beschrijving
3. Voeg relevante screenshots of error messages toe

## 🔄 Updates

- v1.0.0 - Eerste release
  - Stapsgewijs brand guide proces
  - Superhelden selectie
  - PDF export functionaliteit