#!/usr/bin/python3
def class_to_json(obj):
    if not hasattr(obj, '__dict__'):
        raise ValueError("Input object must be an instance of a class with attributes.")

    obj_dict = vars(obj)
    serializable_dict = {}

    for key, value in obj_dict.items():
        if isinstance(value, (list, dict, str, int, bool)):
            serializable_dict[key] = value

    return serializable_dict
