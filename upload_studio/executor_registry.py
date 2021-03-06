from rest_framework import status
from rest_framework.exceptions import APIException


class MissingExecutorException(APIException):
    def __init__(self, name):
        super().__init__(
            detail='Executor {} not found. Are you missing a plugin?'.format(name),
            code=status.HTTP_400_BAD_REQUEST,
        )


class _ExecutorRegistry:
    def __init__(self):
        self.executors = {}

    def register_executor(self, executor_class):
        if not executor_class.name:
            raise Exception('An executor class must have a valid name attribute')
        if executor_class.name in self.executors:
            raise Exception('Cannot register an executor with the same name')
        self.executors[executor_class.name] = executor_class

    def get_executor(self, name):
        try:
            return self.executors[name]
        except KeyError:
            raise MissingExecutorException(name)


ExecutorRegistry = _ExecutorRegistry()
