# Sales Analysis Project

This project simulates sales data, uploads it to a MySQL database, and analyzes it using Python.

## Folder Structure

Sales-analysis-project/
│
├── data/
│ └── sales_data.csv # The generated sales data
│
├── notebooks/
│ ├── 01_generate_data.ipynb # Generate and save synthetic data
│ ├── 02_upload_to_mysql.ipynb # Upload data to MySQL
│ └── 03_visualize_sales.ipynb # Visualize sales data
│
├── scripts/
│ └── upload_to_mysql.py # Script version for uploading data
│
├── README.md
├── .gitignore
└── requirements.txt




## Requirements

- Python 3
- MySQL
- Libraries: `pandas`, `numpy`, `matplotlib`, `mysql-connector-python`

## Steps

1. Run `01_generate_data.ipynb` to generate and save the data.
2. Ensure MySQL database and table are created.
3. Run `02_upload_to_mysql.ipynb` or `upload_to_mysql.py` to insert data.
4. Run `03_visualize_sales.ipynb` to generate visual reports.
