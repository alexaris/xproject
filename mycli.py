import cmd
import il2stat

class MyCLI(cmd.CLInterpreter):
    
    def __init__(self):
        cmd.CLInterpreter.__init__(self)
        self.prompt = '> '

    def do_hello(self, arg):
        """Greeting message.
        """
        if arg: arg = ' ' +  arg
        return 'hi%s!' % arg

    def do_stat(self, arg):
        return il2stat.get_stat(r'd:/games/il-2 sturmovik 1946/log.lst')
