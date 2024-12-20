# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.

import pytest
import os

from pathlib import Path


@pytest.fixture
def blender_location() -> Path:
    return Path(os.environ["BLENDER_EXECUTABLE"])


@pytest.fixture
def script_location() -> Path:
    return Path(__file__).parent / "test_scripts"
