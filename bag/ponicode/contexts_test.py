from bag import contexts

class Test_Contexts_Bag_contents:
    def test_bag_contents_1(self):
        result = contexts.bag_contents("GET")

    def test_bag_contents_2(self):
        result = contexts.bag_contents("DELETE")

    def test_bag_contents_3(self):
        result = contexts.bag_contents("PUT")

    def test_bag_contents_4(self):
        result = contexts.bag_contents("")

