(function($) {
	function init() {
		var class_name_field = $(this);
		var select = class_name_field.find('select');
		var text_input = class_name_field.find('input');

		select.change(function() {
			if (select.val()) {
				text_input.hide();
			} else {
				text_input.show();
			}
		});

		select.change();
	}

	$(document).ready(function() {
		$('.field-class_name').each(init);
	});
}(django.jQuery));
