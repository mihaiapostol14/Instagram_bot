"""
This code is for setup user private data he automates create .env file with
user data he is (user_agent, account_username, account_password)
"""

import os


class SetupPrivateData:
    def __init__(self, user_agent: str = '', account_username: str = '', account_password: str = ''):
        self.user_agent = user_agent
        self.account_username = account_username
        self.account_password = account_password

        self.config_exists()

    def create_env_file(self, envfile='.env'):
        private_data = f"""USER_AGENT='{self.user_agent}'\nACCOUNT_USERNAME='{self.account_username}'\nACCOUNT_PASSWORD='{self.account_password}'"""  # private data

        # TODO: create the env file

        with open(file=f'config/{envfile}', mode='w') as file:
            file.write(private_data)
            print(f'File {envfile} success created')

    def config_exists(self):
        try:
            if os.path.exists('config'):
                return self.create_env_file()
        except (FileExistsError, FileNotFoundError):
            print('not found packed config')


def main():
    return SetupPrivateData(
        user_agent=input('Enter your user agent: ').strip(),
        account_username=input('Enter your account username: ').strip(),
        account_password=input('Enter your account password: ').strip(),
    )


if __name__ == '__main__':
    main()

