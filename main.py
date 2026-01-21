from add import add
from sub import sub
from multi import multi
from div import div

def main():
    a = int(input())
    b = int(input())

    print(f"Addition of {a} and {b}: {add(a, b)}")
    print(f"Subtraction of {a} and {b}: {sub(a, b)}")
    print(f"Multiplication of {a} and {b}: {multi(a, b)}")
    print(f"Division of {a} and {b}: {div(a, b)}")


main()
