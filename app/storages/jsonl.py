import jsonlines

from app.storages.base import BaseStore


class JsonlStore(BaseStore):
    async def store(self, query: str, agent: str, answer: str) -> None:
        with jsonlines.open("queries.jsonl", mode="a") as writer:
            writer.write({"query": query, "agent": agent, "answer": answer})
