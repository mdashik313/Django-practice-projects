from celery import Celery

app = Celery('celery_beat')
app.config_from_object('celeryconfig')

@app.task
def print_hello(name):
    print(f"Hello, {name}!")
    return f"Task completed: Hello, {name}!"