from flask import render_template, request, redirect, url_for
import json
import os

from . import app

# Charger les paramètres depuis le fichier JSON
def load_parameters():
    try:
        if os.path.exists('config.json'):
            with open('config.json', 'r') as file:
                return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        pass
    return {}

# Sauvegarder les paramètres dans le fichier JSON
def save_parameters(parameters):
    with open('config.json', 'w') as file:
        json.dump(parameters, file)

@app.route('/')  # Route pour la page d'accueil
def index():
    parameters = load_parameters()
    
    available_cores = int(parameters["nbr_hosts"] * parameters["host_nbr_core"] * (1 - (parameters["reservation"] / 100)))
    available_ram = int(parameters["nbr_hosts"] * parameters["host_nbr_ram"] * (1 - (parameters["reservation"] / 100)))
    vm_by_core = int(available_cores / parameters["vm_nbr_core"])
    vm_by_ram = int(available_ram / parameters["vm_nbr_ram"])
    return render_template('index.html', parameters=parameters, vm_count=min(vm_by_core, vm_by_ram))

@app.route('/edit_all', methods=['GET', 'POST'])  # Route pour modifier tous les paramètres
def edit_all():
    """Modifier tous les paramètres sur une seule page."""
    parameters = load_parameters()  # Charger les paramètres
    if request.method == 'POST':
        # Mettre à jour tous les paramètres
        for key in parameters.keys():
            new_value = request.form.get(key)
            if not new_value or not new_value.isdecimal() or int(new_value) <= 0:
                return render_template('edit_all.html', parameters=parameters, error=f"Veuillez entrer un nombre valide pour {key}.")
            parameters[key] = int(new_value)
        save_parameters(parameters)  # Sauvegarder les paramètres
        return redirect(url_for('index'))
    return render_template('edit_all.html', parameters=parameters)

