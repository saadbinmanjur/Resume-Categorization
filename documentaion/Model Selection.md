# Choosing the Best Model for Resume Categorization

In this documentation, we will discuss the rationale behind selecting the Bagging model as the best choice for the given resume dataset and the analysis of the various models tested.

## Dataset Overview:
The dataset provided for this project contains resumes categorized into different domains. The goal is to train a model that can accurately predict the category of each resume. The dataset poses several challenges, such as a relatively low amount of data and an imbalance among different categories.

## Model Selection and Rationale:

### 1. LSTM (Underfitting):
   - The LSTM model performed poorly due to the limited amount of data available for training.
   - Neural networks, particularly deep models like LSTM, require large amounts of data to generalize well. The dataset's size likely contributed to underfitting on the validation set.

### 2. Multinomial Naive Bayes:
   - Achieved an accuracy of 51.80%.
   - Naive Bayes models are simple and work well for text classification tasks. However, their performance might be limited when handling more complex relationships in the data.

### 3. Logistic Regression:
   - Achieved an accuracy of 65.06%.
   - Logistic Regression is a common choice for text classification tasks. Its better performance compared to Naive Bayes suggests that it can capture more intricate relationships in the data.

### 4. Random Forest:
   - Achieved an accuracy of 69.47%.
   - Random Forest is an ensemble model that can handle non-linearity and interactions in the data. Its performance is encouraging but there's potential to explore more advanced ensemble techniques.

### 5. AdaBoost:
   - Achieved an accuracy of 19.67%.
   - AdaBoost underperformed significantly, possibly due to the complex nature of the dataset. AdaBoost focuses on difficult-to-classify samples, but the data might not fit its assumptions.

### 6. Extra Trees:
   - Achieved an accuracy of 59.43%.
   - Extra Trees is another ensemble model that builds multiple decision trees and combines their predictions. While it's better than some models, it didn't outperform others by a large margin.

### 7. KNeighbors:
   - Achieved an accuracy of 57.42%.
   - k-Nearest Neighbors relies on the proximity of data points. In this case, the imbalance in the dataset might have affected its performance.

### Bagging: The Highest Score Model
   - Achieved the highest accuracy of 71.08%.
   - Bagging (Bootstrap Aggregating) is an ensemble technique that trains multiple models on different subsets of the data and combines their predictions. It helps reduce overfitting and increase stability.
   - Given the dataset's challenges, including limited data and class imbalance, Bagging is likely performing well because it helps mitigate these issues. It's robust to noise and overfitting, and its ability to improve generalization might be especially valuable in this case.