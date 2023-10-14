#!/usr/bin/python3
"""This module contains entry point of command interpreter"""

import cmd
from models.base_model import BaseModel
from models import storage
import json
import re


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

    def do_create(self, line):
        """Creates new instance of a Class"""
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            u = storage.classes()[line]()
            u.save()
            print(u.id)

    def do_show(self, line):
        """Print string representation of instance based on name and id"""
        if line == "" or line is None:
            print("** class name missing **")
        else:
            tk_words = line.split(' ')
            if tk_words[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(tk_words) < 2:
                print("** instance id missing **")
            else:
                my_key = "{}.{}".format(tk_words[0], tk_words[1])
                if my_key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[my_key])

    def do_destroy(self, line):
        """Deletes an instance based on name  and id"""
        if line == "" or line is None:
            print("** class name missing **")
        else:
            tk_words = line.split(' ')
            if tk_words[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(tk_words) < 2:
                print("** instance id missing **")
            else:
                my_key = "{}.{}".format(tk_words[0], tk_words[1])
                if my_key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[my_key]
                    storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances"""
        if line != "":
            tk_words = line.split(' ')
            if tk_words[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                new_list = [str(obj) for key, obj in storage.all().items()
                            if type(obj).__name__ == tk_words[0]]
                print(new_list)
        else:
            new_list2 = [str(obj) for key, obj in storage.all().items()]
            print(new_list2)

    def do_update(self, line):
        """Updates an instance based on class name and id"""
        if line == "" or line is None:
            print("** class name missing **")
            return

        reG = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        Match = re.search(reG, line)
        classname = Match.group(1)
        uid = Match.group(2)
        attribute = Match.group(3)
        value = Match.group(4)

        if not Match:
            print("** class name missing **")
        elif classname not in storage.classes():
            print("** class name doesn't not exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            elif not attribute:
                print("** attribute name missing **")
            elif not value:
                print("** value missing **")
            else:
                cast = None
                if not re.search('^".*"$', value):
                    if '.' in value:
                        cast = float
                    else:
                        cast = int
                else:
                    value = value.replace('""', '')
                attributes = storage.attributes()[classname]
                if attribute in attributes:
                    value = attributes[attribute](value)
                elif cast:
                    try:
                        value = cast(value)
                    except ValueError:
                        pass
                setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
