from sympy import Symbol

from methods import Calculation


def input_arg(text, func=complex) -> complex:
    while True:
        tmp = input(text).replace("i", "j")
        try:
            tmp = func(tmp)
            return tmp
        except Exception:
            print("ERROR!!! Try again...")


def input_func():
    while True:
        try:
            print("------------------------------------------------------------------------------------------------")
            func = input("input Function = ")
            function = lambda x: eval(func)
            function(0)
            if not func.find("x") == -1: return function
            print("ERROR!!!it's not function.Try again...")
        except Exception as e:
            print(e)


def main() -> None:
    print("Hello!!!")
    print("Approximate solution of f(x)=0 by "
          "\n* Newton's method,"
          "\n* Secant method,"
          "\n* Chord method")
    while True:
        function = input_func()
        testing = Calculation(function=function)
        cod_method = {"NEWTON'S": 0, "SECANT": 1, "CHORD": 2}
        flag = True
        while flag:
            flag_ = True
            while flag_:
                method = cod_method.get(input("Input method : ").upper(), -1)
                flag_ = False if method != -1 else True
                if flag_: print("ERROR!!! Try again...")
            if method == 0:
                x0 = input_arg("x0 = ")
                epsilon = input_arg("epsilon = ", float)
                x = Symbol('x')
                dif_str = str(function(x).diff('x'))
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

            print(
                f"A solution is: {str(result).replace('(', '').replace(')', '').replace('+0j', '').replace('j', 'i')}")
            print("------------------------------------------------------------------------------------------------")
            flag = False if input("Change method ? y/n ").lower() != "y" else True
        if input("Change Function? y/n ").lower() == "n": exit("BYE"); break


if __name__ == '__main__':
    main()
