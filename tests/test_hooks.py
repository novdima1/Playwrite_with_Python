import pytest


@pytest.mark.usefixtures('new_class')
@pytest.mark.usefixtures('hi_bye')
class Test1:

    def test1_first(self):
        print("\nFirst test passed")
        assert True

    def test1_second(self):
        print("\nSecond test passed")
        assert True


@pytest.mark.usefixtures('new_class')
class Test2:
    def test2_first(self):
        print("\nFirst test passed")
        assert True

    def test2_second(self):
        print("\nSecond test passed")
        assert True
