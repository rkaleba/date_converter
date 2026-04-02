# Date Converter

A Python tool to convert dates from Notion to Excel format - 'Month DD, YYYY' to 'YYYY-MM-DD'. It reades a filename.csv file containing a single column of 'Month DD, YYYY' and it writes it to filename_converted.csv with a column of 'YYYY-MM-DD'. Empty rows stay empty.

## Requirements
- Python 3.13
- No external packages required

## Setup
1. Clone the repository
2. Create conda environment: `conda create --name date-converter python=3.13`
3. Activate environment: `conda activate date-converter`

## Usage
Run the main script:
`python main.py filename.csv`