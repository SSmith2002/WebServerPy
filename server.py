from webServer import *

def test1(params):
    return "test1"

def test2(params):
    return "test2"

def add(params):
    num1 = int(params["num1"])
    num2 = int(params["num2"])

    return num1 + num2

def main():
    methods = {"test1":(test1,[]),
                "test2":(test2,[]),
                "add":(add,["num1","num2"])}

    server = WebServer(8350,methods)

if __name__ == "__main__":
    main() 