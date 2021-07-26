# PyTorch 
![PyTorch](https://user-images.githubusercontent.com/85128689/126911074-0af5f52e-3d7e-41f4-b052-cdf11edaacdb.png)

----------------------------

## Installation
- [Click here](https://pytorch.org/), you'll be redirected to PyTorch website
- Select your preferences i.e., PyTorch Build, Your OS, Package, Language, Computer platform.
- Finally, Run the command in your command prompt


## Introduction
- It is a Deep Learning Framework based on Torch Library. Many Deep Learning Softwares are built through PyTorch including Tesla Autopilot, Uber's Pyro, Catalyst, PyTorch Lightening etc.
- PyTorch has a C++ interface. It can assemble a graph of a neural network and can perform a forward pass i.e, make predictions and aslo computes the loss/error.
- TensorFlow, Keras, Caffe2, MXNet, and Torch are the most popular alternatives and competitors to PyTorch.
- PyTorch created an API that was both pythonic and easy to customize, allowing new layer types, optimizers to implement in order to solve the problems obtained.

## It has two level features:
- **1. Tensor Computing** - It is like numpy with strong acceleration through GPU ( Graphics Processing Unit ).
- **2. Deep Neural networks** - It is built on a type-based automatic differentiation systems.
- Models defined by two frameworks were mutually incompatible.
- So, Facebook and Microsoft created an Open Neural Exchange (ONNX) to convert model between frameworks as Facebook operates both PyTorch and Convolutional architecture for Fast Feature Embedding.

## PyTorch Tensors
- It supports various sub-types of Tensors. PyTorch defines a class called Tensor i.e torch.Tensor to store and operate homogenous multidimensional rectangular arrays of number.
- PyTorch represents data as multi-dimensional, NumPy like Arrays called Tensors.
- It also stores inputs to your neural netwok, hidden layer representations, and the outputs.
- PyTorch represents data as multi-dimensional, NumPy like Arrays called Tensors.
- It also stores inputs to your neural netwok, hidden layer representations, and the outputs.
- Example:


```python
 import torch
a = torch.Tensor([[1,2],[3,4]])
print(a)
print(a**2)
```

    tensor([[1., 2.],
            [3., 4.]])
    tensor([[ 1.,  4.],
            [ 9., 16.]])
    

## File Extension
- To save models we can use a.pt or .pth file extension.

## Modules :

**1) Autograd Module :**

- It is also called as automatic differentiation. This method is used for building neural networks to save time on one epoch by calculating differentiation of parameters at the forward pass.
- For example , after recording all the operations performed in a recorder, we can replay it backward to compute the gradients.

**2) Optim Module ( torch.optim ) :**
- It implements various optimization algorithms used for building Neural Networks.
- It supports most commonly used methods. So, there will be no need of building them from scratch.

**3) nn Module :**
- PyTorch autograd makes it easy to define computational graphs and take gradients, but raw autograd can be a bit too low-level for defining complex neural networks.
- This is where the nn module helps to get through this.

## Features
- Production Ready
- Distributed Training
- Robust Ecosystem
- Cloud Support
- Ease of Extendability

## Advantages 
- Pythonic
- Easy to learn
- Easy debugging
- Dynamic computational graphs
- Higher developer productivity
- Useful Libraries
- Data Parallelism 
- Community

## Disadvantages
- Lack of model serving in production
- Limited monitoring and visualization interfaces


## More Examples

 ### 1. Example for Autograd


```python
import torch
import math

dtype = torch.float
device = torch.device("cpu")
# device = torch.device("cuda:0")  # Uncomment this to run on GPU

# Create Tensors to hold input and outputs.
# By default, requires_grad=False, which indicates that we do not need to
# compute gradients with respect to these Tensors during the backward pass.
x = torch.linspace(-math.pi, math.pi, 2000, device=device, dtype=dtype)
y = torch.sin(x)

# Create random Tensors for weights. For a third order polynomial, we need
# 4 weights: y = a + b x + c x^2 + d x^3
# Setting requires_grad=True indicates that we want to compute gradients with
# respect to these Tensors during the backward pass.
a = torch.randn((), device=device, dtype=dtype, requires_grad=True)
b = torch.randn((), device=device, dtype=dtype, requires_grad=True)
c = torch.randn((), device=device, dtype=dtype, requires_grad=True)
d = torch.randn((), device=device, dtype=dtype, requires_grad=True)

learning_rate = 1e-6
for t in range(2000):
    # Forward pass: compute predicted y using operations on Tensors.
    y_pred = a + b * x + c * x * 2 + d * x * 3

    # Compute and print loss using operations on Tensors.
    # Now loss is a Tensor of shape (1,)
    # loss.item() gets the scalar value held in the loss.
    loss = (y_pred - y).pow(2).sum()
    if t % 100 == 99:
        print(t, loss.item())

    # Use autograd to compute the backward pass. This call will compute the
    # gradient of loss with respect to all Tensors with requires_grad=True.
    # After this call a.grad, b.grad. c.grad and d.grad will be Tensors holding
    # the gradient of the loss with respect to a, b, c, d respectively.
    loss.backward()

    # Manually update weights using gradient descent. Wrap in torch.no_grad()
    # because weights have requires_grad=True, but we don't need to track this
    # in autograd.
    with torch.no_grad():
        a -= learning_rate * a.grad
        b -= learning_rate * b.grad
        c -= learning_rate * c.grad
        d -= learning_rate * d.grad

        # Manually zero the gradients after updating weights
        a.grad = None
        b.grad = None
        c.grad = None
        d.grad = None

print(f'Result: y = {a.item()} + {b.item()} x + {c.item()} x^2 + {d.item()} x^3')
```

    99 1111.568603515625
    199 715.239501953125
    299 537.4428100585938
    399 457.681884765625
    499 421.900390625
    599 405.8484802246094
    699 398.6474304199219
    799 395.4169616699219
    899 393.9677734375
    999 393.31768798828125
    1099 393.0260009765625
    1199 392.8951721191406
    1299 392.8364562988281
    1399 392.8101806640625
    1499 392.79833984375
    1599 392.79302978515625
    1699 392.7906799316406
    1799 392.7895812988281
    1899 392.78912353515625
    1999 392.7889099121094
    Result: y = -0.0002942959836218506 + 0.31823498010635376 x + -0.23840661346912384 x^2 + 0.15402868390083313 x^3
    

### 2. Example for Optim Module


```python
import torch
import math


# Create Tensors to hold input and outputs.
x = torch.linspace(-math.pi, math.pi, 2000)
y = torch.sin(x)

# Prepare the input tensor (x, x^2, x^3).
p = torch.tensor([1, 2, 3])
xx = x.unsqueeze(-1).pow(p)

# Use the nn package to define our model and loss function.
model = torch.nn.Sequential(
    torch.nn.Linear(3, 1),
    torch.nn.Flatten(0, 1)
)
loss_fn = torch.nn.MSELoss(reduction='sum')

# Use the optim package to define an Optimizer that will update the weights of
# the model for us. Here we will use RMSprop; the optim package contains many other
# optimization algorithms. The first argument to the RMSprop constructor tells the
# optimizer which Tensors it should update.
learning_rate = 1e-3
optimizer = torch.optim.RMSprop(model.parameters(), lr=learning_rate)
for t in range(2000):
    # Forward pass: compute predicted y by passing x to the model.
    y_pred = model(xx)

    # Compute and print loss.
    loss = loss_fn(y_pred, y)
    if t % 100 == 99:
        print(t, loss.item())

    # Before the backward pass, use the optimizer object to zero all of the
    # gradients for the variables it will update (which are the learnable
    # weights of the model). This is because by default, gradients are
    # accumulated in buffers( i.e, not overwritten) whenever .backward()
    # is called. Checkout docs of torch.autograd.backward for more details.
    optimizer.zero_grad()

    # Backward pass: compute gradient of the loss with respect to model
    # parameters
    loss.backward()

    # Calling the step function on an Optimizer makes an update to its
    # parameters
    optimizer.step()


linear_layer = model[0]
print(f'Result: y = {linear_layer.bias.item()} + {linear_layer.weight[:, 0].item()} x + {linear_layer.weight[:, 1].item()} x^2 + {linear_layer.weight[:, 2].item()} x^3')
```

    99 4850.11083984375
    199 2481.67578125
    299 2031.694091796875
    399 1785.566162109375
    499 1539.802978515625
    599 1307.104736328125
    699 1094.93017578125
    799 904.4423828125
    899 734.9064331054688
    999 585.4619750976562
    1099 455.2981262207031
    1199 343.6950378417969
    1299 250.0367889404297
    1399 174.2311553955078
    1499 113.97232818603516
    1599 69.603759765625
    1699 39.29497146606445
    1799 21.143598556518555
    1899 12.359628677368164
    1999 9.424358367919922
    Result: y = -0.0005007918225601315 + 0.8348111510276794 x + -0.0005008040461689234 x^2 + -0.0897076278924942 x^3
    

### 3. Example for nn Module 


```python
import torch
import math


# Create Tensors to hold input and outputs.
x = torch.linspace(-math.pi, math.pi, 2000)
y = torch.sin(x)

# For this example, the output y is a linear function of (x, x^2, x^3), so
# we can consider it as a linear layer neural network. Let's prepare the
# tensor (x, x^2, x^3).
p = torch.tensor([1, 2, 3])
xx = x.unsqueeze(-1).pow(p)

# In the above code, x.unsqueeze(-1) has shape (2000, 1), and p has shape
# (3,), for this case, broadcasting semantics will apply to obtain a tensor
# of shape (2000, 3) 

# Use the nn package to define our model as a sequence of layers. nn.Sequential
# is a Module which contains other Modules, and applies them in sequence to
# produce its output. The Linear Module computes output from input using a
# linear function, and holds internal Tensors for its weight and bias.
# The Flatten layer flatens the output of the linear layer to a 1D tensor,
# to match the shape of `y`.
model = torch.nn.Sequential(
    torch.nn.Linear(3, 1),
    torch.nn.Flatten(0, 1)
)

# The nn package also contains definitions of popular loss functions; in this
# case we will use Mean Squared Error (MSE) as our loss function.
loss_fn = torch.nn.MSELoss(reduction='sum')

learning_rate = 1e-6
for t in range(2000):

    # Forward pass: compute predicted y by passing x to the model. Module objects
    # override the _call_ operator so you can call them like functions. When
    # doing so you pass a Tensor of input data to the Module and it produces
    # a Tensor of output data.
    y_pred = model(xx)

    # Compute and print loss. We pass Tensors containing the predicted and true
    # values of y, and the loss function returns a Tensor containing the
    # loss.
    loss = loss_fn(y_pred, y)
    if t % 100 == 99:
        print(t, loss.item())

    # Zero the gradients before running the backward pass.
    model.zero_grad()

    # Backward pass: compute gradient of the loss with respect to all the learnable
    # parameters of the model. Internally, the parameters of each Module are stored
    # in Tensors with requires_grad=True, so this call will compute gradients for
    # all learnable parameters in the model.
    loss.backward()

    # Update the weights using gradient descent. Each parameter is a Tensor, so
    # we can access its gradients like we did before.
    with torch.no_grad():
        for param in model.parameters():
            param -= learning_rate * param.grad

# You can access the first layer of `model` like accessing the first item of a list
linear_layer = model[0]

# For linear layer, its parameters are stored as `weight` and `bias`.
print(f'Result: y = {linear_layer.bias.item()} + {linear_layer.weight[:, 0].item()} x + {linear_layer.weight[:, 1].item()} x^2 + {linear_layer.weight[:, 2].item()} x^3')
```

    99 782.2467651367188
    199 520.2476196289062
    299 347.0008239746094
    399 232.44122314453125
    499 156.68865966796875
    599 106.59722900390625
    699 73.47418212890625
    799 51.57170104980469
    899 37.088584899902344
    999 27.511627197265625
    1099 21.178892135620117
    1199 16.991376876831055
    1299 14.222370147705078
    1399 12.39136028289795
    1499 11.180593490600586
    1599 10.379993438720703
    1699 9.8505859375
    1799 9.500506401062012
    1899 9.269017219543457
    1999 9.115950584411621
    Result: y = 2.477658199495636e-05 + 0.8399380445480347 x + -4.274150796845788e-06 x^2 + -0.09094033390283585 x^3
    
