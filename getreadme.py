import subprocess
import os
def get_readme():
        """
        Get the README from the path

        Parameters
        -----------
        path - str
            The location of the file or folder

        Returns
        -----------
        str - the contents of a file, bool - whether the README exists
        """
	path = 'README.md'
        if not os.path.isfile(path):
            print('Failure finding file!')

        output = subprocess.Popen(["cat", path], stdout=subprocess.PIPE).stdout.read().decode('utf-8')
        
        return output 
