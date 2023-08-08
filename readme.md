# Unofficial StreamTape API wrapper

It is a simple API wrapper for the streaming service streamtape.com. The API documentation can be found on the docs page. The whole structure of the API has been split into different classes for easy overview and usage.

## Installation

Install with

```python3
pip install streamtape
```

## Usage

### General usage

Every class starts with following initialization:

```python3
my_var = selectedClass(API_USER_KEY, API_PASSWORD)
```

API key and password you can get in your account in **[Account Settings](https://streamtape.com/accpanel#accsettings)**.

### General response

For the general purpose of any response, the ApiResponse class has been created to return a dict with this structure:

```json
{
    "status": <status-code>,
    "msg": "<informational message. might vary, use the status code in your code!>",
    "result": <result of the request. varies depending on the request>
}
```

### Account

Example

```python
account = Account(API_USER_KEY, API_PASSWORD)
print(account.get_info())
```

### Convertation

Example

```python
converts = Convertation(API_USER_KEY, API_PASSWORD)
print(converts.list_converts())
```

### FileManager

Class for working with files and folders

Example

```python
f_manager = FileManager(API_USER_KEY, API_PASSWORD)
print(f_manager.list_data())
```

### Remote

Example

```python
remote = Remote(API_USER_KEY, API_PASSWORD)
print(remote.remote_upload("path_to_file", "folder_id"))
```

### Stream

Example

```python
stream = Stream(API_USER_KEY, API_PASSWORD)
print(stream.file_info("file_id"))
```

### Upload

Example

```python
uploader = Upload(API_USER_KEY, API_PASSWORD)
print(uploader.upload("path_to_file", "folder_id"))
```

