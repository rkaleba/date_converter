import sys
from src.converter import process_file

def main():
    input_file = sys.argv[1]
    output_file = input_file.replace(".csv", "_converted.csv")
    process_file(input_file,output_file)

if __name__ == "__main__":
    main()