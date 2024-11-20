import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
def plot_roc_curve_from_dataset(file_path, target_column):
    # Step 1: Read dataset from CSV
    data = pd.read_csv(file_path)
    # Step 2: Separate features (X) and target (y)
    X = data.drop(columns=[target_column])
    y = data[target_column]
    # Step 3: Split dataset into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    # Step 4: Train a Logistic Regression model
    model = LogisticRegression()
    model.fit(X_train, y_train)
    # Step 5: Predict probabilities
    y_prob = model.predict_proba(X_test)[:, 1]
    # Step 6: Compute ROC curve and AUC
    fpr, tpr, thresholds = roc_curve(y_test, y_prob)
    roc_auc = auc(fpr, tpr)
    # Step 7: Plot the ROC curve
    plt.figure(figsize=(8, 6))
    plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (AUC = {roc_auc:.2f})')
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic (ROC) Curve')
    plt.legend(loc='lower right')
    plt.grid(True)
    plt.show()
# Example usage
file_path = r"C:\Users\HP\Desktop\dmt\input_dataset.csv" # Replace with your dataset file path
target_column = 'target'  # Replace with your target column name
plot_roc_curve_from_dataset(file_path, target_column)