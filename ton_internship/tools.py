import csv, sqlite3, unicodedata, unidecode, datetime 
import numpy as np

class utils:
    #classe utilizada para deixar o codigo mais limpo, em que armazena as ferramentas necessarias para analise
    
    def strip_accents(self, text): #função utilizada para substituir caracteres especiais ao ler o arquivo .csv

        try:
            text = unicode(text, 'utf-8')
        except NameError: # unicode is a default on python 3 
            pass

        text = unicodedata.normalize('NFD', text)\
               .encode('ascii', 'ignore')\
               .decode("utf-8")

        return str(text)
    
    def processing(self,row, key): #função que lida com a transformação dos tipos de variavel e que usa a função definida acima
    
        processed_row = ()

        if key == 'cases': #depende de qual arquivo será lido
            row['channelid'] = int(row['channelid'])
            row['waitingtime'] = int(row['waitingtime'])
            row['pesquisa_de_satisfa_o__c'] = strip_accents(row['pesquisa_de_satisfa_o__c'])
            row['assunto'] = strip_accents(row['assunto'])

            processed_row = (row['accountid'], row['date_ref'], row['channelid'], row['waitingtime'],
                                 row['missed'], row['pesquisa_de_satisfa_o__c'], row['assunto'], row['Id'])

        elif key == 'creds':
            row['shipping_address_city'] = strip_accents(row['shipping_address_city'])

            processed_row = (row['cred_date'], row['shipping_address_city'], row['shipping_address_state'],
                                row['max_machine'], row['accountid'])

        return processed_row

    def transform_date(self,date): #função que transforma uma string que representa uma data em um objeto datetime do python
        date = date.split('-')
        return datetime.datetime(int(date[0]),int(date[1]),int(date[2]))
    
    def transform_array(self,array):
        vfunc = np.vectorize(self.transform_date) #função que aplica a função transform_date para um np array como um todo
        transformed_arr = vfunc(array)
        
        return transformed_arr
    
    def gap(self, array):
        gap_column = [] #calcula o numero de dias entre o dia de credenciamento do cliente e seu chamado
        for row in array:
            cred = row[0]
            chamad = row[1]

            gap = (chamad - cred).days
            gap_column.append(gap)

        return gap_column
    
    def interval(self, array, key): #função que verifica se o numero de dias entre o dia de credenciamento do 
                                    #cliente e seu chamado está dentro de intervalos bem definidos 
        int_array = [0, 0, 0, 0]
        fi_i = 0
        s_i = 0
        t_i = 0
        fo_i = 0
        
        if key == 'long': #depende do tipo de analise
            fi_i = range(0, 7)
            s_i = range(7,14)
            t_i = range(14,30)
            fo_i = range(30,60)
            
        if key == 'short':
            fi_i = range(0, 2)
            s_i = range(2,4)
            t_i = range(4,7)
            fo_i = range(7,14)

        for gap in array:
            if gap in fi_i:
                int_array[0] += 1 
            elif gap in s_i:
                int_array[1] += 1
            elif gap in t_i:
                int_array[2] += 1    
            elif gap in fo_i:
                int_array[3] += 1 

        return int_array   
        
    def client_calls(self, array, key): #função que utiliza as funções acima como se fosse um método só
           #recebe um array de duas colunas (data de cred e data de chamado), faz as transformação para o objeto datetime em 
            #todo o array, calcula o numero de dias entre essas datas e retorna um array em que cada posição representa um
            #intervalo de dias
            #exemplo: array retornado [1,3,7,0], foi mapeado 1 empresa que fez um chamado em 'x' dias após ser credenciada
            # 3 empresas que fizeram um chamado em 'y' dias após serem credenciadas e etc
        vfunc = np.vectorize(self.transform_date)
        join_query = vfunc(array)

        gap_array = self.gap(join_query)

        interval_array = self.interval(gap_array, key)

        return interval_array