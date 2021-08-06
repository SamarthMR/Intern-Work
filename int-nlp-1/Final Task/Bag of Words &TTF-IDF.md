# Bag of Words
A simple model for converting natural languages into machine understandable representation.
The bag-of-words model is a simplifying representation used in natural language processing and information retrieval. 
In this model, a text is represented as the bag of its words, disregarding grammar and even word order but keeping multiplicity. 
The bag-of-words model has also been used for computer vision.

## What exactly is Bag of Words?
```
Bag of words is a Natural Language Processing technique of text modelling. In technical terms, 
we can say that it is a method of feature extraction with text data. This approach is a simple and flexible way of extracting features from documents.
A bag of words is a representation of text that describes the occurrence of words within a document. 
We just keep track of word counts and disregard the grammatical details and the word order. 
It is called a “bag” of words because any information about the order or structure of words in the document is discarded. 
The model is only concerned with whether known words occur in the document, not where in the document.
```
## Why is the Bag-of-Words algorithm used?
One of the biggest problems with text is that it is messy and unstructured, and machine learning algorithms prefer structured, 
well defined fixed-length inputs and by using the Bag-of-Words technique we can convert variable-length texts into a fixed-length vector.
Also, at a much granular level, the machine learning models work with numerical data rather than textual data. So to be more specific, 
by using the bag-of-words (BoW) technique, we convert a text into its equivalent vector of numbers.

## Detailed explanation of Bag of Words and why it is used

**Terms used :**

* Document       : A single written account(such as a particular review)
* Corpus         : A collection of documents
* Matrix         : A structure having rows and columns
* Vector         : Matrix with multiple rows and a single column
* Vocabulary     : A collection of words whose meaning is already known
* Feature Matrix : In this case, a matrix accounting for if the word is present or not

## Let’s Take an Example to Understand Bag-of-Words (BoW) and TF-IDF

we will take a popular example to explain Bag-of-Words (BoW) and TF-DF 

We all love watching movies (to varying degrees). 
I tend to always look at the reviews of a movie before I commit to watching it. I know a lot of you do the same! So, I’ll use this example here.

![image](https://user-images.githubusercontent.com/84801896/127963931-edcf84cb-89e0-4679-8cef-2537351c780a.png)

Image Source :https://medium.com/@MarynaL/analyzing-movie-review-data-with-natural-language-processing-7c5cba6ed922


### Here’s a sample of reviews about a particular horror movie:

Review 1: This movie is very scary and long
Review 2: This movie is not scary and is slow
Review 3: This movie is spooky and good

You can see that there are some contrasting reviews about the movie as well as the length and pace of the movie. 
Imagine looking at a thousand reviews like these. Clearly, there is a lot of interesting insights we can draw from them and build upon them to gauge how well the movie performed.
However, as we saw above, we cannot simply give these sentences to a machine learning model and ask it to tell us whether a review was positive or negative. 
We need to perform certain text preprocessing steps.

### Creating Vectors from Text

It should not result in a sparse matrix since sparse matrices result in high computation cost
We should be able to retain most of the linguistic information present in the sentence
Word Embedding is one such technique where we can represent the text using vectors. The more popular forms of word embeddings are:

BoW, which stands for Bag of Words
TF-IDF, which stands for Term Frequency-Inverse Document Frequency

Bag-of-Words and TF-IDF are two examples of how to do this. 

### Bag of Words (BoW) Model
The Bag of Words (BoW) model is the simplest form of text representation in numbers. Like the term itself, we can represent a sentence as a bag of words vector (a string of numbers).

Let’s recall the three types of movie reviews we saw earlier:

* Review 1: This movie is very scary and long
* Review 2: This movie is not scary and is slow
* Review 3: This movie is spooky and good

We will first build a vocabulary from all the unique words in the above three reviews. 
The vocabulary consists of these 11 words: ‘This’, ‘movie’, ‘is’, ‘very’, ‘scary’, ‘and’, ‘long’, ‘not’,  ‘slow’, ‘spooky’,  ‘good’.
We can now take each of these words and mark their occurrence in the three movie reviews above with 1s and 0s. This will give us 3 vectors for 3 reviews:


![image](https://user-images.githubusercontent.com/84801896/127963008-e18e58a1-6b74-48e2-9aa8-0c7e32609bfe.png)

Image Source :https://www.analyticsvidhya.com/blog/2020/02/quick-introduction-bag-of-words-bow-tf-idf/

``` 
Vector of Review 1: [1 1 1 1 1 1 1 0 0 0 0]
Vector of Review 2: [1 1 2 0 0 1 1 0 1 0 0]
Vector of Review 3: [1 1 1 0 0 0 1 0 0 1 1]
```

And that’s the core idea behind a Bag of Words (BoW) model.

### Drawbacks of using a Bag-of-Words (BoW) Model
In the above example, we can have vectors of length 11. However, we start facing issues when we come across new sentences:
If the new sentences contain new words, then our vocabulary size would increase and thereby, the length of the vectors would increase too.
Additionally, the vectors would also contain many 0s, thereby resulting in a sparse matrix (which is what we would like to avoid)
We are retaining no information on the grammar of the sentences nor on the ordering of the words in the text.

#### Term Frequency-Inverse Document Frequency (TF-IDF)

```
“Term frequency–inverse document frequency, is a numerical statistic that is intended to reflect how important 
a word is to a document in a collection or corpus.”
```

### Term Frequency (TF)
Let’s first understand Term Frequent (TF). It is a measure of how frequently a term, t, appears in a document, d:

### Term Frequency (tf) formula
![image](https://user-images.githubusercontent.com/84801896/127962168-402d5b75-b27e-4bcc-9138-933aa8ab81a4.png)

Here, in the numerator, n is the number of times the term “t” appears in the document “d”. Thus, each document and term would have its own TF value.

We will again use the same vocabulary we had built in the Bag-of-Words model to show how to calculate the TF for Review #2:

Review 2: This movie is not scary and is slow

Here,

Vocabulary: ‘This’, ‘movie’, ‘is’, ‘very’, ‘scary’, ‘and’, ‘long’, ‘not’,  ‘slow’, ‘spooky’,  ‘good’
Number of words in Review 2 = 8
TF for the word ‘this’ = (number of times ‘this’ appears in review 2)/(number of terms in review 2) = 1/8
Similarly,

* TF(‘movie’) = 1/8
* TF(‘is’) = 2/8 = 1/4
* TF(‘very’) = 0/8 = 0
* TF(‘scary’) = 1/8
* TF(‘and’) = 1/8
* TF(‘long’) = 0/8 = 0
* TF(‘not’) = 1/8
* TF(‘slow’) = 1/8
* TF( ‘spooky’) = 0/8 = 0
* TF(‘good’) = 0/8 = 0

We can calculate the term frequencies for all the terms and all the reviews in this manner:

![image](https://user-images.githubusercontent.com/84801896/127962421-fd176f9f-2b22-4c3b-aa9e-951fee19d7d5.png)

### Inverse Document Frequency (IDF)
IDF is a measure of how important a term is. We need the IDF value because computing just the TF alone is not sufficient to understand the importance of words:

## Inverser Document Frequency(IDF) formula

We can calculate the IDF values for the all the words in Review 2:
IDF(‘this’) =  log(number of documents/number of documents containing the word ‘this’) = log(3/3) = log(1) = 0

Similarly,

IDF(‘movie’, ) = log(3/3) = 0
IDF(‘is’) = log(3/3) = 0
IDF(‘not’) = log(3/1) = log(3) = 0.48
IDF(‘scary’) = log(3/2) = 0.18
IDF(‘and’) = log(3/3) = 0
IDF(‘slow’) = log(3/1) = 0.48
We can calculate the IDF values for each word like this. Thus, the IDF values for the entire vocabulary would be:

![image](https://user-images.githubusercontent.com/84801896/127962486-2862beed-c2e9-4af5-891d-9a00776520a4.png)

Hence, we see that words like “is”, “this”, “and”, etc., are reduced to 0 and have little importance; while words like “scary”, “long”, “good”, etc. are words with more importance and thus have a higher value.

We can now compute the TF-IDF score for each word in the corpus. Words with a higher score are more important, and those with a lower score are less important:

TF_IDF formula

We can now calculate the TF-IDF score for every word in Review 2:

TF-IDF(‘this’, Review 2) = TF(‘this’, Review 2) * IDF(‘this’) = 1/8 * 0 = 0

Similarly,

TF-IDF(‘movie’, Review 2) = 1/8 * 0 = 0
TF-IDF(‘is’, Review 2) = 1/4 * 0 = 0
TF-IDF(‘not’, Review 2) = 1/8 * 0.48 = 0.06
TF-IDF(‘scary’, Review 2) = 1/8 * 0.18 = 0.023
TF-IDF(‘and’, Review 2) = 1/8 * 0 = 0
TF-IDF(‘slow’, Review 2) = 1/8 * 0.48 = 0.06
Similarly, we can calculate the TF-IDF scores for all the words with respect to all the reviews:

![image](https://user-images.githubusercontent.com/84801896/127962660-94921973-740c-477e-b1cd-9f2da7b06654.png)

We have now obtained the TF-IDF scores for our vocabulary. 
TF-IDF also gives larger values for less frequent words and is high when both IDF and TF values are high i.e the word is rare in all the documents combined but frequent in a single document.

### Summarize 
* Bag of Words just creates a set of vectors containing the count of word occurrences in the document (reviews), 
while the TF-IDF model contains information on the more important words and the less important ones as well.
* Bag of Words vectors are easy to interpret. However, TF-IDF usually performs better in machine learning models.
While both Bag-of-Words and TF-IDF have been popular in their own regard, there still remained a void where understanding the context of words was concerned. 
* Detecting the similarity between the words ‘spooky’ and ‘scary’, or translating our given documents into another language, requires a lot more information on the documents.

### Reference Links

* https://www.analyticsvidhya.com/blog/2020/02/quick-introduction-bag-of-words-bow-tf-idf/
* https://www.geeksforgeeks.org/bag-of-words-bow-model-in-nlp/
* https://www.mygreatlearning.com/blog/bag-of-words/
* https://medium.com/@MarynaL/analyzing-movie-review-data-with-natural-language-processing-7c5cba6ed922




 







