from typing import Optional, Union

from streamtape.ApiResponse import ApiResponse
from streamtape.BaseConfig import BaseConfig


class FileManager(BaseConfig):
	parameter: str = "file"

	def __init__(self, user: str, password: str):
		super().__init__(user, password)

	def list_data(self, folder_id: Optional[str] = None) -> Union[dict, list]:
		"""
		Retrieves a list of data from a specified folder.

		Args:
		    - folder_id (Optional[str]): The ID of the folder to retrieve data from. Defaults to None.

		Returns:
		    - Union[dict, list]: A dictionary or list containing the retrieved data.

		Raises:
		    - ApiResponseError: If the API response status is not 200.

		Example:
		    >>> list_data("folder123")
		    {
				"status": 200,
				"msg": "OK",
				"result": {
					"folders": [
					    {
						    "id": "B-qlJkdHFeo",
						    "name": "Subfolder"
					    }
					],
					"files": [
					    {
						    "name": "MyMinecraftLetsPlay.mp4",
							"size": 7040842,
							"link": "https://streamtape.com/v/rbAarvRPXdYbaxY/MyMinecraftLetsPlay.mp4",
							"created_at": 1585532987430,
							"downloads": 0,
							"linkid": "rbAarvRPXdYbaxY",
							"convert": "converted"
					    }
					]
				}
			}
		"""
		url = self.url_query(f"{self.parameter}/listfolder", query={
			"folder": folder_id,
		})
		response = BaseConfig.send_request(url)

		if response["status"] == 200:
			return response["result"]
		else:
			return ApiResponse.error_response(response["status"], response["msg"])

	def create_folder(self, folder_name: str, parent_folder: Optional[str] = None) -> dict:
		"""
		Creates a new folder with the given folder name and parent folder.

		Args:
		    - folder_name (str): The name of the folder to be created.
		    - parent_folder (str, optional): The ID of the parent folder. Defaults to None.

		Returns:
		    - dict: A dictionary containing the folder ID if the folder is created successfully.
		          If an error occurs, an error response dictionary is returned.

		Raises:
		    - ApiResponseError: If the API response status is not 200.

		Example:
		    >>> create_folder("New Folder", "12345")
			{
				"status": 200,
				"msg": "OK",
				"result": {
				    "folderid": "LnvnE51P5gc"
				}
			}
		"""
		url = self.url_query(f"{self.parameter}/createfolder", query={
			"name": folder_name,
			"pid" : parent_folder,
		})
		response = BaseConfig.send_request(url)

		if response["status"] == 200:
			return {
				"folderid": response["result"].get("folderid")
			}
		else:
			return ApiResponse.error_response(response["status"], response["msg"])

	def rename_folder(self, folder_name: str, parent_folder: str) -> Union[dict, bool]:
		"""
		Renames a folder with the given folder_name and moves it to the specified parent_folder.

		Args:
		    - folder_name (str): The name of the folder to be renamed.
		    - parent_folder (str): The name of the parent folder where the renamed folder will be moved.

		Returns:
		    - Union[dict, bool]: Returns a boolean value indicating the success of the renaming operation if the response status is 200.
		                       Otherwise, returns an error response as a dictionary using the ApiResponse.error_response method.

		Raises:
		    - ApiResponseError: If the API response status is not 200.
		"""
		url = self.url_query(f"{self.parameter}/renamefolder")
		response = BaseConfig.send_request(url, data={
			"name"  : folder_name,
			"folder": parent_folder,
		})

		if response["status"] == 200:
			return bool(response["result"])
		else:
			return ApiResponse.error_response(response["status"], response["msg"])

	def delete_folder(self, folder_id: str) -> Union[dict, bool]:
		"""
		Deletes a folder with the given folder_id.

		Args:
		    - folder_id (str): The ID of the folder to be deleted.

		Returns:
		    - Union[dict, bool]: Returns a boolean value indicating the success of the deletion operation if the response status is 200.
		                       If the response status is not 200, returns an error response dictionary.

		Raises:
		    - ApiResponseError: If the API response status is not 200.

		Example:
		    >>> delete_folder("folder123")
		    {
				"status": 200,
				"msg": "OK",
				"result": true
			}
		"""
		url = self.url_query(f"{self.parameter}/deletefolder")
		response = BaseConfig.send_request(url, data={
			"folder": folder_id,
		})

		if response["status"] == 200:
			return bool(response["result"])
		else:
			return ApiResponse.error_response(response["status"], response["msg"])

	def rename_file(self, file: str, name: str) -> Union[dict, bool]:
		"""
		Renames a file with the given name.

		Args:
		    - file (str): The name of the file to be renamed.
		    - name (str): The new name for the file.

		Returns:
		    - Union[dict, bool]: Returns a dictionary containing the response result if the request is successful,
		    otherwise returns a boolean value indicating the success of the request.

		Raises:
		    - ApiResponse: If the response status is not 200, an ApiResponse error response is raised.

		Example:
		    >>> obj = MyClass()
		    >>> obj.rename_file("old_file.txt", "new_file.txt")
		    {
				"status": 200,
				"msg": "OK",
				"result": true
			}
		"""
		url = self.url_query(f"{self.parameter}/deletefolder")
		response = BaseConfig.send_request(url, data={
			"file": file,
			"name": name
		})

		if response["status"] == 200:
			return bool(response["result"])
		else:
			return ApiResponse.error_response(response["status"], response["msg"])

	def move_file(self, file_id: str, folder_id: str) -> Union[dict, bool]:
		"""
		Moves a file to a specified folder.

		Args:
		    - file_id (str): The ID of the file to be moved.
		    - folder_id (str): The ID of the folder to which the file will be moved.

		Returns:
		    - Union[dict, bool]: Returns a boolean value indicating the success of the operation if the response status is 200.
		                       Otherwise, returns an error response as a dictionary containing the status code and error message.

		Raises:
		    - ApiResponse: If the response status is not 200, an ApiResponse error response is raised.
		"""
		url = self.url_query(f"{self.parameter}/move")
		response = BaseConfig.send_request(url, data={
			"file"  : file_id,
			"folder": folder_id
		})

		if response["status"] == 200:
			return bool(response["result"])
		else:
			return ApiResponse.error_response(response["status"], response["msg"])

	def delete_file(self, file_id: str) -> Union[dict, bool]:
		"""
		Deletes a file with the given file_id.

		Args:
		    - file_id (str): The ID of the file to be deleted.

		Returns:
		    - Union[dict, bool]: Returns a boolean value indicating the success of the deletion operation if the response status is 200.
		                       If the response status is not 200, returns an error response dictionary.

		Raises:
		    - ApiResponse: If the response status is not 200, an ApiResponse error response is raised.

		Example:
		    >>> delete_file("file123")
		    {
				"status": 200,
				"msg": "OK",
				"result": true
			}
		"""
		url = self.url_query(f"{self.parameter}/delete", query={
			"file": file_id
		})
		response = BaseConfig.send_request(url)

		if response["status"] == 200:
			return bool(response["result"])
		else:
			return ApiResponse.error_response(response["status"], response["msg"])
