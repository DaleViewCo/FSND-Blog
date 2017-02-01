function postComment(post_id){
	var content = $("#comment-text-area-id").val();
	if(content == ''){
		return;
	}
	$.ajax({
		type: 'post',
		contentType: 'application/json',
		dataType: 'json',
		data: JSON.stringify({
			'comment': content,
			'pid': post_id
		}),
		success: function(response){
			var newHTML = $("div#comment-content-id").html();
			var comment_id = response.id;
			var functionText = 'editComment(' + comment_id + ')';

			newHTML += response.data;
			newHTML +='<a class="link" onclick="' + functionText + '>Edit</a>';

			$("div#comment-content-id").html(newHTML);
			$("textarea#comment-text-area-id").val('');
		},
		error: function(request, status, error){
			alert("Error"+request.responseText);
		}
	})
}

function editComment(comment_id){

}