Django DDP Presentation Project
===============================

`Django DDP`_ (realtime) presentation project.  Released under the MIT 
license.

Presentation events (slide advance, questions asked, etc) are dispatched 
asynchronously to browsers using WebSockets_ - people promptly 
participate during delivery & discourse.  ;)


Installation
------------

Install the latest release from pypi (recommended):

.. code:: sh

    pip install dddppp

Clone and use development version direct from GitHub (to test pre-release code):

.. code:: sh

    pip install -e git+https://github.com/tysonclugg/dddppp@develop#egg=dddppp


Contributors
------------
`Tyson Clugg <https://github.com/tysonclugg>`_
    * Author, conceptual design.

.. _Django DDP: https://github.org/commoncode/django-ddp
.. _WebSockets: http://www.w3.org/TR/websockets/
