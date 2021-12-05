# Copyright (C) 2021 By VeezMusicProject

from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    PAY_PAL,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **اهلا [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
💭 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) يسمح لك بتشغيل مقاطع او صوت او حتى بثوث مباشرة على الشات الصوتي!**

💡 **لعرض قائمة الاوامر الخاصه بالبوت انقر على » 📚 الاوامر زر!**
🔖 **لمعرفه كيف تستخدم البوت, الرجاء الضغط على » ❓ تعليمات الاستخدام زر!**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ اضفني في مجموعتك او قناتك ➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("❓ تعليمات الاستخدام", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("📚 الاوامر", callback_data="cbcmds"),
                    InlineKeyboardButton("❤ الدعم المادي", url=f"https://t.me/{PAY_PAL}"),
                ],
                [
                    InlineKeyboardButton(
                        "👥 القروب الرسمي", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "📣 القناة الرسميه", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "المطور", url="https://github.com/levina-lab/video-stream"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ **تعليمات استخدام البوت:**

1.) **اولا اضفني الى مجموعتك.**
2.) **بعدها, اعطيني كامل الصلاحيات عدا الاخفاء.**
3.) **بعد رفعه مشرف اكتب /reload في مجموعتك لتحديث قائمة الادمنية.**
3.) **اضف @{ASSISTANT_NAME} لمجموعتك او اكتب /userbotjoin لجعل البوت يضيف الحساب المساعد.**
4.) **تأكد من تشغيل الشات الصوتي لتشغيل مقطع/صوت.**
5.) **بعض الاوقات, تحديث البوت باستخدام /reload الامر سيساعدك لحل مشكلة البوت.**

📌 **اذا لم ينضم البوت للشات الصوتي تأكد من تشغيل الشات الصوتي اولا, او اكتب /userbotleave ثم اكتب /userbotjoin مجددا.**

💡 **اذا كان لديك سؤال او اقتراح يرجى مراجعه قروب الدعم: @{GROUP_SUPPORT}**

⚡ __تم تطويره {OWNER_NAME} __""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 الى الخلف", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **مرحبا [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

» **اضغط على الزر الذي ادناه لمعرفة الاوامر !**

⚡ __تم تطويره {OWNER_NAME} __""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("👷🏻 اوامر الادمنية", callback_data="cbadmin"),
                    InlineKeyboardButton("🧙🏻 اوامر المطور الاساسي", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("📚 الاوامر الاساسيه", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("🔙 الى الخلف", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 الاوامر الاساسيه:

» /play (اسم الصوت/الرابط) - لتشغيل الصوت بالشات الصوتي
» /stream (الرابط) - لتشغيل صوت البث المباشر على الشات الصوتي
» /vplay (اسم المقطع/الرابط) - لتشغيل المقطع في الشات الصوتي
» /vstream - لتشغيل بث مباشر من اليوتيوب
» /playlist - لإطهار قائمة التشغيل المقاطع
» /video (اسم المقطع) - لتحميل المقطع من اليوتيوب
» /song (اسم المقطع) - لتحميل صوت المقطع من اليوتيوب
» /search (اسم المقطع) - لبحث عن رابط المقطع

» /ping - لمعرفه سرعه استجابه البوت
» /uptime - لمعرفه مدة تشغيل البوت
» /alive - لمعرفه البوت يعمل ام لا (في المجموعه)

⚡️ __تم تطويره {OWNER_NAME} __""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 الى الخلف", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 هنا اوامر الادمن:

» /pause - الايقاف البث مؤقتا
» /resume - لاستمرار البث
» /skip - لتخطي البث
» /stop - لايقاف البث
» /vmute - لكتم البوت في الشات الصوتي
» /vunmute - إلغاء كتم البوت في الشات الصوتي
» /reload - لتحديث قائمة الادمنية
» /userbotjoin - الانظمام الى المجموعه
» /userbotleave - لمغادره مجموعه

⚡️ __تم تطويره {OWNER_NAME} __""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 الى الخلف", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 اوامر المطور الاساسي:

» /rmw - لتنظيف كل الملفات الخامه
» /rmd - لتنظيف كل الملفات
» /leaveall - مغادرة كل المجموعات او القنوات

⚡ __تم تطويره {OWNER_NAME} __""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 الى الخلف", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    await query.message.delete()
