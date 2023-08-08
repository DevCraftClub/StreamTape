from typing import Optional, Union

from streamtape.ApiResponse import ApiResponse
from streamtape.BaseConfig import BaseConfig
from streamtape.Stream import Stream


class Remote(BaseConfig):
	parameter: str = "remotedl"

	def __init__(self, user: str, password: str):
		super().__init__(user, password)

	def remote_upload(self, file_url: str, folder: Optional[str], headers: Optional[dict], name: Optional[str]) -> dict:
		"""
		Uploads a file to a remote server.

		Args:
		    - file_url (str): The URL of the file to be uploaded.
		    - folder (Optional[str]): The folder in which the file should be uploaded. Defaults to None.
		    - headers (Optional[dict]): Additional headers to be included in the request. Defaults to an empty dictionary.
		    - name (Optional[str]): The name of the file. Defaults to None.

		Returns:
		    - dict: A dictionary containing the ID of the uploaded file, the ID of the folder it belongs to, and the file information.

		Raises:
		    - ApiResponse: If the response status is not 200, an error response is returned.

		"""
		url = self.url_query(f"{self.parameter}/add")
		response = BaseConfig.send_request(url, data={
			"url"    : file_url,
			"folder" : folder or None,
			"headers": headers or {},
			"name"   : name or None
		})

		if response["status"] == 200:
			stream = Stream(self.api_user, self.api_password)
			file_info = stream.file_info(response["result"].get('id'))
			return {
				"id"       : response["result"].get('id'),
				"folderid" : response["result"].get('folderid'),
				"file_info": file_info
			}
		else:
			return ApiResponse.error_response(response["status"], response["msg"])

	def remove(self, file_id: str) -> Union[bool, dict]:
		"""
		Removes a file with the given file_id from the server.

		Args:
		    - file_id (str): The ID of the file to be removed.

		Returns:
		    - Union[bool, dict]: Returns a boolean value indicating the success of the operation if the status code is 200.
		                       Otherwise, returns an error response dictionary.

		Raises:
		    - ApiResponse: If the response status is not 200, an error response is returned.

		Example:
		    >>> remove("file123")  # Returns True if the file is successfully removed, otherwise returns an error response dictionary.
		    {
				"status": 200,
				"msg": "OK",
				"result": true
			}
		"""
		url = self.url_query(f"{self.parameter}/remove")
		response = BaseConfig.send_request(url, data={
			"id": file_id,
		})

		if response["status"] == 200:
			return bool(response["result"])
		else:
			return ApiResponse.error_response(response["status"], response["msg"])

	def check_remote_status(self, file_id: str) -> Union[dict, list]:
		"""
		Retrieves the status of a remote file with the given file ID.

		Args:
		    - self (object): The instance of the class.
		    - file_id (str): The ID of the file to check the status for.

		Returns:
		    - Union[dict, list]: The status of the remote file. It can be either a dictionary or a list.

		Raises:
		    - ApiResponseError: If the API response status is not 200.

		Example:
		    >>> check_remote_status("12345")
		    {
				"status": 200,
				"msg": "OK",
				"result": {
					"LnvnE51P5gc": {
					    "id": "LnvnE51P5gc",
					    "remoteurl": "https://vid.me/myvideo123",
					    "status": "new",
					    "bytes_loaded": null,
					    "bytes_total": null,
					    "folderid": "LnvnE51P5gc",
					    "added": "2019-12-31 23:59:59",
					    "last_update": "2019-12-31 23:59:59",
					    "extid": false,
					    "url": false
					},
				}
			}
		"""
		url = self.url_query(f"{self.parameter}/status")
		response = BaseConfig.send_request(url, data={
			"id": file_id,
		})

		if response["status"] == 200:
			return response["result"]
		else:
			return ApiResponse.error_response(response["status"], response["msg"])
