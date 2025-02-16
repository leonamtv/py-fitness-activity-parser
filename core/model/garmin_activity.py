from os import path
from pathlib import Path
from core.model.basic_activity import BasicActivity
from core.model.tcx.tcx_activity import TCXActivity
from config import gpx_file_extension, tcx_file_extension

class GarminActivity:

    def __init__(self, file_path: str):
        if file_path is None:
            raise 'File path cannot be None'
        if not path.exists(file_path):
            raise FileNotFoundError()
        self.file_path = file_path
        
    def parse(self):
        file_path = Path(self.file_path)
        if file_path.suffix == tcx_file_extension :
            return self.__parse_tcx_file(self.file_path)
        elif file_path.suffix == gpx_file_extension :
            return self.__parse_gpx_file(self.file_path)
        else :
            print(f"File format {file_path.suffix} not supported.")

    def __parse_tcx_file(self, file_path: str) -> BasicActivity:
        return TCXActivity(file_path)

    def __parse_gpx_file(self, file_path: str) -> None:
        print("GPX format hasn't been implemented yet.")
        pass