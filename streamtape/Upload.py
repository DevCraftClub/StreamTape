import hashlib
import re
from typing import Optional

from streamtape.ApiResponse import ApiResponse
from streamtape.BaseConfig import BaseConfig
from streamtape.Stream import Stream


class Upload(BaseConfig):
	parameter: str = "file"

	def __init__(self, user: str, password: str):
		super().__init__(user, password)

	def upload(self, file_path: str, folder_id: Optional[str] = None) -> dict:
		"""
		Uploads a file to the server and returns the response.

		Args:
		    - file_path (str): The path of the file to be uploaded.
		    - folder_id (Optional[str], optional): The ID of the folder where the file will be uploaded. Defaults to None.

		Returns:
		    - dict: A dictionary containing the following information:
		        - "url" (str): The URL of the uploaded file.
		        - "valid_until" (datetime): The expiration date of the uploaded file.
		        - "file_info" (dict): Additional information about the uploaded file.

		Raises:
		    - ApiResponse: If the upload request fails, an error response is returned.

		"""
		sha256_hash = hashlib.sha256()
		response: Optional[ApiResponse] = None

		with open(file_path, "rb") as f:
			for byte_block in iter(lambda: f.read(4096), b""):
				sha256_hash.update(byte_block)
			sha256 = sha256_hash.hexdigest()

			url = self.url_query(f"{self.parameter}/ul", query={
				"sha256": sha256,
				"folder": folder_id
			})
			response = BaseConfig.send_request(url)

			f.close()

		if response is not None:
			if response["status"] == 200:
				file_upload_response = BaseConfig.send_request(response["result"]["url"], type_request='POST', files={
					"file1": open(file_path, 'rb')
				})

				if file_upload_response["status"] == 200:
					regex = r"https:\/\/streamtape.com\/v\/(?P<file_id>.*)\/.*"
					match = re.match(regex, file_upload_response["result"]["url"])
					stream = Stream(self.api_user, self.api_password)
					file_info = stream.file_info(match.group('file_id')) if match.group('file_id') else {}
					return file_upload_response["result"]
				else:
					return ApiResponse.error_response(file_upload_response["status"], file_upload_response["msg"])
			else:
				return ApiResponse.error_response(response["status"], response["msg"])
		else:
			return ApiResponse.error_response(404, "Couldn't send request")
