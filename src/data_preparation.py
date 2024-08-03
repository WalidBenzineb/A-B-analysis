import pandas as pd
import numpy as np

def load_data(file_path):
    """
    Load the dataset from a CSV file.
    
    Args:
    file_path (str): Path to the CSV file
    
    Returns:
    pd.DataFrame: Loaded dataset
    """
    return pd.read_csv(file_path)

def clean_data(df):
    """
    Clean the dataset by handling missing values and data types.
    
    Args:
    df (pd.DataFrame): Input dataframe
    
    Returns:
    pd.DataFrame: Cleaned dataframe
    """
    print("Columns in the dataset:", df.columns.tolist())
    
    # Convert 'converted' to boolean
    df['converted'] = df['converted'].astype(bool)
    
    # Convert 'total ads' to integer
    df['total ads'] = df['total ads'].astype(int)
    
    # Convert 'most ads hour' to integer if it's not already
    df['most ads hour'] = pd.to_numeric(df['most ads hour'], errors='coerce').astype('Int64')
    
    # Handle any missing values (if applicable)
    # df = df.dropna()  # Uncomment this line if you want to drop rows with missing values
    
    return df

def create_features(df):
    """
    Create new features from existing data.
    
    Args:
    df (pd.DataFrame): Input dataframe
    
    Returns:
    pd.DataFrame: Dataframe with new features
    """
    # Create a feature for whether a user saw ads during peak hours (assuming 9-17 is peak)
    df['peak_hour_ads'] = df['most ads hour'].between(9, 17)
    
    # Create a feature for weekend vs weekday ads
    df['weekend_ads'] = df['most ads day'].isin(['Saturday', 'Sunday'])
    
    return df

def prepare_data(file_path):
    """
    Main function to load, clean, and prepare the data.
    
    Args:
    file_path (str): Path to the CSV file
    
    Returns:
    pd.DataFrame: Prepared dataframe
    """
    df = load_data(file_path)
    print("Data loaded. Shape:", df.shape)
    print("Columns:", df.columns.tolist())
    print("\nSample data:")
    print(df.head())
    print("\nData types:")
    print(df.dtypes)
    
    df = clean_data(df)
    df = create_features(df)
    return df