"""This is a test program."""
import ast
import pylint.lint

def is_valid_python_code(code_string):
    try:
        ast.parse(code_string)
        return True
    except SyntaxError:
        return False

def is_valid_python_file(filename):
    (pylint_stdout, pylint_stderr) = pylint.lint.py_run(filename, return_std=True)
    return pylint_stdout.getvalue() == ""

def main():
    print(is_valid_python_code('print("hello world")'))


if __name__ == "__main__":
    main()