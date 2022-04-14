import requests
import allure

from helpers.logger import Logger


class Methods:

    @staticmethod
    def post(url: str, params: dict = None, data: dict = None, headers: dict = None, cookies: dict = None):
        with allure.step(f"POST request to url {url}"):
            return Methods._send(url, params, data, headers, cookies, "POST")

    @staticmethod
    def get(url: str, params: dict = None, data: dict = None, headers: dict = None, cookies: dict = None):
        with allure.step(f"GET request to url {url}"):
            return Methods._send(url, params, data, headers, cookies, "GET")

    @staticmethod
    def put(url: str, params: dict = None, data: dict = None, headers: dict = None, cookies: dict = None):
        with allure.step(f"PUT request to url {url}"):
            return Methods._send(url, params, data, headers, cookies, "PUT")

    @staticmethod
    def delete(url: str, params: dict = None, data: dict = None, headers: dict = None, cookies: dict = None):
        with allure.step(f"DELETE request to url {url}"):
            return Methods._send(url, params, data, headers, cookies, "DELETE")

    @staticmethod
    def _send(url: str, params: dict, data: dict, headers: dict, cookies: dict, method: str):

        url = f"https://playground.learnqa.ru{url}"

        Logger.add_request(url, data, params, headers, cookies, method)

        if headers is None:
            headers = {}
        if cookies is None:
            cookies = {}

        if method == "GET":
            response = requests.get(url, params=params, headers=headers, cookies=cookies)
        elif method == "POST":
            response = requests.post(url, params=params, data=data, headers=headers, cookies=cookies)
        elif method == "PUT":
            response = requests.put(url, params=params, data=data, headers=headers, cookies=cookies)
        elif method == "DELETE":
            response = requests.delete(url, params=params, data=data, headers=headers, cookies=cookies)
        else:
            raise Exception(f"Bad http method {method} was received")

        Logger.add_response(response)

        return response

