import unittest
from model.Model import Model
from model.db.Db import Db


class TestModel(unittest.TestCase):
    def setUp(self):
        self.db = Db()
        self.model = Model(self.db)

    def test_reading_file(self):
        file_path = 'utils/text.txt'
        center_name_1 = 'sever'
        center_name_2 =  'south'

        self.model.add(center_name_1, file_path)
        res_1 = self.model.show_all()
        res_assert_1 = """Some text some text texxt Some text some text;
texxtS ome text some text texxtSome text some, text! texxt
iuqyweiyeqw7y237y13yo12y3jkwbdkadbkhawbdhkawbdk"""

        self.assertEqual(res_assert_1, res_1['12:11'])

        self.model.add(center_name_2, file_path)
        res_2 = self.model.show_all()
        res_assert_2 = """Some text some text texxt 11:22 Some. text" some text"
texxtS ome text some text texxtSome text some text texxs
poiuywejmb 123797977977&&&988123"""

        self.assertEqual(res_assert_2, res_2['11:10'])


        """
        center_name_1:{
            '04:10': {
                   asdasdasdadadasdasdadasdasd
                   asdasdasdasdasdasdasdasdasdasd
                   asdasdasd 
                },
            
        },
        center_name_2... 
        
        """