from libs.tokens.gen_token_header import gen_token_header
from libs.tokens.gen_token_acceso import gen_token_acceso

class tokens():

    def gen_token_header(self):
        return gen_token_header()
        
    def gen_token_acceso(self):
        return gen_token_acceso()

        

tokens_api = tokens()
