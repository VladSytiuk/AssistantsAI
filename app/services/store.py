from abc import ABC, abstractmethod

import jsonlines


class BaseStore(ABC):
    @abstractmethod
    def store(self, query, agent, answer):
        pass


class JsonlStore(BaseStore):
    async def store(self, query: str, agent: str, answer: str) -> None:
        with jsonlines.open("queries.jsonl", mode="a") as writer:
            writer.write({"query": query, "agent": agent, "answer": answer})
