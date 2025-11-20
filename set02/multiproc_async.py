import os
import multiprocessing
import asyncio
import logging


logger = logging.getLogger()


class BatchProcessor:
    @staticmethod
    def setup():
        pass

    @staticmethod
    def process(iter_data: list):
        common_data = {}
        return asyncio.run(BatchProcessor.process_batches_async(iter_data, common_data))

    @staticmethod
    async def process_batches_async(iter_data, common_data, chunk_size=20):
        result = []
        iter_data_chunked = [iter_data[idx:idx+chunk_size] for idx in range(0, len(iter_data), chunk_size)]
        for chunked_data in iter_data_chunked:
            values = await asyncio.gather(*[BatchProcessor.process_data(_data, common_data) for _data in chunked_data])
            result.extend(values)
        return result, True

    @staticmethod
    async def process_data(data, common_data):
        await asyncio.sleep(2)
        print(data)
        return data, True


class Tasker:
    def __init__(self):
        self.pool = multiprocessing.Pool(
            initializer=BatchProcessor.setup,
            processes=2     # os.cpu_count()
        )

    def execute(self, iter_arr, batch_size=50):
        try:
            batches = [iter_arr[idx:idx + batch_size] for idx in range(0, len(iter_arr), batch_size)]
            self.pool.map(BatchProcessor.process, batches)
        except Exception as e:
            logger.error(e)
        finally:
            pass


if __name__ == "__main__":
    Tasker().execute([x for x in range(100)])
