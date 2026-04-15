def clean_data(df):
    print("\nMissing Values:\n", df.isnull().sum())
    
    df = df.dropna()
    
    print("\nDuplicates:", df.duplicated().sum())
    df = df.drop_duplicates()
    
    return df