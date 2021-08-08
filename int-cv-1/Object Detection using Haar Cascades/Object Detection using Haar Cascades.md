# **Object Detection using Haar Cascades**

## **What is Object Detection?**

Object Detection is a computer technology related to computer vision, image processing and deep learning that deals with the **detecting instances of objects** in the images and videos. We will do object detection in this topic using something known as _**haar cascades**_.

## **What are Haar Cascades?**

Haar Cascade classifiers are a very effective way for object detection. This method was first proposed by Paul Viola and Michael Jones in their paper **Rapid Object Detection using a Boosted Cascade of Simple Features.** Haar Cascade is a machine learning-based approach where a lot of positive and negative images are used to train the classifier. 

_**Positive images**_ – These images contain the images that we want our classifier to identify.  
_**Negative Images**_ – Images of everything else, which does not contain the object that we want to detect.

**Requirements:**

Make sure you have installed python, Matplotlib and OpenCV on your pc (all the latest versions).
The haar cascade files can be downloaded from the [OpenCV Github repository](https://github.com/opencv/opencv/tree/master/data/haarcascades).

## **Theory**

We use Haar Feature-based Cascade Classifiers to detect faces, eyes, smiles as well as eyeglasses. In short, haarcascade is a machine learning method where a cascade function is trained on a large amount of positive and negative images, which in turn can be used for object detection.  
To actually explain them, we introduce the concept of Haar features. They are obtained by black and white boxes below which they act as convolutional kernels. The features are more specifically just single values received by subtracting the sum of pixels under the white rectangles from the sum of pixels under the black rectangles.

<p align="center">
   <img src="https://github.com/SamarthMR/Intern-Work/blob/main/int-cv-1/images/Object%20detection%20Images/1_hbFPsfsCqV8rf1MV8b8p5w.jpeg"
</p>

### **Convolution**

It is essentially the result of two functions affecting one another. Here, in our case, it signifies how the sum of pixels in the white and black part of the boxes interact, i.e., how they are differentiated to produce a single value.  There is also an algorithm for calculating the sum of pixels efficiently inside an area, it’s called _**summed-area table**_ and was published by F. Crow in 1984. It was later popularized in the image processing domain and goes under the name integral image.

<p align="center">
   <img src="https://github.com/SamarthMR/Intern-Work/blob/main/int-cv-1/images/Object%20detection%20Images/1_CbOUB2WgVOzVRx8iDv5APQ.png"
</p>

### **Haar Feature Selection**

Objects are classified on very simple features to encode ad-hoc domain knowledge and operate much faster than the pixel system. The feature is similar to haar filters, hence the name 'Haar'. An example of these features is a 2-rectangle feature, defined as the difference of the sum of pixels of area inside the rectangle, which can be any position and scale within the original image. 

Here, we try the different Haar features and see which of those produce the largest value for the difference between the sums of pixels between the black and white rectangles. We have an example below where the optimal Haar features have been found. The eyes are usually a bit darker whereas the area below is likely lighter, and thus a horizontal rectangle with black up top and white below is suitable. Secondly, the bridge of the nose is often lighter than the eyes and as such a Haar feature with a vertical white box in the middle is the way to go.

<p align="center">
   <img src="https://github.com/SamarthMR/Intern-Work/blob/main/int-cv-1/images/Object%20detection%20Images/1_64MTUF8nuEvSgBvYmOfhKA.png">
   <br />
   <b> Optimal Haar features for an image</b>
   <br />

   <br />
</p>

The name Haar features sounds a bit odd, but it actually originates from the intuitive similarity with Haar wavelets.

They are not directly used, but the features (black and white boxes) are what we call Haar-like. Lots of these Haar-like features can be applied to an image and using the _**Adaboost algorithm**_ which finds an optimal threshold for classifying the training images correctly. But placing one of those somewhere, even on the best possible position, it will result in some error still, since all images within the positive and negative sets differ from each other. In the end, the Haar features with the smallest error rates are chosen as **classifiers**.

<p align="center">
   <img src="https://github.com/SamarthMR/Intern-Work/blob/main/int-cv-1/images/Object%20detection%20Images/1_MUeF9CIalU87NC-6T7mNWw.png"
</p>

The final number of features can be quite large despite the measures taken, so the inventors introduced the concept of Cascade of Classifiers which is now specifically in general, termed as **Haar Feature-based Cascade Classifiers**. This is used when doing the detection, since it would be slow to do it with lots of features, instead, the classifier consists of a cascade of features when detecting. So the initial Haar feature might just check if the image could possibly be a face (in the case of face detection), then the following stages have a few more of the most essential Haar features. This is a favorable method since in the earlier days, the images not containing the desired object are discarded and not processed anymore. By comparinng this to throwing all the features at the image at once, we can see the gain. Therefore, Haar Cascades are arguably OpenCV’s most popular object detection algorithm.

## **Problems and limitations of Haar cascades**

1. The classifier tends to be the most effective only for frontal images of the face.  
2. **Haar cascades are notoriously prone to false-positives** — the Viola-Jones algorithm can easily report a face in an image when no face is present.  
3. It can be quite tedious to tune the OpenCV detection parameters. There will be times when we can detect all the faces in an image. There will be other times when:  
    (1) regions of an image are falsely classified as faces, and/or  
    (2) faces are missed entirely.
4. Parameter tuning when being applied for inference/detection, and just, in general, are not as accurate as the more “modern” algorithms that we have today.

## **Applications**

1. Despite the arrival of deep learning (RCNN, YOLO, etc), this haarcascade classifier method is still used in many applications for face and object detection, as this is very simple yet powerful.
2. One of the primary benefits of Haar cascades is that they are just so **fast** — it’s hard to beat their speed.
3. It is an important part of the computer vision and image processing literature.
4. It is still used with OpenCV.
5. Very useful, particularly when working in resource-constrained devices when we cannot afford to use more computationally expensive object detectors.

## **Implementation**

We have taken Face mask Detection and Social Distancing as an example for object detection using the Haar Cascade classifiers and implemented them using OpenCV in Python.  
The Notebook file where we have done the implementation can be found [here](https://github.com/SamarthMR/Intern-Work/blob/main/int-cv-1/Object%20Detection%20using%20Haar%20Cascades/Face_Mask_Detection_and_Social_Distancing.ipynb).