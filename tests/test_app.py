try:
    from app import app
    import unittest

except Exception as e:
    print("Some Modules are Missing {}".format(e))

class FlaskTest(unittest.TestCase):
        # check for response 200
        def test_index(self):
            tester = app.test_client(self)
            response = tester.get("/")
            statuscode = response.status_code
            self.assertEqual(statuscode, 200)

        # check if content return application Json
        def test_index_content(self):
            tester = app.test_client(self)
            response = tester.get("/")
            self.assertEqual(response.content_type, "text/html; charset=utf-8")

        # check for Data returned
        def test_index_data(self):
                tester = app.test_client(self)
                response = tester.get("/")
                self.assertTrue(b'html' in response.data)

        def test_login(self):
            tester = app.test_client(self)
            response = tester.get("/login")
            statuscode = response.status_code
            self.assertEqual(statuscode, 200)

        def test_login_content(self):
            tester = app.test_client(self)
            response = tester.get("/login")
            self.assertEqual(response.content_type, "text/html; charset=utf-8")

            # check for Data returned

        def test_login_data(self):
            tester = app.test_client(self)
            response = tester.get("/")
            self.assertTrue(b'html' in response.data)

        def test_signup(self):
            tester = app.test_client(self)
            response = tester.get("/signup")
            statuscode = response.status_code
            self.assertEqual(statuscode, 200)

        def test_signup_content(self):
            tester = app.test_client(self)
            response = tester.get("/signup")
            self.assertEqual(response.content_type, "text/html; charset=utf-8")

            # check for Data returned

        def test_signup_data(self):
            tester = app.test_client(self)
            response = tester.get("/signup")
            self.assertTrue(b'html' in response.data)

        def test_User(self):
            tester = app.test_client(self)
            response = tester.get("/login")
            statuscode = response.status_code
            self.assertEqual(statuscode, 200)

        def test_user_content(self):
            tester = app.test_client(self)
            response = tester.get("/User")
            self.assertEqual(response.content_type, "text/html; charset=utf-8")

            # check for Data returned

        def test_User_data(self):
            tester = app.test_client(self)
            response = tester.get("/user")
            self.assertTrue(b'' in response.data)

        def test_logout(self):
            tester = app.test_client(self)
            response = tester.get("/login")
            statuscode = response.status_code
            self.assertEqual(statuscode, 200)

        def test_logout_content(self):
            tester = app.test_client(self)
            response = tester.get("/logout")
            self.assertEqual(response.content_type, "text/html; charset=utf-8")

            # check for Data returned

        def test_logout_data(self):
            tester = app.test_client(self)
            response = tester.get("/logout")
            self.assertTrue(b'' in response.data)


if __name__ == "__main__":
    unittest.main()