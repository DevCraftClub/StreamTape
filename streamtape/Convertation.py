from typing import Union

from streamtape.ApiResponse import ApiResponse
from streamtape.BaseConfig import BaseConfig


class Convertation(BaseConfig):
	parameter: str = "file"

	def __init__(self, user: str, password: str):
		super().__init__(user, password)

	def list_converts(self) -> Union[dict, list]:
		"""
		Retrieves a list of running converts from the specified URL.

		Returns:
			- Union[Dict, List]: A dictionary or a list containing the running converts.

		Raises:
			- ApiResponse: If the API response status is not 200, an error response is returned.
		"""

		url = self.url_query(f"{self.parameter}/runningconverts")
		response = BaseConfig.send_request(url)

		if response["status"] == 200:
			return response["result"]
		else:
			return ApiResponse.error_response(response["status"], response["msg"])

	def list_failed_converts(self) -> Union[dict, list]:
		"""
		Retrieves a list of failed conversions from the specified URL.

		Returns:
		    - Union[Dict, List]: A dictionary or a list containing the failed conversions.

		Raises:
		    - ApiResponseError: If the API response status is not 200.

		Example:
		    >>> obj = YourClassName()
		    >>> obj.list_failed_converts()
		    {'status': 200, 'result': ['conversion1', 'conversion2']}
		"""
		url = self.url_query(f"{self.parameter}/failedconverts")
		response = BaseConfig.send_request(url)

		if response["status"] == 200:
			return response["result"]
		else:
			return ApiResponse.error_response(response["status"], response["msg"])

	def get_thumbnail(self, file_id: str) -> Union[dict, list]:
		"""
		Retrieves the thumbnail for a given file ID.

		Args:
		    - self (object): The instance of the class.
		    - file_id (str): The ID of the file for which the thumbnail is requested.

		Returns:
		    - Union[dict, list]: The thumbnail information as a dictionary or a list.

		Raises:
		    - ApiResponseError: If the API response status is not 200.

		Example:
		    >>> thumbnail = get_thumbnail("file123")
		    {
				"status": 200,
				"msg": "OK",
				"result": "https://thumb.tapecontent.net/thumb/wg8ad12d3QiJRXG/thumb.jpg"
			}
		"""
		url = self.url_query(f"{self.parameter}/getsplash", query={
			"file": file_id
		})
		response = BaseConfig.send_request(url)

		if response["status"] == 200:
			return response["result"]
		else:
			return ApiResponse.error_response(response["status"], response["msg"])
