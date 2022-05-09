def my_function(*args, **kwargs):
    test_number = Element("test-input").element.value
    if int(test_number)%2==0:
        Element("test-output").element.innerHTML = "Even"
    else:
        Element("test-output").element.innerHTML = "Odd"
