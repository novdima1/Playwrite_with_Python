import pytest
import allure


@pytest.mark.usefixtures('new_class')
@pytest.mark.usefixtures('hi_bye')
class Test1:
    @allure.title("First Test")
    @allure.id("001")
    @allure.description('Test test')
    @allure.severity(allure.severity_level.TRIVIAL)
    def test1_first(self):
        print("\nFirst test passed")
        assert True

    @allure.severity(allure.severity_level.TRIVIAL)
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
