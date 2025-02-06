import pandas as pd
import os

# Directory containing your XLSX files
input_folder = r"C:\Users\Public\Documents\NTD Dashboard\Database Data\2020\xlsx"
output_folder = r"C:\Users\Public\Documents\NTD Dashboard\Database Data\2020\csv"

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Convert all XLSX files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".xlsx"):
        file_path = os.path.join(input_folder, filename)
        output_file = os.path.join(output_folder, filename.replace(".xlsx", ".csv"))

        # Read and convert to CSV
        df = pd.read_excel(file_path, engine='openpyxl')
        df.to_csv(output_file, index=False)

print("Conversion completed!")
