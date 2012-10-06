OneRPC
======

Prototype of an RPC framework to build Services that can
be used as libraries *or* as client/server.


**Step #1 - write your library in plain Python**

Example -- a *science.py* module::


    def multiplication(one, two):
        """Returns one * two

        Options: one and two
        """
        return int(one) * int(two)


**Step #2 - use it it your code with onerpc.Service**

Example::

    from onerpc import Service

    science_service = Service('science')
    print science_service.multiplication(3, 5)


The only difference with plain Python is the **Service** indirection,

When called, the code will be called directly unless configured otherwise.

In other words, everything will be running in pure Python and you will
get the usual traceback, pdb and so on.

The service name must be the fully qualified importable name you
would use with an import statement. For example, if you have
an **elasticsearch** module in a **apps** packages, you would
use::

    es = Service('elasticsearch.apps')


**Step #3 - at deployment time, chose where to run the Service**

The interesting thing happens when the application is deployed.

Beside plain Python, the Service can run on ITC, IPC or TCP

Example with TCP on port 1234 -- server-side::

    $ zerorpc --server --bind tcp://0.0.0.0:1234 science


On the client-side, a **locate_service()** function can be used to point the application
to the right endpoint in the Application startup code::

    # application init time...
    from onerpc import locate_service
    locate_service('science', 'tcp://0.0.0.0:1234')

    # the code, as before...
    from onerpc import Service

    science_service = Service('science')
    print science_service.multiplication(3, 5)

