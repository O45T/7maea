from config import Config 
import requests
from telebot import types
import random
import telebot
from datetime import date ,timedelta ,time
import time 
elhypamody = '6311805458'
bot = telebot.TeleBot(Config.TG_BOT_TOKEN)
p3 = types.InlineKeyboardMarkup()
p5 = types.InlineKeyboardButton(text = "🔱 𝐒𝐨𝐔𝐑𝐂𝐄 • 𝐒𝐋𝐒 🔱",url="t.me/zwzwwzz")
A1 = types.InlineKeyboardButton(text = "اوامر الحماية .",callback_data="A1")
A2 = types.InlineKeyboardButton(text = "اوامر التسلية .",callback_data="A2")
A3 = types.InlineKeyboardButton(text = "اوامر الالعاب .",callback_data="A3")
A4 = types.InlineKeyboardButton(text = "اوامر الموسيقى ",callback_data="A4")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
  f2 = message.from_user.first_name 
  t2 = message.from_user.username 
  bot.reply_to(message,text="""*اهلا بك عزيزي - *[{}](t.me/{})،
*  في بوت الاوامر، 
لمعرفة اوامر البوت ارسل الاوامر*
""".format(f2,t2),disable_web_page_preview=True,parse_mode="markdown")

abod = ["متى تكون البراءه ذئب ؟",
            "هل تتوقع أن يصل البشر لمرحلة من التطور تجعلهم يتنقلون بين الكواكب بسهولة ؟",
            "أشياء ومنتجات جربتها في السفر أعجبتك ؟",
            "( الحياة مرة )/ هل قرأتها بالضمة أم بالفتحة ؟",
            "يتجاهلك بالقصد بعد صداقة طويلة، ما مقصده برأيك ؟",
            "شعورك الحالي في جملة ؟",
            "عندكم في الشلة ذلك الشخص الخجول جدًا ؟",
            "أشياء تجعلك تستمر وتتحمّل صعوبات الحياة ؟",
            "فنان/ة تحلم بلقائه ؟",
            "بتنام ولا بتواصل ؟",
            "ردة فعلك لو أوقفتك الشرطة في الطريق وسمعتهم يقولون هذا هو القاتل ؟",
            "شاركنا افضل قناة عندك ؟",
            "شيء جميل حصل معك اليوم ؟",
            "شاركنا صوره تمثل تخصصك ؟",
            "للإناث | لديكِ الجرأة لمصارحة الشخص اللي أذاك بكل شيء في قلبك ؟",
            "أكثر طبع غريب فيك وتحبه ؟",
            "أبسط شيء بعدل يومك كامل ؟",
            "سؤال تسأل نفسك فيه دائمًا ولا حصلت جواب ؟",
            "أسم تحب تقوله ؟",
            "أسم بنت تحبه ؟",
            "أسم ولد تحبه ؟",
            "وش تحس من يوم يناديك أبوك ؟",
            "مين أشد عصبية أمك أو أبوك ؟",
            "عادي تتابع فلم/مسلسل أكثر من مره ؟",
            "تقدر ترسل أخر صوره حفظتها ؟",
            "وش هي أكلتك المفظلة ؟",
            "وش الصفة الي تميزك عن غيرك ؟",
            "أنت شخص مسالم ؟",
            "شيء تسمعه كثير من الناس عنك ؟",
            "تحس أنك غامض ولا سراويلك منشوره ؟",
            "صفة تكرهها ؟",
            "أنت من النوع الي يعرف يسولف ويفتح مواضيع ؟",
            "موضوع ما تتقبل المزح فيه ؟",
            "كِلمة توجهها لوالديك ؟",
            "سطر من أخر أغنية سمعتها ؟",
            "عندك شخص تقوله كل تفاصيل يومك ؟",
            "ليش الاغلب يفضلون العلاقات الإكترونية ؟",
            "وش رأيك بالأهل الي يفتشون الجوالات ؟",
            "أهلك يفتشون جوالك ؟",
            "هل أنت راضي عن نفسك الفترة ذي ؟",
            "أنت من مُحبين الموسيقى القديمة أو الجديدة ؟",
            "أكله ودك تجربها ؟",
            "لو كانت للأيام الجميلة رائحه ماذا ستكون ؟",
            "تاريخ ودك تعيش فيه ؟",
            "لو تكرهه جدًا ؟",
            "عطينا إقتباس تحبه ؟",
            "عطينا حكمة لليوم ؟",
            "حكمتك الي ماشي عليها ؟",
            "أنت فاشل دراسيًا ؟",
            "انت متوظف ؟",
            "أسمك الي بالبرنامج غير عن الواقعي ؟",
            "مين الي أختار لك أسمك ؟",
            "كذبت في الأسئلة الي راحت ؟",
            "لو العالم مافيه أحد غيرك وش بتسوي ؟",
            "هل يومك جيد ؟",
            "القهوة بنظرك ؟",
            "تفكيرك الأن مُختلف عن العام الماضي ؟",
            "لو تروح مكتبه مثل جرير اول قسم تتوجه له دائمًا ؟",
            "تقدر تستغني عن هاتفك لأسبوع ؟",
            "شيء تحس لو ما سويته ليوم تفقده ؟",
            "رسالة لنفسك المستقبيلة ؟",
            "وش رأيك في الي يطلب السناب ؟",
            "تقدر تعطي سنابك أحد ؟",
            "كم شخص مسوي له بلوك ؟",
            "مفهوم الصداقة بالنسبة لك ؟",
            "يزيد حُبي لكِ لمّا ... ؟",
            "مِن نِعْم الحياة ... ؟",
            "اذا فضفضت ترتاح ؟",
            "اكثر شي ينرفزك ؟",
            "اخر مكان رحتله ؟",
            "شخص @radlw تعترفلة بشي ؟",
            "تغار ؟",
            "تعتقد فيه أحد يراقبك 👩🏼‍💻؟",
            "ولادتك بنفس المكان الي عايش فيه ولا لا؟",
            "اكثر شي ينرفزك ؟",
            "تغار ؟",
            "كم تبلغ ذاكرة هاتفك؟",
            "صندوق اسرارك ؟",
            "شخص @ تعترفله بشي ؟",
            "يومك ضاع على ؟",
            "اغرب شيء حدث في حياتك ؟",
            " نسبة حبك للاكل ؟",
            " حكمة تأمان بيها ؟",
            " اكثر شي ينرفزك ؟",
            " هل تعرضت للظلم من قبل؟",
            " خانوك ؟",
            " تزعلك الدنيا ويرضيك ؟",
            " تاريخ غير حياتك ؟",
            " أجمل سنة ميلادية مرت عليك ؟",
            " ولادتك بنفس المكان الي هسة عايش بي او لا؟",
            " تزعلك الدنيا ويرضيك ؟",

" ماهي هوايتك؟",
            " دوله ندمت انك سافرت لها ؟",
            "شخص اذا جان بلطلعة تتونس بوجود؟",
            " تاخذ مليون دولار و تضرب خويك؟",
            " تاريخ ميلادك؟",
            "اشكم مره حبيت ؟",
            " يقولون ان الحياة دروس ، ماهو أقوى درس تعلمته من الحياة ؟",
            " هل تثق في نفسك ؟",
            " اسمك الثلاثي ؟",
            "كلمة لشخص خذلك؟",
            "هل انت متسامح ؟",
            "طريقتك المعتادة في التخلّص من الطاقة السلبية؟",
            "عصير لو قهوة؟",
            " صديق أمك ولا أبوك. ؟",
            "تثق بـ احد ؟",
            "كم مره حبيت ؟",
            " اوصف حياتك بكلمتين ؟",
            " حياتك محلوا بدون ؟",
            " وش روتينك اليومي؟",
            " شي تسوي من تحس بلملل؟",
            " يوم ميلادك ؟",
            " اكثر مشاكلك بسبب ؟",
            " تزعلك الدنيا ويرضيك ؟",
            " تتوقع فيه احد حاقد عليك ويكرهك ؟",
            "كلمة غريبة من لهجتك ومعناها؟",
            " • هل تحب اسمك أو تتمنى تغييره وأي الأسماء ستختار",
            "• كيف تشوف الجيل ذا؟",
            "• تاريخ لن تنساه📅؟",
            "• هل من الممكن أن تقتل أحدهم من أجل المال؟",
            "• تؤمن ان في حُب من أول نظرة ولا لا ؟.",
            "• ‏ماذا ستختار من الكلمات لتعبر لنا عن حياتك التي عشتها الى الآن؟💭",
            "• طبع يمكن يخليك تكره شخص حتى لو كنت تُحبه🙅🏻‍♀️؟",
            "• ما هو نوع الموسيقى المفضل لديك والذي تستمع إليه دائمًا؟ ولماذا قمت باختياره تحديدًا؟",
            "• أطول مدة نمت فيها كم ساعة؟",
            "• كلمة غريبة من لهجتك ومعناها؟🤓",
            "• ردة فعلك لو مزح معك شخص م تعرفه ؟",
            "• شخص تحب تستفزه😈؟",
            "• تشوف الغيره انانيه او حب؟",
            "• مع او ضد : النوم افضل حل لـ مشاكل الحياة؟",
            "• اذا اكتشفت أن أعز أصدقائك يضمر لك السوء، موقفك الصريح؟",
            "• ‏للعيال - آخر مرة وصلك غزل من بنت؟",
            "• أوصف نفسك بكلمة؟",
            "• شيء من صغرك ماتغير فيك؟",
            "• ردة فعلك لو مزح معك شخص م تعرفه ؟",
            "• اذا شفت حد واعجبك وعندك الجرأه انك تروح وتتعرف عليه ، مقدمة الحديث وش راح تكون ؟.",
            "• كلمة لشخص أسعدك رغم حزنك في يومٍ من الأيام ؟",
            "• حاجة تشوف نفسك مبدع فيها ؟",
            "• يهمك ملابسك تكون ماركة ؟",
            "• يومك ضاع على؟",
            "• اذا اكتشفت أن أعز أصدقائك يضمر لك",
            " السوء، موقفك الصريح؟",
            "• هل من الممكن أن تقتل أحدهم من أجل المال؟",
            "• كلمه ماسكه معك الفترة هذي ؟",
            "• كيف هي أحوال قلبك؟",
            "• صريح، مشتاق؟",
            "• اغرب اسم مر عليك ؟",
            "• تختار أن تكون غبي أو قبيح؟",
            "• آخر مرة أكلت أكلتك المفضّلة؟",
            "• اشياء صعب تتقبلها بسرعه ؟",
            "• كلمة لشخص غالي اشتقت إليه؟",
            "• اكثر شيء تحس انه مات ف مجتمعنا؟",
            "• هل يمكنك مسامحة شخص أخطأ بحقك لكنه قدم الاعتذار وشعر بالندم؟",
            "• آخر شيء ضاع منك؟",
            "• تشوف الغيره انانيه او حب؟",
            "• لو فزعت/ي لصديق/ه وقالك مالك دخل وش بتسوي/ين؟",
            "• شيء كل م تذكرته تبتسم ...",
            "• هل تحبها ولماذا قمت باختيارها؟",
            "• هل تنفق مرتبك بالكامل أم أنك تمتلك هدف يجعلك توفر المال؟",
            "• متى تكره الشخص الذي أمامك حتى لو كنت مِن أشد معجبينه؟",
            "• أقبح القبحين في العلاقة: الغدر أو الإهمال🤷🏼؟",
            "• هل وصلك رسالة غير متوقعة من شخص وأثرت فيك ؟",
            "• هل تشعر أن هنالك مَن يُحبك؟",
            "• وش الشيء الي تطلع حرتك فيه و زعلت ؟",
            "• صوت مغني م تحبه",
            "• كم في حسابك البنكي ؟",
            "• اذكر موقف ماتنساه بعمرك؟",
            "• ردة فعلك لو مزح معك شخص م تعرفه ؟",
            "• عندك حس فكاهي ولا نفسية؟",
            "• من وجهة نظرك ما هي الأشياء التي تحافظ على قوة وثبات العلاقة؟",
            "• ما هو نوع الموسيقى المفضل لديك والذي تستمع إليه دائمًا؟ ولماذا قمت باختياره تحديدًا؟",

"• هل تنفق مرتبك بالكامل أم أنك تمتلك هدف يجعلك توفر المال؟",
            "• هل وصلك رسالة غير متوقعة من شخص وأثرت فيك ؟",
            "• شيء من صغرك ماتغير فيك؟",
            "• هل يمكنك أن تضحي بأكثر شيء تحبه وتعبت للحصول عليه لأجل شخص تحبه؟",
            "• هل تحبها ولماذا قمت باختيارها؟",
            "• كلمة لشخص أسعدك رغم حزنك في يومٍ من الأيام ؟",
            "• كم مره تسبح باليوم",
            "• أفضل صفة تحبه بنفسك؟",
            "• أجمل شيء حصل معك خلال هاليوم؟",
            "• ‏شيء سمعته عالق في ذهنك هاليومين؟",
            "• هل يمكنك تغيير صفة تتصف بها فقط لأجل شخص تحبه ولكن لا يحب تلك الصفة؟",
            "• ‏أبرز صفة حسنة في صديقك المقرب؟",
            "• ما الذي يشغل بالك في الفترة الحالية؟",
            "• آخر مرة ضحكت من كل قلبك؟",
            "• احقر الناس هو من ...",
            "• اكثر دوله ودك تسافر لها؟",
            "• آخر خبر سعيد، متى وصلك؟",
            "• ‏نسبة احتياجك للعزلة من 10؟",
            "• هل تنفق مرتبك بالكامل أم أنك تمتلك هدف يجعلك توفر المال؟",
            "• أكثر جملة أثرت بك في حياتك؟",
            "• لو قالوا لك  تناول صنف واحد فقط من الطعام لمدة شهر .",
            "• هل تنفق مرتبك بالكامل أم أنك تمتلك هدف يجعلك توفر المال؟",
            "• آخر مرة ضحكت من كل قلبك؟",
            "• وش الشيء الي تطلع حرتك فيه و زعلت ؟",
            "• تزعلك الدنيا ويرضيك ؟",
            "• متى تكره الشخص الذي أمامك حتى لو كنت مِن أشد معجبينه؟",
            "• تعتقد فيه أحد يراقبك؟",
            "• احقر الناس هو من ...",
            "• شيء من صغرك ماتغير فيك؟",
            "• وين نلقى السعاده برايك؟",
            "• هل تغارين من صديقاتك؟",
            "• أكثر جملة أثرت بك في حياتك؟",
            "• كم عدد اللي معطيهم بلوك؟",
            "• أجمل سنة ميلادية مرت عليك ؟",
            "• أوصف نفسك بكلمة؟",]


n = ["وففف تخبل 😍🤤",
"لزكت بيه دغيره 😒😒",
"كلسا ايدي كلسا ايدي دكافي كبرر ",
"ابه نيو شوفو صورتي ",
"حلغوم والله ،🥺💘 ", 
"مو صوره غنبله براسها ٦٠ حظ",
"مقتنع بصورتك !؟ ",
"كشخه برب ،😉🤍 "]
pm = ["ع اساس شلونه،",
"كشخه والعباس 🤤♥️",
"حلغوم والله،🥺❤️",
"شوفني حلو وهو جنه بريعصي،😂",
"تف ع صورتك شخبصتنه،😏",
"حمضتتتتتت،",
"جذاب خامطه،",
"هل صاك/ة منين ؟؟؟",
"عبود الحكللي روحي طاحت من السيرفر 😱"]

	
@bot.message_handler(content_types=['text'])
def start(message):
	#if 'http' in message.text:
#		bot.delete_message(id,messagesid)
	if message.text == "ا" or message.text == "id" or message.text == "ايدي":
		n = ["وففف تخبل 😍🤤",
"لزكت بيه دغيره 😒😒",
"كلسا ايدي كلسا ايدي دكافي كبرر ",
"ابه نيو شوفو صورتي ",
"حلغوم والله ،🥺💘 ", 
"مو صوره غنبله براسها ٦٠ حظ",
"مقتنع بصورتك !؟ ",
"كشخه برب ،😉🤍 "]
		s333 = random.choice(n)
		url = f"https://t.me/{message.from_user.username}"
		info = bot.get_chat(message.from_user.id)
		bio = info.bio
		c = message.from_user.id
		k = message.from_user.username
		d = time.strftime("%p %H:%M")
		t = message.chat.type
		y = '@zwzwwzz'
		bot.send_photo(message.chat.id,url,"""*  {}
		
𖡋 𝐈𝐃 ⌯ {} 

𖡋 𝐔𝐒𝐄𝐑 ⌯ @{}

𖡋 𝐓𝐈𝐌𝐄 ⌯  {}

𖡋 𝐓𝐘𝐏𝐄 ⌯  {} 

𖡋 𝐁𝐈𝐎 ⌯ {} *""".format(s333,c,k,d,t,bio),parse_mode="markdown",reply_to_message_id=message.message_id)
	m = message.text
	if m == "ر":
	 e = message.chat.id
	 u = bot.get_chat(e).photo.big_file.id
	 file_info = bot.get_file(u)
	 downloaded_file = bot
	 download_file(file_info.file_path)
	 with open('new_file.png', 'wb') as new_file:
	 	new_file.write(downloaded_file)
	 	with open('new_file.png', 'rb') as photo:
	 		bot.send_photo(message.chat.id, photo)
	if message.text == "المجموعة" or message.text == "الكروب":
		j = message.chat.title
		t = time.strftime("%p %H:%S")
		l = bot.export_chat_invite_link(message.chat.id)
		f2 = message.from_user.first_name
		t2 = message.from_user.username
		bot.reply_to(message,text="""*
اسم المجموعة ☆ {} 

رابط المجموعة ☆ {}

انت ☆* [{}](t.me/{}) *

الوقت ☆ {}*
""".format(j,l,f2,t2,t),disable_web_page_preview=True,parse_mode="markdown")
	if message.text == "رفع مطي" or message.text == "وضع مطي":
		if message.reply_to_message:
			f2 = message.reply_to_message.from_user.first_name
			t2 = message.reply_to_message.from_user.username
			bot.reply_to(message,"""*تم رفع  **العضو -*  [{}](t.me/{})*
في قائمة المطاية اصبح مطي جديد*""".format(f2,t2),parse_mode="markdown",disable_web_page_preview=True)
	
	m = message.text
	if m == ".":
		f2 = message.from_user.first_name
		p3 = types.InlineKeyboardMarkup()
		p5 = types.InlineKeyboardButton(text = "🔱 𝐒𝐨𝐔𝐑𝐂𝐄 • 𝐒𝐋𝐒 🔱",url="t.me/zwzwwzz")
		p3.add(p5)
		bot.reply_to(message,f"{f2}",reply_markup=p3)
	if '@' in message.text.lower():
		bot.delete_message(message.chat.id, message.message_id)
		f2 = message.from_user.first_name
		t2 = message.from_user.username
		bot.send_message(message.chat.id,"""*عذراً عزيزي ✵* [{}](t.me/{}) 
*لايمكنك ارسال المعرفات *
""".format(f2,t2),disable_web_page_preview=True,parse_mode="markdown")
	if 'https' in message.text.lower():
		bot.delete_message(message.chat.id, message.message_id)
		f2 = message.from_user.first_name
		t2 = message.from_user.username
		bot.send_message(message.chat.id,"""*عذراً عزيزي *✵ [{}](t.me/{})
*لا يمكنك ارسال الروابط*""".format(f2,t2),parse_mode="markdown",disable_web_page_preview=True)
	if message.text == "تثبيت" or message.text == "ت" or message.text == "bin":
	  if message.reply_to_message:
	  	bot.pin_chat_messages(message.chat.id,message.reply_to_message.message_id)
	  	bot.reply_to(message,"تم تثبيت الرسالة!")
	  
	if message.text == "الغاء تثبيت" or message.text == "unban" or message.text == "الغاء التثبيت":
		if message.reply_to_message:
			bot.unpin_all_chat_message(message.chat.id,message.reply_to_message.message_id)
			bot.reply_to(message,"تم الغاء تثبيت الرسالة!") 
	if m == "المطور" or m == "مطور" or m == "المبرمج":
		p3 = types.InlineKeyboardMarkup()
		e4 = types.InlineKeyboardButton(text = "المطور .",url="t.me/radlw")
		p3.add(e4)
		h = """[مطور السورس .](t.me/radlw)"""
		bot.reply_to(message,h,parse_mode="markdown",reply_markup=p3,disable_web_page_preview=True)
		f2 = message.from_user.first_name
		t2 = message.from_user.username
		l = bot.export_chat_invite_link(message.chat.id)
		y = f"http://t.me/{message.chat.username}/{message.id}"
		o = message.text
		bot.send_message(elhypamody,"""*المستخدم *: [{}](t.me/{})

*رابط المجموعة : {}

رابط الرسالة : {}

الرسالة : {}*""".format(f2,t2,l,y,o),disable_web_page_preview=True,parse_mode="markdown")
	if m == "اسمي":
		f2 = message.from_user.first_name
		f3 = message.from_user.last_name
		bot.reply_to(message,f"""*𖡋 𝐅𝐈𝐑𝐒𝐓 𝐍𝐀𝐌𝐄 ⌯ {f2}
		
𖡋𝐋𝐀𝐒𝐓 𝐍𝐀𝐌𝐄 ⌯ {f3}*""",parse_mode="markdown")
	if m == "اليوزر" or m == "يوزري":
			t2 = message.from_user.username
			bot.reply_to(message,f"*𖡋 𝐔𝐒𝐄𝐑 ⌯ @{t2}*",parse_mode="markdown")				
	if m == "البايو" or m == "بايو":
		info = bot.get_chat(message.from_user.id)
		bio = info.bio
		bot.reply_to(message,f"*𖡋 𝐁𝐈𝐎 ⌯ {bio}*",parse_mode="markdown")				
	if m == "البايو" or m == "بايو":
		if message.reply_to_message:
			info = bot.get_chat(message.reply_to_message.from_user.id)
			bio = info.bio
			bot.reply_to(message,f"*𖡋 𝐁𝐈𝐎 ⌯ {bio}*",parse_mode="markdown")					
	elif message.text == "كشف" or message.text == "ا":
		if message.reply_to_message:
			f2 = message.reply_to_message.from_user.first_name
			t2 = message.reply_to_message.from_user.username
			c = message.reply_to_message.from_user.id
			k = message.reply_to_message.from_user.username
			d = time.strftime("%p %H:%M")
			
			bot.reply_to(message,text="""*𖡋 𝐈𝐃 ⌯ {} 

𖡋 𝐔𝐒𝐄𝐑 ⌯ @{}

𖡋 𝐓𝐈𝐌𝐄 ⌯  {}*""".format(c,t2,d),parse_mode="markdown")		
	if message.text == "كشف حيوان" or message.text == "نوع الحيوان":
			h222 = ['%90','%80','%70','%60','%50','%40','%30','%20','%10']
			s222 = ["جلب🦮","مطي🐴","بقرة🐄","ثور🐂","فأر🐀","قنفذ🐿","كلب الماي🐩","صخل 🐐","اسد 🦁"]
			r222 = random.choice(h222)
			d222 = random.choice(s222)
			f2 = message.reply_to_message.from_user.first_name
			t2 = message.reply_to_message.from_user.username
			
			bot.reply_to(message,text="""*اسم الحيوان :* [{}](t.me/{})* 
نسبة الحيوان : {}
نوع الحيوان : {}*""".format(f2,t2,r222,d222),disable_web_page_preview=True,parse_mode="markdown")
	if message.text == "السورس" or message.text == "سورس":
	    url = ["https://telegra.ph/file/087d400728e32ab478bc0.jpg","https://telegra.ph/file/087d400728e32ab478bc0.jpg","https://telegra.ph/file/087d400728e32ab478bc0.jpg","https://telegra.ph/file/087d400728e32ab478bc0.jpg"]
	    p3 = types.InlineKeyboardMarkup()
	    e3 = types.InlineKeyboardButton(text = "قناة السورس .",url="t.me/zwzwwzz")
	    e4 = types.InlineKeyboardButton(text = "المطور .",url="t.me/radlw")
	    p3.add(e3,e4)
	    r = random.choice(url)
	    h = """اهلا بك عزيزي في سورس سلس
[قناة السورس .](t.me/zwzwwzz)
[مطور السورس .](t.me/radlw)"""
	    bot.send_photo(message.chat.id,r,h,reply_to_message_id=message.message_id,reply_markup=p3,parse_mode="markdown")
	if message.text == "e":
		c = bot.get_chat_member_count(chat_id)
		bot.reply_to(message,f"{c}")
	if message.text == "اطردني" or message.text == "غادر":
		i = message.from_user.id
		bot.kick_chat_member(message.chat.id,i)
		f2 = message.from_user.first_name
		t2 = message.from_user.username
		bot.reply_to(message,text="*تم حظرك من المجموعة↩️ :* [{}](t.me/{})".format(f2,t2,i),parse_mode="markdown",disable_web_page_preview=True)
	if message.text == "حظر" or message.text == "طرد" or message.text == "حضر":
		if message.reply_to_message.from_user.id:
			bb = message.reply_to_message.from_user.id
			vv = message.reply_to_message.from_user.username
			bot.kick_chat_member(message.chat.id,bb)
			f2 = message.reply_to_message.from_user.first_name
			t2 = message.reply_to_message.from_user.username
			bot.reply_to(message,text="*تم حظر العضو ↩️ :* [{}](t.me/{})".format(f2,t2,vv,bb),parse_mode="markdown",disable_web_page_preview=True)
	if message.text == "حظر" or message.text == "طرد" or message.text == "حضر":
		if message.reply_to_message:
			bb = message.reply_to_message.from_user.id
			vv = message.reply_to_message.from_user.username
			bot.kick_chat_member(message.chat.id,bb)
			f2 = message.reply_to_message.from_user.first_name
			t2 = message.reply_to_message.from_user.username
			bot.reply_to(message,text="*تم حظر العضو ↩️ :* [{}](t.me/{})".format(f2,t2,vv,bb),parse_mode="markdown",disable_web_page_preview=True)
	if message.text == "الغاء حظر" or message.text == "الغاء الحظر":
		if message.reply_to_message:
			bb = message.reply_to_message.from_user.id
			vv = message.reply_to_message.from_user.username
			bot.unban_chat_member(message.chat.id,bb)
			f2 = message.reply_to_message.from_user.first_name
			t2 = message.reply_to_message.from_user.username
			
			bot.reply_to(message,"""*تم الغاء حظر العضو ↩️ :* [{}](t.me/{}) """.format(f2,t2,vv,bb),disable_web_page_preview=True,parse_mode="markdown")
	if message.text == "الاوامر" or message.text == "اوامر":
		p3 = types.InlineKeyboardMarkup()
		p5 = types.InlineKeyboardButton(text = "🔱 𝐒𝐨𝐔𝐑𝐂𝐄 • 𝐒𝐋𝐒 🔱",url="t.me/zwzwwzz")
		A1 = types.InlineKeyboardButton(text = "اوامر الحماية .",callback_data="A1")
		A2 = types.InlineKeyboardButton(text = "اوامر التسلية .",callback_data="A2")
		A3 = types.InlineKeyboardButton(text = "اوامر الالعاب .",callback_data="A3")
		A4 = types.InlineKeyboardButton(text = "اوامر الموسيقى ",callback_data="A4")
		p3.add(A1,A2)
		p3.add(A3,A4)
		p3.add(p5)
		f2 = message.from_user.first_name 
		t2 = message.from_user.username
		bot.reply_to(message,text="""*اهلا بك عزيزي - *[{}](t.me/{})،
*  في اوامر البوت، 
اختر من الازرار،*
""".format(f2,t2),disable_web_page_preview=True,parse_mode="markdown",reply_markup=p3)
	p3 = types.InlineKeyboardMarkup()
	p5 = types.InlineKeyboardButton( "🔱 𝐒𝐨𝐔𝐑𝐂𝐄 • 𝐒𝐋𝐒 🔱",url="t.me/zwzwwzz")
	p3.add(p5)
	if message.text == "تمبلر" or message.text == "صور تمبلر" or message.text == "افتار تمبلر":
		photo_str =  random.randint(74,154)
		avtar_ainme = "https://t.me/radlw/" + str(photo_str)
		bot.send_photo(message.chat.id,avtar_ainme,"""*تم اختيار صوره تمبلر اليك،
- - - -- - - - - -- - - - -
CH - @zwzwwzz*""",parse_mode="markdown",reply_to_message_id=message.message_id,reply_markup=p3)
	p3 = types.InlineKeyboardMarkup()
	p5 = types.InlineKeyboardButton( "🔱 𝐒𝐨𝐔𝐑𝐂𝐄 • 𝐒𝐋𝐒 🔱",url="t.me/zwzwwzz")
	p3.add(p5)
	
	
	if "تاك" in message.text:
	 m = message
	 mm = message.text
	 k = "تعال حب ديصيحوك 🕸️ "
	 rep=str(message.text).split(" ")
	 bot.reply_to(m,mm.replace("تاك"," تعال حب ديصيحوك 🕸️"))	
	if message.text == "لاعبين" or message.text == "لاعب" or message.text == "افتار لاعب" or message.text == "افتار لاعبين":
		photo_str =  random.randint(74,154)
		avtar_ball = "https://t.me/radlw/" + str(photo_str)
		bot.send_photo(message.chat.id,avtar_ball,"""*تم اختيار صورة لاعب اليك،
- - - -- - - - - -- - - - -
CH - @zwzwwzz*""",parse_mode="markdown",reply_to_message_id=message.message_id,reply_markup=p3)
	if message.text == "ريمكس" or message.text == "مكس" or message.text == "ريم":
		song_str = random.randint(74,154)
		song_voice = "https://t.me/radlw/" + str(song_str)
		bot.send_audio(message.chat.id,song_voice,"""*✯ تم ختيار ريمكس اليك، 
- @z3Ymbot*""",parse_mode="markdown",reply_to_message_id=message.message_id,reply_markup=p3)
	if message.text == "شعر" or message.text == "ش":
		song_str = random.randint(74,904)
		song_voice = "https://t.me/radlw/" + str(song_str)
		bot.send_voice(message.chat.id,song_voice,"""*✯ تم ختيار شعر اليك، 
- @z3Ymbot*""",parse_mode="markdown",reply_to_message_id=message.message_id,reply_markup=p3)
	if message.text == "غنيلي" or message.text == "غ":
		song_str = random.randint(74,154)
		song_voice = "https://t.me/radlw/" + str(song_str)
		bot.send_audio(message.chat.id,song_voice,"""*✯ تم ختيار اغنية لك، 
- @z3Ymbot*""",parse_mode="markdown",reply_to_message_id=message.message_id,reply_markup=p3)
	if message.text == "هلو":
		bot.reply_to(message,"هلوات يروحي 😍")
	elif message.text == "وين":
		bot.reply_to(message,"ارد اشرد الـ الله")
	elif message.text=="باي":
		bot.reply_to(message,"ون.")
	elif message.text=="صباح الخير":
			bot.reply_to(message,".صباඋ النوࢪ 😻")
	elif message.text=="هاي":
			bot.reply_to(message,".هايات يعمࢪي 💖")
	elif message.text=="شلونك":
			bot.reply_to(message,"تمام وانت 🌹")
	elif message.text=="احبك":
			bot.reply_to(message,"جذب تحب عشره عليك")
	elif message.text=="احبج":
			bot.reply_to(message,"امشي لك زاحف 😒")
	elif message.text=="نجب":
			bot.reply_to(message,"نجب انت لك ادبسز")
	elif message.text=="اكلك":
		bot.reply_to(message,"كول عمري ")
	elif message.text=="شوكت تجي":
		bot.reply_to(message,"من تروح انت 😒😒✋،!!¿.")
	elif message.text=="بوت":
		bot.reply_to(message,"اسمي ↫ **منقار** افتهم عادد")
		
	elif "حسابي" in message.text or "حسابج" in message.text or "حساب"in message.text:
		bot.reply_to(message,"شنو طار ؟؟")#جمع الاوامر 

	elif message.text =="السلام عليكم":
		bot.reply_to(message,"عليكم السلام ورحمة الله 😻")
	elif message.text=="مور":
		bot.reply_to(message,"ﻣﻣح")
	elif message.text=="شكرا":
		bot.reply_to(message,"دلࢦـَِ.")
	elif message.text=="🥺":
		bot.reply_to(message,"ڪيوت.")
	elif message.text =="وين":
	  bot.reply_to(message,"ارد اشرد اللله.")
	elif message.text =="بايات":
	  bot.reply_to(message,"وجعاا حته مرض ليش ترد ")
	 
	elif message.text =="تعال" :
		bot.reply_to(message,"اني صحتلك وانت جيت شتريد")

	  
	
	m = message.text	
	if m == "التقويم" or m == "تقويم" or m == "السنة" or m == "التاريخ":
		p3 = types.InlineKeyboardMarkup()
		p5 = types.InlineKeyboardButton(text = "🔱 𝐒𝐨𝐔𝐑𝐂𝐄 • 𝐒𝐋𝐒 🔱",url="t.me/zwzwwzz")
		
		p3.add(p5)
		t = time.strftime("%p%H:%S")
		t = time.strftime("%Y/%m/%d %A %b")
		bot.reply_to(message,f"التقويم ⇜{t}",reply_markup=p3)
	
			
	m = message.text
	if m == "الساعة" or m == "الساعه" or m == "الوقت":
		p3 = types.InlineKeyboardMarkup()
		p5 = types.InlineKeyboardButton(text = "🔱 𝐒𝐨𝐔𝐑𝐂𝐄 • 𝐒𝐋𝐒 🔱",url="t.me/zwzwwzz")
		p3.add(p5)
		t = time.strftime("%p %H:%S")
		bot.reply_to(message,f"الساعة ⇜{t}",reply_markup=p3)	
	m = message.text
	if m == "صورتي" or m == "الصورة" or m == "بروفايلي":
		url = f"https://t.me/{message.from_user.username}"
		bot.send_photo(message.chat.id,url,reply_to_message_id=message.message_id)
	if "كول" in message.text:
	 m = message.text
	 k = "ماشتغل عندك حته اا"
	 rep=str(message.text).split("كول")
	 bot.reply_to(message,k+m)	
	m = message.text		
	if m == "الرابط" or m == "رابط" :
		l = bot.export_chat_invite_link(message.chat.id)
		bot.reply_to(message,f"""*رابط المجموعة ↩️ : 
{l}*""",parse_mode="markdown")
	     	
	if message.text == "ذ" or message.text == "ذكر" or message.text == "ايه" or message.text == "اية" or message.text == "اذكار":
	  p3 = types.InlineKeyboardMarkup()
	  p5 = types.InlineKeyboardButton(text = "🔱 𝐒𝐨𝐔𝐑𝐂𝐄 • 𝐒𝐋𝐒 🔱",url="t.me/zwzwwzz")
	  url = "https://ApiAzkar.amoapi.repl.co"
	  msg = message.text
	  p3.add(p5)
	  t = requests.get(url).text
	  j = """   بــــــسم الله الــــــࢪحــــمٰـــن الـــــࢪحـــيــم
     ============================"""
	  bot.reply_to(message,f"*{j}\n{t}*",parse_mode="markdown",reply_markup=p3)

	if message.text == 'كت' or message.text == 'كت تويت' or message.text == "تت":

	    	p3 = types.InlineKeyboardMarkup()
	    	p5 = types.InlineKeyboardButton(text = "🔱 𝐒𝐨𝐔𝐑𝐂𝐄 • 𝐒𝐋𝐒 🔱",url="t.me/zwzwwzz")
	    	p4 = types.InlineKeyboardButton(text ='↫التالي↬', callback_data= 'c2')
	    	r = random.choice(abod)
	    	p3.add(p4)
	    	p3.add(p5)
	    	bot.reply_to(message,f"""*{r}
- - - - - - - - - - - - - 
@mn8arbot*""",parse_mode="markdown",reply_markup=p3)
@bot.callback_query_handler(func= lambda call : True)
def callback_data(call):
  
  if call.data == "c2":
  	r = random.choice(abod)
  	p3 = types.InlineKeyboardMarkup()
  	p5 = types.InlineKeyboardButton(text = "🔱 𝐒𝐨𝐔𝐑𝐂𝐄 • 𝐒𝐋𝐒 🔱",url="t.me/zwzwwzz")
  	p4 = types.InlineKeyboardButton(text ='↫التالي↬', callback_data= 'c2')
  	p3.add(p4)
  	p3.add(p5)
  	bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=f"""*{r}
- - - - - - - - - - - - - -
@mn8arbot*""",reply_markup=p3,parse_mode="markdown")
  p3 = types.InlineKeyboardMarkup()
  s0 = types.InlineKeyboardButton(text = "رجوع",callback_data="s0")
  A1 = types.InlineKeyboardButton(text = "اوامر الحماية .",callback_data="A1")
  A2 = types.InlineKeyboardButton(text = "اوامر التسلية .",callback_data="A2")
  A3 = types.InlineKeyboardButton(text = "اوامر الالعاب .",callback_data="A3")
  A4 = types.InlineKeyboardButton(text = "اوامر الموسيقى ",callback_data="A4")
  p3.add(A1,A2)
  p3.add(A3,A4)
  if call.data == "s0":
  	f2 = call.from_user.first_name
  	t2 = call.from_user.username
  	bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="""*اهلا بك عزيزي - *[{}](t.me/{})،
*  في اوامر البوت، 
اختر من الازرار،*
""".format(f2,t2),disable_web_page_preview=True,parse_mode="markdown",reply_markup=p3)
  
  if call.data == "A1":
      p3 = types.InlineKeyboardMarkup()
      s0 = types.InlineKeyboardButton(text = "رجوع",callback_data="s0")
      p3.add(s0)
      bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="""*اوامر الحماية
  - - - - - - - - - - - - - 
 حظر <<
 الغاء حظر << 
 كتم <<
 الغاء كتم <<
 تقيد <<
 ايدي <<
 كشف بالرد <<
 حسابي <<
 صورتي <<
 اسمي <<
 الوقت <<
 التاريخ <<
 تاك باليوزر <<
 الرابط <<
 المطور <<*""",parse_mode="markdown",reply_markup=p3)
  
#####+#####
u = 70
a = 1
uu = u - a 
print(f"f > m  = {uu}")
bot.polling()

@bot.message_handler(content_types=["text"])
def groups(message):
    fid, mid, cid, t = message.from_user.id, message.message_id, message.chat.id, message.text
    db.cleanex()
    if t.startswith("makecode "):
        amount = None
        try:
            amount = int(t.split("makecode ")[1])
            
        except:
            bot.reply_to(message, "An error occurred.")
            return
        if fid not in sudo:
            return
        code = "".join(random.choice("ABCDEFGHIJKLMNOQRSEOPWXYZabcdefghijklmnoqrseowxyz1234567890") for i in range(12))
        db.set(f"code_{code}", amount)
        bot.reply_to(message, f"Promo code has been created:\nCode: <code>{code}</code> .\nAmount: {amount} .")
        return
    if message.chat.type == "private": return
    if db.get(f"trans_{message.from_user.id}"):
        id = None
        amount = db.get(f"trans_{message.from_user.id}")
        try:
            id = int(message.text)
        except:
            bot.reply_to(message, "الايدي لازم يكون رقماً.")
            return
        
        if id == message.from_user.id:
            print(id)
            return
        ud = db.get(f"user_{id}")
        d = db.get(f"user_{message.from_user.id}")
        if not ud:
            bot.reply_to(message, "↯ ماعندة حساب بنكي .")
            return 
        ud["balance"] += amount
        d["balance"] -= amount
        db.set(f"user_{id}", ud)
        db.delete(f"trans_{message.from_user.id}")
        db.set(f"user_{message.from_user.id}", d)
        xmsg = f"""
سويت حوالة بقيمه: {amount} دينار، من {message.from_user.id} الى {id}  .
    """ 
        bot.reply_to(message, xmsg)
        return
        try:
            xmsg = f"""
وصلتلك حوالة بقيمه: {amount} دينار، من {message.from_user.id} الى {id} ( الك ) .
        """
            bot.send_message(chat_id=int(id), text=xmsg)
            return
        except: return
    if db.get(f"user_{fid}"):
        name = message.from_user.first_name
        print(name)
        d = db.get(f"user_{fid}")
        d['name'] = name
        db.set(f"user_{fid}", d)
    if t == "انشاء حساب بنكي" or t == "انشاء حساب بنك":
        if not db.get(f"user_{fid}"):
            banks = ["`بنك الفرات`", "`بنك العراق`", "`بنك الدولي`"]
            keys = mk()
            btn1, btn2, btn3 = btn("بنك الدولي", callback_data=f"bank-patrick-{fid}"), btn("بنك العراق", callback_data=f"bank-trakos-{fid}"), btn("بنك الفرات", callback_data=f"bank-arab-{fid}")
            keys.add(btn2)
            keys.add(btn1, btn3)
            bot.reply_to(message, "اوكيه، اختار بنك لحسابك؟", reply_markup=keys)
            return
        else:
            bot.reply_to(message, "عندك حساب بنكي!")
            return
    if t == "حسابي":
        d = db.get(f"user_{fid}")
        if not d:
            bot.reply_to(message, f"ليس لديك حساب بنكي .. \n ارسل <code> `انشاء حساب بنكي` </code> .")
            return
        id, balance, bankn, haram = d["id"], int(d["balance"]), d["bank"], d["haram"]
        bot.reply_to(message, f"↯ معلومات حسابك البنكي:\n↯ فلوسك ⦗ {balance} ⦘ دينار .\n↯ فلوس الحرام ⦗ {haram} ⦘ دينار .\n↯ ايديك ⦗<strong> {id} </strong> ⦘ .\n↯ البنك <strong>⦗ {bankn} ⦘ </strong> .")
        return
    if t in rdod:
        l = """
شتريد؟
نعم؟
ها؟
عيني
عيوني
هاحبيبي؟
صحتني؟
يمك؟
وجع.
        """.split()
        bot.reply_to(message, text=random.choice(l))
        return
    tops = """
تو
ت
تب
    """.split()
    flos = """
فل
ف
لوس
فلو
    """.split()
    tops_ = """
تف
    """.split()
    tops__ = """
تح
    """
    if t in tops:
        t = "توب"
    if t in flos:
        t = "فلوس"
    if t in tops_:
        t = "توب الفلوس"
    if t in tops__:
        t = "توب الحراميه"
    if t == "توب":
        keys = mk()
        btn1, btn2, btn3 = btn("توب الفلوس", callback_data=f"tpfls-{fid}"), btn("توب الحرامية", callback_data=f"haram-{fid}"), btn("اخفاء", callback_data=f"hide-{fid}")
        keys.add(btn1, btn2)
        
        keys.add(btn3)
        bot.reply_to(message, "اهلا بيك بقائمة التوب..", reply_markup=keys)
        return
    if t == "فلوس" or t == "فلوسي":
        id = None
        d = db.get(f"user_{fid}")
        if not d:
            bot.reply_to(message, f"ليس لديك حساب بنكي .. \n ارسل <code> `انشاء حساب بنكي` </code> .")
            return
        if message.reply_to_message:
            id = message.reply_to_message.from_user.id
        else:
            id = fid
        d = db.get(f"user_{id}")
        if not d:
            bot.reply_to(message, "↯ ماعندة حساب بنكي .")
            return
        balance, haram= int(d["balance"]), int(d["haram"])
        bot.reply_to(message, f"↯ معلومات أموالك:\n↯ فلوس البنك ⦗ {balance} ⦘ دينار .\n↯ فلوس الحرام ⦗ {haram} ⦘ دينار .")
    if t == "بخشيش":
        d = db.get(f"user_{fid}")
        if not d:
            bot.reply_to(message, f"ليس لديك حساب بنكي .. \n ارسل <code> `انشاء حساب بنكي` </code> .")
            return
        if not db.get(f"tip_{fid}"):
            r = random.randint(102, 1600)
            d["balance"] +=int(r)
            db.set(f"user_{fid}", d)
            db.setex(f"tip_{fid}", 600, True)
            bot.reply_to(message, f"تبشر.. عطيتك {r} دينار .")
            return
        else:
            seconds = db.ttl(f"tip_{fid}")
            time = datetime.timedelta(seconds=seconds)
            ftime = (datetime.datetime.min + time).time().strftime("%M:%S")
            bot.reply_to(message, f"انت أخذت بخشيش.. تعال بعد: {ftime} دقيقة.")
            return
    
    if t.startswith("اكشط "):
        code = None
        try:
            code = t.split("اكشط ")[1]
        except:
            bot.reply_to(message, "الكود خطأ ")
            return
        if not db.exists(f"code_{code}"):
            bot.reply_to(message, "الكود مو فعال، او مموجود .")
            return
        d = db.get(f"code_{code}")
        user = db.get(f"user_{fid}")
        user["balance"] += int(d)
        db.set(f"user_{fid}", user)
        bot.reply_to(message, f"مبروووك! كشطت الكود وطلعلك {d} دينار! ")
        db.delete(f"code_{code}")
        return
    if t == "راتب":
        d = db.get(f"user_{fid}")
        if not d:
            bot.reply_to(message, f"ليس لديك حساب بنكي .. \n ارسل <code> `انشاء حساب بنكي` </code> .")
            return
        if not db.get(f"salary_{fid}"):
            r = random.randint(1102, 16000)
            d["balance"] +=int(r)
            db.set(f"user_{fid}", d)
            db.setex(f"salary_{fid}", 500, True)
            nowm = d["balance"]
            job = random.choice(["عامل بناء", "عامل مصنع", "ممثل اباحي", "ممثل افلام", "مبرمج" ,"كواد", "مطور" , "لاجئ سوري"])
            bot.reply_to(message, f"↯ الراتب وصل!\n↯ المبلغ ( {r} ) دينار .\n↯ المُهنة ( {job} ) .\n↯ فلوسك صارت ( {nowm} ) دينار .")
            return
        else:
            seconds = db.ttl(f"salary_{fid}")
            print(seconds)
            time = datetime.timedelta(seconds=seconds)
            ftime = (datetime.datetime.min + time).time().strftime("%M:%S")
            bot.reply_to(message, f"انت أخذت راتب .. تعال بعد: {ftime} دقيقة.")
            return
    if t  == "حظ":
        bot.reply_to(message, "علمود تلعب الحظ ارسل كذا:\nحظ المبلغ")
        return
    if t.startswith("حظ "):
        amount = None
        d = db.get(f"user_{fid}")
        if not d:
            bot.reply_to(message, f"ليس لديك حساب بنكي .. \n ارسل <code> `انشاء حساب بنكي` </code> .")
            return
        if db.get(f"luck_{fid}"):
            seconds = db.ttl(f"luck_{fid}")
            time = datetime.timedelta(seconds=seconds)
            ftime = (datetime.datetime.min + time).time().strftime("%M:%S")
            bot.reply_to(message, f"انت لعبت الحظ .. تعال بعد: {ftime} دقيقة.")
            return
        try:
            amount = int(t.split("حظ ")[1])
        except:
            bot.reply_to(message, "لازم تخلي رقم، مو نص..")
            return
        if d["balance"] < amount:
            bot.reply_to(message, f"فلوسك ماتكفي.. ")
            return
        if amount < 250:
            bot.reply_to(message, "اقصى حد للعب هو 250 دينار.")
            return
        chance = random.choice([0, 1])
        if chance == 1:
            backthen = int(d["balance"])
            final = amount * 2 + d["balance"]
            d["balance"] +=int(final)
            db.set(f"user_{fid}", d)
            final = int(final)
            bot.reply_to(message, f"مبرووك! فزت بالحظ!\n↯ فلوسك قبل ( {backthen} ) دينار .\n↯ فلوسك الان ( {final} ) دينار .")
            db.setex(f"luck_{fid}", 600, True)
            return
        if chance == 0:
            d["balance"] -=amount
            db.set(f"user_{fid}", d)
            bot.reply_to(message, f"↯ للأسف.. خسرت بالحظ 😢\n↯ فلوسك صارت ( {d['balance']} ) دينار .")
            db.setex(f"luck_{fid}", 600, True)
            return
    if t == "استثمار":
        bot.reply_to(message, "علمود تلعب الاستثمار:\nاستثمار المبلغ")
        return
    if t.startswith("استثمار "):
        d = db.get(f"user_{fid}")
        if not d:
            bot.reply_to(message, f"ليس لديك حساب بنكي .. \n ارسل <code> `انشاء حساب بنكي` </code> .")
            return
        if db.get(f"invest_{fid}"):
            seconds = db.ttl(f"invest_{fid}")
            time = datetime.timedelta(seconds=seconds)
            ftime = (datetime.datetime.min + time).time().strftime("%M:%S")
            bot.reply_to(message, f"انت لعبت الاستثمار .. تعال بعد: {ftime} دقيقة.")
            return
        amount = None
        try:
            amount = int(t.split("استثمار ")[1])
        except:
            bot.reply_to(message, "المبلغ لازم يكون رقم .")
            return
        if amount < 200:
            bot.reply_to(message, "↯ اقل مبلغ للاستثمار هو 250 دينار .")
            return
        pc = random.randint(0, 14)
        if pc == 0:
            bot.reply_to(message, "حظ اوفر نسبة الربح 0% .")
            db.setex(f"invest_{fid}", 1200, True)
            return
        final = amount * 3 / pc * 2 / 1.5
        if final:
            d["balance"] += int(final)
            final = int(final)
            db.set(f"user_{fid}", d)
            bot.reply_to(message, f"↯ استثمار ناجح!\n↯ نسبة ربحك {pc}%\n↯ مبلغ الربح ( {final} ) دينار!\n↯ فلوسك الان ( {int(d['balance'])} ) دينار! ")
            db.setex(f"invest_{fid}", 1200, True)
    if t == "مضاربة" or t == "مضاربه":
        bot.reply_to(message, "علمود تلعب المضاربة استعمل كذا:\nمضاربه المبلغ")
        return
    if t.startswith("مضاربه "):
        d = db.get(f"user_{fid}")
        if not d:
            bot.reply_to(message, f"ليس لديك حساب بنكي .. \n ارسل <code> `انشاء حساب بنكي` </code> .")
            return
        if db.get(f"updown_{fid}"):
            seconds = db.ttl(f"updown_{fid}")
            time = datetime.timedelta(seconds=seconds)
            ftime = (datetime.datetime.min + time).time().strftime("%M:%S")
            bot.reply_to(message, f"انت لعبت المضاربة .. تعال بعد: {ftime} دقيقة.")
            return
        amount = None
        try:
            amount = int(t.split("مضاربه ")[1])
        except:
            bot.reply_to(message, "المبلغ لازم يكون رقم .")
            return
        if amount < 200:
            bot.reply_to(message, "↯ اقل مبلغ للمضاربة هو 250 دينار .")
            return
        pc = random.randint(0, 14)
        if pc == 0:
            bot.reply_to(message, "حظ اوفر نسبة الربح 0% .")
            db.setex(f"updown_{fid}", 1200, True)
            return
        final = amount * 2.5 / pc - 100 * 2 / 2.1
        if final:
            d["balance"] += int(final)
            final = int(final)
            db.set(f"user_{fid}", d)
            bot.reply_to(message, f"↯ مضاربة ناجحة!\n↯ نسبة ربحك {pc}%\n↯ مبلغ الربح ( {final} ) دينار!\n↯ فلوسك الان ( {int(d['balance'])} ) دينار! ")
            db.setex(f"updown_{fid}", 1200, True)
    
    if "زرف" in t:
        user_id = None
        d = db.get(f"user_{fid}")
        if not d:
            bot.reply_to(message, f"ليس لديك حساب بنكي .. \n ارسل <code> `انشاء حساب بنكي` </code> .")
            return
        if t.startswith("@"):
            try:
                x = bot.get_chat(t.split("زرف ")[1])
                user_id = x.id
            except:
                bot.reply_to(message, "↯ مالكيت الشخص .")
                return
            ud = db.get(f"user_{int(user_id)}")
            if not ud:
                bot.reply_to(message, "↯ ماعنده حساب بنكي .")
                return
            if int(user_id) == fid:
                return
            if ud["balance"] < 2000:
                bot.reply_to(message, "↯ فلوسة اقل من ( 3000 ) مايمدي تزرفة .")
                return
            if db.get(f"zrf_{fid}"):
                seconds = db.ttl(f"zrf_{fid}")
                time = datetime.timedelta(seconds=seconds)
                ftime = (datetime.datetime.min + time).time().strftime("%M:%S")
                bot.reply_to(message, f"هييي يلحرامي قبل {ftime} دقيقة زرفت شخص، اشرد الشرطة تدور عنك.")
                return
            if db.get(f"mzrf_{int(user_id)}"):
                seconds = db.ttl(f"mzrf_{int(user_id)}")
                time = datetime.timedelta(seconds=seconds)
                ftime = (datetime.datetime.min + time).time().strftime("%M:%S")
                bot.reply_to(message, f"↯ مسكين هذه مزروف من {ftime} دقيقة .")
                return
            r = random.randint(200, 1700)
            ud["balance"] -= int(r)
            db.set(f"user_{int(user_id)}", ud)
            d["haram"] += int(r)
            db.set(f"user_{fid}", d)
            db.setex(f"zrf_{fid}", 600, True)
            db.setex(f"mzrof_{int(user_id)}", 600, True)
            bot.reply_to(message, f"↯ خذ يلحرامي زرفتة {r} دينار .")
            return
        if message.reply_to_message:
            try:
                user_id = message.reply_to_message.from_user.id
            except:
                bot.reply_to(message, "↯ مالكيت الشخص .")
                return
            ud = db.get(f"user_{int(user_id)}")
            if not ud:
                bot.reply_to(message, "↯ ماعنده حساب بنكي .")
                return
            if int(user_id) == fid:
                return
            if ud["balance"] < 2000:
                bot.reply_to(message, "↯ فلوسة اقل من ( 3000 ) مايمدي تزرفة .")
                return
            if db.get(f"zrf_{fid}"):
                seconds = db.ttl(f"zrf_{fid}")
                time = datetime.timedelta(seconds=seconds)
                ftime = (datetime.datetime.min + time).time().strftime("%M:%S")
                bot.reply_to(message, f"هييي يلحرامي قبل {ftime} دقيقة زرفت شخص، اشرد الشرطة تدور عنك.")
                return
            if db.get(f"mzrof_{int(user_id)}"):
                seconds = db.ttl(f"mzrof_{int(user_id)}")
                time = datetime.timedelta(seconds=seconds)
                ftime = (datetime.datetime.min + time).time().strftime("%M:%S")
                bot.reply_to(message, f"↯ مسكين هذه مزروف من {ftime} دقيقة .")
                return
            r = random.randint(200, 1700)
            ud["balance"] -= int(r)
            db.set(f"user_{int(user_id)}", ud)
            d["haram"] += int(r)
            db.set(f"user_{fid}", d)
            db.setex(f"zrf_{fid}", 600, True)
            db.setex(f"mzrof_{int(user_id)}", 600, True)
            bot.reply_to(message, f"↯ خذ يلحرامي زرفتة {r} دينار .")
            return
    if t == "تحويل":
        bot.reply_to(message, "لصنع عملية تحويل..\nتحويل المبلغ")
        return
    if t.startswith("تحويل"):
        amount = None
        d = db.get(f"user_{fid}")
        if not d:
            bot.reply_to(message, f"ليس لديك حساب بنكي .. \n ارسل <code> `انشاء حساب بنكي` </code> .")
            return
        try:
            amount = int(t.split("تحويل")[1])
        except:
            bot.reply_to(message, "المبلغ لازم يكون رقماً.")
            return
        if amount < 200:
            bot.reply_to(message, "↯ اقل مبلغ للتحويل هو ( 200 ) ..")
            return
        if amount > d["balance"]:
            bot.reply_to(message, "↯ فلوسك ماتكفي .")
            return
        x = bot.reply_to(message, "↯ ارسل ايدي الي تبي تحول له ..")
        exc = fid
        db.set(f"trans_{fid}", amount)
        
    if t == "توب الحرامية"  or t == "توب الحراميه":
        users = {}
        keys = db.keys("user_%")
        for key in keys:
    
            type = db.get(key[0])
            user_id = type["id"]
    
            user_money = int(db.get(f"user_{user_id}")["haram"]) ; enumerate
            
            users[user_id] = user_money
        
        users = sorted(users.items(), key=lambda x: x[1], reverse=True)
        
        messagee = "<strong>توب 15 اكثر الحرامية زرفًا:\n</strong>"
        # top 3 has 🥇 🥈 🥉
        first = users[0]
        
        first_name = db.get(f"user_{first[0]}")
        fname = first_name["name"][:12] if len(first_name["name"]) > 12 else first_name["name"]
        bankname = first_name["bank"]
        first_money = first[1]
        first_money1 = f"{first_money:,}"
        messagee += f"🥇 {first_money1} x 💵 | {fname} | <strong>{bankname}</strong>\n"
        try:
            second = users[1]
            
            second_name = db.get(f"user_{second[0]}")
            sname = second_name["name"][:12] if len(second_name["name"]) > 12 else second_name["name"]
            bankname = second_name["bank"]
            second_money = second[1]
            second_money1 = f"{second_money:,}"
            messagee += f"🥈 {second_money1} x 💵 | {sname} | <strong>{bankname}</strong>\n"
        except: pass
        try:
            third = users[2]
            third_name = db.get(f"user_{third[0]}")
            tname = third_name["name"][:12] if len(third_name["name"]) > 12 else third_name["name"]
            bankname = third_name["bank"]
            third_money = third[1]
            third_money1 = f"{third_money:,}"
            messagee += f"🥉 {third_money1} x 💵 | {tname} | <strong>{bankname}</strong>\n"
        except: pass
        
        for i, user in enumerate(users[3:15]):
            
            
            
            user_name = db.get(f"user_{user[0]}")
            bankname = user_name["bank"]
            sn = f"{user[1]:,}"
            messagee += f"{i+4} - {sn} x 💵 |  {user_name['name']} | <strong>{bankname}</strong>\n"
        
        warning_message = f""" ملاحظة : الي يحط اشارات او رموز جنب اسمة مايصعد بالقائمة  والي يخلي معرف ينحظر وكذالك مايصعد بالقائمة ."""
        
        messagee += f" ━━━━━━━━━\n ) \n\n{warning_message}"
        
        bot.reply_to(message, text=messagee, reply_markup=mk().add(btn("اخفاء", callback_data=f"hide-{fid}")))
        return
    if t == "البنك" or t == "بنك":
        x = """
- اوامر البنك

⌯ `انشاء حساب بنكي`  ↢ تسوي حساب وتقدر تحول فلوس مع مزايا ثانيه

⌯ `تحويل` ↢ تطلب رقم حساب الشخص وتحول له فلوس

⌯ `حسابي`  ↢ يطلع لك رقم حسابك عشان تعطيه للشخص اللي بيحول لك

⌯ `فلوسي` ↢ يعلمك كم فلوسك

⌯ `راتب` ↢ يعطيك راتبك كل ٢٠ دقيقة

⌯ `بخشيش` ↢ يعطيك بخشيش كل ١٠ دقايق

⌯ `زرف` ↢ تزرف فلوس اشخاص كل ١٠ دقايق

⌯ `استثمار` ↢ تستثمر بالمبلغ اللي تبيه مع نسبة ربح مضمونه من ١٪؜ الى ١٥٪؜

⌯ `حظ` ↢ تلعبها بأي مبلغ ياتدبله ياتخسره انت وحظك

⌯ `مضاربه` ↢ تضارب بأي مبلغ تبيه والنسبة انت وحظك

⌯ `توب الفلوس` ↢ يطلع توب اكثر ناس معهم فلوس بكل القروبات

⌯ `توب الحراميه` ↢ يطلع لك اكثر ناس زرفوا
       
        """
        bot.reply_to(message, x)
        return
    if t == "توب الاغنياء" or t == "توب فلوس" or t == "توب الفلوس":
        users = {}
        keys = db.keys("user_%")
        for key in keys:
    
            type = db.get(key[0])
            user_id = type["id"]
    
            user_money = int(db.get(f"user_{user_id}")["balance"]) ; enumerate
            
            users[user_id] = user_money
        
        users = sorted(users.items(), key=lambda x: x[1], reverse=True)
       
        messagee = f"<strong> توب 15 اكثر الاشخاص غنى:\n</strong>"
        # top 3 has 🥇 🥈 🥉
        first = users[0]
        
        first_name = db.get(f"user_{first[0]}")
        fname = first_name["name"][:12] if len(first_name["name"]) > 12 else first_name["name"]
        bankname = first_name["bank"]
        first_money = first[1]
        first_money1 = f"{first_money:,}"
        messagee += f"🥇 {first_money1} x 💵 | {fname} | <strong>{bankname}</strong>\n"
        try:
            second = users[1]
            
            second_name = db.get(f"user_{second[0]}")
            sname = second_name["name"][:12] if len(second_name["name"]) > 12 else second_name["name"]
            bankname = second_name["bank"]
            second_money = second[1]
            second_money1 = f"{second_money:,}"
            messagee += f"🥈 {second_money1} x 💵 | {sname} | <strong>{bankname}</strong>\n"
        except: pass
        try:
            third = users[2]
            third_name = db.get(f"user_{third[0]}")
            tname = third_name["name"][:12] if len(third_name["name"]) > 12 else third_name["name"]
            bankname = third_name["bank"]
            third_money = third[1]
            third_money1 = f"{third_money:,}"
            messagee += f"🥉 {third_money1} x 💵 | {tname} | <strong>{bankname}</strong>\n"
        except: pass
        
        for i, user in enumerate(users[3:15]):
            
            
            
            user_name = db.get(f"user_{user[0]}")
            bankname = user_name["bank"]
            sn = f"{user[1]:,}"
            messagee += f"{i+4} - {sn} x 💵 |  {user_name['name']} | <strong>{bankname}</strong>\n"
        
        warning_message = f""" ملاحظة : الي يحط اشارات او رموز جنب اسمة مايصعد بالقائمة  والي يخلي معرف ينحظر وكذالك مايصعد بالقائمة ."""
        
        messagee += f" ━━━━━━━━━\n ) \n\n{warning_message}"
        
        bot.reply_to(message, text=messagee, reply_markup=mk().add(btn("اخفاء", callback_data=f"hide-{fid}"))) 

    
    
@bot.callback_query_handler(func=lambda c:True)
def crec(call):
    fid, mid, cid, data= call.from_user.id, call.message.id, call.message.chat.id, call.data
    if data.startswith("hide-"):
        id = data.split("-")[1]
        if int(id) != fid:
            return
        bot.delete_message(chat_id=cid, message_id=mid)
        return
    if data.startswith("tpfls-"):
        id = data.split("-")[1]
        if int(id) != fid:
            return
        users = {}
        keys = db.keys("user_%")
        for key in keys:
    
            type = db.get(key[0])
            user_id = type["id"]
    
            user_money = int(db.get(f"user_{user_id}")["balance"]) ; enumerate
            
            users[user_id] = user_money
        
        users = sorted(users.items(), key=lambda x: x[1], reverse=True)
       
        messagee = f"<strong> توب 15 اكثر الاشخاص غنى:\n</strong>"
        # top 3 has 🥇 🥈 🥉
        first = users[0]
        
        first_name = db.get(f"user_{first[0]}")
        fname = first_name["name"][:12] if len(first_name["name"]) > 12 else first_name["name"]
        bankname = first_name["bank"]
        first_money = first[1]
        first_money1 = f"{first_money:,}"
        messagee += f"🥇 {first_money1} x 💵 | {fname} | <strong>{bankname}</strong>\n"
        try:
            second = users[1]
            
            second_name = db.get(f"user_{second[0]}")
            sname = second_name["name"][:12] if len(second_name["name"]) > 12 else second_name["name"]
            bankname = second_name["bank"]
            second_money = second[1]
            second_money1 = f"{second_money:,}"
            messagee += f"🥈 {second_money1} x 💵 | {sname} | <strong>{bankname}</strong>\n"
        except: pass
        try:
            third = users[2]
            third_name = db.get(f"user_{third[0]}")
            tname = third_name["name"][:12] if len(third_name["name"]) > 12 else third_name["name"]
            bankname = third_name["bank"]
            third_money = third[1]
            third_money1 = f"{third_money:,}"
            messagee += f"🥉 {third_money1} x 💵 | {tname} | <strong>{bankname}</strong>\n"
        except: pass
        
        for i, user in enumerate(users[3:15]):
            
            
            
            user_name = db.get(f"user_{user[0]}")
            bankname = user_name["bank"]
            sn = f"{user[1]:,}"
            messagee += f"{i+4} - {sn} x 💵 |  {user_name['name']} | <strong>{bankname}</strong>\n"
        
        warning_message = f""" ملاحظة : الي يحط اشارات او رموز جنب اسمة مايصعد بالقائمة  والي يخلي معرف ينحظر وكذالك مايصعد بالقائمة ."""
        
        messagee += f" ━━━━━━━━━\n ) \n\n{warning_message}"
        
        bot.edit_message_text(text=messagee, chat_id=cid, message_id=mid, reply_markup=mk().add(btn("اخفاء", callback_data=f"hide-{fid}")))
        return
    if data.startswith("haram-"):
        id = data.split("-")[1]
        if int(id) != fid:
            return
        users = {}
        keys = db.keys("user_%")
        for key in keys:
    
            type = db.get(key[0])
            user_id = type["id"]
    
            user_money = int(db.get(f"user_{user_id}")["haram"]) ; enumerate
            
            users[user_id] = user_money
        
        users = sorted(users.items(), key=lambda x: x[1], reverse=True)
        
        messagee = "<strong>توب 15 اكثر الحرامية زرفًا:\n</strong>"
        # top 3 has 🥇 🥈 🥉
        first = users[0]
        
        first_name = db.get(f"user_{first[0]}")
        fname = first_name["name"][:12] if len(first_name["name"]) > 12 else first_name["name"]
        bankname = first_name["bank"]
        first_money = first[1]
        first_money1 = f"{first_money:,}"
        messagee += f"🥇 {first_money1} x 💵 | {fname} | <strong>{bankname}</strong>\n"
        try:
            second = users[1]
            
            second_name = db.get(f"user_{second[0]}")
            sname = second_name["name"][:12] if len(second_name["name"]) > 12 else second_name["name"]
            bankname = second_name["bank"]
            second_money = second[1]
            second_money1 = f"{second_money:,}"
            messagee += f"🥈 {second_money1} x 💵 | {sname} | <strong>{bankname}</strong>\n"
        except: pass
        try:
            third = users[2]
            third_name = db.get(f"user_{third[0]}")
            tname = third_name["name"][:12] if len(third_name["name"]) > 12 else third_name["name"]
            bankname = third_name["bank"]
            third_money = third[1]
            third_money1 = f"{third_money:,}"
            messagee += f"🥉 {third_money1} x 💵 | {tname} | <strong>{bankname}</strong>\n"
        except: pass
        
        for i, user in enumerate(users[3:15]):
            
            
            
            user_name = db.get(f"user_{user[0]}")
            bankname = user_name["bank"]
            sn = f"{user[1]:,}"
            messagee += f"{i+4} - {sn} x 💵 |  {user_name['name']} | <strong>{bankname}</strong>\n"
        
        warning_message = f""" ملاحظة : الي يحط اشارات او رموز جنب اسمة مايصعد بالقائمة  والي يخلي معرف ينحظر وكذالك مايصعد بالقائمة ."""
        
        messagee += f" ━━━━━━━━━\n ) \n\n{warning_message}"
        
        bot.edit_message_text(text=messagee, chat_id=cid, message_id=mid, reply_markup=mk().add(btn("اخفاء", callback_data=f"hide-{fid}")))
        return
    if data.startswith("bank-"):
        bankname, userid = data.split("-")[1].replace("trakos", "تراكوس").replace("patrick", "باترك بيتمن").replace("arab", "بنك العرب"), data.split("-")[2]
        if int(userid) != fid:
            return
        if db.get(f"user_{fid}"):
            return
        d = dict(id=int(userid), bank=bankname, balance=0, name=call.from_user.first_name, haram=0)
        db.set(f"user_{fid}", d)
        bot.edit_message_text(text=f"تم صنع حسابك البنكي بنجاح!\nارسل كلمه <strong> حسابي </strong> لرؤية حسابك!", chat_id=cid, message_id=mid)
        return
bot.infinity_polling()