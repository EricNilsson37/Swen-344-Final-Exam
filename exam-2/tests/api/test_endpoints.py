import unittest
import requests
from tests.test_utils import *
import json

class TestCase1(unittest.TestCase):

    def test_a_edit_bleat(self):

        insert_test_data()

        payload = {'ID':13,'USER_ID':5,'BLEAT_CONTENT':"game bro is a joke and we both know it."}

        put_rest_call(self, 'http://localhost:5000/edit/bleat', payload)

        http = 'http://localhost:5000/info/'+ str(13)

        value = get_rest_call(self, http)

        print("Question 1: " + str(value))

        assert("game bro is a joke and we both know it." == value)

    def test_b_get_info(self):

        user = get_rest_call(self, 'http://localhost:5000/users/SansUndertale')

        print("Question 2: { Username: " + str(user[0][1])+ ", Favorite Thing: " + str(user[0][3])+ ", Email: " + user[0][2])

    
    def test_c_edit_bleat(self):

        http = 'http://localhost:5000/info/'+ str(3)

        values = get_rest_call(self, http)

        bleat_text = values + " ok, i will send someone over to fix it." 

        payload = {'ID':3,'USER_ID':2,'BLEAT_CONTENT':bleat_text}

        put_rest_call(self, 'http://localhost:5000/edit/bleat', payload)

        value = get_rest_call(self, http)

        assert(bleat_text == value)

        print("Question 3:" + value)
    
    def test_d_print_all_Jegbert(self):

        value = get_rest_call(self, 'http://localhost:5000/users/Jegbert/bleats')

        text = ""
        ints = 0

        for x in value :
            text += str(value[ints][2]) + ","
            ints += 1

        print("Question 4: " + text)

    def test_e_print_all_SansUndertale(self):

        value = get_rest_call(self, 'http://localhost:5000/users/SansUndertale/bleats')

        text = ""
        ints = 0

        for x in value :
            text += str(value[ints][2]) + ","
            ints += 1

        print("Question 5: " + text)

    def test_f_delete_bealts(self):

        delete_rest_call(self,'http://localhost:5000/delete/bleat?ID=8')
        delete_rest_call(self,'http://localhost:5000/delete/bleat?ID=9')

        print("Question 6: Deleting bleat id 9 and 8")
    

    def test_g_check_delete(self):

        value = get_rest_call(self, 'http://localhost:5000/users/Boba/bleats')
        value2 = get_rest_call(self, 'http://localhost:5000/users/Jeffie/bleats')


        text = ""
        ints = 0

        for x in value :
            text += str(value[ints][2]) + ","
            ints += 1

        ints = 0
        for x in value2 :
            text += str(value[ints][2]) + ","
            ints += 1


        print("Question 7: " + text)

    def test_h_add_bleat(self):

        bleat_text = 'No burg is complete without cheese'

        payload = {'ID':16,'USER_ID':1,'BLEAT_CONTENT':bleat_text}

        post_rest_call(self, 'http://localhost:5000/compose/bleat', payload)

        print('Question 8: Adding SarahZ bleat')

    def test_i_check_add(self):

        value = get_rest_call(self, 'http://localhost:5000/users/SarahZ/bleats')

        text = ""
        ints = 0

        for x in value :
            text += str(value[ints][2]) + ","
            ints += 1

        print("Question 9: " + text)

        
        
