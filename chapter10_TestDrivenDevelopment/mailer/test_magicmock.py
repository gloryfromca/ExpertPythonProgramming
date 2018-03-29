import smtplib
from unittest.mock import MagicMock
from .mailer import send

def test_send(monkeypatch):
    smtp_mock = MagicMock()
    smtp_mock.sendmail.return_value = {}

    monkeypatch.setattr(
        smtplib, "SMTP", MagicMock(return_value=smtp_mock)
    )

    res = send(
        "huizhang1995@gmail.com",
        "huizhang1995@gmail.com",
        "happy birthday",
        "happy birthday, zhanghui!",
    )

    assert res == {}