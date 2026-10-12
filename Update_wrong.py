
def update_wrong():
    print(score)
    score = score + 10


print("Original code result:")

try:
    update_wrong()
except UnboundLocalError as e:
    print("UnboundLocalError:", e)


score = 50


def update():
    global score
    print(score)
    score = score + 10


print("Corrected code output:")
update()
print(score)
