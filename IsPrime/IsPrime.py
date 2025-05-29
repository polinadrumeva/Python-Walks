
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    try:
        number = int(input("Въведете цяло число: "))
        if is_prime(number):
            print(f"{number} е просто число.")
        else:
            print(f"{number} не е просто число.")
    except ValueError:
        print("Грешка: моля, въведете валидно цяло число.")

if __name__ == "__main__":
    main()