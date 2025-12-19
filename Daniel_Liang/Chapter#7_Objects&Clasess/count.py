class Count:
    def __init__(self, count = 0):
        self.count = count

def main():
    c1 = Count()
    times = 0
    for i in range(100):
        increment(c1, times)

    print(f"count is {c1.count}")
    print(f"times is {times}")

def increment(c, times):
    c.count += 1
    times +=1

main()