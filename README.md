# Технические индикаторы котировок ценных бумаг.

Данный репозиторий содержит в себе множество (в будущем все) различных технических индикаторов на Python.

# RSI-индикатор

RSI — это индикатор, с помощью которого можно определить моменты, когда цена актива выросла или упала слишком сильно. То есть когда лучше покупать этот актив, а когда — продавать. Кроме того, RSI может предупреждать о скором росте или падении цены.

На данной фотографии Вы можете наблюдать формулу данного индикатора:
![Image alt](https://github.com/LRKZZ/technical-indicators/blob/main/technical%20indicators/tech_pictures/RSIpic.jpg)

Как RSI показывает, когда лучше покупать актив, а когда — продавать?

Перекупленность наступает, когда цена актива вырастает слишком сильно. Из‑за высокой цены желающих купить актив становится меньше, а инвесторы, у которых этот актив уже есть, хотят успеть продать его по высокой цене. То есть покупок становится меньше, а продаж — больше. Из‑за этого с каждой минутой растет вероятность, что цена начнет снижаться.

Перепроданность, наоборот, показывает, что цена слишком сильно упала. В такие моменты желающих купить актив становится все больше, и вскоре цена может начать расти.

Если график индикатора RSI опускается ниже 30%, актив перепродан. Если поднимается выше 70%, актив перекуплен. От 30 до 70% — голубая зона, в которой индикатор нейтрален.

# SMA-индикатор

Формула индикатора:

![Image alt](https://github.com/LRKZZ/technical-indicators/blob/main/technical%20indicators/tech_pictures/SMA_indicator.jpg)

SMA индикатор неспроста является таким популярным. Он предусматривает большое количество функциональных возможностей, которые полезны для трейдера. Это способствует улучшению процесса торговли и позволяет свести к минимуму все ошибки. Несмотря на простоту настроек и структуры, данный инструмент является отличным фильтром. Рассмотрим детальнее его возможности:

1. Выявление тенденции – посмотрев на линию МА можно легко определить направление действующего тренда. Направление линии свидетельствует о направлении движения тренда. Главное, грамотно экспериментировать с установкой периода индикатора

2. Обнаружения флэта. Простая MA является одним из тех немногих индикаторов, способных сигнализировать о наступлении бокового тренда. Такая возможность несет большую пользу для трейдера, поскольку во флэте иные правила торговли.

3. Подтверждение тенденции – в данном случае простая MA служит фильтром и подходит для многих стратегий торговли, в том числе и автоматизированных.
Прогнозирование ценовых разворотов. Эта функция наиболее популярна. Если трейдер применяет несколько скользящих средних с разными периодами, с большой вероятностью произойдет разворот, когда быстрые и медленные МА пересекутся.

4. Подтверждение перелома тенденции. Когда пересекается цена с медленной МА, генерируется основной и очень надежный сигнал о том, что произойдет перелом тенденции.
Определение момента вхождения в рынок. Есть много вариантов применения МА, в которых генерируются точные сигналы о том, что необходимо открывать сделку или выставлять Stop Loss.

# Полосы Боллинджера

Идея полос Болинджера состоит в том, чтобы объединить в себе трендовый индикатор, индикатор волатильности и осциллятор. Полосы обозначают на графике направление и диапазон колебаний цены, с учетом тренда и волатильности, характерной для текущей фазы рынка. Графически индикатор представляет из себя три линии: скользящая средняя посередине, характеризующая основное направление движения, и две линии, ограничивающие график цены с обеих сторон и характеризующие его волатильность.

Как это выглядит на графике:

![Image alt](https://github.com/LRKZZ/technical-indicators/blob/main/technical%20indicators/tech_pictures/BollingerBands_pic.jpg)

Верхняя и нижняя линии — это та же скользящая средняя, но смещенная на несколько стандартных (среднеквадратичных) отклонений. Поскольку величина стандартного отклонения зависит от волатильности, полосы сами регулируют свою ширину: она увеличивается, когда рынок неустойчив, например, во время публикации новостей, и уменьшается в более стабильные периоды. Таким образом индикатор реализует в себе функции осциллятора в более удобной форме, когда можно сразу на графике с учетом амплитуды колебаний оценить, в состоянии перекупленности или перепроданности находится инструмент.

Сам Боллинджер рекомендовал использовать 20-периодное простое скользящее среднее в качестве средней линии и 2 стандартных отклонения для расчета границ полосы. Как правило, период устанавливается от 13 до 24, а отклонение от 2 до 5. Также, можно использовать в качестве периодов круглые значения 50, 100, 200 или числа Фибоначчи. При этом нужно учитывать, что чем выше период, тем ниже чувствительность индикатора и тем больше будет запаздывание. На инструментах с низкой волатильностью такие настройки сделают индикатор бесполезным.

#CCI-индикатор

Формула индикатора:

![Image alt](https://github.com/LRKZZ/technical-indicators/blob/main/technical%20indicators/tech_pictures/SMA_indicator.jpg

У него (индикатора) есть зона перекупленности, расположенная выше 100, и зона перепроданности, которая находится под отметкой -100.

Чем дальше от этих критических значений находится кривая индикатора и чем дольше она пребывает в таком состоянии, тем большее время актив находится в состоянии перекупленности или перепроданности. Это значит, что уже в ближайшее время может поступить сигнал о смене тенденции в рамках диапазона.

Поэтому, как только индикатор, падая, пересекает линию +100 сверху вниз, приходит сигнал на открытие шорта. Если же индикатор CCI, вырастая, пересекает линию -100 снизу вверх, необходимо открывать лонг. Некоторые трейдеры для открытия позиции используют пересечение индикатора с нулевой линией. То есть открытие короткой позиции происходит при пересечении нулевой линии сверху вниз, а длинной — при пересечении снизу вверх.

