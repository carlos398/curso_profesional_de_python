def make_division_by(n :int):
    def number(x :int) -> float:
        assert n  > 0 , "u can't divide by 0"
        return x/n
    return number


def run():
    divide_by = make_division_by(5)
    print(divide_by(100))


if __name__ == "__main__":
    run()