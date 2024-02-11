#!/usr/bin/python3
"""base model"""

import uuid
from datetime import datetime


class BaseModel:

    """BaseModle Class"""

    def __init__(self, *args, **kwargs):
        """Initializes attributes

        Args:
            - *args: list of arguments
            - **kwargs: dict of key-values arguments
        """

        tformat = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs is not None and kwargs != {}:
            for k in kwargs:
                if k == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], tformat)
                elif k == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], tformat)
                else:
                    self.__dict__[k] = kwargs[k]
        else
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """string representation"""

        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at"""

        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__"""

        myDict = self.__dict__.copy()
        myDict["__class__"] = type(self).__name__
        myDict["created_at"] = myDict["created_at"].isoformat()
        myDict["updated_at"] = myDict["updated_at"].isoformat()
        return myDict
