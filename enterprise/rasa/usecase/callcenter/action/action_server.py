from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

from builtins import str
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from gevent.pywsgi import WSGIServer
from rasa_core_sdk.executor import ActionExecutor, logger
from rasa_core_sdk import ActionExecutionRejection

DEFAULT_SERVER_PORT = 5055


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


def endpoint_app(cors_origins=None,
                 action_package_name=None
                 ):
    app = Flask(__name__)

    if not cors_origins:
        cors_origins = []

    executor = ActionExecutor()
    executor.register_package(action_package_name)

    CORS(app, resources={r"/*": {"origins": cors_origins}})

    @app.route("/health", methods=['GET', 'OPTIONS'])
    @cross_origin(origins=cors_origins)
    def health():
        """Ping endpoint to check if the server is running and well."""
        return jsonify({"status": "ok"})

    @app.route("/webhook", methods=['POST', 'OPTIONS'])
    @cross_origin()
    def webhook():
        """Webhook to retrieve action calls."""
        action_call = request.json
        try:
            response = executor.run(action_call)
        except ActionExecutionRejection as e:
            logger.error(str(e))
            result = {"error": str(e), "action_name": e.action_name}
            response = jsonify(result)
            response.status_code = 400
            return response

        return jsonify(response)

    return app


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger('matplotlib').setLevel(logging.WARN)
    logging.addLevelName(logging.WARNING, "\033[1;31m%s\033[1;0m" % logging.getLevelName(logging.WARNING))
    logging.addLevelName(logging.ERROR, "\033[1;41m%s\033[1;0m" % logging.getLevelName(logging.ERROR))

    # Logs
    # configure_colored_logging("DEBUG")  # --verbose --quiet
    configure_file_logging("DEBUG", "logs/app-action.log")

    logger.info("Starting action endpoint server...")
    app = endpoint_app(action_package_name='actions.actions')

    http_server = WSGIServer(('0.0.0.0', DEFAULT_SERVER_PORT), app)

    http_server.start()
    logger.info("Action endpoint is up and running. on {0}:{1}"
                .format(http_server.server_host, http_server.server_port))

    http_server.serve_forever()
