from typing import Any, Dict, Optional

from streamtape.ApiResponse import ApiResponse
from streamtape.BaseConfig import BaseConfig


class Account(BaseConfig):
	parameter: str = "parameter"

	def __init__(self, user: str, password: str):
		super().__init__(user, password)

	def get_info(self) -> dict:
		"""
		Retrieves information about the user from the API.

		Returns:
		    A dictionary containing the user's information if the API response status is 200.
		    The dictionary includes the following keys:
		        - 'apiid': The user's API ID.
		        - 'email': The user's email address.
		        - 'signup_at': The user's signup date and time in datetime format.

		    If the API response status is not 200, an error response dictionary is returned.
		    The error response dictionary includes the following keys:
		        - 'status': The API response status code.
		        - 'msg': The error message returned by the API.
		"""
		url = self.url_query(f"{self.parameter}/info")
		response = BaseConfig.send_request(url)
		if response["status"] == 200:
			return {
				"apiid"    : response.result.get('apiid'),
				"email"    : response.result.get('email'),
				"signup_at": BaseConfig.str_to_datetime(response.result.get('signup_at'))
			}
		else:
			return ApiResponse.error_response(response["status"], response["msg"])
