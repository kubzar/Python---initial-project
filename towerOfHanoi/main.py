def main():
    print("Hello world!")
    print("Hello world!")

if __name__ == '__main__':
    main()

def hanoi(n, pile1, pile2, pile3):
    if n == 1:
        print(f"Move disc from {pile1} to {pile2}.")
    else:
        hanoi(n - 1, pile1, pile3, pile2)
        print(f"Move disc from {pile1} to {pile2}.")
        hanoi(n - 1, pile3, pile2, pile1)

hanoi(3,"A","B","C")

