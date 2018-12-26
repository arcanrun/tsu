import unittest
from model.Model import Model
from model.db.Db import Db


class TestModel(unittest.TestCase):
    def setUp(self):
        self.db = Db()
        self.model = Model(self.db)

    def test_reading_files_and_appending_new_data_by_the_same_key(self):
        file_path = 'utils/sever.txt'
        center_name_1 = 'sever'

        self.model.add(center_name_1, file_path)
        res_1 = self.model.show_all()
        res_assert_1 = """sever severseverseversever severseverseversever severseversever"""

        self.assertEqual(res_assert_1, res_1[center_name_1]['05:10'])

        # ==============================
        file_path_2 = 'utils/south.txt'
        center_name_2 = 'south'

        self.model.add(center_name_2, file_path_2)
        res_2 = self.model.show_all()
        res_assert_2 = """south"""

        self.assertEqual(res_assert_2, res_2[center_name_2]['22:10'])

        # ==================================
        file_path_2 = 'utils/sever1.txt'

        self.model.add(center_name_1, file_path_2)
        res_3 = self.model.show_all()
        res_assert_3 = """sever-1 sever-1 sever-1 sever-1 sever-1 sever-1 sever-1 sever-1"""

        self.assertEqual(res_assert_3, res_3[center_name_1]['02:10'])


    def test_get_data_by_center_name(self):
        query_1 = 'south'

        assert_res_1 = {
                        "21:10" : "south south",
   	                    "22:10" : "south"
                        }

        res_1 = self.model.show_by_center(query_1)

        self.assertEqual(assert_res_1, res_1)

        # ====================================

        query_2 = 'sever'

        assert_res_2 = {
            "05:10" : """sever severseverseversever severseverseversever severseversever""",
   	"11:10" : """sever severseverseversever severseverseversever""",
   	"01:10" : """sever-1 sever-1 sever-1 sever-1""",
   	"02:10" : """sever-1 sever-1 sever-1 sever-1 sever-1 sever-1 sever-1 sever-1"""
        }

        res_2 = self.model.show_by_center(query_2)

        self.assertEqual(assert_res_2, res_2)

    def test_get_all_centers_names_and_lens(self):

        res = self.model.list_centers()

        self.assertEqual({'length': 2, 'keys': ['south','sever']}, res)

    def test_get_messages_by_center_and_time_interval(self):
        # center_name_1 = 'sever'
        # time = '04:54-12:00'
        #
        # res_1 = self.model.show_message_by_time(center_name_1, time)
        # assert_res_1 = {'05:10': 'sever severseverseversever severseverseversever severseversever', '11:10': 'sever severseverseversever severseverseversever'}
        # self.assertEqual(assert_res_1, res_1)

        # ==========
        center_name_2 = 'south'
        time = '21:30-23:59'

        res_2 = self.model.show_message_by_time(center_name_2, time)
        assert_res_2 = {"22:10":"south"}
        self.assertEqual(assert_res_2, res_2)

    def test_show_messages_by_phrase(self):
        center_name_1 = 'sever'
        phrase_1 = 'sever-1 sever-1 sever-1 sever-1 sever-1 sever-1 sever-1 sever-1'

        res_1 = self.model.show_by_phrase(center_name_1, phrase_1)
        assert_res_1 = {"02:10":"sever-1 sever-1 sever-1 sever-1 sever-1 sever-1 sever-1 sever-1"}


        self.assertEqual(assert_res_1, res_1)

    def test_for_pirnting_hello_world(self):
        assert_res = 'hello'

        res = self.model.hello()

        self.assertEqual(assert_res, res)
