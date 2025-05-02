import pandas as pd
from datasets import Dataset

def load_and_prepare(csv_path):
    df = pd.read_csv(csv_path)

    # Rename columns for clarity
    df = df.rename(columns={'question': 'input', 'sql': 'output'})

    # Add T5 prefix
    df['input'] = df['input'].apply(lambda x: f"translate English to SQL: {x}")

    # Convert to HuggingFace Dataset
    dataset = Dataset.from_pandas(df)
    return dataset


