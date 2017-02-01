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
			var comment_id = response.id;
			$("p#comment-content-id").html('');
			$("p#comment-content-id").html(newHTML);
			$("textarea#comment-text-area-id").val('');
			// $("a#latest-comment-edit-link-id").text('Edit');
			// $("a#latest-comment-edit-link-id").attr("onclick",
				// 'editComment(comment_id)');
		},
		error: function(request, status, error){
			alert("Error"+request.responseText);
		}
	})
}

function editComment(comment_id){
}