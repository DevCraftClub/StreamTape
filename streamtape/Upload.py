import hashlib
import re
from typing import Optional

from streamtape.ApiResponse import ApiResponse
from streamtape.BaseConfig import BaseConfig


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
		url = self.url_query(f"{self.parameter}/ul")

		sha256_hash = hashlib.sha256()

		with open(file_path, "rb") as f:
			for byte_block in iter(lambda: f.read(4096), b""):
				sha256_hash.update(byte_block)
			sha256 = sha256_hash.hexdigest()

		response = BaseConfig.send_request(url, type_request='POST', data={
			"sha256": sha256,
			"folder": folder_id
		})

		if response["status"] == 200:
			regex = r"https:\/\/streamtape.com\/v\/(?P<file_id>.*)\/.*"
			match = re.match(regex, response["result"].get('url'))
			file_info = self.file_info(match.group('file_id')) if match.group('file_id') else {}
			return {
				"url"        : response["result"].get('url'),
				"valid_until": BaseConfig.str_to_datetime(response["result"].get('valid_until')),
				"file_info"  : file_info
			}
		else:
			return ApiResponse.error_response(response["status"], response["msg"])
