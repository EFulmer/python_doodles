w = 3


def modify_w():
    w = w + 1


try:
    modify_w()
except Exception as e:
    print("Can't let you do that, Star Fox!")


def modify_w_works():
    global w
    w = w + 1


modify_w_works()

print(w)
