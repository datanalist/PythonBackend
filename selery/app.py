from celery import Celery


celery_app = Celery('tasks', broker="BROKER_URL", backend="BACKEND_URL")

celery_app.conf.update(
    enable_utc=True,
    timezone='Europe/Moscow',
)