import os
import requests_mock
import unittest

from functions.Slack.main import handle, ButtonClickType


@requests_mock.Mocker()
class SlackTestCase(unittest.TestCase):
    """Test processing of IoT button states"""

    @classmethod
    def setUpClass(self):
        self.slack_webhook_url = "https://hooks.slack.com/test"
        self.slack_channel = '#test'

        os.environ['COFFEE_BUTTON_SLACK_WEBHOOK_URL'] = self.slack_webhook_url
        os.environ['COFFEE_BUTTON_SLACK_CHANNEL'] = self.slack_channel

    def test_single_click_type(self, mock):
        mock.post(self.slack_webhook_url)
        handle({'clickType': str(ButtonClickType.Single)}, None)
        self.assertTrue(mock.called)
        self.assertEquals(mock.call_count, 1)

    def test_double_click_type(self, mock):
        mock.post(self.slack_webhook_url)
        handle({'clickType': str(ButtonClickType.Double)}, None)
        self.assertFalse(mock.called)

    def test_long_click_type(self, mock):
        mock.post(self.slack_webhook_url)
        handle({'clickType': str(ButtonClickType.Long)}, None)
        self.assertFalse(mock.called)
