import requests

from config import STRATEGY, apis_base_urls, fake_api_responses


class APIHAndler:
    """ API handler class to manage all the api data processing"""
    def __init__(self, member_id, strategy=None):
        self.member_id = member_id
        self.strategy = strategy
        if self.strategy is None:
            self.strategy = STRATEGY
        self.data_values = []
        self.data = {}

    def get_data(self):
        self._get_data_values()
        self._apply_strategy()
        return self.data

    def _get_data_values(self):
        for api_base_url in apis_base_urls:
            # Switch between the two lines below to make real/fake requests (for real request you should update the
            # apis_base_urls if necessary.
            # api_response = self._make_api_call(f'{api_base_url}?member_id={self.member_id}')
            api_response = self._make_fake_api_call(f'{api_base_url}?member_id={self.member_id}')
            self.data_values.append(api_response)

    @staticmethod
    def _make_api_call(path):
        try:
            data = requests.get(path).json()
        except Exception as ex:
            msg = f'Error making a call to "{path}": {ex}'
            print(msg)
            raise ValueError(msg)
        return data

    @staticmethod
    def _make_fake_api_call(path):
        fake_path = f"{path.split('=')[0]}=1"
        return fake_api_responses[fake_path]

    def _apply_strategy(self):
        for key in self.data_values[0].keys():
            if self.strategy == 'avg':
                self.data[key] = int(sum(d[key] for d in self.data_values) / len(self.data_values))
            elif self.strategy == 'max':
                self.data[key] = max(d[key] for d in self.data_values)
            elif self.strategy == 'min':
                self.data[key] = min(d[key] for d in self.data_values)


