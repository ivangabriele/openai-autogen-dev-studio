from typing import List

import agents
from agents.base_agent import BaseAgent
import utils


class Core:
    current_team_agent_index: int = 0
    product_owner: agents.ProductOwner
    team_agents: List[BaseAgent]
    """Ordered list of agents. They will call the Product Owner in order to ask him what to do next."""

    def __init__(
        self,
        product_owner: agents.ProductOwner,
        team_agents: List[BaseAgent],
    ):
        self.product_owner = product_owner
        self.team_agents = team_agents

    async def start(self, initial_message: str):
        self.product_owner.as_assistant_agent.clear_history()
        for agent in self.team_agents:
            agent.as_assistant_agent.clear_history()

        await self.product_owner.ask(initial_message)
        await self.next()

    async def next(self):
        print(self.team_agents)
        print(self.current_team_agent_index)
        current_team_agent = self.team_agents[self.current_team_agent_index]

        await self.product_owner.ask_for_next_task(
            sender=current_team_agent,
        )

        self.current_team_agent_index = (self.current_team_agent_index + 1) % len(
            self.team_agents
        )

        await self.next()
