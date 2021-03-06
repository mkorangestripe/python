# Pip
pip list # list packages installed by pip
pip list --outdated  # list outdated and current versions
pip list --uptodate # list up to date packages
pip list --editable # list editable projects
pip list --local # use when in virtualenv to exclude global packages
pip freeze # list packages in "requirements format"
pip show ipython # show info about the ipython package
pip search ipython # search for ipython packages
pip install ipython # install ipython
pip install --user ipython # install ipython in user directory
pip install --upgrade ipython # upgrade ipython
pip install --upgrade --force-reinstall ipython # upgrade or force-reinstall current version
pip uninstall ipython # uninstall ipython
pip install -r requirements.txt  # install required packages

# Packaging
setup.py  # defines packages to install, can reference requirements.txt for requirements
ping_scan/__init__.py  # required for directories to be seen as packages
ping_scan/ping_scan.py
LICENSE
README.md
tests/  # for unit tests, if any

# Install a project in editable mode (develop mode):
# Project appears to be installed, but is still editable from the src tree.
# This is likely done through symlinks.
pip install -e . # install packages using ./setup.py
pip install -e git+https://git.repo/some_pkg.git#egg=SomeProject

# Virtualenv
mkdir virt-cos-sdk
virtualenv virt-cos-sdk # creates a virtual environment in the directory
. virt-cos-sdk/bin/activate # activate the virtual environment
# Do the package installs with the virtualenv active
deactivate # deactivate the virtual environment
# Note, a leftover .Python file from virtualenv can cause problems when recreating the env.

# Python 3 Virtualenv
pipenv --python python3.7 # Creates a virtualenv and install necessary packages
pipenv shell # Start a shell with the virtualenv active

# Python 3, package code
# This creates a dist directory with a .whl and a tar.gz file.
python3 setup.py sdist bdist_wheel

# Install a wheel package
pip3 install ping_scan_mkorangestripe-0.0.1-py3-none-any.whl
python3 -m pip install ping_scan_mkorangestripe-0.0.1-py3-none-any.whl
