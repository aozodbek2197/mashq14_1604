# 1-mashq
class CircuitBreaker:
    def __init__(self, limit):
        self.failures = 0
        self.limit = limit

    def call(self, func):
        if self.failures >= self.limit:
            print("Blocked")
            return
        try:
            return func()
        except:
            self.failures += 1
# 2-mashq
class Middleware:
    def __init__(self, next=None):
        self.next = next

    def handle(self, req):
        print("Middleware")
        if self.next:
            self.next.handle(req)
# 3-mashq
class Request:
    def __init__(self, data):
        self.data = data

class Response:
    def __init__(self, data):
        self.data = data
# 4-mashq
class Router:
    def __init__(self):
        self.routes = {}

    def add(self, path, func):
        self.routes[path] = func

    def resolve(self, path):
        return self.routes.get(path)
# 5-mashqclass Container:
    def __init__(self):
        self.services = {}

    def register(self, name, obj):
        self.services[name] = obj

    def get(self, name):
        return self.services.get(name)
