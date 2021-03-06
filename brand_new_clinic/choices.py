# coding=utf-8
import datetime

MATERIAL_SUPPLIES_GROUP_CHOICE = (
    (1, u'Медицинский инструментарий'),
    (2, u'Расходный хирургический материал'),
    (3, u'Расходный медицинский материал'),
    (4, u'Изотопы'),
    (5, u'Импланты, протезы'),
    (6, u'Мягкий инвентарь'),
    (7, u'Медицинские газы'),
    (8, u'Реактивы, реагенты'),
    (9, u'Одноразовое лабораторное оборудование'),
    (10, u'Кровь и кровезаменители'),
    (11, u'Прочие материалы для непосредственного оказания услуги(CD-диски, бланки, пакеты и пр.)'),
)

POSITION_CATEGORY_CHOICE = (
    ('senior', u'Врачи'),
    ('middle', u'Средний медперсонал'),
    ('junior', u'Младший медперсонал'),
    ('science', u'Научные сотрудники'),
    ('else', u'Прочие'),
)

OS_GROUP = (
    ('instrumental', u'ОС медициноского назначения (Инструментарий)'),
    ('diagnostic', u'ОС медициноского назначения (Диагностическое)'),
    ('lab', u'ОС медициноского назначения (Лабораторное)'),
    ('operate', u'ОС медициноского назначения (Операционное)'),
    ('etc', u'ОС медициноского назначения (Прочее)'),
)

SERVICE_TYPE_CHOICE = (
    ('visit', u'Прием (осмотр, консультация) и наблюденик врача-специалиста'),
    ('inst_research', u'Инструментальные методы исследования'),
    ('nonmedicamental', u'Немедикоментозные методы профилактики лечения медицинской реабилитации'),
    ('procedure', u'Хирургические, эндоноскопические, эндоваскулярные и другие методы, требующие анестезиологического и/или реаниматологического сопровождения'),
    ('observation', u'Наблюдение и уход за пациентом медицинскими работниками со средним профессиональным образованием'),
)

YEAR_CHOICES = [(year, year) for year in range(2000, (datetime.datetime.now().year+1))]
