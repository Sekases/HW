from pydantic import BaseModel
from ujson import loads, dumps
from aiohttp import ClientSession


class GetDifficulty(BaseModel):
    progressPercent: float
    difficultyChange: float
    estimatedRetargetDate: int
    remainingBlocks: int
    remainingTime: int
    previousRetarget: float
    previousTime: int
    nextRetargetHeight: int
    timeAvg: int
    timeOffset: int
    expectedBlocks: float


class GetBlockStatus(BaseModel):
    in_best_chain: bool
    height: int
    next_best: str


class GetRewardStats(BaseModel):
    startBlock: int
    endBlock: int
    totalReward: str
    totalFee: str
    totalTx: str


async def get_difficulty() -> dict:
    async with ClientSession(
        base_url='https://mempool.space',
        json_serialize=dumps
    ) as session:
        response = await session.get(
            url='/api/v1/difficulty-adjustment'
        )
        return await response.json(loads=loads)


async def get_block_status() -> dict:
    async with ClientSession(
        base_url='https://mempool.space',
        json_serialize=dumps
    ) as session:
        response = await session.get(
            url='/api/block/0000000000000000000065bda8f8a88f2e1e00d9a6887a43d640e52a4c7660f2/status'
        )
        return await response.json(loads=loads)


async def get_block_stats() -> dict:
    async with ClientSession(
        base_url='https://mempool.space',
        json_serialize=dumps
    ) as session:
        response = await session.get(
            url='/api/v1/mining/reward-stats/100'
        )
        return await response.json(loads=loads)

if __name__ == '__main__':
    import asyncio
    get_diff = asyncio.run(get_difficulty())
    get_block = asyncio.run(get_block_status())
    get_rew_stat = asyncio.run(get_block_stats())

    get_diff_schema = GetDifficulty(**get_diff)
    get_block_schema = GetBlockStatus(**get_block)
    get_rew_stat_schema = GetRewardStats(**get_rew_stat)
