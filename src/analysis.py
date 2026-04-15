def basic_analysis(df):
    print("\nShape:", df.shape)
    print("\nColumns:", df.columns)

    print("\nStatistical Summary:\n", df.describe())

    print("\nPlacement Count:\n", df['status'].value_counts())

    placed = df[df['status'] == 'Placed'].shape[0]
    total = df.shape[0]

    print("\nPlacement Rate:", (placed / total) * 100)