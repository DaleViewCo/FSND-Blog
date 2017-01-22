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
			var existingHTML = $("p#comment-content-id").html();
			existingHTML += response.data;
			$("p#comment-content-id").html(existingHTML);
			$("textarea#comment-text-area-id").val('');
		},
		error: function(request, status, error){
			alert("Error"+request.responseText);
		}
	})
}

// function renderComment(data){
// 	alert(data);
// 	$("p#comment-content").text(data);
// }

// $(document).ready(postComment('123'));
// $(window).on("load", postComment('123'));
