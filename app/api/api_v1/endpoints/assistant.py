from fastapi import APIRouter

from app.services.assistants import BaseAssistant
from app.schemas.query import Query
from app.services.store import JsonlStore

router = APIRouter()


@router.post("/query")
async def send_query(query: Query):
    assistant_service = BaseAssistant()
    answer = await assistant_service.process_query(query.query)
    store_service = JsonlStore()
    await store_service.store(query.query, assistant_service.agent, answer)
    return {"message": answer}
