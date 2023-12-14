This project was completed for the Knowledge Representation course at Vrije Universiteit

# Introduction
Human discussion can be formally represented by logical programming. We show that using the preferred semantics of argumentation frameworks, we can implement a Discussion Game to determine acceptability of arguments. Furthermore, we answer questions to Credulous Decision Problems by implementing admissible, preferred, stable, complete and grounded semantics.

# Usage

### Argumentation game
Our game can be run from a command line instantiated in the project directory by
executing python main.py. The user will then be prompted to choose a argumentation
framework in JSON format to load from /frameworks. Any time there is an argument
to be chosen, the possible choices will be printed alongside their indices. To indicate
their choice, the user must type the corresponding index

### Credulous decision
The credulous decision problem can be answered for any framework calling the
credulous acceptance.py script running a command following the format:
python credulous acceptance.py FULL PATH TO FRAMEWORK ARGUMENT IDENTIFIER.
The JSON framework should be given in the standard format, since it will be automatically converted to our representation. The same file can also be run manually and the ar-
guments can be specified modifying the variables framework path and framework path
directly, under the if name == ’ main ’: line.
Ultimately, the credulous acceptance procedure can also be tested automatically on
every argument over each framework file inside the eponymous folder running the script
tests.py.
