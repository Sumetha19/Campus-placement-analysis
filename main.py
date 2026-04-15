from src.load_data import load_dataset
from src.data_cleaning import clean_data
from src.analysis import basic_analysis
from src.visualization import plot_graphs
from src.model import train_model

# Load data
df = load_dataset("E:\Campus placement analysis\data\Placement_Data_Full_Class.csv")

# Clean data
df = clean_data(df)

# Analysis
basic_analysis(df)

# Visualization
plot_graphs(df)

# Model
train_model(df)