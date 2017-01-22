function editPost(){
	var post_content = $("textarea#post-content").val();
	$.ajax({
		type: 'post',
		contentType: 'application/json',
		dataType: 'json',
		data: JSON.stringify({
			'post': post_content,
		}),
		success: function(response){
		},
		error: function(request, status, error){
			alert("Error"+request.responseText);
		}
	})
}

function cancelEditPost(){
	$.ajax({
		type: 'post',
		contentType: 'application/json',
		dataType: 'json',
		data: JSON.stringify({
			'post': $("#post-content").val(),
			'pid': post_id
		}),
		success: function(response){
		},
		error: function(request, status, error){
			alert("Error"+request.responseText);
		}
	})
}