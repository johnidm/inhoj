import unittest
import pytest

from inhoj.funcs import getn
from inhoj.funcs import getni


class TestGetNestedDict(unittest.TestCase):

	def test_geti_basic_chain(self):

		my_dict = {
			'key1': 99	
		}

		value = getni(my_dict, 'key1')
		assert value == 99

		value = getni(my_dict, 'key99')
		assert value == None

		value = getni(my_dict, 'key99', fallback=99)
		assert value == 99

	def test_getni_get_two_level_chain(self):

		my_dict = {
			'key1': {
				'key2' : True
			}
		}

		value = getni(my_dict, 'key1')
		assert value == my_dict['key1']

		value = getni(my_dict, 'key1.key2')
		assert value == True

		value = getni(my_dict, 'key1.key3', False)
		assert value == False

	def test_getni_biggest_level_chain(self):
		my_dict = {
			'key1': {
				'key2' : {
					'key3': {
						'key4': {
							'key5': 'Hi' 
						}
					}
				}
			}
		}

		value = getni(my_dict, 'key1.key2.key3.key4.key5')
		assert value == 'Hi'

		value = getni(my_dict, 'key1.key2.key3.key4.key5.key6')
		assert value == None

		value = getni(my_dict, 'key99.key2.key3.key4.key5')
		assert value == None

		value = getni(my_dict, 'key1.key2.key3.key4.key5.key6', 'Hello')
		assert value == 'Hello'

	def test_getn_basic_chain(self):

		my_dict = {
			'key1': 99	
		}

		value = getn(my_dict, 'key1')
		assert value == 99

		value = getn(my_dict, 'key99')
		assert value == None

		value = getn(my_dict)
		assert value == my_dict

		value = getn(my_dict, 'key99', fallback=99)
		assert value == 99

	def test_getn_get_two_level_chain(self):

		my_dict = {
			'key1': {
				'key2' : True
			}
		}

		value = getn(my_dict, 'key1')
		assert value == my_dict['key1']

		value = getn(my_dict, 'key1', 'key2')
		assert value == True

		value = getn(my_dict, 'key1', 'key3', fallback=False)
		assert value == False

	def test_getn_biggest_level_chain(self):
		my_dict = {
			'key1': {
				'key2' : {
					'key3': {
						'key4': {
							'key5': 'Hi' 
						}
					}
				}
			}
		}

		value = getn(my_dict, 'key1', 'key2', 'key3', 'key4', 'key5')
		assert value == 'Hi'

		value = getn(my_dict, 'key1', 'key2', 'key3', 'key4', 'key5', 'key6')
		assert value == None

		value = getn(my_dict, 'key99', 'key2', 'key3', 'key4', 'key5')
		assert value == None

		value = getn(my_dict, 'key1', 'key2', 'key3', 'key4', 'key5', 'key6', fallback='Hello')
		assert value == 'Hello'
