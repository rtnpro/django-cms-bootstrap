// This scripts show an example how to integrate
$(function() {

	$('#cms_toolbar-toggle').css('display','none');

	{% if user.is_authenticated %}	//we don't need to show the button 
									// if the user is not authenticated

		var updateToggleToolbar = function() {
			CMS.API.Toolbar.toggleToolbar();
		};

		$('#cms_tb_toggle').click(updateToggleToolbar);

	{% endif %}
});
