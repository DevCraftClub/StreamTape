from typing import Optional, Union


class ApiResponse:
	status: Optional[int] = None
	msg: Optional[str] = None
	result: Optional[Union[list, bool, dict]] = None

	@staticmethod
	def message_info(status: int) -> str:
		"""
		Returns a message corresponding to the given status code.

		Parameters:
			- status (int): The status code to retrieve the message for.

		Returns:
			- str: The message corresponding to the given status code.

		Raises:
			- None

		Examples:
		>>> message_info(200)
		'Everything is OK. Request succeeded'
		>>> message_info(404)
		'File not found'
		>>> message_info(503)
		'Some error occurred'
		"""
		msg = "Some error occurred"

		if status == 200: msg = "Everything is OK. Request succeeded"
		elif status == 400: msg = "Bad request (e.g. wrong parameters)"
		elif status == 403: msg = "Permission denied (wrong api login/key, action on a file which does not belong to you, ...)"
		elif status == 404: msg = "File not found"
		elif status == 451: msg = "Unavailable For Legal Reasons"
		elif status == 509: msg = "Bandwidth usage exceeded. Please try again later. (you might see this during peak hours)"
		elif status != 509 and 500 <= status < 600: msg = "Server errors"

		return msg

	@staticmethod
	def error_response(status: int, error_msg: str):
		"""
		Returns a dictionary representing an error response.

		Parameters:
		- status (int): The status code of the error.
		- error_msg (str): The error message.

		Returns:
		- dict: A dictionary containing the error information.

		Example:
		>>> error_response(404, "Page not found")
		{
		    'error': True,
		    'status_id': 404,
		    'error_msg': 'Not Found',
		    'api_msg': 'Page not found'
		}
		"""
		return {
			'error'    : True,
			'status_id': status,
			'error_msg': ApiResponse.message_info(status),
			'api_msg'  : error_msg
		}
