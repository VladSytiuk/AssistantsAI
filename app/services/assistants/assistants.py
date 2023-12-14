from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from langchain_core.messages import SystemMessage

from app.services.assistants.templates import (
    TRAVEL_AGENT_PROMPT_TEMPLATE,
    MARKETING_SPECIALIST_PROMPT_TEMPLATE,
)
from app.services.assistants.errors import WrongQueryError


class BaseAssistant:
    def __init__(self):
        self.llm = ChatOpenAI(model_name="gpt-3.5-turbo")
        self.prompt = None
        self.agent = None

    async def process_query(self, query: str) -> str:
        self.agent = await self._get_agent_or_raise_exception(query)
        self.prompt = await self._get_assistant_prompt(self.agent)
        answer = self.llm(
            [SystemMessage(content=self.prompt), HumanMessage(content=query)]
        )
        return answer.content

    async def _get_agent_or_raise_exception(self, query: str) -> str:
        agent = self.llm(
            [
                HumanMessage(
                    content=f"Check if this question is related to marketing or traveling: {query} "
                    f"if it's related to marketing, answer 'marketing-specialist' "
                    f"if it's related to traveling, answer 'travel-agent', "
                    f"if it's not related to marketing or traveling, answer 'False'"
                )
            ]
        )
        if agent.content == "False":
            raise WrongQueryError()
        return agent.content

    @staticmethod
    async def _get_assistant_prompt(agent: str) -> str:
        if agent == "travel-agent":
            return TRAVEL_AGENT_PROMPT_TEMPLATE
        if agent == "marketing-specialist":
            return MARKETING_SPECIALIST_PROMPT_TEMPLATE
