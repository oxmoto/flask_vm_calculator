# PremierProjetWebApp

This project is a web application built using Flask, designed to manage and configure parameters for a cluster of virtual machines.

## Project Structure

```
PremierProjetWebApp
├── app
│   ├── __init__.py          # Initializes the Flask application and sets up routes
│   ├── routes.py            # Contains route definitions for the web application
│   ├── static
│   │   └── style.css        # CSS styles for the web application
│   └── templates
│       ├── base.html        # Base template for the web application
│       ├── index.html       # Main page displaying the current state
│       └── config.html      # Page for displaying and editing configuration parameters
├── config.json              # Configuration parameters in JSON format
├── requirements.txt         # Lists dependencies required for the project
└── README.md                # Documentation for the project
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd PremierProjetWebApp
   ```

2. **Install dependencies:**
   It is recommended to use a virtual environment. You can create one using:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
   Then install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. **Run the application:**
   You can start the Flask application by running:
   ```
   flask run
   ```
   The application will be accessible at `http://127.0.0.1:5000/`.

## Usage

- Navigate to the main page to view the current configuration of the cluster.
- Use the configuration page to edit parameters such as the number of hosts, reservation percentages, and VM specifications.
- Changes will be saved to `config.json` for persistence.

## License

This project is licensed under the MIT License.