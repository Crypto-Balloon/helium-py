"""Base client for Helium Blockchain API."""
import logging
import math
from typing import Generator, Optional, Union
from urllib.parse import urlunsplit

import requests
from urllib3.util.retry import Retry

from ..version import VERSION
from .constants import (
    HELIUM_API_BETA_HOST,
    HELIUM_API_DEFAULT_HOST,
    HELIUM_API_DEFAULT_VERSION,
    HELIUM_API_OFFICIAL_HOSTS,
    HELIUM_API_TESTNET_HOST,
)

logger = logging.getLogger(__name__)


class Client:
    """Base client class for Helium Blockchain API.

    Sub-classes define specific paths or parameters for different aspects of the
    API.
    """

    base_path = ''
    host = HELIUM_API_DEFAULT_HOST
    port = 443
    user_agent = ''
    _page_cache: dict = {}

    def __init__(
        self,
        host: str = None,
        port: int = None,
        user_agent: str = None,
        base_path: str = None,
    ) -> None:
        """Initialize the API client.

        Args:
            host (str): Hostname for Helium blockchain API.
            port (int): Port for Helium blockchain API.
            user_agent (str): Custom user agent.
        """
        if host is not None:
            self.host = host
        if port is not None:
            self.port = port
        if user_agent is not None:
            self.user_agent = user_agent
        if base_path is not None:
            self.base_path = base_path

        self.netloc = f'{self.host}:{self.port}'

        self.session = requests.Session()
        retry_adapter = requests.adapters.HTTPAdapter(
            max_retries=Retry(
                total=10,
                status_forcelist=[429, 503],
                backoff_factor=1.5,
            ),
        )
        base_url = urlunsplit(('https', self.netloc, '', '', ''))
        self.session.mount(base_url, retry_adapter)
        self.session.headers.update({'User-Agent': self.build_user_agent()})

    def build_user_agent(self):
        """Return the User-Agent."""
        agent = f'helium-py/{VERSION}'
        return f'{agent} {self.user_agent}' if self.user_agent else agent

    @property
    def _base_path(self) -> str:
        base_path = ''
        if self.host in HELIUM_API_OFFICIAL_HOSTS:
            base_path += f'{HELIUM_API_DEFAULT_VERSION}/'
        if self.base_path:
            base_path += f'{self.base_path}'

        return base_path

    def __get(self, path: str = None, params: dict = None) -> dict:
        """Get the response for a request.

        Args:
            path: URL path for query.
            params: Query parameters.
        Returns:
            The payload from the request.
        Raises:
            requests.exceptions.HTTPError: If the response code is not a successful one.
        """
        if path is None:
            path = ''
        if params is None:
            params = {}
        url = urlunsplit(('https', self.netloc, f'{self._base_path}{path}/', '', ''))
        r = self.session.get(url, params=params)
        r.raise_for_status()
        return r.json()

    def get(self, path: str = None, params: dict = None):
        """Get the response for a request.

        Args:
            path: URL path for query.
            params: Query parameters.
        Returns:
            The payload from the request, unpacked if possible
        Raises:
            requests.exceptions.HTTPError: If the response code is not a successful one.
        """
        result = self.__get(path=path, params=params)
        return result['data'] if isinstance(result, dict) and 'data' in result else result

    def fetch_all(
        self,
        path: str = '',
        params: Optional[dict] = None,
        page_limit: Union[float, int] = math.inf,
    ) -> Generator[dict, None, None]:
        """Yield objects returned by API.

        Args:
            path: Path for initial query.
            params: Query params
            page_limit: The max number of pages to return. float is permitted since math.inf
                is the provided representation of inifinity in the language, and the default is
                that there is no limit.
        """
        params = params or {}
        page_limit = int(page_limit) if type(page_limit) is float and page_limit is not math.inf else page_limit
        page_count = 0
        page: dict = {}
        prev_page_cursor = None

        while page_count < page_limit:
            page = self.get_next_page(page, path, params)
            data = page['data']
            if type(data) is list:
                for obj in data:
                    yield obj
            else:
                yield data
            if prev_page_cursor:
                self._page_cache[prev_page_cursor] = page  # Unknown: Can we cache the first 'None' call?
                logger.debug(f'caching page: {prev_page_cursor}')
            prev_page_cursor = page.get('cursor', None)
            page_count += 1
            if 'cursor' not in page:
                page_limit = -1  # break
            else:
                params['cursor'] = page['cursor']

    def get_next_page(self, current_page: dict, path: str, params: dict) -> dict:
        """Return the next page from cache or from the API.

        Args:
            current_page: Current page or empty dict.
            path: Path for initial query.
            params: Query params
        """
        if 'cursor' in current_page and current_page['cursor'] in self._page_cache:
            page = self._page_cache[params['cursor']]
            logger.debug(f'loaded page from cache: {params["cursor"]}')
        else:
            page = self.__get(path, params)
        return page

    def post(self, path: str, json: Optional[dict]) -> dict:
        """Get the response for a POST request.

        Args:
            path: URL path for query.
            json: JSON payload as dict.
        Returns:
            The payload from the request.
        Raises:
            requests.exceptions.HTTPError: If the response code is not a successful one.
        """
        if json is None:
            json = {}
        url = urlunsplit(('https', self.netloc, f'{self._base_path}{path}/', '', ''))
        r = self.session.post(url, json=json)
        r.raise_for_status()
        return r.json()


__all__ = [
    'HELIUM_API_DEFAULT_HOST',
    'HELIUM_API_BETA_HOST',
    'HELIUM_API_TESTNET_HOST',
    'HELIUM_API_OFFICIAL_HOSTS',
    'HELIUM_API_DEFAULT_VERSION',
    'Client',
]
