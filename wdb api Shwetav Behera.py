from flask import Flask, jsonify, request

# create a locally run app on http://127.0.0.1:8000/
app = Flask(__name__)

# data of my completed modules and their results
module = [
    {
        'name': 'gan',
        'noten': [
            {
                'pruefung_1': 5.8,
                'pruefung_2': 4.4,
                'portfoliogespraech': 6
            }
        ]
    },
    {
        'name': 'gla',
        'noten': [
            {
                'pruefung_1': 4.8,
                'pruefung_2': 3.4,
                'portfoliogespraech': 6
            }
        ]
    },
    {
        'name': 'eda',
        'noten': [
            {
                'pruefung_1': 3,
                'pruefung_2': 5.25
            }
        ]
    },
    {
        'name': 'wer',
        'noten': [
            {
                'pruefung_1': 4.8
            }
        ]
    },
    {
        'name': 'mag',
        'noten': [
            {
                'pruefung_1': 3.8
            }
        ]
    },
    {
        'name': 'ced1',
        'noten': [
            {
                'pruefung_1': 5.5
            }
        ]
    },
    {
        'name': 'gds',
        'noten': [
            {
                'pruefung_1': 5.1
            }
        ]
    },

]

# define home page
@app.route('/')
def home():
    return "Noten Api"

# define create action
@app.route('/modul', methods=['POST'])
def create_modul():
    request_data = request.get_json()
    new_modul = {
        'name': request_data['name'],
        'noten': []
    }
    module.append(new_modul)
    return jsonify(new_modul)

# get module
@app.route('/modul/<string:name>')
def get_modul_name(name):
    for modul in module:
        if(modul['name'] == name):
            return jsonify(modul)
    return jsonify({'message': 'module not found'})

# get all module names
@app.route('/modul')
def get_all_modul_name():
    return jsonify({'module': module})

# create results for existing modules
@app.route('/modul/<string:name>/note', methods=['POST'])
def create_modul_note(name):
    request_data = request.get_json()
    for modul in module:
        if(modul['name'] == name):
            new_note = {
                'pruefung_1': request_data['pruefung_1'],
                'pruefung_2': request_data['pruefung_2'],
                'portfoliogespraech': request_data['portfoliogespraech']
            }
            modul['noten'].append(new_note)
            return jsonify(new_note)
    return jsonify({'message':'module not found'})

# get results of existing module
@app.route('/modul/<string:name>/note')
def get_modul_note(name):
    for modul in module:
        if(modul['name'] == name):
            return jsonify(modul['noten'])
    return jsonify({'message': 'module not found'})


app.run(port=8000)