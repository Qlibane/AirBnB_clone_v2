# 0x04. AirBnB clone - Web framework

PythonBack-endWebserver
### Concepts

_For this project, we expect you to look at this concept:_

-   [AirBnB clone](https://intranet.alxswe.com/concepts/74)

## Resources

**Read or watch**:

-   [What is a Web Framework?](https://intranet.alxswe.com/rltoken/64SQpOGx46Ljp0zFJchESg "What is a Web Framework?")
-   [A Minimal Application](https://intranet.alxswe.com/rltoken/NopQlHIr9J_9OPX9XRgfvw "A Minimal Application")
-   [Routing](https://intranet.alxswe.com/rltoken/cQiIhbSdIcg1Ao1MICseBg "Routing")  (_except “HTTP Methods”_)
-   [Rendering Templates](https://intranet.alxswe.com/rltoken/DBM65T59nySd0ZRlZZ0CXw "Rendering Templates")
-   [Synopsis](https://intranet.alxswe.com/rltoken/5Y_A7XB9Qo1JeZgiSUq0yQ "Synopsis")
-   [Variables](https://intranet.alxswe.com/rltoken/ITzobwYP1Lc4KqEUUcYCGw "Variables")
-   [Comments](https://intranet.alxswe.com/rltoken/ykUFuQSE9KD1M7WGY-4v4w "Comments")
-   [Whitespace Control](https://intranet.alxswe.com/rltoken/NMLZom50ZVOxQlgYW3rnuQ "Whitespace Control")
-   [List of Control Structures](https://intranet.alxswe.com/rltoken/5AGhzIt0zSpPJh9SFysdMQ "List of Control Structures")  (_read up to “Call”_)
-   [Flask](https://intranet.alxswe.com/rltoken/VJs151_hsE9g7Cw-Pz5bVg "Flask")
-   [Jinja](https://intranet.alxswe.com/rltoken/2y_hunzGCCvSot06EW67UQ "Jinja")
## Learning Objectives

At the end of this project, you are expected to be able to  [explain to anyone](https://intranet.alxswe.com/rltoken/fja4_zmJuVaRtHFviyVv9Q "explain to anyone"),  **without the help of Google**:

### General

-   What is a Web Framework
-   How to build a web framework with Flask
-   How to define routes in Flask
-   What is a route
-   How to handle variables in a route
-   What is a template
-   How to create a HTML response in Flask by using a template
-   How to create a dynamic template (loops, conditions…)
-   How to display in HTML data from a MySQL database

### Copyright - Plagiarism

-   You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
-   You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
-   You are not allowed to publish any content of this project.
-   Any form of plagiarism is strictly forbidden and will result in removal from the program.

## Requirements

### Python Scripts

-   Allowed editors:  `vi`,  `vim`,  `emacs`
-   All your files will be interpreted/compiled on Ubuntu 20.04 LTS using  `python3`  (version 3.4.3)
-   All your files should end with a new line
-   The first line of all your files should be exactly  `#!/usr/bin/python3`
-   A  `README.md`  file, at the root of the folder of the project, is mandatory
-   Your code should use the  `PEP 8`  style (version 1.7)
-   All your files must be executable
-   The length of your files will be tested using  `wc`
-   All your modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
-   All your classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
-   All your functions (inside and outside a class) should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`  and  `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
-   A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

### HTML/CSS Files

-   Allowed editors:  `vi`,  `vim`,  `emacs`
-   All your files should end with a new line
-   A  `README.md`  file at the root of the folder of the project is mandatory
-   Your code should be W3C compliant and validate with  [W3C-Validator](https://intranet.alxswe.com/rltoken/_bfSTiq2t4otmyPespKhEg "W3C-Validator")  (except for jinja template)
-   All your CSS files should be in the  `styles`  folder
-   All your images should be in the  `images`  folder
-   You are not allowed to use  `!important`  or  `id`  (`#...`  in the CSS file)
-   All tags must be in uppercase
-   Current screenshots have been done on  `Chrome 56.0.2924.87`.
-   No cross browsers

## More Info

### Install Flask

```
$ pip3 install Flask
```
