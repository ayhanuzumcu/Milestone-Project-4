from profiles import views

class Test_Views_Profile:
    def test_profile_1(self):
        result = views.profile("DELETE")

    def test_profile_2(self):
        result = views.profile("POST")

    def test_profile_3(self):
        result = views.profile("PUT")

    def test_profile_4(self):
        result = views.profile("")

