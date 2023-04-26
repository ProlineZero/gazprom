# gazprom
Функционал:
	api/view_articles - json всех статей
	wiki/<str:arctcieName> - json всех статей с именем arctcieName (по ТЗ инфу о статье по точному совпадению, но названия повторяются)
	wiki/<str:arctcieName>?pretty=true - то же самое, но json форматирован
	category/<str:slug> - json статей, которые относятся к категории (название категории прописывается как slug)
	category/ - json всех категорий
	/admin/wikiquote_app/article/ - редактирование/добавление статей
	/admin/wikiquote_app/category/ - редактирование/добавление категорий

Инструменты:
	Django
	Django Rest Framework
  Postgresql
