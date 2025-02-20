This repository is a convenient place to hold and document the UHSSS Lab research materials for XR Zero Input Authentication research.

### Data
You can import your own experiment data files to be analyzed, but there is a strict folder structure.\
```python
| data # can be anything, just rename it in the globals in the workbook
|─ 1 # represents the first participant
|  |─ controller # all data in here is controller data for the participant
|     |─ 1 # represents the first experiment 
|        |─ <x>.csv # represents the actual file with the experiment data
|        |─ ...
|  |─ hand # all data in here is hand data for the participant
|     |─ 1
|        |─ <x>.csv
|        |─ ...
|─ 2
|  |─ ...
|─ ...
```
The sample data that comes with this repository also can be used as reference.

### Files
`cleanup_data.py` is a handy script that will run through a `data` folder with a very specific folder structure and
remove duplicate data entries, prioritizing the files with the largest size.

`classification_workbook.ipynb` is the jupyter notebook where the machine learning data analysis is done.\
Global variables can be set to suit your needs (different data folder names, features, etc.) as well as the code logic iteself, if needed.

### Using this workbook
To use this workbook:
- Create a virtual environment (venv or conda)
- Use the `requirements.txt` file to install dependencies
- Run your code in `classification_workbook.ipynb` with experimental modifications as needed
