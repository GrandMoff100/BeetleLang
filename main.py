from interpreter import Interpreter

    
interpreter = Interpreter()

while True:
    program = interpreter.compile(input(">>> "))

    program.run()

