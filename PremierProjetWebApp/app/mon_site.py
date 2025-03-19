#!/bin/env python3
"""
Correction du projet pour le stage de 2nd pro
"""
import json
import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Paramètres par défaut si le fichier de configuration n'existe pas
default_parameters = {
    "nbr_hosts": 2,
    "reservation": 20,
    "host_nbr_core": 10,
    "host_nbr_ram": 256,
    "vm_nbr_core": 2,
    "vm_nbr_ram": 4,
}
file_config = "config.json"

# Charger les paramètres au démarrage
if os.path.exists(file_config):
    with open(file_config, "r") as file:
        prog_param = json.load(file)
else:
    prog_param = default_parameters.copy()


def home():
    """Page d'accueil affichant les paramètres actuels."""
    value = calculate(prog_param)
    return render_template('index.html', parameters=prog_param, vm_count=value)


def edit_param(param_key):
    """Modifier un paramètre spécifique."""
    if request.method == 'POST':
        new_value = request.form.get('value')
        if not new_value.isdecimal() or int(new_value) <= 0:
            return render_template('edit.html', param_key=param_key, error="Veuillez entrer un nombre supérieur à 0.")
        prog_param[param_key] = int(new_value)
        save_param(file_config, prog_param)
        return redirect(url_for('home'))
    return render_template('edit.html', param_key=param_key)


def save():
    """Sauvegarder les paramètres dans le fichier JSON."""
    save_param(file_config, prog_param)
    return redirect(url_for('home'))


def calculate(parameters: dict) -> int:
    """Calculer le nombre de VM moyennes pouvant être créées."""
    available_cores = int(parameters["nbr_hosts"] * parameters["host_nbr_core"] * (1 - (parameters["reservation"] / 100)))
    available_ram = int(parameters["nbr_hosts"] * parameters["host_nbr_ram"] * (1 - (parameters["reservation"] / 100)))
    vm_by_core = int(available_cores / parameters["vm_nbr_core"])
    vm_by_ram = int(available_ram / parameters["vm_nbr_ram"])
    return min(vm_by_core, vm_by_ram)


def save_param(fichier_json: str, param: dict) -> None:
    """Sauvegarder les paramètres dans un fichier JSON."""
    with open(fichier_json, "w") as fileToWrite:
        json.dump(param, fileToWrite, sort_keys=True, indent=4)


if __name__ == '__main__':
    app.run(port=5000)