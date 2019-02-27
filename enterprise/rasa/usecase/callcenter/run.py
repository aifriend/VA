from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import os
import rasa_core

from typing import Text, List
from gevent.pywsgi import WSGIServer
from rasa_core import constants, server
from rasa_core import utils
from rasa_core.agent import Agent
from rasa_core.channels import UserMessage, InputChannel
from rasa_core.interpreter import RegexInterpreter
from rasa_core.tracker_store import TrackerStore
from rasa_core.utils import AvailableEndpoints
from rest import HttpInputComponent
from config import Config


def handle_channels(initial_agent: Agent, channels: List[InputChannel],
                    http_port: int = constants.DEFAULT_SERVER_PORT,
                    serve_forever: bool = True,
                    route: Text = "/webhooks/") -> WSGIServer:
    # Build APIs
    app = server.create_app(initial_agent)

    rasa_core.channels.channel.register(channels,
                                        app,
                                        initial_agent.handle_message,
                                        route=route)

    http_server = WSGIServer(('0.0.0.0', http_port), app)  # gunicorn
    http_server.start()

    if serve_forever:
        http_server.serve_forever()
    return http_server


def run_callcenter():
    logging.basicConfig(level="DEBUG")  # Options: "DEBUG" for information about intent and entities
    logging.addLevelName(logging.WARNING, "\033[1;31m%s\033[1;0m" % logging.getLevelName(logging.WARNING))
    logging.addLevelName(logging.ERROR, "\033[1;41m%s\033[1;0m" % logging.getLevelName(logging.ERROR))

    # Logs
    # utils.configure_colored_logging("DEBUG")  # --verbose --quiet
    utils.configure_file_logging("DEBUG", "logs/app-run.log")

    # End points
    if Config().isDev():
        endpoints = AvailableEndpoints.read_endpoints("endpoints-dev.yml")
    else:
        endpoints = AvailableEndpoints.read_endpoints("endpoints-pro.yml")

    # Tracker store
    tracker_store = TrackerStore.find_tracker_store(None, endpoints.tracker_store)

    # Load agent
    dialog_model = os.path.abspath("usecase/callcenter/models/dialogue/")
    agent = Agent.load(
        dialog_model,
        interpreter=RegexInterpreter(),
        generator=endpoints.nlg,
        tracker_store=tracker_store,
        action_endpoint=endpoints.action
        )

    # Server start
    logging.debug("Chatbot has been initialized")
    rasa_server = handle_channels(agent, [HttpInputComponent()])

    return rasa_server


if __name__ == '__main__':
    run_callcenter()
