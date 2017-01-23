function editPost(post_id){
	var post_content = $("textarea#post-content").val();
	$.ajax({
		type: 'post',
		contentType: 'application/json',
		dataType: 'json',
		data: JSON.stringify({
			'post': post_content
		}),
		success: function(){
			window.location.replace('/blog/'+ post_id);
		}
	})
}

function cancelEditPost(post_id){
	window.location.replace('/blog/'+ post_id);
}