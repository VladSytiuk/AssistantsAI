from app.storages import BaseStore
from app.storages import JsonlStore
from app.services.assistants.assistants import BaseAssistant


def get_store() -> BaseStore:
    return JsonlStore()


def get_assistant() -> BaseAssistant:
    return BaseAssistant()
