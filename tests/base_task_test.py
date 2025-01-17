from pathlib import Path
from unittest.mock import call

import pytest

from dbt_sugar.core.config.config import DbtSugarConfig
from dbt_sugar.core.flags import FlagParser
from dbt_sugar.core.main import parser
from dbt_sugar.core.task.audit import AuditTask
from dbt_sugar.core.task.base import COLUMN_NOT_DOCUMENTED

FIXTURE_DIR = Path(__file__).resolve().parent


def __init_descriptions():
    flag_parser = FlagParser(parser)
    config_filepath = Path(FIXTURE_DIR).joinpath("sugar_config.yml")
    flag_parser.consume_cli_arguments(
        test_cli_args=["audit", "--config-path", str(config_filepath)]
    )
    sugar_config = DbtSugarConfig(flag_parser)
    sugar_config.load_config()
    audit_task = AuditTask(flag_parser, FIXTURE_DIR, sugar_config=sugar_config)
    audit_task.dbt_definitions = {"columnA": "descriptionA", "columnB": "descriptionB"}
    audit_task.repository_path = Path("tests/test_dbt_project/").resolve()
    return audit_task


@pytest.mark.parametrize(
    "model_name, is_exluded_model",
    [
        pytest.param("my_first_dbt_model", False, id="model is not excluded"),
        pytest.param("my_first_dbt_model_excluded", True, id="model is not excluded"),
    ],
)
def test_is_excluded_model(model_name, is_exluded_model):
    audit_task = __init_descriptions()
    if is_exluded_model:
        with pytest.raises(ValueError):
            audit_task.is_exluded_model(model_name)
    else:
        audit_task.is_exluded_model(model_name)
