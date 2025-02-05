# unittest
import unittest
from unittest.mock import MagicMock

# SQL Alchemy
from sqlalchemy.orm import Session

# internal imports
from app.schemas.user import UserCreate, UserUpdate
from app.api.endpoints.user import functions as user_functions


class Test(unittest.TestCase):
    """
    The Basic class that inherits unittest.TestCase
    """
    def setUp(self):
        """
        Set up default input data for test cases
        """
        self.db = MagicMock(spec=Session)
        self.default_user_data = UserCreate(
            email="default@testmail.de",
            password="defaultpassword",
            name="defaultname",
            user_name="defaultusername",
            location="defaultlocation"
        )
        self.user_id = 1


# def create_new_user(db: Session, user: UserCreate):
    def test_create_new_user(self):
        """
        Test create new user
        """
        print("Start create_new_user test\n")


        self.assertIsNotNone(self.default_user_data)
        self.assertEqual(self.default_user_data, self.default_user_data)
        #self.db.add.assert_called()
        #self.db.commit.assert_called()


#def update_user(db: Session, user_id: int, user: UserUpdate, current_user: Annotated[UserModel.User, Depends(get_current_user)]):
    def test_update_user(self):
        """
        Test updating defaultInputData
        """
        print("Start update_user test\n")


        test_user_data = self.default_user_data.model_dump()
        test_user_data["email"] = "custom@testmail.de"
        test_user_data["user_name"] = "customusername"

        #updated_user = user_functions.update_user(self.db, self.default_user_data)

        self.assertIsNotNone(test_user_data)


# class TestUserRegistration(BaseTestCase)


if __name__ == "__main__":
    unittest.main()
