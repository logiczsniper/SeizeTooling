from abc import abstractmethod, ABC
from src.constants import CommandStrings


class Command(ABC):

    def __init__(self, name, help_string):
        self.name = name
        self.help = help_string

    @abstractmethod
    def run(self):
        pass

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class This(Command):

    def __init__(self):
        super().__init__(CommandStrings.THIS,
                         """
Usage-----------------------¬

λ seize this *path to target directory* *flags*

Flags-----------------------¬

1. Automatic specific folder generation -> --a
    Among the basic subdirectories generated, will search for common words among each directory. 
    If one is spotted, will create a further
    subdirectory of that name and move those files with that word into that directory. 
    For example, if the word "background" is found in multiple of a type of file, they will be 
    moved into a newly generated backgrounds subdirectory.

2. Initialize each subdirectory with readme -> --r
    Each directory created will have a auto-generated readme.md file created with the basic 
    information about the folder.

3. Safe create -> --s
    Before the seize is started, it will make a copy of the original in case you do not like or 
    what to undo the changes made you can simply delete the updated directory and revert 
    back to using the original.

4. Create git commit -> --g
    The changes made will automatically be added to a git commit. Obviously this means the 
    parent directory must be a remote git repository or this will raise an error.

5. Help -> --h
    View this text.
                         """)

    def run(self):
        print("THIS COMMAND")


class Transfer(Command):

    def __init__(self):
        super().__init__(CommandStrings.TRANSFER, "Transfer help")

    def run(self):
        print("TRANSFER COMMAND")


class Shift(Command):

    def __init__(self):
        super().__init__(CommandStrings.SHIFT, "Shift help")

    def run(self):
        print("SHIFT COMMAND")


class Help(Command):

    def __init__(self):
        super().__init__(CommandStrings.SHIFT, "Help")

    def run(self):
        print("""
Usage-----------------------¬

λ seize *command* *required parameters* *optional flags*

Commands--------------------¬

1. this
    The base seize command to complete the main functionality of seize. Organises files, refractors scripts and more 
    depending on the flags used. Use: 'seize this --h' for more help details and flags available.
    
2. shift
    Only move a single directory from one path to another, refractors the scripts. Use: 'seize shift --h' for more help 
    details and flags available.
    
3. transfer 
    Only move a single file from one directory to another, refractors the scripts. Use 'seize transfer --h' for more 
    help details and flags available.

More------------------------¬

If you did not find the information you were looking for, go to the README file found here:
https://github.com/logiczsniper/SeizeTooling/blob/master/README.md
                         """)
