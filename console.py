#!/usr/bin/python3
"""
Contains the entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel
import models
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command interpreter"""
    prompt = '(hbnb) '


    def do_all(self, line):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        if not line or line == 'BaseModel':
            print(str(value) for key, value in storage.all().items()])
        else:
            print("** class doesn't exist **")

    def do_EOF(self, line):
        """EOF command to exit the program"""
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """
        Do nothing
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
