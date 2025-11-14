def serve_chai():
    yield "CUP 1: Masala Chai"
    yield "Cup 2: Ginger chai"
    yield "Cup 3: Elaichi Chai"

stall=serve_chai()

for cup in stall:
    print(cup)


def get_chai_list():
    return ["cup 1","cup 2","cup 3"]

def get_chai_gen():
    yield "Cup 1"
    yield "Cup 2"
    yield "cup 2"


chai=get_chai_gen()
print(next(chai))
print(next(chai))