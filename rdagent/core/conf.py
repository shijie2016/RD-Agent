from __future__ import annotations

from pathlib import Path

from pydantic_settings import BaseSettings

# TODO: use pydantic for other modules in Qlib
# from pydantic_settings import BaseSettings


class RDAgentSettings(BaseSettings):
    # TODO: (xiao) I think LLMSetting may be a better name.
    # TODO: (xiao) I think most of the config should be in oai.config
    # Log configs
    # TODO: (xiao) think it can be a separate config.
    log_trace_path: str | None = None

    # azure document intelligence configs
    azure_document_intelligence_key: str = ""
    azure_document_intelligence_endpoint: str = ""
    # factor extraction conf
    max_input_duplicate_factor_group: int = 300
    max_output_duplicate_factor_group: int = 20
    max_kmeans_group_number: int = 40

    # workspace conf
    workspace_path: Path = Path.cwd() / "git_ignore_folder" / "RD-Agent_workspace"

    # multi processing conf
    multi_proc_n: int = 1

    # pickle cache conf
    cache_with_pickle: bool = True  # whether to use pickle cache
    pickle_cache_folder_path_str: str = str(
        Path.cwd() / "pickle_cache/",
    )  # the path of the folder to store the pickle cache
    use_file_lock: bool = (
        True  # when calling the function with same parameters, whether to use file lock to avoid
        # executing the function multiple times
    )


RD_AGENT_SETTINGS = RDAgentSettings()
