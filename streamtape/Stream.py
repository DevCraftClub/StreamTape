from streamtape.ApiResponse import ApiResponse
from streamtape.BaseConfig import BaseConfig


class Stream(BaseConfig):
	parameter: str = "file"

	def __init__(self, user: str, password: str):
		super().__init__(user, password)

	def dlticket(self, file_id: str) -> dict:
		"""
		Retrieves a download ticket for a given file ID.

		Args:
		    - file_id (str): The ID of the file for which to retrieve the download ticket.

		Returns:
		    - dict: A dictionary containing the download ticket information, including the ticket itself,
		          the wait time in seconds, and the expiration date and time.

		Raises:
		    - ApiResponseError: If the API response status is not 200, indicating an error occurred.

		"""
		url = self.url_query(f"{self.parameter}/dlticket")
		response = BaseConfig.send_request(url, data={
			"file": file_id
		})

		if response["status"] == 200:
			return {
				"ticket"     : response["result"].get('ticket'),
				"wait_time"  : int(response["result"].get('wait_time')),
				"valid_until": BaseConfig.str_to_datetime(response["result"].get('valid_until')),
			}
		else:
			return ApiResponse.error_response(response["status"], response["msg"])

	def download_link(self, file_id: str) -> dict:
		"""
		Downloads a file from the server using the provided file ID.

		Args:
		    - file_id (str): The ID of the file to be downloaded.

		Returns:
		    - dict: A dictionary containing the name, size, and URL of the downloaded file.

		Raises:
		    - ApiResponseError: If the server returns an error response.

		"""
		dl_ticket = self.dlticket(file_id)
		url = self.url_query(f"{self.parameter}/dl", use_login=False)
		response = BaseConfig.send_request(url, data={
			"file"  : file_id,
			"ticket": dl_ticket
		})

		if response["status"] == 200:
			return {
				"name": response["result"].get('name'),
				"size": int(response["result"].get('size')),
				"url" : response["result"].get('url'),
			}
		else:
			return ApiResponse.error_response(response["status"], response["msg"])

	def file_info(self, file_id: list) -> dict:
		"""
		Retrieves information about the specified files.

		Args:
		    - file_id (list): A list of file IDs for which information needs to be retrieved.

		Returns:
		    - dict: A dictionary containing the information about the files.

		Raises:
		    - ApiResponseError: If the API response status is not 200.
		"""
		url = self.url_query(f"{self.parameter}/info")
		response = BaseConfig.send_request(url, data={
			"file": ','.join(file_id),
		})

		if response["status"] == 200:
			return response["result"]
		else:
			return ApiResponse.error_response(response["status"], response["msg"])
