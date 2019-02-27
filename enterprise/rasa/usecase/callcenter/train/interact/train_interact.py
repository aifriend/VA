import logging
import os
import shutil
import stat

from rasa_core import utils, train
from rasa_core.training import interactive
from rasa_core.utils import AvailableEndpoints

logger = logging.getLogger(__name__)

DOMAIN = "data/domain/domain.yml"
STORY = "data/story/"
STORY_GRAPH = "data/display/story_graph.html"
MODEL_PATH = "models/"
MODEL_DIALOG = "dialogue"
POLICY = "policy.yml"
ENDPOINT = "endpoints.yml"


def _handle_error(func, path, exc_info):
    # Check if file access issue
    if not os.access(path, os.W_OK):
        # Try to change the permision of file
        os.chmod(path, stat.S_IWUSR)

        # call the calling function again
        func(path)


def _remove_actual_model(path):
    try:
        #  Delete an empty directory using os.rmdir() and handle exceptions
        try:
            os.rmdir(path)
        except:
            pass

        dir_path = path

        # Delete all contents of a directory using shutil.rmtree() and  handle exceptions
        try:
            # Delete all contents of a directory and handle errors
            shutil.rmtree(dir_path, onerror=_handle_error)
        except:
            pass
    except:
        pass


def train_agent():
    # End points: ActionServer, NlgServer, TrackerStore and CoreEndpoint
    endpoints = AvailableEndpoints.read_endpoints(ENDPOINT)

    return train.train_dialogue_model(domain_file=DOMAIN,
                                      stories_file=STORY,
                                      output_path=MODEL_DIALOG,
                                      endpoints=endpoints,
                                      policy_config=POLICY,
                                      kwargs={
                                          "max_training_samples": 300
                                      })


if __name__ == '__main__':
    utils.configure_colored_logging(loglevel="INFO")

    # Remove previous model
    _remove_actual_model(MODEL_PATH)

    # Train new model
    agent = train_agent()

    agent.visualize(STORY, output_file=STORY_GRAPH, max_history=2)

    interactive.run_interactive_learning(agent, STORY)
