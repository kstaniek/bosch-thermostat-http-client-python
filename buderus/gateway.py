import asyncio
import json

from io import StringIO

from aiohttp import client_exceptions

from .encryption import Encryption


class Gateway(object):
    _magic = bytearray.fromhex("867845e97c4e29dce522b9a7d3a3e07b152bffadddbed7f5ffd842e9895ad1e4")

    host = None

    serial_number = None
    access_key = None
    password = None

    encryption = None
    
    websession = None

    def __init__(self, websession, host, access_key, password, ):
        """
        :param access_key:
        :param password:
        :param host:
        """

        self.access_key = access_key
        self.password = password
        self.host = host
        self.websession = websession

        self.encryption = Encryption(self._magic, access_key, password)
  
    def encrypt(self, data):
        return self.encryption.encrypt(data)

    def decrypt(self, data):
        return self.encryption.decrypt(data)

#    async def initialize(self):
#        result = await self.request('get', '/')
     #   decrypted_result = decrypt(resutl)
     #   print decrypted_result

#        self.config = Config(result['config'], self.request)
#        self.groups = Groups(result['groups'], self.request)
#        self.lights = Lights(result['lights'], self.request)
#        self.scenes = Scenes(result['scenes'], self.request)
#        self.sensors = Sensors(result['sensors'], self.request)


    async def request(self, path):

        headers = {'User-agent': 'TeleHeater/2.2.3' ,'Accept': 'application/json'}
        
        """Make a request to the API."""
        url = 'http://{}'.format(self.host)
        
        url += path

        try:
            async with self.websession.request('get', url, headers=headers) as res:
        #        if res.content_type != 'application/json':
        #            raise ResponseError(
        #                'Invalid content type: {}'.format(res.content_type))
                data = await res.text()
        #        _raise_on_error(data)
                return data
        except client_exceptions.ClientError as err:
            raise RequestError(
                'Error requesting data from {}: {}'.format(self.host, err)
            ) from None

    async def submit(self, data, path):
        headers = {'User-agent': 'TeleHeater/2.2.3' ,'Accept': 'application/json'}
        
        """Make a request to the API."""
        url = 'http://{}'.format(self.host)
        
        url += path

      #  try:
       #     async with self.websession.request('put', url, data, headers=headers) as req:

           
        #    if not req.status == 204:
         #       self.logger.debug(req.read())




    async def get(self, path):
        encrypted = await self.request(path) 
        result = self.encryption.decrypt(encrypted)
        return result

    async def get_json(self,path):
        data = await self.get(path)
        jsondata =  json.loads(data)
        return jsondata
            

