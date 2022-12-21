from webServer import *

counter = 0

def increment(increment):
    global counter
    counter += int(increment)
    return counter

def add(num1,num2):
    return int(num1) + int(num2)

def main():
    methods = {"increment":(increment,["increment"]),
                "add":(add,["num1","num2"])}

    server = WebServer(80,methods)

if __name__ == "__main__":
    main() 