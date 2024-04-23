import unittest
import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_testing import TestCase
from app import create_app
from models import db, Blacklist

class TestBlacklistAPI(TestCase):
    def create_app(self):
        app = create_app(testing=True)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_blacklist_entry(self):
        with self.app.test_client() as client:
            response = client.post('/blacklists', json={
                'email': 'test@example.com',
                'app_uuid': 'abc123',
                'blocked_reason': 'Test block'
            }, headers={})

            data = json.loads(response.data.decode('utf-8'))

            self.assertEqual(response.status_code, 401)
            self.assertEqual(data.get("error"), "Invalid or missing password")

    def test_get_blacklist_entry(self):
        entry = Blacklist(email='test@example.com', ip='127.0.0.1', app_uuid='abc123', blocked_reason='Test block')
        db.session.add(entry)
        db.session.commit()

        with self.app.test_client() as client:
            response = client.get('/blacklists/test@example.com', headers={'Authorization': 'Bearer password'})
            data = json.loads(response.data.decode('utf-8'))

            self.assertEqual(response.status_code, 200)
            self.assertEqual(data.get("is_blacklisted"), True)
            self.assertEqual(data.get("blocked_reason"), "Test block")

if __name__ == '__main__':
    unittest.main()
