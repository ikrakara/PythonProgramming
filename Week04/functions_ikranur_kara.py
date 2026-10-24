import inspect

# 1. custom_power (Lambda Function)
custom_power = lambda x=0, /, e=1: x ** e


# 2. custom_equation
def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """Calculates custom equation.

    :param x: First positional argument
    :param y: Second positional argument
    :param a: Exponent for x
    :param b: Exponent for y
    :param c: Divisor
    :return: Result of the equation
    """
    for param_name, param_val in [('x', x), ('y', y), ('a', a), ('b', b), ('c', c)]:
        if not isinstance(param_val, int) or isinstance(param_val, bool):
            raise TypeError(f"Argument {param_name} must be an integer.")

    return float((x ** a + y ** b) / c)


# 3. fn_w_counter
def fn_w_counter() -> (int, dict[str, int]):
    if not hasattr(fn_w_counter, "total_calls"):
        fn_w_counter.total_calls = 0
        fn_w_counter.caller_counts = {}

    fn_w_counter.total_calls += 1

    # Çağıran modülün adını alalım
    frame = inspect.currentframe().f_back
    caller_name = frame.f_globals.get("__name__", "__main__")

    fn_w_counter.caller_counts[caller_name] = fn_w_counter.caller_counts.get(caller_name, 0) + 1

    return fn_w_counter.total_calls, dict(fn_w_counter.caller_counts)
