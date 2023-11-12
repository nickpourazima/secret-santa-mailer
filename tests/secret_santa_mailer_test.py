import json
import pytest
from secret_santa.secret_santa_mailer import SecretSantaMailer

@pytest.fixture
def mailer():
    return SecretSantaMailer('test_sender.json', 'test_participants.json')

def test_generate_and_send_assignments(mailer):
    mailer.generate_and_send_assignments()
