import sys
import time
args = sys.argv[1:]

class Random:
    def __init__(self):
        self.ver = "0.0.2"

    def randint(self, startA, end, step, start=False, difficult=1):
        c = 0
        if start == False:
            start = time.time()
        arr = []
        for i in range(int((end - startA) / step) + 1):
            arr.append(i * step)
        for i in range(100000*difficult):
            c += 1
        res = time.time()
        out = int(str(res - start)[-(len(str(len(arr) - 1))):-1] + str(res-start)[-1])
        if out > len(arr) - 1:
            out = int(str(res - start)[7:len(str(len(arr) - 1))+7])
        if out > len(arr) - 1:
            out = int((len(arr)) - self.randint(0,len(arr) - 1,1))

        try:
            return round(arr[out],5)
        except:
            return round(arr[0],5)

    def randelem(self,arr):
        return arr[self.randint(0,len(arr)-1,1)]

    def random(self, steps):
        arr = []
        for i in range(steps):
            arr.append(self.randint(0,1,0.0001))
        return array(arr)

random = Random()

if len(args) > 1:
    if args[0] == "randint":
        difficult = 1
        if len(args) > 4:
            difficult = int(args[4])
        print(random.randint(int(args[1]),int(args[2]),float(args[3]),difficult=difficult))
    elif args[0] == "randelem":
        print(random.randelem(args[1].split(",")))
    elif args[0] == "help":
        print("""HELP
    randint - рандомное число; пример - NumPy.exe randint 0 10 1; если хотите увеличить рандомность добавьте ещё цифру; пример NumPy.exe randint 0 10 1 5
    randelem - рандомный элемент из массива; пример - NumPy.exe randelem hi,hello
    Спасибо что используете мой рандом :)""")
    else:
        print("Я не понял вашей команды, напишите help")
elif __name__ == "__main__":
    randint = random.randint(0,10,1)
    print(f"Вот пример рандома от 0 до 10, с размером шага 1 - {randint}")
