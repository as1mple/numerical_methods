from methods import Calculation


def hello() -> None:
    print("Hello!!!")
    print("Approximate solution of f(x)=0 by "
          "\n* Newton's method,"
          "\n* Secant method,"
          "\n* Chord method")


def input_func():
    while True:
        try:
            print("-" * 92)
            func = input("input Function = ")
            function = lambda x: eval(func)
            function(101.101)
            if not func.find("x") == -1: return function
            print("ERROR!!!it's not function.Try again...")
        except Exception as e:
            print(e)


def input_arg(text, func=complex) -> complex:
    while True:
        tmp = input(text).replace("i", "j")
        try:
            tmp = func(tmp)
            return tmp
        except Exception:
            print("ERROR!!! Try again...")


def input_method(cod_method: dict) -> str:
    while True:
        method = cod_method.get(input("Input method : ").upper(), -1)
        if method != -1: return method
        print("ERROR!!! Try again...")


def print_result(method, res) -> None:
    if method == 3:
        for name, result in res.items():
            print(
                f"{name} Method -> A solution is: {str(result[0]).replace('(', '').replace(')', '').replace('+0j', '').replace('j', 'i')} -> "
                f"after {result[1]} iterations.")
    else:
        print(
            f"A solution is: {str(res[0]).replace('(', '').replace(')', '').replace('+0j', '').replace('j', 'i')} -> "
            f"after {res[1]} iterations.")
    print("-" * 92)


def main() -> None:
    hello()
    cod_method = {"NEWTON'S": 0, "SECANT": 1, "CHORD": 2, "ALL": 3}
    while True:
        function = input_func()
        Numerical_method = Calculation(function=function)
        while True:
            method = input_method(cod_method)
            x0 = input_arg("x0 = ")
            x1 = input_arg("x1 = ")
            epsilon = input_arg("epsilon = ", float)
            if method == 0:
                result = Numerical_method.newton(x0=(x0 + x1) / 2, epsilon=epsilon)
            elif method == 1:
                result = Numerical_method.secant(x0=x0, x1=x1, epsilon=epsilon)
            elif method == 2:
                result = Numerical_method.chord(x0=x0, x1=x1, epsilon=epsilon)
            elif method == 3:
                result = {"Newton's": Numerical_method.newton(x0=x0, epsilon=epsilon),
                          "Secant": Numerical_method.secant(x0=x0, x1=x1, epsilon=epsilon),
                          "Chord": Numerical_method.chord(x0=x0, x1=x1, epsilon=epsilon)}
            print_result(method=method, res=result)
            if input("Change method ? y/n ").lower() == "n": break
        if input("Change Function? y/n ").lower() == "n": exit("BYE")


if __name__ == '__main__':
    main()
