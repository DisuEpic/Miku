init:
    $ mods["hts_prolog_1"]=u"Хацунэ"
    
    
    #Персонажи
    $ gpt = Character(u'Голос по телефону', color="EEE8AA", what_color="E2C778")
    $ gl = Character(u'Девушка', color="#0AC71A", what_color="E2C778")
    
    
    #Музыка
    $ exodus = "mods/HTS/music/Exodus.mp3"
    
    #Эмбиенс
    
    #Звуки
    $ zaa = "mods/HTS/sfx/zvuk-avtomobilnoj-avarii.ogg"
    
    #Спрайты
    
    #Арты (ЦГ)
    
    #BG 
    image bus = "mods/HTS/bg/bus.png"
    image semen_room_clean = "mods/HTS/bg/int_semen_room_clean_7dl.jpg"
    image vhod_v_sovenok = "mods/HTS/bg/vhod_v_sovenok.jpg"
    
label hts_prolog_1:
    
    scene bg semen_room_window with dissolve
    play music music_list["a_promise_from_distant_days"] fadein 2
    
    "Как часто вы ловили себя на мысли, что жизнь не справедлива?"
    "Казалось ли вам, что вы нежеланны в своей истории с самого начала?" 
    "Если бы я помнил о чём думал при рождении, уверен это была бы одна единственная фраза: «Почему?»"
    "Есть большая вероятность того, что моя биологическая мать именно так и подумала, впервые взяв меня на руки. Только так я могу объяснить то, что она бросила меня спустя всего неделю от роду."
    "Типичная история, когда ты не нужен своей родной матери, а про отца никогда и не слышал." 
    "Не знаю рассказывал бы я сейчас эту историю, если бы не человек, который подарил мне этот шанс."
    "Когда мать сбежала, единственное, что пришло ей на ум, кроме как бросить меня в сточную канаву или под дверью детдома – привезти меня в отчий дом, к моей бабушке. Женщине, благодаря которой я до сих пор брожу по этому миру."
    "Самые яркие воспоминания моего детства – я, бабушка и дорога в сад.  Мы собирали каштаны, который валялись под ногами то тут, то там. Я набирал их полные карманы, а когда кончалось место, она клала их в сумку, лишь бы я мог унести как можно больше."
    "Внутри стен садика я снова становился никому не нужным, я слезливо просил бабушку не бросать меня. И каждый раз она повторяла, что в конце дня мы снова встретимся, утирала мои красные от слёз глаза и щёки."
    "Обещала беречь собранные мною каштаны до момента нашей встречи, чтобы они не потерялись без моего присмотра. И я верил, только ей я всегда мог довериться."
    "И она не подводила, каждый вечер мы вместе шли домой, держась за руки. Я жаловался на других детей, с которыми никогда не мог найти общий язык, а она слушала не перебивая."
    "В школу я пошёл на год позже, чем все остальные, был недостаточно развит для своих сверстников физически."
    "Возможно, на это влияло плохое питание, а возможно я просто с самого детства был бракован."
    "Утро с каштанами сменилось истериками по дороге в школу. Хоть я и был старше всех в классе на целый год, чести мне это не делало."
    "Я был изгоем. Виноват ли в этом мой характер? Или изначально был лишним сам факт моего наличия в обществе?"
    "Меня не травили, но я был одиночкой. Мальчиком, с которым отказывались сидеть, фукая на весь класс, стоило лишь учительнице ко мне подсадить кого-либо."
    "Я витал в облаках, пока дети вокруг меня заводили знакомства, влюблялись или искали себя."
    "Только дома я мог быть самим собой. Бабушка не ругала меня, просто была рядом, выслушивая очередные жалобы на одноклассников, учителей, уроки"
    "В ответ я любил слушать её рассказы о молодости, мне всегда казалось, что я родился не в том времени, не в том месте."
    "Я хотел быть значимым, как великие поэты или художники. Хотел быть рыцарем или королём. Первым человеком на земле? Адамом? Кем угодно, только не тем никем, кто я есть в своём мире."
    "Обычным серым парнем, коих вокруг миллионы.."
    "Не быть собой мне помогали книги, стихи. Я читал, иногда писал сам. Но никогда не делился этим, ни с кем."
    "Так я закончил 11 классов, сидел до последнего, потому что просто не знал чего хочу от жизни. Всё тот же мальчик с последней парты, ищущий виноватых в том, кто он есть."
    "«С родителями моя жизнь сложилась бы иначе? Она была бы лучше или хуже того, что я имею сейчас?»"
    "Пару раз я пытался разговорить бабушку на тему, связанную с Алиной. Матерью."
    "Я перестал называть её «мамой», когда мне стукнуло десять лет. А считать таковой, наверное, ещё раньше. Теперь была просто Алина, которая когда-то выпихнула меня из себя и из своей жизни следом."
    "Ответов я не получил: выходила ли она на связь? Со мной - нет. Большего мне знать и не хотелось. Этого было достаточно, чтобы забросить идею и расспросы. Может её и в живых нет давно?"
    "Если честно, плевать."
    "Я поступил на кафедру журналистики, просто потому что достойно смог сдать лишь литературу и русский язык. Но не видел я себя акулой в этой сфере."
    "Лезть в чужие дела, тыкаться камерой и диктофоном в толпе, желая узнать последние сплетни и вытащить наружу грязное бельё очередного политикана. Да уж, верх моих мечтаний. Но другого выбора я не имел."
    "Четыре года из «своих лучших лет жизни», как у нас принято говорить, я потратил на написание статей и стенгазет."
    "Меня шпыняли как шавку с одного угла в другой, заваливали работой, которая не должна была выполняться мною, но кого это волновало."
    "Студент — это лишь рабочая сила, выполняй или вали на завод. Где так же будешь слушать чьи-то приказы, при этом теряя здоровья с двойной скоростью за гроши."
    "Практика лишний раз показала какое место я занимаю в Иерархии этого мира. Но чтобы получить диплом, ради которого и были эти мучения, я должен был терпеть." 
    "Погрузившись в свои мысли, я понял, что моё присутствие было обнаружено, девочкой у моих ног."
    "Дипломную работу браковали трижды. Сначала проверка на плагиат, потом их не устраивало раскрытие моей темы."
    "«Много воды» - заявил проверяющий."
    "Как будто журналистика не состоит из этой воды полностью. Урод просто хотел, чтобы я сунул руку с деньгами ему в карман."
    "Около недели я проводил свои вечера в библиотеке, штудируя литературу и статьи по теме моей курсовой."
    "12 кругов Ада Данте и рядом не стояли с тем, через что тогда прошли я и мой мозг. Последний вечер перед сдачей дипломной работы я запомнил слишком хорошо."
    "Потому что именно в тот вечер в моей жизни появилось разочарование номер 2, после Алины."
    "Её звали Катя. Антипова Катя. Студентка четвёртого курса. По совместительству моя однокурсница."
    "С которой за все четыре года я перекинулся разве что парой фраз, в стиле «Поздравляю с 8 марта», когда именно мне достался подарок для неё."
    "Преподавательница закупила их на наши деньги, которые пришлось сдавать и вручила каждому представителю мужского пола перед своей парой, предварительно попросив девочек покинуть кабинет."
    "Я уже собирался уходить, возвращая книги на полки, когда услышал всхлипы за одним из стеллажей. Она сидела на полу, в окружении книг и своего ноутбука."
    "«Повезло» Отметил я. Себе такое удовольствие я позволить не мог. И я сейчас не о слезах."
    "Отложенные мною деньги на свой собственный ноутбук ушли бабушке. Последний год она стала частым гостем городской больницы, а лекарства, капельницы и уколы стоили не дёшево."
    "Погрузившись в свои мысли, я понял, что моё присутствие было обнаружено, девочкой у моих ног. Сейчас уже и не вспомнить, что именно тревожило Катю тогда."
    "Единственное, что важно в этой истории, что после того вечера, когда я не ушёл домой, я впервые остался добровольно кому-то помочь."
    "Мне не хотелось возвращаться в пустую квартиру, снова. Она давила на меня обречённостью, как будто это одиночество и так единственное, что останется со мной, когда однажды бабушка просто не вернётся назад."
    "А ещё слёзы Кати, вторая причина, не давшая мне уйти."
    "Я был выращен женщиной, женщиной старого мира, не удивительно, что я вырос мягким. Что на меня легко было влиять чужой слабостью."
    "И знаете, в будущем я осознал, что лучше бы делал это и дальше."
    "Лучше бы ушёл домой, в одиночество, лёг спать, на утром сдал дипломную, а дальше было бы как было."
    "Но уже поздно думать, как жизнь сложилась бы в таком случае. Я всегда одумывался слишком поздно, когда опускался на самое дно."
    "Катя стала моей тюрьмой. Я потерялся в первом человеке, которому решил помочь. А она использовала это против меня. Возможно, я и правда слишком тупой."
    "Она была девочкой, которую уважал класс и преподавательский состав. А кем был я? Мальчиком с последней парты. Молчаливым, отрешённым."
    "Как думаете, чью в итоге работу одобрили, а чью забраковали? Чьи старания слили в унитаз, кого обвинили в плагиате?"
    "В той ситуации я всегда винил только себя, ведь я сам решил остаться, сам предоставил ей свою работу на блюдечке. Мне просто хотелось стать полезным хоть раз, влиться в общество, которое не отворачивается, а подаёт руку помощи. "
    "Но в итоге это общество отвернулось от меня, подавшего руку."
    "Катя снова плакала, но в её руках был заветный диплом, а в моём перечёркнутая работа. "
    "И осознание, что я застрял здесь на ещё один год."
    "Одна лишь мысль пугала меня до чёртиков, я не переживу это снова. Я не выдержу. Бабушка не выдержит. У нас больше нет денег на мою учёбу."
    "И даже после этого я словно идиот успокаивал рядом сидящую девушку."
    "Актриса, использовавшая мой сценарий, чтобы сыграть свою самую яркую роль. Она извинялась, что всё так вышло, что пойдёт и объяснит всем, что это я был оригиналом, а не жалкой копией."
    "А я всё никак не мог понять, почему не отпускаю её, почему сам молча слушал, как меня обвиняют и выставляю за дверь."
    "Возможно, тем вечером в библиотеке я просто почувствовал, что кому-то могу быть полезен. Могу быть нужным, а не просто никем. Что из серого мальчика, смогу стать рыцарем, спасшим понравившуюся девочку от беды."   
    "Её рассказы об матери, которая, по её мнению, убила бы её в случае не сдачи. Сложное детство идеальной девочки, из которой растили отличницу."    
    "Может тогда я просто был глупым и наивным сопляком, который повёлся на слезливую историю."    
    "А может жизнь в очередной раз хотела указать мне на моё место."    
    "Любовь живёт три года."   
    "Так обычно пишут в этих заумных психологических книжках про отношения? В моём случае, так званая любовь, не прожила и крепких двух."    
    "Всё время, с тех пор как мы съехались, я чувствую напряжение. Казалось бы, за такой не малый срок мы должны были хотя бы притереться друг к другу."    
    "Да я и пытался."     
    "После неудачи с дипломной работой, я бросил институт, не было ни сил, ни денег пройти через это снова."
    "С распростёртыми объятиями меня встретила работа на заводе, которым всю жизнь я сам себя пугал. Я получал гроши, медленно убивая себя, гробя здоровье, спину и то хорошее, что возможно было во мне когда-то."
    "Денег всегда было недостаточно, хоть на какое-то время моей бабушке Нине и стало легче, она вернулась домой и расходы на лечение сократились, остальные нужды сами себя не закрывали."
    "Я разрывался между двумя жизнями, между двумя домами."
    "Родители Кати помогли нам с квартирой, но коммунальные услуги были не дешёвыми, да и питаться тоже нужно было хотя бы гречкой или макаронами."
    "Люди состоят на 80 процентов из воды? Я состою на те же 80процентов из круп и теста."
    "Пенсия бабушки была мизерной, и всеми силами я старался помочь и ей, из-за чего часто происходили конфликты в моей, новоприобретённой семье в лице Катюши."
    "Она не поднялась по карьерной лестнице в самый верх, как грезили её родители, видя дочь на вершине мира журналистики. Обычный маркетолог, занимающийся рекламой любого дерьма, за которое заплатил деньги рекламодатель."
    "Неоднократной ей самой приходилось покрывать расходы, которые били по нашему карману. То кинули с рекламой, то подали в суд за неоправданный пиар товара. И снова новые причины для конфликта."
    "Не помню, когда последний раз мы могли позволить себе выйти в люди, сходить в ресторан или в кино."
    "Хоть начиналось всё неплохо, в первый год отношений я из кожи вон лез, чтобы она не чувствовала себя обделённой."
    "К её Дню Рождения я приготовился основательно, копил деньги на дорогой букет и серебряные серёжки, которые присмотрел в ювелирном. Всё должно было быть идеально, кроме того момента, что у моей девушки оказалась сильная аллергия на серебро."
    "Так я стал виновником её испорченного праздника."
    "Серёжки то ей понравились, я давно не видел, чтобы она так искренне мне улыбалась, если улыбалась вообще. Но всего через полчаса на её лице возникла, громкоговорящая о себе, сыпь."
    "Затем небольшие волдыри, поднялась температура и вместо того, чтобы праздновать в кругу семьи, мы провели вечер в больнице."
    "Я выслушал много не благоприятных слов в свой адрес и был выставлен за дверь больничной палаты, с серёжками в кармане и не нужным букетом, брошенным где-то в кафе."
    "Это стало первым небольшим шагом в сторону нашего взаимного саморазрушения в отношениях. Потом дело оставалось за бытом, и он поглотил нас окончательно."
    "А к своему Дню Рождения я получил от неё рюкзак, который стал моим панцирем."
    "Я не часто получал подарки за свою жизнь, кроме конфет от бабушки в детстве или новой формы для школы, поэтому сильно привязался к проявленному знаку внимания, в виде простенького рюкзака."
    "Мне было достаточно и этого, он вмещал в себя всё что нужно, начиная от телефона и зарядного устройства, заканчивая бутылкой воды и инструментами, которые я таскал с собой на работу."
    "Я никогда не пытался прыгнуть выше головы, перестал хотеть выделиться на фоне остальных. Мне нравилось находиться в своей укромной берлоге, с самого детства."
    "К сожалению, больше я позволить себе этого не мог, я жил не один, поэтому желание спрятаться только усиливалось с каждым днём."
    "Катя не оставляла меня в покое, она всё больше хотела, чтобы я изменился. Указывала пальцем на бывших одногруппников или «общих» знакомых, которые скорее были её знакомыми, сравнивала их и меня."
    "Чего добились другие и кем стал я."
    "Честно, мне было плевать, я не видел смысла меняться."
    "Меняться ради девушки, которую, возможно, никогда и не любил? К которой просто привязался из-за проявленного внимания? Которая и сама видимо не знала, что делает рядом с таким как я."
    "Обычное чувство вины или долга после того случая с дипломом? Или она тоже была одинока, хоть и находилась в окружении других, в отличии от меня."
    "Когда она бросила идею добиться от меня какой-либо реакции, я понял, что скоро всё кончится. Всё больше она стала задерживаться на работе, всё чаще уходила спать, не дожидаясь меня. Больше не требовала внимания." 
    "И единственное, что осталось для меня напоминанием, что мы хоть что-то друг для друга представляли, заставка на моём смартфоне."
    "Селфи, где Катя целует меня и делает снимок. Может когда-то мы всё-таки были счастливы?"
    "Или нет?"
    jump hts_prolog_2
    
label hts_prolog_2:

    
    
    $ ringtone = "mods/HTS/sfx/ringtone_7dl.ogg" 
    
    scene semen_room_clean with dissolve
    
    stop music
    
    "Знакомо ли вам понятие – земля ушла из-под ног?"
    "Никогда не чувствовал этого на себе и надеялся, что никогда не почувствую."
    play sound ringtone
    "Звонок в воскресение вечером решил иначе"
    
    
    
    me "Да?"
    
    stop sound
    
    gpt "Это Семён Персунов?"
    me "Да. А Вы кто?"
    gpt "Я дежурный городской больницы №12. Ваш номер записан как экстренный в карте у пациентки Персуновой Нины Фёдоровны. "
    gpt "Она находится у нас в отделении Б. Её доставили к нам на скорой помощи в тяжелом состоянии. Подозрение на сердечный приступ."
    gpt "Вы знали, что это не первый случай, сможете приехать?"
    th "Да, вы правильно поняли, именно тогда земля и ушла у меня из-под ног."
    th "Бабушка, как известно, была частым гостем в больнице, но приходила она туда на своих двоих. Никогда её не привозили туда, тем более с приступом."
    gpt "Ало? Вы меня слышите?"
    me "Да..."
    "Мне пришлось прокашляться, потому что внезапно пропал голос."
    me "Да, я слышу. Я сейчас же приеду."
    gpt "Хорошо. Ожидаем. До свидания."
    me "Стойте. Скажите, сколько мне нужно привезти денег?"
    th "Нужна операция, капельницы, лекарства?"
    gpt"Я не обладаю подобной информацией, простите. Мне кажется, сейчас здесь нужны только вы…"
    "Его многозначительное молчание было громче любых слов или прогнозов."
    me "Я возьму всё."
    "Скинув трубку, я впопыхах стал надевать разбросанные по комнате вещи. Телефон и деньги, отложенные на коммуналку, бабушкино день рождение и продукты я сложил в свою сумку и выбежал на улицу, не удосужившись даже закрыть квартиру."
    
    scene bus with dissolve
    
    "Было около девяти вечера я успевал на автобус, стоявший около моей остановки, запрыгнув туда почти на ходу, я почувствовал, как за спиной закрылись двери. "
    "Лицо обдало морозным воздухом, а невидимая дрожь прошла по всему телу."
    "Одно единственное место было свободно прямо у окна. "
    "Запоздало я подумал о том, что следовало взять такси, но тут же остановил себя, любые деньги сейчас не были лишними, тратить их на дорогущее такси в преддверье нового года было дурной идеей."
    "Я оглянулся, почувствовав на затылке чей-то взгляд, но там никого не было."
    "Люди вокруг не обращали на меня внимания, каждый ехал по своим делам, с сумками набитыми угощениями, подарками. К любимым, близким. К семье."
    "А я… я ехал в больницу к умирающей бабушке."
    "И в этом отчаянье я был один."
    "Достав из сумки телефон, я судорожно набрал номер Кати. Гудки известили меня о том, что абонент не настроен на разговор."
    "Я набрал номер заново."
    "«Абонент находится не в зоне действия сети»"
    me "Блять!"
    "Теперь некоторые пассажиры и правда поглядывали на меня. Я одарил их сердитым взглядом, который вернул их носы обратно в свои дела."
    "До нужной остановки оставалось минут десять, я впёр взгляд в окно. "
    "Силуэты прохожих, снег, дома и магазины проносились за стеклом. Силуэты прохожих, снег, дома и магазины проносились за стеклом."
    "«Дорогие друзья, мы приглашаем всех мальчишек и девчонок на игровую программу «Почувствуй себя пионером». Свяжитесь с нами по номеру…» - гласила одна из них."
    "Неплохо было бы оказаться там, а не здесь."
    "Стать ребёнком, которого не волнуют взрослые проблемы, у которого ещё вся жизнь впереди, а не растрачена впустую на не любимую работу и человека, который блокирует твои вызовы."
    "Вернутся во времени назад, когда я был маленький, а бабушка вела меня в садик, собирая по дороге каштаны."
    "Я почувствовал, как по щеке покатилась слеза, прямо как в детстве, когда она оставляла меня в садике на целый день, а я плакал и просил забрать меня с собой."
    "Только некому было теперь вытереть мои скатывающиеся слёзы, мокрые щеки и опухшие глаза. Я снова остался один."
    scene black
    play sound zaa     
    "Говорят, что перед смертью перед глазами человека проносится вся его жизнь. Видимо, я очередное исключение."
    
    
    
    jump HTS20_day1
   
  
    
    
    



    

    
    




    
    
    
    
        
        
     
    