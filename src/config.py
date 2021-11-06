STRATEGY = 'avg'
STRATEGIES = ['avg', 'min', 'max']

apis_base_urls = [
    'https://api1.com',
    'https://api2.com',
    'https://api3.com'
]

fake_api_responses = {
    'https://api1.com?member_id=1': {'deductible': 1000, 'stop_loss': 10000, 'oop_max': 5000},
    'https://api2.com?member_id=1': {'deductible': 1200, 'stop_loss': 13000, 'oop_max': 6000},
    'https://api3.com?member_id=1': {'deductible': 1000, 'stop_loss': 10000, 'oop_max': 6000}
}