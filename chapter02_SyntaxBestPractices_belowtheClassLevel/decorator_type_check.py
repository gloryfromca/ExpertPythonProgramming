from functools import wraps
import collections
methods_args_dict = {}
def args_check(_in=(), _out=()):
    def function_control(function):
        name = function.__name__
        in_out = collections.namedtuple("types", ["in_types", "out_types"])
        methods_args_dict[name] = in_out(_in, _out)
        print(_in, "is a ", type(_in))
        print(_out, "is a ", type(_out))
        def _check_types(_types, _args):
            for _type, _arg in zip(_types, _args):
                if isinstance(_arg, _type):
                    continue
                raise TypeError("arg: %s should be %s"%(_arg, _type))

        @wraps(function)
        def function_replacer(*args):
            print("args is a" + str(type(args)))
            _check_types(methods_args_dict[name].in_types, args)

            res = function(args)
            if type(res) not in (tuple, ):
                res = (res, )
            _check_types(methods_args_dict[name].out_types, res)

            return res
        return function_replacer
    return function_control

@args_check((list, ), (int, int))
def ss(d):
    return 1, 6
ss([1, 2])

@args_check((list, ), (float, int))
def ss(d):
    return 1, 6
ss([1, 2])
