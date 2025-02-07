import pandas as pd
import os


def clean_agency_information_csv(
    input_csv, output_csv="2023_Agency_Information_cleaned.csv"
):
    """
    Reads the CSV from 'input_csv', performs typical cleaning
    operations, and writes the cleaned DataFrame to 'output_csv'.
    """
    # 1. Load CSV from the local file path
    df = pd.read_csv(input_csv)
    print("CSV loaded successfully. Number of rows:", len(df))

    # 2. Standardize column names:
    #    - Lowercase
    #    - Replace spaces with underscores
    #    - Strip any extra whitespace or parentheses
    df.columns = [
        col.strip().lower().replace(" ", "_").replace("(", "").replace(")", "")
        for col in df.columns
    ]
    print("Standardized columns:", df.columns.tolist())

    # 3. Drop any completely empty rows (optional)
    df.dropna(how="all", inplace=True)

    # 4. Remove duplicate rows
    before_dedup = len(df)
    df.drop_duplicates(inplace=True)
    after_dedup = len(df)
    print(f"Dropped {before_dedup - after_dedup} duplicate row(s).")

    # 5. Trim leading and trailing whitespace in all string columns
    str_cols = df.select_dtypes(include="object").columns
    for col in str_cols:
        df[col] = df[col].astype(str).str.strip()

    # 6. Replace common placeholder values with proper NaN
    df.replace(
        to_replace=["N/A", "NA", "null", "", "None", "?", "nan"],
        value=pd.NA,
        inplace=True,
    )

    # 7. (Optional) Convert columns to numeric or datetime if needed
    # if 'column_name_that_should_be_numeric' in df.columns:
    #     df['column_name_that_should_be_numeric'] = pd.to_numeric(
    #         df['column_name_that_should_be_numeric'], errors='coerce'
    #     )
    #
    # if 'column_name_that_should_be_a_date' in df.columns:
    #     df['column_name_that_should_be_a_date'] = pd.to_datetime(
    #         df['column_name_that_should_be_a_date'], errors='coerce'
    #     )

    # 8. (Optional) Rename columns for clarity
    # df.rename(columns={'original_column_name': 'new_column_name'}, inplace=True)

    # 9. Export cleaned DataFrame to a new CSV
    df.to_csv(output_csv, index=False)
    print(f"Cleaned CSV written to '{output_csv}'. Final row count: {len(df)}")


if __name__ == "__main__":
    INPUT_FILE = (
        "/Users/jaywon/Downloads/TransPro/NTD Project/"
        "NTD_Dataset/2023/csv_raw/2023 Agency Information.csv"
    )

    # Change the output filename if desired
    OUTPUT_FILE = "/Users/jaywon/Downloads/TransPro/NTD Project/NTD_Dataset/2023/csv_cleaned/2023 Agency Information.csv"

    # Make sure the file path exists (optional check)
    if not os.path.isfile(INPUT_FILE):
        print(f"Error: File not found at '{INPUT_FILE}'")
    else:
        clean_agency_information_csv(INPUT_FILE, OUTPUT_FILE)
