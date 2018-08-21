# -*- coding: utf8 -*-
'''
Created on 13 april 2013

@author: vl
'''

class Analyser(object):
    '''
    classdocs
    '''
    
    def __init__(self, filepath):
        '''
        Constructor
        '''
        self.__filepath = filepath
        self.__data = []
    
    def load_file(self):
        '''
        Load data from log file
        '''
        log_file = open(self.__filepath,'r')
        data = log_file.readlines()
        log_file.close()
        for line in data:
            self.append_record(line.split())
        return self
    
    def append_record(self, record):
        '''
        Append record
        '''
        self.__data.append(record)
        return self
    
    def get_data(self):
        '''
        Get data
        '''
        return self.__data
    
    def countries(self):
        '''
        Touple of countries
        '''
        #print(self.__data)

        countr = []
        countries = (countr)
        for elem in self.__data:
            if elem[2] not in countr:
                countr.append(elem[2])
        # TODO: стоврити кортеж країн інформація про які зберігається в лог файлі
        # Список рядків лог файлу доступний в self.__data
                
        return countries
        
    def resources(self):
        '''
        List of resources
        '''
        resources = []
        for res in self.__data:
            item = res[1]
            strt_pos = item.find('/', 7,)
            if item[strt_pos:] not in resources:
                if strt_pos != -1:
                    resources.append(item[strt_pos:])
                else:
                    if "/" not in resources:
                        resources.append("/")
        # TODO: створити кортеж ресурсів сайту. Кожен ресурс предстивити відносно верхнього каталогу
        # Наприклад для запису 'http://google.com/' результат має бути '/'
        # а для запису 'http://google.com/index/?g=1' результат буде '/index/?g=1'
        return resources
