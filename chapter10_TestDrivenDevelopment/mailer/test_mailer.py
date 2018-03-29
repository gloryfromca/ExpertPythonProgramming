from chapter10_TestDrivenDevelopment.mailer.mailer import send
import pytest
import smtplib

class FakeSMTP(object):
    def __init__(self, *args, **kwargs):
        pass
    def quit(self):
        pass
    def sendmail(self, *args, **kwargs):
        return {}

@pytest.yield_fixture()
def patch_smtplib():
    old_smtp = smtplib.SMTP
    smtplib.SMTP = FakeSMTP
    yield
    smtplib.SMTP = old_smtp

def test_send(patch_smtplib):
    res = send(
    "huizhang1995@gmail.com",
    "huizhang1995@gmail.com",
    "happy birthday",
    "happy birthday, zhanghui!",
    )
    assert res == {}