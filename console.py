#!/usr/bin/python3
"""This module contains entry point of command interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Class for commandline interpreter"""

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Exits the program when called"""
        return True

    def do_EOF(self, line):
        """Handles EOF Character"""
        print()
        return True

    def emptyline(self):
        """Doesn't execute when nothing is passed or you press  ENTER"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
