# f2py_hello
Demo for bug report on python packaging of Fortran extension with `pyf` file as source

## How to reproduce
* After cloning the repository, create a pyton virtual environment, and activate it: 
```
python3 -m venv venv
. venv/bin/activate
```
* Install and upgrade `pip` and `build` (a PEP-517 package builder)
```
pip install --upgrade pip
pip install --upgrade build
```
* Build the package and notice that it fails when trying to build the binary extension
```
python3 -m build
```
* Open `setup.py` in an editor, and remove the comment on line 29
* Start with a clean slate by removing the directories `build`, `dist`, and `hello.egg-info`
```
rm -rf build/ dist/ hello.egg-info/
```
* Build the package again, and notice that the build now succeeds
```
python3 -m build
```

Line 29 is a work-around to force `hello.pyf` in the source distribution. This should not be necessary. Side effect of the current soluiton is that the `pyf` file also ends up in the binary distribution. Not a huge deal, but strictly speaking it doesn't belong in there.
