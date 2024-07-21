def greet(fx):
    def mfx():
        print("good morning")
        fx()
        print("thanks for using this function")
    return mfx()
@greet
def hello():
    print("hello world")
greet(hello())



def welcome(fx):
    def bfx():
        print("hello coders")
    fx()
    print("i hope that it is good experience for all of you")
    return bfx()

@welcome
def hi():
    print("hi everyone")

welcome(hi())