======================
AJAYIEZEKIEL9000SCRUMY
======================

Ajayiezekiel9000scrumy is a simple Django app created during six-week Django Linuxjobber internship. 

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "ajayiezekiel9000scrumy" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'ajayiezekiel9000scrumy',
    ]

2. Include the ajayiezekiel9000scrumy URLconf in your project urls.py like this::

    path('ajayiezekiel9000scrumy/', include('ajayiezekiel9000scrumy')),

3. Run ``python manage.py migrate`` to create the ajayiezekiel9000scrumy models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a ajayiezekiel9000scrumy (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/ajayiezekiel9000scrumy/ to consume the application