import requests
from airflow.hooks.base_hook import BaseHook

class MovielensHook(BaseHook):
    """
    Hook for MovieLens API

    Abstract details of the MoviceLens (REST) API and provides several convenience
    methods for fetching data (e.g. ratings, users, movies) from the API. Also
    provides support for automatic retries of failed requests, transparent handling
    of pagination, authentication, etc.

    Parameters
    conn_id: str
        ID of the connection to use to connect to the MovieLens API. Connection is
        expected to include authentication details (login/ password) and the host
        that is serving the API.
    """

    DEFAULT_SCHEMA="http"
    DEFAULT_PORT=5000

    def __init__(self, conn_id, retry=3):
        super().__init__()
        self._conn_id = conn_id
        self._retry = retry

        self._session = None
        self._base_url = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def get_conn(self) :
        """
        Returns the connection used by the hook for querying the data
        Should in principle not be used directly.
        :return:
        """

        if self._session is None:
            # Fetching config for the given connection (host, login, etc).
            config = self.get_connection(self._conn_id)

            if not config.host:
                raise ValueError(f"No host specified in connection {self._conn_id}")

            schema = config.schema or self.DEFAULT_SCHEMA
            port = config.port or self.DEFAULT_PORT

            self._base_url = f"{schema}://{config.host}:{port}"

            # Build our session instance, which we will use for any request to the
            # API
            self._session = requests.Session()

            if config.login:
                self._session.auth = (config.login, config.password)

        return self._session, self._base_url

    def close(self):
        """
        Closes any active session.
        :return:
        """

        if self._session:
            self._session.close()
        self._session=None
        self._base_url=None

        # API methods

        def get_movices(self):
            """
            Fetches a list of movies.
            :param self:
            :return:
            """

            raise NotImplementedError()

        def get_users(self):
            """
            Fetches a list of users.
            :param self:
            :return:
            """

            raise NotImplementedError()

        def get_ratings(self, start_date=None, end_date=None, batch_size=100):
            """
            Fetches rating between the given start/ end dates.
            :param self:
            :param start_date: str
                Start date to start fetching ratings from (inclusive). Expected
                format is YYYY-MM-DD (equal to Airflow's ds formats).
            :param end_date: str
                End date to fetching ratings up to (exclusive). Expected format
                is YYYY-MM-DD (equal to Airflow's ds formats).
            :param batch_size: int
                Size of the batches (pages) to fetch from the API. Larger values
                mean less requests, but more data transfered per request.
            :return:
            """

            yield from self._get_with_pagination(
                endpoint="/ratings",
                params={"start_date": start_date, "end_date": end_date},
                batch_size=batch_size,
            )

        def _get_with_pagination(self, endpoint, params, batch_size=100):
            """

            :param self:
            :param endpoint:
            :param params:
            :param batch_size:
            :return:
            """

            session, base_url = self.get_conn()
            url = base_url +endpoint

            offset = 0
            total = None
            while total is None or offset < total:
                response = session.get(
                    url, params={**params, **{"offset": offset, "limit": batch_size}}
                )
                response.raise_for_status()
                response_json = response.json()

                yield from response_json["result"]

                offset += batch_size
                total = response_json["total"]