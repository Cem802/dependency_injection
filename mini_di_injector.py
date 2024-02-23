class DIContainer:
    def __init__(self):
        self._services = {}
        self._instances = {}

    def register(self, service, implementation, has_dependencies=False):
        self._services[service] = (implementation, has_dependencies)

    def get(self, service):
        if service in self._instances:
            return self._instances[service]

        implementation, has_dependencies = self._services.get(service, (None, False))
        if not implementation:
            raise ValueError(f"Service {service} not found")

        if has_dependencies:
            instance = implementation(self)
        else:
            instance = implementation()

        self._instances[service] = instance
        return instance

# Usage
class ServiceA:
    def do_something(self):
        return "ServiceA is working"

class ServiceB:
    def __init__(self, container):
        self.serviceA = container.get('serviceA')

    def do_something(self):
        return f"ServiceB is working and {self.serviceA.do_something()}"

container = DIContainer()
container.register('serviceA', ServiceA)
container.register('serviceB', ServiceB, has_dependencies=True)

serviceB = container.get('serviceB')
print(serviceB.do_something())