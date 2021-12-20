from time import time
import csv

from exceptions import WrongFileTypeSaveException


class Link:

    def __init__(self, text: str) -> None:

        self.value = text

    def __repr__(self):
        return self.value


class Links:

    def __init__(self) -> None:

        self._list_links = list()
        self._type_file = None,
        self._path = None

    def add(self, value: str):
        """Method for add value to the list of links

        Args:
            value (str): value for add
        """
        self._list_links.append(value)

    def save(self, type_file: str = None, path: str = '.'):
        """Method for save the list of links in file csv/txt

        Args:
            type_file (str, optional): file type for save. Defaults to None.
            path (str, optional): path where save the file. Defaults to '.'.
        """
        self._check_file_type(type_file=type_file)
        self._path = ''.join((path,))
        self._writer()

    def _check_file_type(self, type_file: str):
        """Check file type which the user entered

        Args:
            type_file (str): file type for save

        Raises:
            WrongFileTypeSaveException
        """
        if type_file == 'csv':
            self._type_file = type_file
        elif type_file == 'txt':
            self._type_file = type_file
        else:
            raise WrongFileTypeSaveException(
                'unsupported file type "{}"'.format(type_file)
            )

    def _path_builder(self):
        """Method to build path for save the file

        Returns:
            (str): buildered path
        """
        curent_time = str(time())
        name_file = 'links{time}.{type}'.format(
            time=curent_time.replace('.', ''),
            type=self._type_file
        )
        return self._path + '/' + name_file

    def _writer(self):
        """Writer to write the file .csv/txt
        """
        if self._type_file == 'csv':
            self._csv(self._path_builder())
        else:
            self._txt(self._path_builder())

    def _txt(self, path):
        """Implementation to writer for .txt

        Args:
            path (str): path to the file
        """
        with open(path, 'w', encoding='UTF8') as f:
            for link in self._list_links:
                f.write(link + '\n')

    def _csv(self, path):
        """Implementation to writer for .csv

        Args:
            path (str): path to the file
        """
        with open(path, 'w', newline='', encoding='UTF8') as f:
            writer = csv.writer(f, delimiter=' ')
            for link in self._list_links:
                writer.writerow([link, ])

    def get(self):
        """Method to get values from list of links

        Returns:
            (list): values from list of links
        """
        return self._list_links
