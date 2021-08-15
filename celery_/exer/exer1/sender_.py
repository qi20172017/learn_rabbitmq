from celery_.exer.exer1.task1 import app

app.send_task('tasks', args=(3, 5))