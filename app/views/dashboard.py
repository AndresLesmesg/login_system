from . import views


@views.route('/')
def index():
    return "Home"
