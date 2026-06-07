from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from keyboards import claim_types_kb

router = Router(name="start")


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext) -> None:
    await state.clear()
    await message.answer(
        "Бот-генератор претензий «Хлебник Франчайзинг».\n\n"
        "Выберите тип претензии.\n"
        "Нужного партнёра нет в базе? — /addpartner",
        reply_markup=claim_types_kb(),
    )


@router.message(Command("cancel"))
async def cmd_cancel(message: Message, state: FSMContext) -> None:
    await state.clear()
    await message.answer("Действие отменено. /start — начать заново.")
