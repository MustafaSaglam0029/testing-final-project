# Testing-Final-Project

Testing-Final_Project  is created to test 3 different fastapi endpoints and their functions.

## Installation

'''bash
pip install pyscopg2
pip install uvicorn
pip install pytest
pip install pytest-cov
'''

## Usage
Set your pythonpath as pytest like  "PYTHONPATH=./ pytest" to avoid import issues.
You should test in terminal
Usage example: pytest tests/integration_testing/mandate_data_itt.py

If you want to use the coverage set your pythonpath "PYTHONPATH=./ pytest --cov=src tests/" to avoid import issues
Usage example: pytest --cov=src/meter_data tests/integration_testing/meter_data_itt.py

## Contributing
Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## Authors 
Mustafa Saglam
Thanks to valuable contributions of David Bros




