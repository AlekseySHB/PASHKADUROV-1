from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from sqlalchemy.ext.asyncio import async_sessionmaker
from logic.bot_logic import BotLogic
from .bot_commands import private_commands

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message, session_maker: async_sessionmaker):
    async with session_maker() as session:
        logic = BotLogic(session)
        if message.from_user:
            response = await logic.register_user(message.from_user.id, message.from_user.full_name)
            await message.answer(response)
        else:
            await message.answer("Не удалось определить пользователя.")

@router.message(Command("status"))
async def cmd_status(message: Message, session_maker: async_sessionmaker):
    async with session_maker() as session:
        logic = BotLogic(session)
        if message.from_user:
            response = await logic.get_user_status(message.from_user.id)
            await message.answer(response)
        else:
            await message.answer("Не удалось определить пользователя.")

@router.message(Command("vmpath"))
async def cmd_vmpath(message: Message, session_maker: async_sessionmaker):
    async with session_maker() as session:
        logic = BotLogic(session)
        if message.from_user and message.text:
            parts = message.text.split(maxsplit=1)
            if len(parts) != 2:
                await message.answer("Используйте: /vmpath ip:username:password")
                return
            data = parts[1].strip()
            creds = data.split(":")
            if len(creds) != 3:
                await message.answer("Используйте: /vmpath ip:username:password")
                return
            ip, username, password = creds
            response = await logic.save_vm_path(message.from_user.id, ip, username, password)
            await message.answer(response)
        else:
            await message.answer("Не удалось определить пользователя или текст сообщения.")

@router.message(Command("check"))
async def cmd_check(message: Message, session_maker: async_sessionmaker):
    async with session_maker() as session:
        logic = BotLogic(session)
        if message.from_user:
            response = await logic.check_vm_connection(message.from_user.id)
            await message.answer(response)
        else:
            await message.answer("Не удалось определить пользователя.")

@router.message(Command("ls"))
async def cmd_ls(message: Message, session_maker: async_sessionmaker):
    async with session_maker() as session:
        logic = BotLogic(session)
        if message.from_user:
            response = await logic.list_home_dir(message.from_user.id)
            await message.answer(response, parse_mode="Markdown")
        else:
            await message.answer("Не удалось определить пользователя.")

@router.message(Command("cat"))
async def cmd_cat(message: Message, session_maker: async_sessionmaker):
    async with session_maker() as session:
        logic = BotLogic(session)
        if message.from_user:
            response = await logic.cat_text_files(message.from_user.id)
            # Разбиваем длинное сообщение на части
            if len(response) > 4096:
                parts = [response[i:i+4096] for i in range(0, len(response), 4096)]
                for part in parts:
                    await message.answer(part)
            else:
                await message.answer(response)
        else:
            await message.answer("Не удалось определить пользователя.")

@router.message(Command("help"))
async def cmd_help(message: Message):
    commands_text = "Доступные команды:\n\n"
    for cmd in private_commands:
        commands_text += f"/{cmd.command} - {cmd.description}\n"
    await message.answer(commands_text)