import seaborn as sns
import matplotlib.pyplot as plt

def plot_graphs(df):
    
    # Placement Count
    sns.countplot(x='status', data=df)
    plt.title("Placement Distribution")
    plt.show()

    # Gender vs Placement
    sns.countplot(x='gender', hue='status', data=df)
    plt.title("Gender vs Placement")
    plt.show()

    # Degree % vs Placement
    sns.boxplot(x='status', y='degree_p', data=df)
    plt.title("Degree % vs Placement")
    plt.show()

    # Salary Distribution
    sns.histplot(df['salary'], bins=20)
    plt.title("Salary Distribution")
    plt.show()