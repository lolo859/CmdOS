import uuid
import random
def execute():
    uuid.uuid4()
    while True:
        id=str(uuid.uuid4())
        trimmed=id[:random.randint(0,len(id)-1)]
        spaces=" " * random.randint(0,15)
        print(f"{spaces}{trimmed}")