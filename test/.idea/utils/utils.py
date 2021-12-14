def adder_int(a: int, b: int) -> int:
    result = a + b
    return result


def adder_float(a, b) -> float:
    result = a + b
    return result


def compare_two_numbers_int(a: int, b: int):
    if a == b:
        print(f' {a} = {b}')
    elif a > b:
        print(f' {a} > {b}')
    else:
        print(f' {a} < {b}')