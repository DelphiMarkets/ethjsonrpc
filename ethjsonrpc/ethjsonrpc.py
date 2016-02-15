import requests
import json


class EthJsonRpc:

    def __init__(self, host="localhost", port="8545"):
        self.host = host
        self.port = port

    def _call(self, method, params=None):
        if params is None:
            params = []
        data = json.dumps({
            'jsonrpc': '2.0',
            'method': method,
            'params': params,
            'id': 0
        })
        headers = {'content-type': 'application/json'}
        response = requests.post("http://{}:{}".format(self.host, self.port), data=data, headers=headers).json()
        return response

    def eth_sendTransaction(self, from_address, to_address=None, data=None, value=0, gas=0, gas_price=0):
        """
        Creates new message call transaction or a contract creation, if the data field contains code.
        """
        params = {
            'from': from_address,
            'gas': hex(gas) if gas else hex(0),
            'gasPrice': hex(gas_price) if gas_price else hex(0),
            'value': hex(value) if value else hex(0)
        }
        if to_address:
            params['to'] = to_address
        if data:
            params['data'] = data
        return self._call('eth_sendTransaction', [params])

    def eth_sendRawTransaction(self, raw_transaction):
        """
        Sends a raw transaction to the network
        """
        return self._call('eth_sendRawTransaction', [raw_transaction])

    def eth_call(self, from_address, to_address, data=None, default_block="latest"):
        """
        Executes a new message call immediately without creating a transaction on the block chain.
        """
        params = [
            {
                'from': from_address,
                'to': to_address,
                'data': data
            },
            default_block
        ]
        return self._call('eth_call', params)

    def eth_getBlock(self, block_number):
        """
        Returns block with given block number.
        """
        return self._call('eth_getBlock', [block_number])

    def eth_getBlockNumber(self):
        """
        Returns the current client version.
        """
        return self._call('eth_getBlockNumber')

    def web3_clientVersion(self):
        """
        Returns the current client version.
        """
        return self._call('web3_clientVersion')

    def web3_sha3(self, data):
        """
        Returns SHA3 of the given data.
        """
        data = str(data).encode('hex')
        return self._call('web3_sha3', [data])

    def net_version(self):
        """
        Returns the current network protocol version.
        """
        return self._call('net_version')

    def net_listening(self):
        """
        Returns true if client is actively listening for network connections.
        """
        return self._call('net_listening')

    def net_peerCount(self):
        """
        Returns number of peers currenly connected to the client.
        """
        return self._call('net_peerCount')

    def eth_version(self):
        """
        Returns the current ethereum protocol version.
        """
        return self._call('eth_version')

    def eth_coinbase(self):
        """
        Returns the client coinbase address.
        """
        return self._call('eth_coinbase')

    def eth_mining(self):
        """
        Returns true if client is actively mining new blocks.
        """
        return self._call('eth_mining')

    def eth_gasPrice(self):
        """
        Returns the current price per gas in wei.
        """
        return self._call('eth_gasPrice')

    def eth_accounts(self):
        """
        Returns a list of addresses owned by client.
        """
        return self._call('eth_accounts')

    def eth_blockNumber(self):
        """
        Returns the number of most recent block.
        """
        return self._call('eth_blockNumber')

    def eth_getBalance(self, address, default_block="latest"):
        """
        Returns the balance of the account of given address.
        """
        return self._call('eth_getBalance', [address, default_block])

    def eth_getStorageAt(self, address, position, default_block="latest"):
        """
        Returns the value from a storage position at a given address.
        """
        return self._call('eth_getStorageAt', [address, hex(position), default_block])

    def eth_getTransactionCount(self, address, default_block="latest"):
        """
        Returns the number of transactions send from a address.
        """
        return self._call('eth_getTransactionCount', [address, default_block])

    def eth_getBlockTransactionCountByHash(self, block_hash):
        """
        Returns the number of transactions in a block from a block matching the given block hash.
        """
        return self._call('eth_getTransactionCount', [block_hash])

    def eth_getBlockTransactionCountByNumber(self, block_number):
        """
        Returns the number of transactions in a block from a block matching the given block number.
        """
        return self._call('eth_getBlockTransactionCountByNumber', [hex(block_number)])

    def eth_getUncleCountByblockHash(self, block_hash):
        """
        Returns the number of uncles in a block from a block matching the given block hash.
        """
        return self._call('eth_getUncleCountByblockHash', [block_hash])

    def eth_getUncleCountByblockNumber(self, block_number):
        """
        Returns the number of uncles in a block from a block matching the given block number.
        """
        return self._call('eth_getUncleCountByblockNumber', [hex(block_number)])

    def eth_getCode(self, address, default_block="latest"):
        """
        Returns code at a given address.
        """
        return self._call('eth_getCode', [address, default_block])

    def eth_getBlockByHash(self, block_hash, transaction_objects=True):
        """
        Returns information about a block by hash.
        """
        return self._call('eth_getBlockByHash', [block_hash, transaction_objects])

    def eth_flush(self):
        """
        """
        return self._call('eth_flush')

    def eth_getBlockByNumber(self, block_number, transaction_objects=True):
        """
        Returns information about a block by hash.
        """
        return self._call('eth_getBlockByNumber', [block_number, transaction_objects])

    def eth_getTransactionByHash(self, transaction_hash):
        """
        Returns the information about a transaction requested by transaction hash.
        """
        return self._call('eth_getTransactionByHash', [transaction_hash])

    def eth_getTransactionByblockHashAndIndex(self, block_hash, index):
        """
        Returns information about a transaction by block hash and transaction index position.
        """
        return self._call('eth_getTransactionByblock_hashAndIndex', [block_hash, hex(index)])

    def eth_getTransactionByblockNumberAndIndex(self, block_number, index):
        """
        Returns information about a transaction by block number and transaction index position.
        """
        return self._call('eth_getTransactionByblock_numberAndIndex', [block_number, hex(index)])

    def eth_getTransactionReceipt(self, transaction_hash):
        """
        Returns the receipt of a transaction by transaction hash.
        """
        return self._call('eth_getTransactionReceipt', [transaction_hash])

    def eth_getUncleByblockHashAndIndex(self, block_hash, index, transaction_objects=True):
        """
        Returns information about a uncle of a block by hash and uncle index position.
        """
        return self._call('eth_getUncleByblock_hashAndIndex', [block_hash, hex(index), transaction_objects])

    def eth_getUncleByblockNumberAndIndex(self, block_number, index, transaction_objects=True):
        """
        Returns information about a uncle of a block by number and uncle index position.
        """
        return self._call('eth_getUncleByblock_numberAndIndex', [block_number, hex(index), transaction_objects])

    def eth_getCompilers(self):
        """
        Returns a list of available compilers in the client.
        """
        return self._call('eth_getCompilers')

    def eth_compileSolidity(self, code):
        """
        Returns compiled solidity code.
        """
        return self._call('eth_compileSolidity', [code])

    def eth_compileLLL(self, code):
        """
        Returns compiled LLL code.
        """
        return self._call('eth_compileLLL', [code])

    def eth_compileSerpent(self, code):
        """
        Returns compiled serpent code.
        """
        return self._call('eth_compileSerpent', [code])

    def eth_newFilter(self, from_block="latest", to_block="latest", address=None, topics=None):
        """
        Creates a filter object, based on filter options, to notify when the state changes (logs).
        To check if the state has changed, call eth_getFilterChanges.
        """
        _filter = {
            'fromBlock': from_block,
            'toBlock': to_block,
            'address': address,
            'topics': topics
        }
        return self._call('eth_newFilter', [_filter])

    def eth_newBlockFilter(self):
        """
        Creates a filter object, based on an option string, to notify when state changes (logs). To check if the state has changed, call eth_getFilterChanges.
        """
        return self._call('eth_newBlockFilter')

    def eth_uninstallFilter(self, filter_id):
        """
        Uninstalls a filter with given id. Should always be called when watch is no longer needed. Additonally Filters timeout when they aren't requested with eth_getFilterChanges for a period of time.
        """
        return self._call('eth_uninstallFilter', [filter_id])

    def eth_getFilterChanges(self, filter_id):
        """
        Polling method for a filter, which returns an array of logs which occurred since last poll.
        """
        return self._call('eth_getFilterChanges', [hex(filter_id)])

    def eth_getFilterLogs(self, filter_id):
        """
        Returns an array of all logs matching filter with given id.
        """
        return self._call('eth_getFilterLogs', [hex(filter_id)])

    def eth_getLogs(self, filter_object):
        """
        Returns an array of all logs matching a given filter object.
        """
        return self._call('eth_getLogs', [filter_object])

    def eth_getWork(self):
        """
        Returns the hash of the current block, the seedHash, and the difficulty to be met.
        """
        return self._call('eth_getWork')

    def eth_submitWork(self, nonce, header, mix_digest):
        """
        Used for submitting a proof-of-work solution.
        """
        return self._call('eth_submitWork', [nonce, header, mix_digest])

    def db_putString(self, database_name, key_name, string):
        """
        Stores a string in the local database.
        """
        return self._call('db_putString', [database_name, key_name, string])

    def db_getString(self, database_name, key_name):
        """
        Stores a string in the local database.
        """
        return self._call('db_getString', [database_name, key_name])

    def db_putHex(self, database_name, key_name, string):
        """
        Stores binary data in the local database.
        """
        return self._call('db_putHex', [database_name, key_name, string.encode('hex')])

    def db_getHex(self, database_name, key_name):
        """
        Returns binary data from the local database.
        """
        return self._call('db_getString', [database_name, key_name]).decode('hex')

    def shh_version(self):
        """
        Returns the current whisper protocol version.
        """
        return self._call('shh_version')

    def shh_post(self, topics, payload, priority, ttl, _from=None, to=None):
        """
        Sends a whisper message.
        """
        whisper_object = {
            'from': _from,
            'to': to,
            'topics': topics,
            'payload': payload,
            'priority': priority,
            'ttl': ttl
        }
        return self._call('shh_post', [whisper_object])

    def shh_newIdentinty(self):
        """
        Creates new whisper identity in the client.
        """
        return self._call('shh_newIdentinty')

    def shh_hasIdentity(self, address):
        """
        Checks if the client hold the private keys for a given identity.
        """
        return self._call('shh_hasIdentity', [address])

    def shh_newGroup(self):
        """
        """
        return self._call('shh_hasIdentity')

    def shh_addToGroup(self):
        """
        """
        return self._call('shh_addToGroup')

    def shh_newFilter(self, to, topics):
        """
        Creates filter to notify, when client receives whisper message matching the filter options.
        """
        _filter = {
            'to': to,
            'topics': topics
        }
        return self._call('shh_newFilter', [_filter])

    def shh_uninstallFilter(self, filter_id):
        """
        Uninstalls a filter with given id. Should always be called when watch is no longer needed.
        Additonally Filters timeout when they aren't requested with shh_getFilterChanges for a period of time.
        """
        return self._call('shh_uninstallFilter', [hex(filter_id)])

    def shh_getFilterChanges(self, filter_id):
        """
        Polling method for whisper filters.
        """
        return self._call('shh_getFilterChanges', [hex(filter_id)])

    def shh_getMessages(self, filter_id):
        """
        Get all messages matching a filter, which are still existing in the node.
        """
        return self._call('shh_getMessages', [hex(filter_id)])
