import logging
import os
import shutil
import stat

from rasa_core import train, utils
from config import Config
from rasa_core.utils import AvailableEndpoints

BUILD_PATH = "usecase/callcenter/" if Config().isPrePro() else ""

DOMAIN = BUILD_PATH + "data/domain/domain.yml"
STORY = BUILD_PATH + "data/story/"
STORY_GRAPH = BUILD_PATH + "data/display/story_graph.html"
MODEL_PATH = BUILD_PATH + "models/"
MODEL_DIALOG = MODEL_PATH + "dialogue"
POLICY = BUILD_PATH + "policy.yml"
ENDPOINT = BUILD_PATH + "endpoints.yml"


#############################
KERAS_SPLIT_VALIDATION = 0.2
#############################
AUGMENTATION_FACTOR = 20
#############################


logger = logging.getLogger(__name__)


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


def _train_dialogue():
    # End points: ActionServer, NlgServer, TrackerStore and CoreEndpoint
    endpoints = AvailableEndpoints.read_endpoints(ENDPOINT)

    # Training model
    return train.train_dialogue_model(domain_file=DOMAIN,
                                      stories_file=STORY,
                                      output_path=MODEL_DIALOG,
                                      endpoints=endpoints,
                                      policy_config=POLICY,
                                      kwargs={
                                          'augmentation_factor': AUGMENTATION_FACTOR,
                                          'validation_split': KERAS_SPLIT_VALIDATION}
                                      )


if __name__ == '__main__':
    utils.configure_colored_logging(loglevel="INFO")

    # Remove previous model
    _remove_actual_model(MODEL_PATH)

    # Train new model
    _train_dialogue()
