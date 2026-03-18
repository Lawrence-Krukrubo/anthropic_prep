from collections import defaultdict

class FileSystem:
    def __init__(self):
        self.files = defaultdict(str)

    def create_file(self, name:str)->bool:
        if name in self.files:
            return False
        self.files[name]
        return True
    
    def write_to_file(self, name: str, content: str) -> None:
        if not name in self.files:
            raise ValueError(f'Warning! No file with name: {name}')
        else:
            self.files[name] = content

    def read_file(self, name: str) -> str:
        if not name in self.files:
            raise ValueError(f'Warning! No file with name: {name}')
        else:
            return self.files[name]
        
    def delete_file(self, name: str) -> bool:
        if not name in self.files:
            return False
        del self.files[name]
        return True


