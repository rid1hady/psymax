# -*- coding: utf-8 -*-
"""
You can create a file called `.env` in the root of the repo, containing your local env vars.
"""
from dotenv import load_dotenv

# Load environment variables
# needs to happen before anything else (to properly instantiate constants)

load_dotenv(verbose=True)

import pytest
import json
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk import Tracker
from rasa_sdk.types import DomainDict
from rasa.shared.core.domain import Domain


@pytest.fixture
def tracker() -> Tracker:
    """Load a tracker object"""
    with open("tests/data/initial_tracker.json") as json_file:
        tracker = Tracker.from_dict(json.load(json_file))
    return tracker


@pytest.fixture
def dispatcher() -> CollectingDispatcher:
    """Create a clean dispatcher"""
    return CollectingDispatcher()


@pytest.fixture
def domain() -> DomainDict:
    """Load the domain and return it as a dictionary"""
    domain = Domain.load("domain.yml")
    return domain.as_dict()
