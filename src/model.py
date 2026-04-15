from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def train_model(df):
    
    X = df[['degree_p']]   # you can add more features later
    y = df['status']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = LogisticRegression()
    model.fit(X_train, y_train)

    accuracy = model.score(X_test, y_test)

    print("\nModel Accuracy:", accuracy)