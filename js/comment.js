function postComment(post_id){
	$.ajax({
		type: 'post',
		contentType: 'application/json',
		dataType: 'json',
		data: JSON.stringify({
			'comment': $("#comment-text-area-id").val(),
			'pid': post_id
		}),
		success: function(response){
			var newHTML = $("p#comment-content-id").html();
			newHTML += response.data;
			$("p#comment-content-id").html('');
			$("p#comment-content-id").html(newHTML);
			$("textarea#comment-text-area-id").val('');
		},
		error: function(request, status, error){
			alert("Error"+request.responseText);
		}
	})
}