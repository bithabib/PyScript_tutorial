# PyScript Full Tutorial

## 1. Getting started with PyScript | Bangla | School of Thought

```html
<!DOCTYPE html>
<html>

<head>
    <!-- <link rel="stylesheet" href="https://pyscript.net/alpha/pyscript.css" /> -->
    <script defer src="https://pyscript.net/alpha/pyscript.js"></script>
    <!-- CSS only -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
</head>

<body>
    <div class="container">
        <h1>My First Heading</h1>
        <p>My first paragraph.</p>

        <!-- Magic is here! -->
        <py-script class="text-center"> print('Hello, World!') </py-script>
        <py-script> print('Hello, World!') </py-script>
        <py-script> print('Hello, World!') </py-script>
    </div>
</body>

</html>
```
## 2. Console and Log using PyScript | Bangla | School of Thought

```html
<!DOCTYPE html>
<html>

<head>
    <!-- <link rel="stylesheet" href="https://pyscript.net/alpha/pyscript.css" /> -->
    <script defer src="https://pyscript.net/alpha/pyscript.js"></script>

</head>

<body>

    <h1>Welcome to Python Compiler </h1>
    <p>PyScript is Awesome</p>

    <py-script>
from js import console
console.log("Console Log from PyScript")
console.warn("Console Warn from PyScript")
console.error("Console Error from PyScript")
console.info("Console Info from PyScript")
    </py-script>
</body>

</html>
```

## 3. Simple input and output using PyScript | Bangla | School of Thought

```html
<!DOCTYPE html>

<html>

<head>
  <!--<link rel="stylesheet" href="https://pyscript.net/alpha/pyscript.css" />-->
  <script defer src="https://pyscript.net/alpha/pyscript.js"></script>
</head>

<body>
  <div>Type an sample input here</div>
  <input type="text" id="test-input"/>
  <button id="submit-button" type="submit" pys-onClick="my_function">OK</button>
  <div id="test-output"></div>

<py-script>
from js import console

def my_function(*args, **kwargs):

    #print('args:', args)
    #print('kwargs:', kwargs)

    console.log(f'args: {args}')
    console.log(f'kwargs: {kwargs}')
    
    text = Element('test-input').element.value

    #print('text:', text)
    console.log(f'text: {text}')

    Element('test-output').element.innerText = text
</py-script>

  </body>
</html>
```
## 4. If Else using PyScript | Bangla | School of Thought

```html
<!DOCTYPE html>
<html>

<head>
    <!-- <link rel="stylesheet" href="https://pyscript.net/alpha/pyscript.css" /> -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <script defer src="https://pyscript.net/alpha/pyscript.js"></script>
</head>

<body>
    <div class="container text-center p-5">
        <h1>Input and Output</h1>
        <input type="number" id="test-input"/> 
        <button id="test-button" pys-onclick="my_function">Click me</button>
        <p id="test-output" class="p-3"></p>
        <py-script>
def my_function(*args, **kwargs):
    test_number = Element("test-input").element.value
    if int(test_number)%2==0:
        Element("test-output").element.innerHTML = "Even"
    else:
        Element("test-output").element.innerHTML = "Odd"
        </py-script>
    </div>
</body>

</html>
```

## 5. Loop using PyScript | Bangla | School of Thought
```html
<!DOCTYPE html>
<html>

<head>
    <!-- <link rel="stylesheet" href="https://pyscript.net/alpha/pyscript.css" /> -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <script defer src="https://pyscript.net/alpha/pyscript.js"></script>
</head>

<body>
    <div class="container text-center p-5">
        <h1>Input and Output</h1>
        <input type="number" id="test-input"/> 
        <button id="test-button" pys-onclick="my_function">Click me</button>
        <div id="test-output" class="p-3"></div>
        <py-script>
from js import console
def my_function(*args, **kwargs):
    test_number = Element("test-input").element.value
    for i in range(int(test_number)):
        console.log("hello ",i)
        </py-script>
    </div>
</body>

</html>
```

## 6. How to make online python interpreter or console using PyScript Repl | Bangla | School of Thought

```html
<!DOCTYPE html>
<html>

<head>
    <!-- <link rel="stylesheet" href="https://pyscript.net/alpha/pyscript.css" /> -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <script defer src="https://pyscript.net/alpha/pyscript.js"></script>
</head>

<body>
    <div class="container p-5">
        <h1>PyScript py-repl</h1>
        <py-repl auto-generate="true"></py-repl>
    </div>
</body>

</html>
```

## 7. How to Import Python Packages using PyScript | Bangla | School of Thought
```html 
<!DOCTYPE html>
<html>

<head>
    <!-- <link rel="stylesheet" href="https://pyscript.net/alpha/pyscript.css" /> -->
    <script defer src="https://pyscript.net/alpha/pyscript.js"></script>
    <py-env>
        - numpy
        - matplotlib
    </py-env>
</head>

<body>
    <h1>My First Heading</h1>
    <div id="plot"></div>
    <py-script output="plot">
import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(1000)
y = np.random.randn(1000)

fig, ax = plt.subplots()
ax.scatter(x, y)
fig

    </py-script>

</body>

</html>
```

## 8. Import python file in PyScript | Bangla | School of Thought

```html
<!DOCTYPE html>
<html>

<head>
    <!-- <link rel="stylesheet" href="https://pyscript.net/alpha/pyscript.css" /> -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <script defer src="https://pyscript.net/alpha/pyscript.js"></script>
    <py-env>
        - paths:
            - /python/random_n.py
    </py-env>
</head>

<body>
    <div class="container p-5">
        <h1>PyScript Python File Import</h1>
        <py-script src="/python/our_script.py"></py-script>
        <input type="number" id="test-input" name="file" />
        <button type="button" id="test-button" pys-onclick="my_function">Test</button>
        <p id="test-output"></p>

        <py-script>
from random_n import random_number
print(random_number())
        </py-script>

    </div>
</body>

</html>
```