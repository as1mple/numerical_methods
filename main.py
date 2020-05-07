from sympy import Symbol

from methods import Calculation


def input_arg(text, func=float) -> float:
    tmp = input(text)
    try:
        tmp = func(tmp)
        return tmp
    except Exception:
        return 0


def main() -> None:
    print("Hello!!!")
    while True:
        while True:
            try:
                func = input("input Function = ")
                function = lambda x: eval(func)
                function(0)
                # function = lambda x: eval("x ** 5 - 7 * x ** 4 + 3 * x ** 2 - 5 * x + 1")
                break
            except NameError as nm:
                print(nm)

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
                epsilon = input_arg("epsilon = ")
                max_iter = input_arg("max_iter = ", lambda x: int(x))
                x = Symbol('x')
                dif_str = str(function(x).diff('x'))
                print(f"derivative function ")
                dif_function = lambda x: eval(dif_str)

                result = testing.newton(Df=dif_function, x0=x0, epsilon=epsilon, max_iter=max_iter)

            elif method == 1:
                with_ = input_arg("interval with = ")
                to_ = input_arg("intervat to = ")
                count = input_arg("the number of iterations = ", lambda x: int(x))

                result = testing.secant(a=with_, b=to_, N=count)

            else:
                x_prev = input_arg("interval_with = ")
                x_curr = input_arg("interval to = ")
                e = input_arg("e = ")

                result = testing.chord(x_prev=x_prev, x_curr=x_curr, e=e)

            print(result)
            flag = False if input("Change method ? y/n ").lower() != "y" else True
        if input("Change Function? y/n ").lower() == "n": exit("BYE"); break


main()
