#!/usr/bin/python3
"""writing the base class"""
import json


class Base:
    """writing the base class of this model"""

    __nb_objects = 0

    def __init__(self, id=None):
        """constructor method

        Args:
            id : the id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """list of dictionary to json string"""
        if list_dictionaries is None or list_dictionaries == []:
            return ("[]")
        else:
            return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """save the instance of the obj to file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as myfile:
            if (list_objs is None or list_objs == []):
                myfile.write('[]')
            else:
                list_dict = [i.to_dictionary() for i in list_objs]
                myfile.write(Base.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """load list from json string"""
        if json_string is None or json_string == "[]":
            return []
        else:
            return (json.loads(json_string))
