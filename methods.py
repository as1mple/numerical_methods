from sympy import Symbol


class Calculation:
    """Approximate solution of f(x)=0 by Newton's, secant and chord methods.

       Parameters
       ----------
       f : function
           Function for which we are searching for a solution f(x)=0.
       Df : function
           Derivative of f(x).
       x0, x1 : number
           The interval in which to search for a solution.
       epsilon : number
           Stopping criteria is abs(f(x)) < epsilon.
       -------
       """

    def __init__(self, function):
        self.function = function

    def newton(self, x0: complex or float or int, x1, epsilon: float or int) -> complex or None:
        x = Symbol('x')
        dif_str = str(self.function(x).diff('x'))
        Df = lambda x: eval(dif_str)
        xn = x1
        iterations = 0
        while abs(xn - x0) > epsilon:
            fxn = self.function(xn)
            x0 = xn
            iterations += 1
            Dfxn = Df(xn)
            if Dfxn == 0:
                print('Zero derivative.')
                return None, iterations
            xn = xn - fxn / Dfxn
        return xn, iterations

    def secant(self, x0: complex or float or int, x1: complex or float or int,
               epsilon: float or int) -> complex or None:
        iterations = 0
        while abs(x1 - x0) > epsilon:
            tmp = x1
            try:
                x1 = x1 - (x1 - x0) * self.function(x1) / (self.function(x1) - self.function(x0))
            except ZeroDivisionError as e:
                print(e)
                return None, iterations
            x0 = tmp
            iterations += 1

        return x1, iterations

    def chord(self, x0: float or int, x1: float or int, epsilon: float or int) -> complex or None:
        iterations = 0
        while True:
            try:
                xn = x0 - self.function(x0) * (x1 - x0) / (self.function(x1) - self.function(x0))
            except ZeroDivisionError as e:
                print(e)
                return None, iterations

            fxn = self.function(xn)
            iterations += 1
            if abs(fxn) <= epsilon:
                return xn, iterations
            elif self.function(x0).real * fxn.real < 0:
                x0 = x0
                x1 = xn
            elif self.function(x1).real * fxn.real < 0:
                x0 = xn
                x1 = x1
            elif fxn == 0:
                return xn, iterations
            else:
                print("Method fails.")
                return None, iterations
