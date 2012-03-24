import string
class CLInterpreter:
    """A simple class for writing line-oriented command interpreters.

    """
    prompt = '> '
    identchars = string.ascii_letters + string.digits + '_'
    
    def __init__(self):
        pass

    def parseline(self, line):
        """Parse the line into a command name and arguments.
        Returns a tuple containing (command, args).

        """
        line = line.strip()
        if not line:
            return None, None
        i, n = 0, len(line)
        while i < n and line[i] in self.identchars: i += 1
        cmd, arg = line[:i], line[i:].strip()
        return cmd, arg

    def onecommand(self, line):
        """Interpret the command.

        """
        cmd, arg = self.parseline(line)
        if not line:
            return ''
        if cmd is None:
            return ''
        if cmd == '':
            return ''
        else: 
            try:
                func = getattr(self, 'do_' + cmd)
            except AttributeError:
                return 'command not found'
            return func(arg)

    def do_help(self, arg):
        if arg:
            try:
                func = getattr(self, 'help_' + arg)
            except AttributeError:
                try:
                    doc = getattr(self, 'do_' + arg).__doc__
                    if doc:
                        return '%s' % str(doc)
                except AttributeError:
                    pass
                return 'there is no help for %s' % arg
            func()
