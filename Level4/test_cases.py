import pytest
from Level1.search_file import FileFinder
from Level1.drive_finders import SystemDriveFinder
class Test_Drive:
    def test_DriveCase(self):
        obj=SystemDriveFinder()
        self.expected=obj.find_drives()
        self.actual=['C']
        assert self.expected==self.actual
    def test_searchfile(self):
        obj=FileFinder()
        d=obj.find_file('p1.txt','C:/' )
        self.expected_filename=d[0]
        self.expected_res='C:/hcl\\p1.txt'
        assert self.expected_filename==self.expected_res
