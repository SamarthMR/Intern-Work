# *Underfitting* 

`*Table of Contents*`

* _*Introduction*_
* _*What is Underfitting ?*_
* _*Underfitting vs Overfitting*_
* _*Example for Underfitting*_
* _*How to avoid Underfitting ?*_
* _*Conclusion*_


## *Introduction*
   If we consider we are designing a machine learning model. A model is said to be a good machine learning model if it generalizes the input data to get the outcome in a proper way. This helps us in classification and also to make predictions in the future data that the data model has never seen.

   Now, if we want to check how well the machine learning model trains and generalizes to the new data. For that we have overfitting and underfitting, which are responsible for the poor performance of the machine learning algorithms.

## *What is Underfitting*
   Underfitting occurs in data science where a data model is unable to capture the underlying trend of the data. It results in generating a high error rate on both the training set and unseen data. It occurs when a model is very simple(the input features are not expressive enough), which results in model needing more time for training, less regularization and more input features.  when a model is underfitted, it will have training errors and poor performance. If a model is unable to generalize well to new data, then it cannot be good for classification or prediction tasks. A model is a good machine learning model if it generalizes any new input data from the problem every day to make predictions and classify data.
   Low variance and high bias are good indicators of underfitting.


## *Underfitting vs Overfitting*
  * To be simple, overfitting is the opposite of underfitting. It occurs when the model is overtrained or it contains too much complexity, because of this it results in high error rates on test data. Overfitting a model is more common than underfitting one.
  * As mentioned above, the model is underfitting when it performs poorly on the training data. This is because the model is unable to capture the relationship between the input examples and the target values accurately.
  * The model is overfitting your training data when you see that the model performs well on the training data but does not perform well on the evaluation data. This is because the model is unable to generalize to unseen examples and memorizing the data it has seen.
  * Underfitted models are usually easier to identify compared to overfitted ones as their behaviour can be seen while using training data set.
  
   Below is an illustration of the different ways a regression can potentially fit against unseen data:
   ![UNDERFITTING.PNG](https://github.com/DeekshithaKusupati/Intern-Work/blob/main/int-ml-3/Underfitting/Images/UNDERFITTING.png)
## *Example*
Now let us see the example that demonstrates the problems of underfitting and overfitting and how we can use linear regression with polynomial features to approximate nonlinear functions. 

The plot shows the function that we want to approximate, which is a part of the cosine function. In addition, the samples from the real function and the approximations of different models are displayed. The models have polynomial features of different degrees. We can see that a linear function (polynomial with degree 1) is not sufficient to fit the training samples. This is called underfitting. A polynomial of degree 4 approximates the true function almost perfectly. However, for higher degrees the model will overfit the training data, i.e. it learns the noise of the training data. We evaluate quantitatively overfitting or underfitting by using cross-validation. We calculate the mean squared error (MSE) on the validation set, the higher, the less likely the model generalizes correctly from the training data.


```python
print(__doc__)

import numpy as np
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score


def true_fun(X):
    return np.cos(1.5 * np.pi * X)

np.random.seed(0)

n_samples = 30
degrees = [1, 4, 15]

X = np.sort(np.random.rand(n_samples))
y = true_fun(X) + np.random.randn(n_samples) * 0.1

plt.figure(figsize=(14, 5))
for i in range(len(degrees)):
    ax = plt.subplot(1, len(degrees), i + 1)
    plt.setp(ax, xticks=(), yticks=())

    polynomial_features = PolynomialFeatures(degree=degrees[i],
                                             include_bias=False)
    linear_regression = LinearRegression()
    pipeline = Pipeline([("polynomial_features", polynomial_features),
                         ("linear_regression", linear_regression)])
    pipeline.fit(X[:, np.newaxis], y)

    # Evaluate the models using crossvalidation
    scores = cross_val_score(pipeline, X[:, np.newaxis], y,
                             scoring="neg_mean_squared_error", cv=10)

    X_test = np.linspace(0, 1, 100)
    plt.plot(X_test, pipeline.predict(X_test[:, np.newaxis]), label="Model")
    plt.plot(X_test, true_fun(X_test), label="True function")
    plt.scatter(X, y, edgecolor='b', s=20, label="Samples")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.xlim((0, 1))
    plt.ylim((-2, 2))
    plt.legend(loc="best")
    plt.title("Degree {}\nMSE = {:.2e}(+/- {:.2e})".format(
        degrees[i], -scores.mean(), scores.std()))
plt.show()
```
![untitled1.png](https://github.com/DeekshithaKusupati/Intern-Work/blob/main/int-ml-3/Underfitting/Images/underfitting1.png)

## *How to avoid underfitting*
Since we can detect underfitting while using the training set, we can assist in establishing accurate relationship between the input and target variables. we can avoid underfitting and make more accurate predictions by maintaining required complexity.

Below are a few techniques that can be used to reduce underfitting:
 #### *1. Decrease regularization*
   Regularization is usually used to reduce the variance with a model by applying a penalty to the input parameters with the larger coefficients. There are a number of different methods in machine learning which helps to reduce the noise and outliers in a model. By decreasing the amount of regularization, increasing complexity and variation is introduced into the model for successful training of the model.
 #### *2. Increase the Duration of the training*
   Training the model for less time can also result in underfit model that is to try to train the model for more epochs. Ensuring that the loss is decreases gradually over the course of training. However, it is important to make sure that it should not lead to overtraining, and subsequently, overfitting. Finding the balance between the two will be key.
 #### *3. Feature selection*
   There will be a specific features in any model that can be used to determine a required outcome. If there are not enough predictive features present, then more features with greater importance or more features, should be introduced. This process can increase the complexity of the model, resulting in getting better training results.
## *Conclusion* 
 The get a good machine learning model with a good fit it should be between the underfitted and overfitted model, so that it can make accurate predictions.

 when we train our model for a particular time, the errors in the training data and testing data go down. But if we train the model for a long duration of time, then overfitting occurs which reduce the performance of model, as the model also learn the noise present in the dataset. The errors in the test dataset start increasing, so the point, just before the raising of errors, is the good point, and we can stop here for achieving a good model. 
 
### *By : Kusupati Deekshitha , Subham Nanda*
 
  
