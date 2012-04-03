# -*- coding: utf-8 -*
import cmd
import il2stat


class MyCLI(cmd.CLInterpreter):
    
    def __init__(self):
        cmd.CLInterpreter.__init__(self)
        self.prompt = '> '

    def do_quit(self, arg):
        """Terminates this application.
        """
        return 'hack_exit'

    def do_exit(self, arg):
        """Terminates this application.
        """
        return 'hack_exit'

    def do_clear(self, arg):
        """Clears the console.
        """
        return 'hack_clear'

    def do_foo(self, arg):
        """This is a command for different test tasks
        """
        if arg: arg = ' ' +  arg
        return 'hi%s!' % arg

    def do_chat(self, arg):
        """Displays chat from log file
        """
        return main.config

    def do_stat(self, arg):
        return il2stat.get_stat(r'd:/games/sturmovik/log.lst')


