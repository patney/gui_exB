import configparser
import os

class ProductConfigFile():
    def __init__(self, file_name_1='config/config.ini', file_name_2=''):
        # The Configuration File location is the Current working directory.
        self.ini_cfg_file = file_name_1
        self.ini_cfg_file_2 = file_name_2
        self.config = configparser.ConfigParser()
        # MAINTAIN CASE....had issue where some data may be imported in lowercase
        self.config.optionxform = str

    def get_ini_file_sections(self):
        """

        Returns:

        """
        try:
            self.config.read(self.ini_cfg_file)
            return self.config.sections()
        except Exception as err:
            print('CONFIG PARSER', err)

    def get_data_from_ini(self, section):
        """

        :param section:
        :return:
        """
        ini_section = section
        try:
            self.config.read(self.ini_cfg_file)
        except Exception as err:
            return err

        if ini_section in self.config.sections():
            return dict(self.config.items(ini_section))

        msg = '"{}" Part Number Not Found {}'.format(ini_section, self.ini_cfg_file)
        raise ValueError(msg)

    def load_ini_file_to_dict(self):
        """

        Returns:

        """
        self.config.read(self.ini_cfg_file)
        try:
            return {section: dict(self.config.items(section)) for section in self.config.sections()}
        except Exception as err:
            print(err)
            return False


if __name__ == '__main__':
    pass
