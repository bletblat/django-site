$('body').on('click', '.tabb__box .tabb', function (event) {
	targ = event.target;
	if (!$(this).hasClass('tabb__active')) {
		let a = $('body').find('.tabb__active')[0];
		if (a) {
			$(a).removeClass('tabb__active');
			$(a).find('.tabb__conteiner')[0].style.maxHeight = 0;
		};
		$(this).addClass('tabb__active');
		let elem = $(this).find('.tabb__conteiner')[0];
		elem.style.maxHeight = elem.scrollHeight + "px";
	}
	else {
		if (targ == $(this).find('.lable')[0]) {
			$(this).removeClass('tabb__active');
			$(this).find('.tabb__conteiner')[0].style.maxHeight = 0;
		}
	}

});

$('body').on('mouseenter', '.header__menu ul li', function (event) {
	if (!$(this).hasClass('activ__li_menu')) {
		$(this).addClass('activ__li_menu');
	}
});

$('body').on('mouseleave', '.header__menu ul li', function (event) {
	if ($(this).hasClass('activ__li_menu')) {
		$(this).removeClass('activ__li_menu');
	}
});