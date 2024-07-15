from pathlib import Path

from rdagent.components.coder.model_coder.model import ModelExperiment
from rdagent.core.prompts import Prompts
from rdagent.core.scenario import Scenario

prompt_dict = Prompts(file_path=Path(__file__).parent / "prompts.yaml")

QlibModelExperiment = ModelExperiment


class QlibModelScenario(Scenario):
    @property
    def background(self) -> str:
        return prompt_dict["qlib_model_background"]

    @property
    def source_data(self) -> str:
        raise NotImplementedError("source_data of QlibModelScenario is not implemented")

    @property
    def output_format(self) -> str:
        return prompt_dict["qlib_model_output_format"]

    @property
    def interface(self) -> str:
        return prompt_dict["qlib_model_interface"]

    @property
    def simulator(self) -> str:
        return prompt_dict["qlib_model_simulator"]

    def get_scenario_all_desc(self) -> str:
        return f"""Background of the scenario:
{self.background}
The interface you should follow to write the runnable code:
{self.interface}
The output of your code should be in the format:
{self.output_format}
The simulator user can use to test your model:
{self.simulator}
"""