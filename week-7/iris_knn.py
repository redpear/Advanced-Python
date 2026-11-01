from sklearn.datasets import load_iris
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.neighbors import KNeighborsClassifier

# Load the Iris flower measurements and labels
iris = load_iris()
X = iris.data
y = iris.target

# Use the same five splits for each k value
folds = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

best_k = None
best_score = -1
print('Iris KNN Hyperparameter Tuning')
print('Samples:', len(X), '| Features:', X.shape[1])
print('Testing k values from 1 to 20 using 5-fold cross-validation\n')
print('k Average accuracy  Standard deviation')
print('------------------------------------------')
for k in range(1, 21):
    model = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(model, X, y, cv=folds, scoring='accuracy')
    average = scores.mean()
    print(f'{k:2d}       {average:4f}        {scores.std():.4f}')
    if average > best_score:
        best_score = average
        best_k = k

    print(f'\nBest k:{best_k}')
    print(f'Best average cross-validation accuracy: {best_score:.2%}')
    print('If multiple k values tie, this program chooses the smallest one.')