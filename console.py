#!/usr/bin/python3
"""
Contains the entry point of the command interpreter
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter"""
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
