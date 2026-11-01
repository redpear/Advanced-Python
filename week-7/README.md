# Module 7: Hyperparameter Tuning

## Advanced Python – Critical Thinking Assignment

### Project Description

For this assignment, I used the Iris dataset to practice hyperparameter tuning with machine learning. The goal was to find the best k value for the K-Nearest Neighbors (KNN) classification algorithm.

The Iris dataset contains 150 flower samples with four measurements for each flower. The flowers are classified into three different species.

### Python Libraries Used

- Python 3
- Scikit-learn
- NumPy

### How the Program Works

1. Load the Iris dataset using `load_iris()`.
2. Separate the flower measurements and target classifications.
3. Create a loop to test k values from 1 to 20.
4. Use `KNeighborsClassifier` to create a model for each k value.
5. Use `StratifiedKFold` with 5 splits to divide the dataset into training and testing groups.
6. Use `cross_val_score()` to calculate the accuracy for each k value.
7. Calculate the average accuracy for each value of k.
8. Find the k value with the highest average accuracy.
9. Display the results.

### How to Run the Program

First, install the required Python libraries using the terminal:

```bash
python3 -m pip install scikit-learn numpy
```

Run the Python program:

```bash
python3 iris_knn.py
```

### Program Results

After running the program, the best k value was 15, with an average cross-validation accuracy of 98%.

- Best k value: 15
- Average accuracy: 98%
- Number of samples