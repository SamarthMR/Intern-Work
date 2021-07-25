# OVERFITTING

### Over fitting is a term defined in machine learning which is used when a model is trained on a dataset so closely that it negatively impacts the performance of the model on a new dataset.

### In Over fitting we try to train the data so much that it should match every point on the data set and with so much attributes and so much complex training model. So it creates a problem for new data points to fit in the model. The problem is that these concepts do not apply to new data and negatively impact the models ability to generalize.

### Let’s try to understand it with an example:-

### Let’s say we have to predict where the given item is a ball or not and we have defined too many parameters for that like:-

1. It should be spherical in shape
1. It should have a radius of 5cm
1. It should not be fruit
1. It should not be an eatable
1. It should bounce with a speed of 5m/s.

### And many more parameters and we try to fit the training model with every data point and gets a model shown below.

### As we can see that the above model and very complex and try to fit every data point and hence it makes very difficult for a new data point to fit into the model.

# Methods to overcome Overfitting
<ol>   How to prevent:
<li>Cross-validation</li>
<li>Remove features</li>
<li>Early Stopping</li>
<li>Regularization</li>
<li>Ensembling</li>
<li>Hold out </li>
<li>Data Augmentation</li>
<li>Drop out</li>
</ol>
<h4>Cross-validation:</h4>
<p>Cross-validation is a powerful preventative method for overfitting . To overcome overfitting we can split our dataset into k groups
(K-fold Cross-validation).We let one of the groupsto be the testing set
and others as training set. We repeat this until each individual
group has been used as testing set </p>
<h4>Remove features:</h4>
<p>If we have large amount of features in our dataset,we should just use most important features 
for training.  We should remove unnecessary features which can be cause of overfitting. </p>
<h4>Early Stopping:</h4>
<p>We can first train our model for an arbitrary large number of
epochs and plot the validation loss graph. Once validation loss
start to degrade, we stop to train our model . It can be implemented 
by monitoring loss graph or set an early stopping trigger. </p>

<h4>Regularization:</h4>
<p>It is technique to constrain network from learning complex model
which may therefore overfit. We can add penalty terms on cost function to push estimated coefficients towards zero.
We normally use L2 regularization which allows weights to push to zero but not exactly zero.</p>

<h4>Hold out: </h4>
<p>Rather than using full dataset we can simply split our dataset into test set and train set.
We normally follow common split ratio -80%(training set) and 20%(testing set).We train our model until it performs well not only training set but also for testing set.This approach would require
an enough large dataset to train on even after splitting  .</p>

<h4>Dropout:</h4>
<p>By applying dropout to our layers, we just ignore a subset of units of our networkwith a set probability. 
We can reduce interdependent learning among units, which can be cause of overfitting. 
With dropout, we need need more epochs for our model to converge.
</p>

# Effects and Impacts of Overfitting
### If our model does much better on the training set than on the test set, then we’re likely overfitting.

## Consequences

The most obvious consequence of overfitting is poor performance on the validation dataset. Other negative consequences include :

* A function that is overfitted is likely to request more information about each item in the validation dataset than does the optimal function; gathering this additional unneeded data can be expensive or error-prone, especially if each individual piece of information must be gathered by human observation and manual data-entry.

* A more complex, overfitted function is likely to be less portable than a simple one. At one extreme, a one-variable linear regression is so portable that, if necessary, it could even be done by hand. At the other extreme are models that can be reproduced only by exactly duplicating the original modeler's entire setup, making reuse or scientific reproduction difficult.

## How to prevent Overfitting
1. ### Training with more data
    + One of the ways to prevent overfitting is by training with more data. Such an option makes it easy for algorithms to detect the signal better to minimize errors. As the user feeds more training data into the model, it will be unable to overfit all the samples and will be forced to generalize to obtain results.
    + Users should continually collect more data as a way of increasing the accuracy of the model. However, this method is considered expensive, and, therefore, users should ensure that the data being used is relevant and clean.
 
2. ### Data augmentation
    + An alternative to training with more data is data augmentation, which is less expensive compared to the former. If you are unable to continually collect more data, you can make the available data sets appear diverse.
    + Data augmentation makes a sample data look slightly different every time it is processed by the model. The process makes each data set appear unique to the model and prevents the model from learning the characteristics of the data sets.
    + Another option that works in the same way as data augmentation is adding noise to the input and output data. Adding noise to the input makes the model become stable, without affecting data quality and privacy, while adding noise to the output makes the data more diverse. However, noise addition should be done with moderation so that the extent of the noise is not so much as to make the data incorrect or too different.
 
3. ### Data simplification
    + Overfitting can occur due to the complexity of a model, such that, even with large volumes of data, the model still manages to overfit the training dataset. The data simplification method is used to reduce overfitting by decreasing the complexity of the model to make it simple enough that it does not overfit.
    + Some of the actions that can be implemented include pruning a decision tree, reducing the number of parameters in a neural network, and using dropout on a neutral network. Simplifying the model can also make the model lighter and run faster.
 
4. ### Ensembling
    + Ensembling is a machine learning technique that works by combining predictions from two or more separate models. The most popular ensembling methods include boosting and bagging.
    + Boosting works by using simple base models to increase their aggregate complexity. It trains a large number of weak learners arranged in a sequence, such that each learner in the sequence learns from the mistakes of the learner before it.
    + Boosting combines all the weak learners in the sequence to bring out one strong learner. The other ensembling method is bagging, which is the opposite of boosting. Bagging works by training a large number of strong learners arranged in a parallel pattern and then combining them to optimize their predictions.