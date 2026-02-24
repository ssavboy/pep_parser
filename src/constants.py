from pathlib import Path

BASE_DIR = Path(__file__).parent
MAIN_DOC_URL = 'https://docs.python.org/3/'
PEP_URL = 'https://peps.python.org/'
DT_FORMAT = '%d.%m.%Y %H:%M:%S'
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
LOG_FORMAT = '"%(asctime)s - [%(levelname)s] - %(message)s"'
ENCODING_UTF8 = 'utf-8'
RESULTS = 'results'
DOWNLOADS = 'downloads'
PRETTY_FORMAT = 'pretty'
FILE_FORMAT = 'file'
LOGS = 'logs'
PARSER_FILE = 'parser.log'
DEFAULT_FORMAT = None
EXPECTED_STATUS = {
    'A': ('Active', 'Accepted'),
    'D': ('Deferred',),
    'F': ('Final',),
    'P': ('Provisional',),
    'R': ('Rejected',),
    'S': ('Superseded',),
    'W': ('Withdrawn',),
    '': ('Draft', 'Active'),
}
