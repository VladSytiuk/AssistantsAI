from fastapi import APIRouter, Depends

from app.api.dependencies import get_store, get_assistant
from app.services.assistants.assistants import BaseAssistant
from app.schemas.query import Query
from app.storages import BaseStore


router = APIRouter()


@router.post("/query")
async def send_query(
    query: Query,
    store: BaseStore = Depends(get_store),
    assistant: BaseAssistant = Depends(get_assistant),
):
    answer = await assistant.process_query(query.query)
    await store.store(query.query, assistant.agent, answer)
    return {"message": answer}
