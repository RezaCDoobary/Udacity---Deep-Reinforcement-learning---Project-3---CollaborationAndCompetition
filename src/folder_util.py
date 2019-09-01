import os

class util:
    @staticmethod
    def date_and_time(with_time = False):
        """
        Returns a YYYYMMDD string with out without time
        
        Params
        ======
            with_time (boolean) : Gives time in string is True, does not otherwise.
        """
        import datetime
        
        YEAR = str(datetime.datetime.today().year)
        
        MONTH = str(0) + str(datetime.datetime.today().month) if datetime.datetime.today().month < 10 \
        else str(datetime.datetime.today().month)
        
        DAY = str(0) + str(datetime.datetime.today().day) if datetime.datetime.today().day < 10 \
        else str(datetime.datetime.today().day)
        
        HOUR = str(0) + str(datetime.datetime.today().hour) if datetime.datetime.today().hour < 10\
        else str(datetime.datetime.today().hour)
        
        MINUTE = str(0) + str(datetime.datetime.today().minute) if datetime.datetime.today().minute < 10\
        else str(datetime.datetime.today().minute)
        
        if with_time:
            return YEAR+MONTH+DAY+'_'+HOUR+MINUTE
        else:
            return YEAR+MONTH+DAY

    @staticmethod
    def if_folder_not_there_create(folder_destination):
        """Creates a folder if it does not exist
        
        Params
        ======
            folder_destination (string) : The path to be created if it does not already exist.
        """
        if not os.path.exists(folder_destination):
            os.makedirs(folder_destination)
    
    @staticmethod
    def folder_number(path):
        """Creates a folder of the form run_# in case we have multiple runs per day
        
        Params
        ======
            path (string) : The path to be created if it does not already exist.
        """

        folders = []

        # r=root, d=directories, f = files
        for r, d, f in os.walk(path):
            for folder in d:
                folders.append(os.path.join(r, folder))

        numbers = []
        for f in folders:
            ff = f.split('_')
            numbers.append(ff[-1])

        if len(numbers) == 0:
            new_folder = "run"+"_1"
        else:
            m = int(numbers[-1])
            new_folder = "run"+"_"+str(m+1)

        util.if_folder_not_there_create(path + "//" +new_folder)  
        return new_folder
        

        
