from datetime import datetime
from typing import Optional
from urllib.parse import urlencode

import requests

from streamtape.ApiResponse import ApiResponse


class BaseConfig:
	url: str = 'https://api.streamtape.com'
	api_user: Optional[str] = None
	api_password: Optional[str] = None

	def __init__(self, user: str, password: str):
		"""
		Initializes an instance of the class with the provided user and password.

		Args:
		    - user (str): The username for the API authentication.
		    - password (str): The password for the API authentication.

		Returns:
		    - None
		"""
		self.api_user = user
		self.api_password = password

	def set_api_url(self, url: str):
		"""
		Sets the API URL for the object.

		Parameters:
		- self: The object itself.
		- url (str): The URL to be set as the API URL.

		Returns:
		- None

		Example:
		>>> obj = MyClass()
		>>> obj.set_api_url("https://api.example.com")
		"""
		self.url = url

	def url_query(self, parameter: str, query: dict = {}, use_login: bool = True) -> str:
		"""
		Constructs a URL query string for making API requests.

		Args:
		    - self (object): The instance of the class.
		    - parameter (str): The parameter to be appended to the base URL.
		    - query (dict, optional): Additional query parameters to be included in the URL. Defaults to an empty dictionary.
		    - use_login (bool, optional): Flag indicating whether to include login credentials in the query parameters. Defaults to True.

		Returns:
		    - str: The constructed URL query string.

		Example:
		    >>> obj = ClassName()
		    >>> obj.url_query("endpoint", {"param1": "value1", "param2": "value2"}, False)
		    'https://example.com/endpoint?param1=value1&param2=value2'
		"""
		api_url = f"{self.url}/{parameter}"
		api_query = {"login": self.api_user, "key": self.api_password} if use_login else {}
		api_query = {**api_query, **query}

		return f"{api_url}?{urlencode(api_query)}"

	@staticmethod
	def send_request(url: str, type_request: str = 'GET', data: Optional[dict] = None, parameters: Optional[dict] = None, files: Optional[dict] = None) -> ApiResponse:
		"""
		Sends a HTTP request to the specified URL using the specified request type.

		Args:
			- url (str): The URL to send the request to.
			- type_request (str, optional): The type of request to send. Defaults to 'GET'.
			- data (dict, optional): The data to send with the request. Defaults to None.
			- parameters (dict, optional): The parameters to include in the request. Defaults to None.
			- files (dict, optional): The files to include in the request. Defaults to None.

		Returns:
			- ApiResponse: The response from the server.

		Raises:
			None

		Examples:
			>>> response = send_request('https://api.example.com/users', type_request='GET')
			{
				"status": <status-code>,
				"msg": "<informational message. might vary, use the status code in your code!>",
				"result": <result of the request. varies depending on the request>
			}
		"""
		s = requests.Session()
		response: Optional[ApiResponse] = None
		if type_request.upper() == 'GET':
			response = s.get(url, data=data, params=parameters, files=files).json()
		elif type_request.upper() == 'POST':
			response = s.post(url, data=data, params=parameters, files=files).json()

		return response

	@staticmethod
	def str_to_datetime(date_string: str, format_string: str = '%y-%m-%d %H:%M:%S'):
		"""
		Converts a string representation of a date and time to a datetime object.

		Args:
			- date_string (str): The string representation of the date and time.
			- format_string (str, optional): The format string specifying the expected format of the date and time string.
				Defaults to '%y-%m-%d %H:%M:%S'.

		Returns:
			- datetime: A datetime object representing the parsed date and time.

		Raises:
			- ValueError: If the date_string does not match the format_string.

		Examples:
			>>> str_to_datetime('2022-01-01 12:00:00')
			datetime.datetime(2022, 1, 1, 12, 0)

			>>> str_to_datetime('01-01-2022 12:00:00', '%d-%m-%Y %H:%M:%S')
			datetime.datetime(2022, 1, 1, 12, 0)

		Note:
			- The format_string follows the same conventions as the strftime() method of datetime objects.
			- If the date_string does not match the format_string, a ValueError is raised.
		"""
		return datetime.strptime(date_string, format_string)
