InstaNotifier
=============

Checking for new feed entries periodically, accumulates new entries and sends the notifications.
Includes API based UI listing all the saved entries. UI allows rating, searching, filtering (deployed to Heroku free dyno `instanotifier.herokuapp.com`_)

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django


:Python: 3.7
:Django: 2.2
:License: MIT


Introductory Documentation
==========================

Goal
----
Periodically check for updates on some source (RSS, API, etc.), store new entries into db, and send notifications about the new ones (email, FB Messenger, push, Slack, etc.).

Components
----------
**Fetcher** → **Parser** → **Model**  → **Publisher**

**Fetcher**  ← *(source from where to fetch)* ← **FeedSource settings** → (*target where to send notification)* → **Publisher**


:Fetcher: Gets data from the particular source (RSS, API)
:Parser: Formalize the data fetched from the particular source into some model instance
:Filter: Having the set of new data entries, filters out the existing ones
:Model: Saves the data into the db
:Publisher: Sends out the data into the particular channel (email, fb messenger, etc.)
:FeedSource Settings: The settings application for wiring up the source to fetch from, target to publish notifications to, interval with which to fetch data, and on/off switcher
:API: REST API exposing access to stored data
:UI: Displays the stored entries, supports filtering and searching. API based

Implemented functionality
-------------------------

* Modular architecture
* RssFetcher → RssParser → RssNotification model → Email publisher
* FeedSource settings application
* Using of FeedSource instance data in the RssFetcher and Email publisher
* Tests
* User registration, integration with Mailgun (out of box from the cookiecutter project template)
* Ansible deployment scripts for VPS (Located in `separate repository`_)

* REST API for listing, rating, searching, filtering of stored entries
* API based UI listing all the saved RssNotifications. Allows rating of items, searching, filtering by date
* UI is deployed to Heroku `instanotifier.herokuapp.com`_ (It is a free dyno, so wait a little for it to wake up)

.. _`separate repository`: https://github.com/AlexanderKaluzhny/deployment-scripts/tree/v0.7
.. _`instanotifier.herokuapp.com`: https://instanotifier.herokuapp.com/api/v1/?format=html

Possible features to be added
-----------------------------

* Make a relation of RssNotification to the particular user.
* Showing only user-owned content.
* Allow sending of emails to the verified user email only
* Run Celery tasks in separate queues
* Send logs to log aggregator
* Send errors to Sentry
* Monitor server metrics
* Cache existing entry ids in the Redis to avoid requests to db every time the feed is fetched
* Using API of specific source platform, request additional information about particular source entry
* Getting updates on already saved entries
* [Implemented] Expose access to saved entries through REST API
* Use non-blocking I/O for fetching of RSS


Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.


Celery
^^^^^^

To run celery:

.. code-block:: bash

    cd instanotifier
    celery -A instanotifier.taskapp worker -B -l info


Running tests
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ ./manage.py test


Live reloading and Sass CSS compilation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Moved to `Live reloading and SASS compilation`_.

.. _`Live reloading and SASS compilation`: http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html




Email Server
^^^^^^^^^^^^

In development, it is often nice to be able to see emails that are being sent from your application. For that reason local SMTP server `MailHog`_ with a web interface is available as docker container.

.. _mailhog: https://github.com/mailhog/MailHog

Container mailhog will start automatically when you will run all docker containers.
Please check `cookiecutter-django Docker documentation`_ for more details how to start all containers.

With MailHog running, to view messages that are sent by your application, open your browser and go to ``http://127.0.0.1:8025``




Deployment
----------

The following details how to deploy this application.


Starting up with `tmuxinator` locally
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Just use the ``tmuxinator-inr.yml`` script provided.


VPS Server using Ansible and Fabric
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Scripts are located `in this repository`_.

.. _`in this repository`: https://github.com/AlexanderKaluzhny/deployment-scripts


Heroku
^^^^^^

See detailed `cookiecutter-django Heroku documentation`_.

.. _`cookiecutter-django Heroku documentation`: http://cookiecutter-django.readthedocs.io/en/latest/deployment-on-heroku.html



Docker
^^^^^^

See detailed `cookiecutter-django Docker documentation`_.

.. _`cookiecutter-django Docker documentation`: http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html


Settings
--------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html
