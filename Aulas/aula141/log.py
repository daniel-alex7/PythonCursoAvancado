# Abstração 
# Herança - é um

class Log:
    def log(self, msg):
        raise NotImplementedError('Implemente método log')
    
    def log_error(self, msg):
        return self.log(f'Error: {msg}')
       
class LogFileMixin(Log):
    def log(self, msg):
        print(msg)
        
class LogPrintMixin(Log):
    def log(self, msg):
        print(msg)        
       
if __name__ == '__main__':
    l = LogFileMixin()
    l.log('Alguma coisa')        
