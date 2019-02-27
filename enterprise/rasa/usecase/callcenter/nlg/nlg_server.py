from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import argparse
import json

from flask import Flask, request, jsonify
from gevent.pywsgi import WSGIServer
from rasa_core.domain import Domain
from rasa_core.nlg import TemplatedNaturalLanguageGenerator
from rasa_core.trackers import DialogueStateTracker

logger = logging.getLogger(__name__)

DEFAULT_SERVER_PORT = 5056


def configure_colored_logging(loglevel):
    import coloredlogs
    field_styles = coloredlogs.DEFAULT_FIELD_STYLES.copy()
    field_styles['asctime'] = {}
    level_styles = coloredlogs.DEFAULT_LEVEL_STYLES.copy()
    level_styles['debug'] = {}
    coloredlogs.install(
        level=loglevel,
        use_chroot=False,
        fmt='%(asctime)s %(levelname)-8s %(name)s  - %(message)s',
        level_styles=level_styles,
        field_styles=field_styles)


def configure_file_logging(loglevel, logfile):
    if logfile:
        fh = logging.FileHandler(logfile)
        fh.setLevel(loglevel)
        logging.getLogger('').addHandler(fh)
    logging.captureWarnings(True)


def create_argument_parser():
    """Parse all the command line arguments for the nlg server script."""

    parser = argparse.ArgumentParser(
            description='starts the nlg endpoint')
    parser.add_argument(
            '-p', '--port',
            default=DEFAULT_SERVER_PORT,
            type=int,
            help="port to run the server at")
    parser.add_argument(
            '--domain',
            type=str,
            default=None,
            help="path of the domain file to load utterances from"
    )

    return parser


def generate_response(nlg_call, domain):
    kwargs = nlg_call.get("arguments", {})
    template = nlg_call.get("template")
    sender_id = nlg_call.get("tracker", {}).get("sender_id")
    events = nlg_call.get("tracker", {}).get("events")
    tracker = DialogueStateTracker.from_dict(sender_id, events, domain.slots)
    channel_name = nlg_call.get("channel")

    return TemplatedNaturalLanguageGenerator(domain.templates).generate(
            template, tracker, channel_name, **kwargs)


def create_app(d_domain):
    app = Flask(__name__)

    logging.basicConfig(level=logging.DEBUG)

    @app.route("/nlg", methods=['POST', 'OPTIONS'])
    def nlg():
        """Check if the server is running and responds with the version."""
        nlg_call = request.json

        if isinstance(nlg_call, str):
            nlg_call = json.loads(nlg_call)

        response = generate_response(nlg_call, d_domain)
        return jsonify(response)

    return app


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger('matplotlib').setLevel(logging.WARN)
    logging.addLevelName(logging.WARNING, "\033[1;31m%s\033[1;0m" % logging.getLevelName(logging.WARNING))
    logging.addLevelName(logging.ERROR, "\033[1;41m%s\033[1;0m" % logging.getLevelName(logging.ERROR))

    # Logs
    configure_colored_logging("DEBUG")  # --verbose --quiet
    configure_file_logging("DEBUG", "logs/app-nlg.log")

    domain = Domain.load("domain/domain.yml")
    app = create_app(domain)

    http_server = WSGIServer(('0.0.0.0', DEFAULT_SERVER_PORT), app)

    http_server.start()
    logging.info("NLG endpoint is up and running. on {0}".format(http_server.address))

    http_server.serve_forever()
