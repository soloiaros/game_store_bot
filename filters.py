from config import ADMINS
import asyncio

from aiogram import executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.dispatcher.filters.state import StatesGroup, State
import logging
import config
from filters import *
from aiogram.dispatcher.filters import BoundFilter, AdminFilter
import aiogram
from aiogram.dispatcher.filters import Command

class IsUser(BoundFilter):
    async def check(self, message: Message):
        return message.from_user.id not in ADMINS


class IsAdmin(BoundFilter):
    async def check(self, message: Message):
        return message.from_user.id in ADMINS


class IsGroup(BoundFilter):
    async def check(self, message: Message) -> bool:
        return message.chat.type == 'group'



class IsChannel(BoundFilter):
    async def check(self, message: types.Message):
        if message.forward_from_chat:
            return message.forward_from_chat.type == types.ChatType.CHANNEL