<template>
    <v-container>
        <div class="text-h3 py-6 mx-10 text-left">Руководство пользователя</div>

        <v-btn  variant="outlined" class="mx-10" :to="{name: 'Home'}">
            <v-icon icon="mdi-arrow-collapse-left" color="purple-darken-4" class="mr-2"></v-icon>назад
        </v-btn>

        <v-container>
            <v-card>
                <v-toolbar
                    color="purple-darken-4"
                >
                    <v-toolbar-title>Разделы меню</v-toolbar-title>
                </v-toolbar>
                <div class="d-flex flex-row">
                <v-tabs
                    v-model="tab"
                    direction="vertical"
                    color="purple-darken-4"
                >
                    <v-tab value="option-1">
                        Маршруты
                    </v-tab>

                    <v-tab value="option-2">
                        Добавить маршрут
                    </v-tab>

                    <v-tab value="option-3">
                        Информация о маршруте
                    </v-tab>

                    <v-tab value="option-4">
                        История маршрута
                    </v-tab>
                    <v-tab value="option-5">
                        Аккаунт
                    </v-tab>
                </v-tabs>
                <v-window v-model="tab">
                    <v-window-item value="option-1">
                        <v-card flat>
                            <v-card-text>
                                <v-container>
                                    <div class="text-h4 mb-5 text-left">Выбор пункта "Маршруты"</div>
                                    <div class="mb-5">В меню пользователь должен нажать на кнопку <b>"Маршруты"</b> (выделено красным цветом на ниже представленном скриншоте)</div>
                                    <v-img
                                        :width="1000"
                                        src="../assets/photo_for_manul/выбор меню маршрута.jpg"
                                    >
                                    </v-img>
                                    <div class="text-h4 mt-15 mb-5 text-left">Страница "Маршруты"</div>

                                    <div class="mb-5">После выбора пункта в меню пользователь окажется на странице "Маршруты" (как выглядит страница "Маршруты" изображено на ниже предсталенном скриншоте)</div>
                                    <v-img
                                        :width="1000"
                                        src="../assets/photo_for_manul/про маршруты 2.jpg"
                                    >
                                    </v-img>

                                    <div class="text-h4 mt-15 mb-5 text-left">Возвращение обратно в меню</div>
                                    <div class="mb-5">Для перехода обратно в меню пользователь должен нажать на кнопку <b>"НАЗАД"</b> (выделено красным цветом на ниже представленном скриншоте)</div>
                                    <v-img
                                        :width="1000"
                                        src="../assets/photo_for_manul/про маршруты кнопка назад.jpg"
                                    >
                                    </v-img>

                                    <div class="text-h4 mt-15 mb-5 text-left">Переход на страницу "Добавить маршрут"</div>
                                    <div class="mb-5">Для перехода на страницу <b>"Добавить маршрут"</b> пользователь должен нажать на кнопку <b>"Добавить маршрут"</b> (выделено красным цветом на ниже представленном скриншоте)</div>
                                    <v-img
                                        :width="1000"
                                        src="../assets/photo_for_manul/про маршруты кнопка добавить маршрут.jpg"
                                    >
                                    </v-img>

                                    <div class="text-h4 mt-15 mb-5 text-left">Переход на страницу "Информация о конкретном маршруте"</div>
                                    <div class="mb-5">Для перехода на страницу о конкретном маршруте пользователь должен навеститсь на блок с краткой информацией о маршруте, выбранный блок подсветится фиолетовым цветом и ползовотель должен нажать на блок (выделено красным цветом на ниже представленном скриншоте)</div>
                                    <v-img
                                        :width="1000"
                                        src="../assets/photo_for_manul/Выбрать конкретный маршрут.jpg"
                                    >
                                    </v-img>

                                    <div class="text-h4 mt-15 mb-5 text-left">Удалить уже созданный маршрут</div>
                                    <div class="mb-5">Для того, чтобы удалить конкретный маршрут, пользователю необходимо нажать на кнопку <b>"УДАЛИТЬ"</b>, которая находится под каждым маршрутом (выделено красным цветом на ниже представленном скриншоте)</div>
                                    <v-img
                                        :width="1000"
                                        src="../assets/photo_for_manul/про маршруты кнопка удалить.jpg"
                                    >
                                    </v-img>

                                    <div class="text-h4 mt-15 mb-5 text-left">Статусы маршрутов</div>

                                    <v-row class="mt-5 ml-2">
                                        <v-card color="teal-accent-4" class="text-h5 px-10 py-2">в процессе</v-card> <span class="text-h6 ml-2 mt-2">- статус показывающий, что в данном маршруте есть промежуточные маршруты, но они еще не достигают финальную точку.</span>
                                    </v-row>

                                    <v-row class="mt-10 ml-2">
                                        <v-card color="orange-accent-4" class="text-h5 px-10 py-2">завершение</v-card> <span class="text-h6 ml-2 mt-2">- статус показывающий, что построены все промежуточные маршруты, но не стоит дата завершения маршрута.</span>
                                    </v-row>

                                    <v-row class="mt-10 ml-2">
                                        <v-card color="blue-grey" class="text-h5 px-10 py-2">завершён</v-card> <span class="text-h6 ml-2 mt-2">- статус показывающий, что построены все промежуточные маршруты и установлены все даты.</span>
                                    </v-row>
                                    
                                    
                                    

                                </v-container>
                                
                            </v-card-text>
                        </v-card>
                    </v-window-item>
                <v-window-item value="option-2">
                    <v-card flat>
                        <v-card-text>
                            <v-container>
                                    <div class="text-h4 mb-5 text-left">Введите имя судна</div>
                                    <div class="mb-5">Пользователь должен в поле <b>Название судна</b> ввести название судна (выделено красным цветом на ниже представленном скриншоте)</div>
                                    <v-img
                                        :width="1000"
                                        src="../assets/photo_for_manul/добавить маршрут название судна.jpg"
                                    >
                                    </v-img>

                                    <div class="text-h4 mt-15 mb-5 text-left">Подробно о каждом ледовом классе</div>
                                    <div class="mb-5">Пользователь может назвать на кнопку <b>Подробно</b> и ему будет представлена краткая информация о ледовом классе. При нажатии кнопки <b>Подробно</b> краткая информация закроется (выделено красным цветом на ниже представленном скриншоте)</div>
                                    <v-img
                                        :width="1000"
                                        src="../assets/photo_for_manul/добавить маршруты подробно.jpg"
                                    >
                                    </v-img>

                                    <div class="text-h4 mt-15 mb-5 text-left">Выбор ледового класса судна</div>
                                    <div class="mb-5">Пользователь должен выбрать один ледовый класс судна нажав на кнопку напротив название ледового класса судна(выделено красным цветом на ниже представленном скриншоте)</div>
                                    <v-img
                                        :width="1000"
                                        src="../assets/photo_for_manul/добавить маршрут выбор ледовго класса.jpg"
                                    >
                                    </v-img>

                                    <div class="text-h4 mt-15 mb-5 text-left">Переход на следующий шаг</div>
                                    <div class="mb-5">После выше описанных действий пользользователь должен нажать на кнопку <b>СЛЕДУЮЩИЙ ШАГ</b>(выделено красным цветом на ниже представленном скриншоте)</div>
                                    <v-img
                                        :width="1000"
                                        src="../assets/photo_for_manul/Добавить маршрут 1-ей следущий шаг.jpg"
                                    >
                                    </v-img>

                                    <div class="text-h4 mt-15 mb-5 text-left">Выбор ледовой обстановки (Случайным образом)</div>
                                    <div class="mb-5">После выше описанных действий пользователь окажется на втором шаге добавления маршрута, на карте уже будет отображена ледовая обстановка за сегоднешний день, но если пользовтаель хочет сформировать случайную ледовую обстановку, то он может нажать на кнопку <b>СГЕНЕРИРОВАТЬ ЛЕДОВУЮ ОБСТАНОВКУ</b>(выделено красным цветом на ниже представленном скриншоте)</div>
                                    <v-img
                                        :width="1000"
                                        src="../assets/photo_for_manul/добавить маршрут лед случайный.jpg"
                                    >
                                    </v-img>

                                    <div class="text-h4 mt-15 mb-5 text-left">Загрузить ледовую обстановку (фаилы формата JSON)</div>
                                    <div class="my-5">Так как на интерактивной карте лёд изображен при помощи полигонов, пример синтаксиса (выделено красным цветом на ниже представленном скриншоте)</div>
                                    <v-img
                                        :width="600"
                                        src="../assets/photo_for_manul/пример полигона в geojson.jpg"
                                    >
                                    </v-img>

                                    <div class="my-5">Пользовтаель также может сформировать ледовую обстановку на основе файлов структуры geoJSON, нажав на кнопку <b>ЗАГРУЗИТЬ ЛЕДОВУЮ ОБСТАНОВКУ</b>(выделено красным цветом на ниже представленном скриншоте)</div>
                                    <v-img
                                        :width="1000"
                                        src="../assets/photo_for_manul/Добавить маршрут загрузить ледовую обстановку из JSON.jpg"
                                    >
                                    </v-img>

                                    <div class="my-5">После нажатия на кнопку <b>ЗАГРУЗИТЬ ЛЕДОВУЮ ОБСТАНОВКУ</b> пользователю будет выведена форма для загрзки льда (выделено красным цветом на ниже представленном скриншоте)</div>
                                    <v-img
                                        :width="1000"
                                        src="../assets/photo_for_manul/Добавить маршрут форма для загрузки ледовой обстановки.jpg"
                                    >
                                    </v-img>

                                    <div class="my-5">Чтобы загрузить фаил формата JSON с ледовой обстановкой, необходимо нажать на форму с название льда, который вы хотите загрузить(выделено красным цветом на ниже представленном скриншоте)</div>
                                    <v-img
                                        :width="1000"
                                        src="../assets/photo_for_manul/добавить маршрут прикрепить фаил.jpg"
                                    >
                                    </v-img>
                                    <div class="my-5">При нажатии на форму появится проводник и пользователю необходимо выбрать фаил с ледовой обстановкой и нажать кнопку <b>открыть</b>(выделено красным цветом на ниже представленном скриншоте)</div>
                                    <v-img
                                        :width="1000"
                                        src="../assets/photo_for_manul/добавить маршрут имя фаила.jpg"
                                    >
                                    </v-img>
                                    <v-img class="mt-5"
                                        :width="1000"
                                        src="../assets/photo_for_manul/Добавить маршрут кнопка открыть.jpg"
                                    >
                                    </v-img>

                                    <div class="my-5">После прикрепления всех файлов с ледовой обстановкой, пользователю необходимо нажать кнопку <b>ЗАГРУЗИТЬ</b> (выделено красным цветом на ниже представленном скриншоте)</div>

                                    <v-img class="mt-5"
                                        :width="1000"
                                        src="../assets/photo_for_manul/Добавить маршрут кнопка загрузить.jpg"
                                    >
                                    </v-img>

                                    <div class="text-h4 mt-15 mb-5 text-left">Загрузить фотографию ледовую обстановку</div>
                                    <div class="my-5">Пользовтаель также может сформировать ледовую обстановку на основе файлов структуры geoJSON, нажав на кнопку <b>ЗАГРУЗИТЬ ФОТО ЛЕДОВОЙ ОБСТАНОВКИ</b>(выделено красным цветом на ниже представленном скриншоте)</div>

                                    <v-img class="mt-5"
                                        :width="1000"
                                        src="../assets/photo_for_manul/добавить маршрут загрузить фото ледовойо обстановки.jpg"
                                    >
                                    </v-img>

                                    <div class="my-5">После нажатия на кнопку <b>ЗАГРУЗИТЬ ФОТО ЛЕДОВОЙ ОБСТАНОВКИ</b> пользователю будет выведена форма для загрзки фото (выделено красным цветом на ниже представленном скриншоте)</div>

                                    
                            </v-container>
                        </v-card-text>
                    </v-card>
                </v-window-item>
                <v-window-item  value="option-3">
                    <v-card flat >
                        <v-card-text>
                        <p>
                            Fusce a quam. Phasellus nec sem in justo pellentesque facilisis. Nam eget dui. Proin viverra, ligula sit amet ultrices semper, ligula arcu tristique sapien, a accumsan nisi mauris ac eros. In dui magna, posuere eget, vestibulum et, tempor auctor, justo.
                        </p>

                        <p class="mb-0">
                            Cras sagittis. Phasellus nec sem in justo pellentesque facilisis. Proin sapien ipsum, porta a, auctor quis, euismod ut, mi. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nam at tortor in tellus interdum sagittis.
                        </p>
                        </v-card-text>
                    </v-card>
                    </v-window-item>
                </v-window>
            </div>
            </v-card>
        </v-container>
    </v-container>
</template>

<script>
  export default {
    data: () => ({
      tab: 'option-1',
    }),
  }
</script>