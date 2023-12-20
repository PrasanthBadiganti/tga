import asyncio
import time


class AsyncService:

    def execute_synchronous_query(self, tables):
        result = []
        for table in tables:
            response = self.execute_sync_query(table)
            result.append(response)
        return result

    async def execute_asynchronous_query(self, tables):
        result = []
        for table in tables:
            response = self.execute_async_query(table)
            result.append(response)
        async_results = await asyncio.gather(*result)
        return async_results

    @staticmethod
    async def execute_async_query(table):
        await asyncio.sleep(3)
        # consider query takes 3 seconds to complete
        return f'ASync Task for {table} completed'

    @staticmethod
    def execute_sync_query(table):
        time.sleep(3)
        # consider query takes 3 seconds to complete
        return f'Sync Task for {table} completed'
