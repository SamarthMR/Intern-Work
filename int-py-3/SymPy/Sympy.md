     
![Sympy img](https://i.ytimg.com/vi/kx2GzBeGPco/maxresdefault.jpg)


<h2 align="center"><b>PYTHON - SYMPY LIBRARY</b></h2>
<h3 align="center">This mark down file helps understand Sympy library in Python.</h3></br>

_____

</br>

# 📋 **Sympy Library in Python**


**SymPy** stands for Scientific Python . It is a Python library for performing symbolic computation and mathematics. It is a computer algebra system (CAS) that can be used either as a standalone application, as a library to other applications. Since it is a pure Python library, it can be used as interactive mode and as a programmatic application.

SymPy has a wide range of features applicable in the field of basic symbolic arithmetic, calculus, algebra, discrete mathematics, quantum physics, etc. SymPy is capable of formatting the results in variety of formats including LaTeX, MathML, etc. SymPy is distributed under New BSD License.

Some of the areas of applications of SymPy are −

- Polynomials                    
- Calculus
- Discrete maths
- Matrices
- Geometry
- Plotting
- Physics
- Statistics
- Combinatorics and many more..
  

## **Installing sympy module: -**

If you have Python and PIP already installed on a system, then installation of SciPy is very easy.

Install it using this command:

```Python
    pip install sympy
```
If this command fails, then use a Python distribution that already has Sympy installed like, Anaconda, Spyder etc...

## **Import Sympy :-**

Other Python distributions such as Anaconda, Enthought Canopy, etc., may have SymPy already bundled in it . Once SciPy is installed, import the SciPy module(s) you want to use in your applications by adding the *from scipy import module_name* statement . To verify, you can type the following in the Python prompt −

```Python
>>> import sympy
>>> sympy.__version__
'1.6.1'
>>>from scipy import module_name
>>>
```

And you get the below output as the current version of sympy −

'1.6.1'

 Steps for Executing Sympy Program in Python

- Import The Sympy module
- Writing The Expression
- Executing The Expression


### **SymPy ― Symbolic Computation**

Symbolic computation refers to development of algorithms for manipulating mathematical
expressions and other mathematical objects . For example, we calculate square root of a number using Python's math module as given below −

```Python
>>> import sympy
>>> a = (sympy.sqrt(5))
>>> a
sqrt(5)
>>>
```

The output for the above code snippet in python shell is as follows −

```Python
sqrt(5)
```

Same SymPy code, when run in Jupyter notebook, it use  MathJax library to render
mathematical symbols in LatEx form. It's output  is shown in the below :
```Python
√5
```

 SymPy does all sorts of computations (such as
derivatives, integrals, and limits, solve equations, work with matrices) symbolically.

### **SymPy ― Numbers**

The core module in SymPy package contains Number class which represents atomic numbers. This class has two subclasses: 
- Float class
-  Rational class. 

Rational class is further extended by Integer class.<br>

Float class represents a floating point number of arbitrary precision.<br>

Example-1 [Float Class]:
```Python
>>> from sympy import Float
>>> Float(6.32)
6.32000000000000
>>>
```

Rational class is a representation of a number (p/q) form where  q being a non-zero number.
<br>

Example-2 [Rational Class] :

```Python
>>> from sympy import Rational
>>> Rational(3/4)
3/4
>>>
```

Integer class in SymPy represents an integer number of any size. The constructor can accept a Float or Rational number, but the fractional part is discarded.<br>

Example-3 [Integer Class] :

```Python
>>> from sympy import Integer
>>> Integer(3.4)
3
>>>
```

### **SymPy ― Symbols**

Symbol is the most important class in symPy library.SymPy variables are objects of Symbols class.
Symbol() function's argument is a string containing symbol which can be assigned to a
variable

Example :
```Python
>>> from sympy import Symbol
>>> x=Symbol('x')
>>> y=Symbol('y')
>>> expr=x**2+y**2
>>> expr
x**2 + y**2
>>>
```

The above code snippet gives an output equivalent to the below expression :

x**2 + y**2

SymPy also has a Symbols() function that can define multiple symbols at once. String
contains names of variables separated by comma or space.
```Python
>>> from sympy import symbols
>>> x,y,z=symbols("a,b,c")
>>> x
a
>>> y
b
>>> z
c
>>>
```
The output of the above snippet is as follows:

x = a, y = b, z = c

Indexed symbols can be defined using syntax similar to range() function. Ranges are
indicated by a colon. Type of range is determined by the character to the right of the colon.
If itr is a digit, all contiguous digits to the left are taken as the nonnegative starting value where as all contiguous digits to the right are taken as 1 greater than the ending value.

```Python
>>> from sympy import symbols
>>> symbols('a:5')
(a0, a1, a2, a3, a4)
>>>
```
The output of the above snippet is as follows:

(a0, a1, a2, a3, a4) 

### **SymPy ― Substitution**
In SymPy's abc module, all Latin and Greek alphabets are defined as symbols. Hence,
instead of instantiating Symbol object, this method is convenient.
```Python
>>> from sympy.abc import x,y,z
```
Basic operations to be performed on a mathematical expression is
substitution. The subs() function in SymPy replaces all occurrences of first parameter with
second.<br>
Example :
```Python
>>> from sympy import *
>>> from sympy.abc import x,a
>>> expr=sin(x)*sin(x)+cos(x)*cos(x)
>>> expr
sin(x)**2 + cos(x)**2
>>>
```
The above code snippet gives an output equivalent to the below expression:

sin(x)**2 + cos(x)**2

Now , substitution the x to a we get 

```Python
>>> expr.subs(x,a)
sin(a)**2 + cos(a)**2
>>>
```

The above code snippet gives an output equivalent to the below expression:

sin(a)**2 + cos(a)**2

This function is useful if we want to evaluate a certain expression. For example, we can also substitute to an number and 
 calculate values of following expression .

In the same way ,This function is also can be used to replace a subexpression with another subexpression too.


### **SymPy ― sympify() function**

The sympify() function is used to convert any arbitrary expression such that it can be used
as a SymPy expression. Normal Python objects such as integer objects are converted in
SymPy. Integer, etc.., strings are also converted to SymPy expressions.


The sympify() function takes following arguments: 
-  strict: default is False. 

If set to True,
only the types for which an explicit conversion has been defined are converted. Otherwise,
SympifyError is raised where as If set to False, arithmetic and operators will be
converted into their SymPy equivalents without evaluating expression.

Example -
```Python
>>> sympify("10/5+4/2")
4
>>> sympify("10/5+4/2", evaluate=False)
10/5 + 4/2
>>>
```

In first The above code snippet gives the following output:

4

where as when the evaluate is set to false then it is being not executed and the above code snippet gives the output 

10/5 + 4/2

### **SymPy ― evalf() function**

This function evaluates a given numerical expression upto a given floating point precision
upto 100 digits. The function also takes subs parameter a dictionary object of numerical
values for symbols.

Examples :
```Python
>>> from sympy.abc import r
>>> expr=pi*r**2
>>> expr
pi*r**2
>>> expr.evalf(subs={r:5})
78.5398163397448
>>>
```

The above code snippet gives the following output:

𝟕𝟖. 𝟓𝟑𝟗𝟖𝟏𝟔𝟑𝟑𝟗𝟕𝟒𝟒𝟖


### **SymPy - Lambdify() function**

The lambdify function translates SymPy expressions into Python functions. If an expression
is to be evaluated over a large range of values, the evalf() function is not efficient. lambdify
acts like a lambda function, except it converts the SymPy names to the names of the given
numerical library, usually NumPy. By default, lambdify on implementations in the math
standard library.

Example :
```Python
>>> from sympy.abc import a,b
>>> expr = a**2+b**2+5
>>> f=lambdify([a,b],expr)
>>> f(2,3)
18
>>>
```

The expression is converted into python and then the value is passed to the function.
The above code snippet gives the following output:

18


### **SymPy ― Derivative**

The derivative of a function is its instantaneous rate of change with respect to one of its
variables. we can find the differentiation of mathematical expressions in the form of variables
by using diff() function in SymPy package.

Example :

```Python
>>> diff(exp(x**2),x)
2*x*exp(x**2)
```

The above code snippet gives an output equivalent to the below expression:

2*x*exp(x**2)


### **SymPy ― Integration**

The SymPy package contains integrals module. It implements methods to calculate definite
and indefinite integrals of expressions. The integrate() method is used to compute both
definite and indefinite integrals. To compute an indefinite or primitive integral, just pass
the variable after the expression.
For example:
- indefinite intergral :

       integrate(f, x)  
- Definite integral, the argument is:

       (integration_variable, lower_limit, upper_limit)

Example :
```Python
>>> expr=exp(-x**2)
>>> integrate(expr,(x,0,oo) )
sqrt(pi)/2
>>>
```

The above code snippet gives an output equivalent to the below expression:

sqrt(pi)/2


There are more function inside sympy module like for assumptions module in SymPy package contains tools for extracting information about by using ask() function , the function simplify() tries to apply intelligent heuristics to make the input expression “simpler”  where as we can plot 2-D and 3-D graphs using the plot() function and many more ..


Using all these modules inside SymPy that  are readable and understandable, one can solve the all sorts of calculation , ploting the graph and computations symbolically. SymPy can act as a calculator simplify expressions,expand the expressions , compute derivatives, integrals, and limits, solve equations,ploting the data in the graph in 2-D & 3-D form,  work with matrices, and much, much more ...