class Calculation:
    """Approximate solution of f(x)=0 by Newton's, secant, chord methods.

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

    def newton(self, Df, x0, epsilon) -> complex or None:
        xn = x0
        flag = True
        count = 0
        while flag:
            fxn = self.function(xn)
            count += 1
            if abs(fxn) < epsilon:
                print('Found solution after', count, 'iterations.')
                return xn
            Dfxn = Df(xn)
            if Dfxn == 0:
                print('Zero derivative. No solution found.')
                return None
            xn = xn - fxn / Dfxn
        print('Exceeded maximum iterations. No solution found.')
        return None

    def secant(self, x0, x1, epsilon) -> complex or None:
        count = 0
        while abs(x1 - x0) > epsilon:
            tmp = x1
            try:
                x1 = x1 - (x1 - x0) * self.function(x1) / (self.function(x1) - self.function(x0))
            except Exception:
                print('Zero derivative. No solution found.')
                return None
            x0 = tmp
            count += 1

        print('Found solution after', count, 'iterations.')
        return x1

    def chord(self, x0, x1, epsilon) -> complex:
        f_x0 = self.function(x0)
        f_x1 = self.function(x1)
        iteration_counter = 0
        while abs(f_x1) > epsilon:
            try:
                denominator = (f_x1 - f_x0) / (x1 - x0)
                x = x1 - f_x1 / denominator
            except ZeroDivisionError:
                print("Error! - denominator zero for x = ", x)
                exit(1)  # Abort with error
            x0 = x1
            x1 = x
            f_x0 = f_x1
            f_x1 = self.function(x1)
            iteration_counter += 1
        # Here, either a solution is found, or too many iterations
        if abs(f_x1) > epsilon:
            print("Solution not found!")
        else:
            print("Number of function calls: ", iteration_counter)
        return x
