from main import webhook

import unittest
from unittest.mock import patch

import flask
from telegram import Bot

app = flask.Flask(__name__)


class ClientTestCase(unittest.TestCase):
    def test_webhook(self):
        with open("test_message.json") as f:
            with patch.object(Bot, "sendMessage", return_value="test message"):
                with app.test_request_context(method="POST", data=f):
                    r = flask.request
                    webhook(r)


if __name__ == "__main__":
    unittest.main()
