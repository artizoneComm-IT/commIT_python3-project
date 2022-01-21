$(document).ready(function(){
	$('#login').hide();
	$('#login').show(1000);
	$('#erreur').hide();
	$('#loading').hide();

	// Connecter ...
	$('#connecter').click(function(){
		if($('#identifiant').val().trim().length === 0){
			alert('Veuillez saisir votre identifiant... Merci !');
		}
		else if($('#password').val().trim().length === 0){
			alert('Veuillez saisir votre mot de passe... Merci !')
		}
		else{
			let donnees = {
				identifiant: $('#identifiant').val(),
				password: $('#password').val()
			};
			$.post('http://localhost:5000/api/login', donnees, function(data, status){
				// if(status == 'success'){
				// 	window.location.replace('');
				// }
				// else{
				// 	alert(data);
				// 	$('#erreur').show();
				// }
				if(status == 'success'){
					console.log(data);
				}
				else{
					console.log('Erreur !');
				}
			});
		}
	});

	$('#inscrire').click(function()
		{
			window.location.href = 'inscription.html';
		});

	$('#forgot_password').click(function()
		{
			window.location.href = 'erreurs/forgot_password.html';
		});

	$('#send_mail').click(function(){
		if($('#email').val().trim().length === 0){
			alert('Veuillez saisir votre adresse email...! Merci !');
		}
		else{
			$('#envoyer').hide();
			$('#loading').show();

			$.post('', {email: $('#email').val()}, function(data){
				if(data == 'success'){
					alert('Veuillez regarder votre email pour la mise à jours de votre mot de passe...!');
					window.location.replace('');
				}

				else{
					alert(data);
					$('#loading').hide();
					$('#envoyer').show();
				}
			});
		}
	});
});
