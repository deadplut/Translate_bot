from googletrans import Translator
import telebot

from telebot import types

FULL = {'af': '_африканский', 'sq': '_албанский', 'am': '_амхарский', 'ar': '_арабский', 'hy': '_армянский',
        'az': '_азербайджанский',
        'eu': '_баскский', 'be': '_белорусский', 'bn': '_бенгальский', 'bs': '_боснийский', 'bg': '_болгарский',
        'ca': '_каталонский',
        'ceb': '_кебуано', 'ny': '_чичева', 'zh-cn': '_китайский упрощенный', 'zh-tw': '_китайский традиционный',
        'co': '_корсиканский',
        'hr': '_хорватский', 'cs': '_чешский язык', 'da': '_датский', 'nl': '_голландский', 'en': '_английский',
        'eo': '_эсперанто',
        'et': '_эстонский', 'tl': '_филиппинский', 'fi': '_финский', 'fr': '_французский', 'fy': '_фризский',
        'gl': '_галисийский',
        'ka': '_грузинский', 'de': '_немецкий', 'el': '_греческий', 'gu': '_гуджарати', 'ht': '_гаитянский креольский',
        'ha': '_хауса',
        'haw': '_гавайский', 'iw': '_иврит', 'he': '_иврит', 'hi': '_хинди', 'hmn': '_хмонг', 'hu': '_венгерский',
        'is': '_исландский',
        'ig': '_игбо', 'id': '_индонезийский', 'ga': '_ирландский', 'it': '_итальянский', 'ja': '_японский',
        'jw': '_яванский',
        'kn': '_канадский', 'kk': '_казахский', 'km': '_кхмерский', 'ko': '_корейский', 'ku': '_курдский',
        'ky': '_кыргызский',
        'la': '_латинский', 'lv': '_латышский', 'lt': '_литовский', 'lb': '_люксембургский', 'mk': '_македонский',
        'mg': '_малагасийский',
        'ms': '_малайский', 'ml': '_малаялам', 'mt': '_мальтийский', 'mi': '_маори', 'mr': '_маратхи',
        'mn': '_монгольский',
        'my': '_мьянма', 'ne': '_непальский', 'no': '_норвежский', 'or': '_одиа', 'ps': '_почта', 'fa': '_персидский',
        'pl': '_полировать', 'pt': '_португальский', 'pa': '_панджаби', 'ro': '_румынский', 'ru': '_русский',
        'sm': '_самоанец',
        'gd': '_шотландский', 'sr': '_сербский', 'st': '_сесото', 'sn': '_шона', 'sd': '_синдхи', 'si': '_сингальский',
        'sk': '_словацкий',
        'sl': '_словенский', 'so': '_сомалийский', 'es': '_испанский', 'su': '_суданский', 'sw': '_суахили',
        'sv': '_шведский',
        'tg': '_таджикский', 'ta': '_тамильский', 'te': '_телугу', 'th': '_тайский', 'tr': '_турецкий',
        'uk': '_украинский', 'ur': '_урду',
        'ug': '_уйгурский', 'uz': '_узбекский', 'vi': '_вьетнамский', 'cy': '_валлийский', 'xh': '_коса', 'yi': '_идиш',
        'yo': '_йоруба', 'zu': '_зулу'}
token = ("5534187600:AAEY8C1kDiqqcVNa2UyLnGkTEHyFv452bhM")

bot = telebot.TeleBot(token)




@bot.inline_handler(func=lambda query: len(query.query) == 0)
def empty_query(query):
    hint = "Введите слово!"
    try:
        r = types.InlineQueryResultArticle(
            id='1',
            # parse_mode='Markdown',
            title="Бот \"Переводчик\"",
            description=hint,
            input_message_content=types.InputTextMessageContent(
                message_text="Эх, зря я не ввёл слова :(")
        )
        bot.answer_inline_query(query.id, [r])
    except Exception as e:
        print(e)


def translater(text, lang='en'):
    translator = Translator()
    return translator.translate(text, dest=lang).text


def button(text, id, lang):
    text_trans = translater(text, lang)
    text_trans = types.InlineQueryResultArticle(
        id=id, title=f"Перевод на {FULL[lang]}",
        # Описание отображается в подсказке,
        # message_text - то, что будет отправлено в виде сообщения
        description=f"Перевод: {text_trans}",
        input_message_content=types.InputTextMessageContent(
            message_text=text_trans
        ))
    return text_trans


@bot.inline_handler(func=lambda query: len(query.query) > 0)
def query_text(query):
    text = query.query

    try:
        bot.answer_inline_query(
            query.id,
            [
                button(text, 1, 'en'),
                button(text, 2, 'fr'),
                button(text, 3, 'ru'),
                button(text, 4, 'de')
            ]
        )
    except Exception as e:
        print("{!s}\n{!s}".format(type(e), str(e)))


if __name__ == '__main__':
    bot.infinity_polling()
