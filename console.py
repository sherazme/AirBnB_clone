#!/usr/bin/python3
"""Defines HBnB console."""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Defines HolbertonBnB command interpreter
    Attributes:
        prompt (str): command prompt
    """

    prompt = "(hbnb) "
    

    def emptyline(self):
        """Do nothing when receiving an empty line"""
        pass


    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

  
if __name__ == "__main__":
    HBNBCommand().cmdloop()
