from mammal import Mammal

class Wolf(Mammal):

    def __init__(self, pack):
        Mammal.__init__(self)
        assert isinstance(pack, str), "Pack name has to be name and not numbers"
        assert len(pack) > 0, "Pack name must be atleast 1 letter long"
        self.__pack_name = pack

    def another_make_sound(self):
        print("*wolf howling*")

    #Getter for pack_name
    def get_pack_name(self):
        return self.__pack_name
    
    def set_pack_name(self, pack):
        self.__pack_name = pack
        