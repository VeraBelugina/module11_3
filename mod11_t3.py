import inspect


def introspection_info(obj):
    info = {'type': type(obj), 'attributes': [attr for attr in dir(obj) if not callable(getattr(obj, attr))],
            'methods': [method for method in dir(type(obj)) if callable(getattr(obj, method))],
            'module': inspect.getmodule(introspection_info), 'id': id(obj)}
    return info


number_info = introspection_info(42)
print(number_info)
