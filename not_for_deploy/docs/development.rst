#################
Development guide
#################


************************
Install the requirements
************************
Install the following:

#. Python
#. PIP_
#. VirtualEnv_
#. virtualenvwrapper_


***********************
Install in a virtualenv
***********************
Create a virtualenv using Python 3 (an isolated Python environment)::

    $ mkvirtualenv -p /usr/local/bin/python3 ievv_opensource

Install the development requirements::

    $ pip install -r requirements.txt


.. _enable-virtualenv:

.. note::

    Whenever you start a new shell where you need to use the virtualenv we created
    with ``mkvirtualenv`` above, you have to run::

        $ workon ievv_opensource


**************
Build the docs
**************
:ref:`Enable the virtualenv <enable-virtualenv>`, and run::

    $ ievv docs --open


*****************************
Create a development database
*****************************
:ref:`Enable the virtualenv <enable-virtualenv>`, and run::

    $ ievv recreate_devdb


*************
Running tests
*************
To run the tests, we need to use a different settings file. We tell ievvtasks to
do this using the ``DJANGOENV`` environent variable::

    $ DJANGOENV=test python manage.py test


.. _PIP: https://pip.pypa.io
.. _VirtualEnv: https://virtualenv.pypa.io
.. _virtualenvwrapper: http://virtualenvwrapper.readthedocs.org/
