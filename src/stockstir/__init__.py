from .providers import Providers
from .gather_info import GatherInfo
from .tools import Tools
from .api import API


class Stockstir():
    def __init__(self, provider = "cnbc", random_user_agent = False, print_output = False):
        self.providers = Providers(provider, print_output)
        self.gatherinfo = GatherInfo()
        self.tools = Tools(random_user_agent, print_output)
        self.api = API()

        # The providers class needs the gatherinfo class to function:
        self.providers.set_gather_info(self.gatherinfo)

        # The gatherinfo class needs the providers class to function:
        self.gatherinfo.set_providers(self.providers)

        # The tools class needs to be set up with the gatherinfo classes.
        self.tools.set_gather_info(self.gatherinfo)