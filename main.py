from sympy import Symbol

from methods import Calculation


def input_arg(text, func=complex) -> complex:
    tmp = input(text)
    try:
        tmp = func(tmp)
        return tmp
    except Exception:
        return 0


def main() -> None:
    print("Hello!!!")
    print("Approximate solution of f(x)=0 by "
          "\n* Newton's method,"
          "\n* Secant method,"
          "\n* Chord method")
    while True:
        while True:
            try:
                func = input("input Function = ")
                function = lambda x: eval(func)
                function(0)
                # function = lambda x: eval("x ** 5 - 7 * x ** 4 + 3 * x ** 2 - 5 * x + 1")
                break
            except Exception as e:
                print(e)

        testing = Calculation(function=function)
        cod_method = {"newtons": 0, "secant": 1, "chord": 2}
        flag = True
        while flag:
            flag_ = True
            while flag_:
                method = cod_method.get(input("Input method : ").lower(), -1)
                flag_ = False if method != -1 else True
                if flag_: print("ERROR!!! Try again...")
            print("Vau")
            if method == 0:
                x0 = input_arg("x0 = ")
                epsilon = input_arg("epsilon = ", float)
                x = Symbol('x')
                dif_str = str(function(x).diff('x'))
                print(f"derivative function ")
                dif_function = lambda x: eval(dif_str)

                result = testing.newton(Df=dif_function, x0=x0, epsilon=epsilon)

            elif method == 1 or method == 2:
                with_ = input_arg("interval with = ")
                to_ = input_arg("intervat to = ")
                epsilon = input_arg("epsilon = ", float)
                if method == 1:
                    result = testing.secant(x0=with_, x1=to_, epsilon=epsilon)
                else:
                    result = testing.chord(x0=with_, x1=to_, epsilon=epsilon)

            print(f"A solution is: {result}")
            flag = False if input("Change method ? y/n ").lower() != "y" else True
        if input("Change Function? y/n ").lower() == "n": exit("BYE"); break


if __name__ == '__main__':
    main()
