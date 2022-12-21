from webServer import *

def test1():
    return "test1"

def test2():
    return "test2"

def add(num1,num2):
    return int(num1) + int(num2)

def main():
    methods = {"test1":(test1,[]),
                "test2":(test2,[]),
                "add":(add,["num1","num2"])}

    server = WebServer(8350,methods)

if __name__ == "__main__":
    main() 