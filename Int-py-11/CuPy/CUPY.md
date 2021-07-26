## Objective 
To develop a basic understanding of CuPy library and it's functions. 

## Table of Content 

- [What is CuPy?](#what)
- [Why is it used?](#why)
- [Install the CuPy library](#install) 
- [Importing CuPy](#import)
- [CuPy vs NumPy Speed](#vs)
- [Overview of Functions of CuPy](#overview)
- [Some Main Functions of CuPy](#main)
- [Basic Programs of CuPy](#program)


## What is CuPy?<a name="what"></a>

CuPy is a library that implements Numpy arrays on *NVIDIA GPUs* with the help of the *CUDA GPU* library. Based on the implementation of Numpy arrays, the multiple CUDA cores of the GPU itself can contribute to better parallel acceleration.

CuPy has almost same interface with Numpy and in most cases, it can directly replace Numpy. CuPy supports most of Numpy's array operations, including *indexing, broadcasting, array math, and various matrix transformations*. It also enables to copy data from CPU to GPU. 

**Note:** If some Numpy operations are encountered that are not supported by CuPy, users can also write custom Python code, which will take advantage of CUDA and GPU acceleration. The whole process only needs a small piece of code in C++ format, and then CuPy can automatically perform GPU conversion.
<br>

## Why is it used?<a name="why"></a>

- Numpy is extensively used in Python but GPU is not supported. Since consumer CPUs usually have only 8 cores or less, the amount of parallel processing and the speedup that can be achieved are limited.
- GPU is getting faster and more important for scientific computing.

## Install the CuPy library via pip<a name="install"></a>
 ```python
  pip install cupy
  ```
 
 **PC configuration needed for CuPy**
 
  - i7–8700k CPU
  - 1080 Ti GPU
  - 32 GB of DDR4 3000MHz RAM
  - CUDA 9.0

## Importing CuPy<a name="import"></a>
 
  ```python
 import  numpy  as  np 
 import  cupy  as  cp 
 import  time
 ```

## CuPy vs NumPy Speed<a name="vs"></a>
- Creating Arrays <br>
The following code creates a 3D array with 1 billion 1's for Numpy and CuPy. In order to measure the speed of creating arrays, Python's native time library is used:

  ```python
  ### Numpy and CPU
  s = time.time() 
  *x_cpu = np.ones(( 1000 , 1000 , 1000 ))* 
  e = time.time() 
  print("NumPy Speed in sec",e-s) 

  ### CuPy and GPU
  s = time.time() 
  *x_gpu = cp.ones(( 1000 , 1000 , 1000 ))* 
  e = time.time() 
  print("CuPy Speed in sec",e-s)
  ```
   **Output:**
    ```
    NumPy Speed in sec: 0.507
    CuPy Speed in sec: 0.000710
    ```

- Performing Mathematical Operations on Array <br>
The following code multiplies the entire array by 5 and check the speed of Numpy and CuPy again.

  ```python
  ### Numpy and CPU
   s = time.time() 
  *x_cpu *=  5 * 
  e = time.time() 
  print("NumPy Speed in sec",e-s) 

  ### CuPy and GPU
   s = time.time() 
  *x_gpu *=  5 * 
  e = time.time() 
  print("CuPy Speed in sec",e-s)
  ```
   **Output:**
    ```
    NumPy Speed in sec: 1.49 
    CuPy Speed in sec: 0.0922
    ```
   
## Overview of Functions of CuPy: <a name="overview"></a>
  - Basics of **cupy.ndarray()**: <br>
    CuPy's core class is ***cupy.ndarray***, which is a substitute for NumPy's ***numpy.ndarray***.

    ```python
      gpu = cp.array([1, 2, 3])
    ```
    ***Cupy.ndarray*** is an example of ***gpu***. As can be seen, **CuPy's** syntax is identical to **NumPy's**. The primary distinction between cupy.ndarray and numpy.ndarray is that CuPy arrays are allocated on the current device.
  - The concept of ***current device***: <br>
     CuPy includes a concept of a current device, which is the default GPU device on which arrays are ***allocated***, ***manipulated***, ***calculated***, and so on. <br> Assume the current device's ID is 0. 
     In this example, the code below would construct an array gpu0 on GPU 0. 
     ```python
     gpu0 = cp.array([1, 2, 3, 4, 5])
     ```
     ***Cupy.cuda.Device.use()*** can be used to change the current device
     ```python
      gpu0 = cp.array([1, 2, 3, 4, 5])
      cp.cuda.Device(1).use()
      gpu1 = cp.array([1, 2, 3, 4, 5])
     ```
  - **Host-device** and **Device-Device** Array Transfer:
    - Move arrays to a device: <br>
      A *numpy.ndarray*, a list, or any object that can be provided to *numpy.array()* may be moved to the current device using ***cupy.asarray()*** 
      
      ```python
        cpu = np.array([1, 2, 3])
        gpu = cp.asarray(cpu)
      ```
    - Move array from a device to the host: <br>
      Moving a device array to the host can be done by ***cupy.asnumpy()*** as follows
      ```python 
        gpu = cp.array([1, 2, 3])
        cpu = cp.asnumpy(x_gpu)
      ```
## Some Main Functions of CuPy: <a name="main"></a>
  - Universal functions(***cupy.ufunc***): 
    CuPy provides universal functions to support various elementwise operations. CuPy’s ufunc supports following features of NumPy’s one:
      - Broadcasting
      - Output type determination
      - Casting rules 
    ### ufunc: 
    ```python
    ufunc(name, nin, nout, _Ops ops[, preamble, …])
    ```
    ### Available ufuncs: 
      - Math operations:
        - **add**: Adds two arrays elementwise
        - **subtract**: Subtracts arguments elementwise
      - Trigonometric functions: 
        - **sin**: Elementwise sine function
        - **cos**: Elementwise cosine function
      - Bit-twiddling functions: 
        - **bitwise_and**: Computes the bitwise AND of two arrays elementwise
        - **bitwise_or**: Computes the bitwise OR of two arrays elementwise
      - Comparison functions: 
        - **greater**: Tests elementwise if x1 > x2 
        - **greater_equal**: Tests elementwise if x1 >= x2
          
        Read more [here](https://docs.cupy.dev/en/stable/reference/ufunc.html)
     ### ufunc.at:
     Currently, *CuPy does not support at* for ufuncs in general. However, ***cupyx.scatter_add()*** can substitute add.at as both behave identically.
        
  - **CuPy-specific functions**: 
    - cupyx.rsqrt: Returns the reciprocal square root <br>
    
         ```
         cupyx.rsqrt = <ufunc 'cupy_rsqrt'>
         ```
  - **cupyx.scatter_add()**: Adds given values to specified elements of an array, ***scatter_add()*** behaves identically to ***numpy.add.at()***.
     <br>
     
     **Note:** *Just like an array indexing, negative indices are interpreted as counting from the end of an array.*
     ```python
     >>> import numpy
     >>> import cupy
     >>> a = cupy.zeros((6,), dtype=numpy.float32)
     >>> i = cupy.array([1, 0, 1])
     >>> v = cupy.array([1., 1., 1.])
     >>> cupyx.scatter_add(a, i, v);
     >>> a
     array([1., 2., 0., 0., 0., 0.], dtype=float32)
     ```
 - Read more [here](https://docs.cupy.dev/en/stable/reference/index.html) 

## Basic Programs of CuPy: <a name="program"></a>
 - **Take the Euclidean norm (a.k.a L2 norm):**
 
   ```python
   import cupy as cp
   import numpy as np

   x_cpu = np.array([1, 2, 3])
   x_gpu = cp.array([1, 2, 3])

   l2_cpu = np.linalg.norm(x_cpu)
   l2_gpu = cp.linalg.norm(x_gpu)

   print("Using Numpy: ", l2_cpu)
   print("\nUsing Cupy: ", l2_gpu)
   ```
   
   ***Output:*** 
   
   ```
   Using Numpy: 3.7416573867739413
   Using Cupy: array(3.74165739)
   ```
 - **Speed Comparison b/w CuPy and NumPy:**

   ```python
   import cupy as cp
   import numpy as np
   import time

   # NumPy and CPU Runtime
   s = time.time()
   x_cpu = np.ones((1000, 1000, 100))
   e = time.time()
   print("Time consumed by numpy: ", e - s)

   # CuPy and GPU Runtime
   s = time.time()
   x_gpu = cp.ones((1000, 1000, 100))
   e = time.time()
   print("\nTime consumed by cupy: "e - s)
   ```
   
   **Output:**

    ```
    Time consumed by numpy: 0.4238910675048828
    Time consumed by cupy: 0.0010099411010742188 
    ```

    **Note:** *The configurations used here are for CPU is intel i7-7700 HQ and GPU is Geforce GTX 1050 4GB using CUDA 9.0.*
