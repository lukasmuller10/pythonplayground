import matplotlib.pyplot as plt
import pandas as pd
class functions:
    def processDate(self, date):
        if date[0] == '8': #o dia 31 de agosto que será utilizado para o calculo da taxa de retorno mensal como cota 
            return 0       #inicial foi subsituido para o valor zero
        else:
            return int((date.split('/'))[1]) #as outras datas do mes de setembro serão substituidas pelo numero 
                                        #correspondente ao dia do mes.
    
    def processName(self, name):
        return int((name.split(' '))[1]) #o nome do fundo é sempre do formato 'Fundo x', logo o nome foi subtituido
                                    #pelo numero do fundo
        
    def plotChart(self,df, i):#função responsável por plotar os gráficos
        df.plot(x='date', y='daily_return', figsize=(10,5))
        
        axes = plt.gca()
        axes.set_xlabel('Days')
        axes.set_ylabel('Return (%)')
        
        plt.suptitle('Fundo '+str(i), y=0.93)    
