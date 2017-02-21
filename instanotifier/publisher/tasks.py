from __future__ import absolute_import

from celery import shared_task

from instanotifier.publisher.email.publisher import RssNotificationEmailPublisher

# TODO: ignore_result ?
@shared_task
def publish(saved_pks, feedsource_pk):

    publisher = RssNotificationEmailPublisher(saved_pks, feedsource_pk)
    publisher.publish()
