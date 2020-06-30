#!/usr/bin/python3
"""
Contains the entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel
import models
from models import storage

modelnames = ("BaseModel", "")

class HBNBCommand(cmd.Cmd):
    """Command interpreter"""
    prompt = '(hbnb) '

    def do_create(self, line):
        items = line.split()
        if len(items) is 0:
            print("** class name missing **")
            return
        if (items[0] in modelnames):
            #do the create Model and print id
            model = eval(items[0] + "()")
            print(model.id)
        else:
            print("** class doesn't exist **")

    def do_all(self, line):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        instances = models.storage.all()
        if line is "":
            for key, value in instances.items():
                print(value)
        else:
            args = line.split()
            if args[0] not in self.tbd_name_based_on_do_create:
                print("** class doesn't exist **")
            else:
                for key, value in instances.items():





    def do_EOF(self, line):
        """EOF command to exit the program"""
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """
        Do none
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
